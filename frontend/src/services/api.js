/**
 * Flight briefing services.
 *
 * The app is a static site (GitHub Pages), so there is no server to proxy through:
 * Gemini is called straight from the browser with the key the pilot enters in the
 * API Key modal. That key stays in this browser's localStorage and travels only to
 * Google - it never passes through a third-party host.
 *
 * Sample briefings are bundled JSON, so the demo flights work with no key at all.
 */

import { BRIEFING_SYSTEM_PROMPT } from './briefingPrompt';
import klaxSample from '../data/sample_aar202_klax.json';
import kjfkSample from '../data/sample_aar224_kjfk.json';

const GEMINI_ENDPOINT =
  'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent';

/** Gemini rejects PDFs over 50MB / 1000 pages; keep well clear and fail early. */
const MAX_PDF_BYTES = 40 * 1024 * 1024;

const SAMPLES = {
  KLAX: {
    briefing: klaxSample,
    document_meta: {
      filename: 'AAR202_RKSI_KLAX_A350_RELEASE_PACKAGE.pdf',
      page_count: 88,
      is_sample: true,
    },
  },
  KJFK: {
    briefing: kjfkSample,
    document_meta: {
      filename: 'AAR224_RKSI_KJFK_A380_RELEASE_PACKAGE.pdf',
      page_count: 95,
      is_sample: true,
    },
  },
};

export function getSampleBriefing(flight = 'KLAX') {
  const key = String(flight || '').toUpperCase();
  const sample = SAMPLES[key] || SAMPLES.KLAX;
  // Deep copy so a page that mutates the briefing cannot poison the bundled sample.
  return structuredClone(sample);
}

/** Fallback NOTAM package for a flight, used when a parsed briefing carries no notam_list. */
export function getFallbackNotams(destIcao) {
  const sample = destIcao === 'KLAX' ? klaxSample : kjfkSample;
  return sample.notam_briefing?.notam_list || [];
}

function fileToBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onerror = () => reject(new Error('PDF 파일을 읽지 못했습니다.'));
    reader.onload = () => {
      const result = String(reader.result || '');
      const comma = result.indexOf(',');
      resolve(comma >= 0 ? result.slice(comma + 1) : result);
    };
    reader.readAsDataURL(file);
  });
}

/** Turns Gemini's error envelope into something a pilot can act on. */
function describeGeminiError(status, payload) {
  const message = payload?.error?.message || '';
  if (status === 400 && /API key not valid/i.test(message)) {
    return 'Gemini API Key가 유효하지 않습니다. 우측 상단에서 키를 다시 입력해 주세요.';
  }
  if (status === 403) {
    return 'Gemini API Key에 이 요청 권한이 없습니다. Google AI Studio에서 키 상태를 확인해 주세요.';
  }
  if (status === 429) {
    return 'Gemini 요청 한도를 초과했습니다. 잠시 후 다시 시도해 주세요.';
  }
  if (status >= 500) {
    return `Gemini 서버 오류 (${status}). 잠시 후 다시 시도해 주세요.`;
  }
  return message || `Gemini 호출 실패 (HTTP ${status})`;
}

async function callGemini({ apiKey, parts, systemInstruction, jsonOutput, temperature }) {
  if (!apiKey) {
    throw new Error('Gemini API Key가 필요합니다. 우측 상단 [API Key] 버튼에서 등록해 주세요.');
  }

  const body = {
    contents: [{ role: 'user', parts }],
    generationConfig: {
      temperature,
      ...(jsonOutput ? { responseMimeType: 'application/json' } : {}),
    },
    ...(systemInstruction
      ? { systemInstruction: { parts: [{ text: systemInstruction }] } }
      : {}),
  };

  let res;
  try {
    res = await fetch(`${GEMINI_ENDPOINT}?key=${encodeURIComponent(apiKey)}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
  } catch {
    throw new Error('Gemini에 연결하지 못했습니다. 네트워크 상태를 확인해 주세요.');
  }

  const payload = await res.json().catch(() => null);
  if (!res.ok) {
    throw new Error(describeGeminiError(res.status, payload));
  }

  const candidate = payload?.candidates?.[0];
  const text = (candidate?.content?.parts || [])
    .map((p) => p.text || '')
    .join('')
    .trim();

  if (!text) {
    const reason = candidate?.finishReason || payload?.promptFeedback?.blockReason;
    throw new Error(
      reason
        ? `Gemini가 응답을 반환하지 않았습니다 (${reason}).`
        : 'Gemini가 빈 응답을 반환했습니다.'
    );
  }
  return text;
}

/** Gemini occasionally wraps JSON in a markdown fence even in JSON mode. */
function parseJsonResponse(text) {
  let cleaned = text.trim();
  if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/, '').trim();
  }
  try {
    return JSON.parse(cleaned);
  } catch {
    throw new Error('Gemini 응답을 브리핑 데이터로 해석하지 못했습니다. 다시 시도해 주세요.');
  }
}

export async function uploadFlightPdf(file, apiKey = '') {
  const name = file?.name || '';
  if (!/\.pdf$/i.test(name) && file?.type !== 'application/pdf') {
    throw new Error('PDF 파일만 분석할 수 있습니다.');
  }
  if (file.size > MAX_PDF_BYTES) {
    throw new Error(
      `PDF 용량이 너무 큽니다 (${(file.size / 1024 / 1024).toFixed(1)}MB). 40MB 이하 파일을 사용해 주세요.`
    );
  }

  const base64 = await fileToBase64(file);

  // The PDF goes to Gemini as-is. Extracting text first (as the old FastAPI backend did)
  // loses the table and column structure that an OFP is almost entirely made of.
  const text = await callGemini({
    apiKey,
    systemInstruction: BRIEFING_SYSTEM_PROMPT,
    jsonOutput: true,
    temperature: 0.2,
    parts: [
      { inlineData: { mimeType: 'application/pdf', data: base64 } },
      {
        text:
          `FILENAME: ${name}\n\n` +
          'Analyze the attached flight operation document and generate the structured pilot briefing JSON.',
      },
    ],
  });

  const briefing = parseJsonResponse(text);

  return {
    success: true,
    briefing,
    document_meta: {
      filename: name,
      page_count: briefing?.document_meta?.page_count ?? null,
      is_sample: false,
    },
  };
}

export async function sendPilotQuestion({ question, briefingContext, apiKey = '' }) {
  const callsign =
    briefingContext?.flight_summary?.callsign ||
    briefingContext?.flight_summary?.flight_number ||
    'FLIGHT';

  const answer = await callGemini({
    apiKey,
    temperature: 0.3,
    parts: [
      {
        text: `You are an expert Flight Operations Assistant & Dispatcher helping a pilot in the cockpit.
Flight Callsign: ${callsign}
The pilot is asking a question regarding their flight documents.

=== STRUCTURED BRIEFING CONTEXT ===
${JSON.stringify(briefingContext ?? {}, null, 2).slice(0, 120000)}

=== PILOT'S QUESTION ===
${question}

Answer concisely, accurately, and authoritatively in Korean, citing relevant ICAO/flight plan data where applicable. Focus on flight safety, fuel management, and operational practicality.`,
      },
    ],
  });

  return { success: true, question, answer };
}
