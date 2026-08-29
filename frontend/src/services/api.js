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

/**
 * Gemini itself allows 50MB / 1000 pages, but the browser has to hold the file,
 * its base64 expansion (+33%) and the JSON request body at once. On a tablet
 * that is the binding limit, not the API's.
 */
const MAX_PDF_BYTES = 20 * 1024 * 1024;

/** A long OFP takes 1-3 minutes; fail with a message rather than spin forever. */
const REQUEST_TIMEOUT_MS = 5 * 60 * 1000;

/** models/gemini-2.5-flash reports outputTokenLimit 65536. Thinking shares it. */
const MAX_OUTPUT_TOKENS = 65536;
const THINKING_BUDGET = 4096;

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
  // structuredClone is Safari 15.4+; an older iPad would otherwise fail on load.
  return typeof structuredClone === 'function'
    ? structuredClone(sample)
    : JSON.parse(JSON.stringify(sample));
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
      // The model's ceiling, asked for explicitly. A full OFP briefing runs to
      // thousands of tokens of JSON and the default cap is lower than this.
      maxOutputTokens: MAX_OUTPUT_TOKENS,
      // Thinking is on by default and its tokens come out of the same budget -
      // a real OFP was spending ~4k of it before a single character of JSON.
      // Bounded rather than disabled: some reasoning helps on a dense document.
      thinkingConfig: { thinkingBudget: THINKING_BUDGET },
      ...(jsonOutput ? { responseMimeType: 'application/json' } : {}),
    },
    ...(systemInstruction
      ? { systemInstruction: { parts: [{ text: systemInstruction }] } }
      : {}),
  };

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  let wentHidden = false;
  const onHide = () => { if (document.hidden) wentHidden = true; };
  document.addEventListener('visibilitychange', onHide);

  let res;
  try {
    res = await fetch(`${GEMINI_ENDPOINT}?key=${encodeURIComponent(apiKey)}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
      signal: controller.signal,
    });
  } catch (err) {
    if (wentHidden) {
      throw new Error(
        '분석 중 화면이 꺼지거나 다른 앱으로 전환되어 요청이 중단되었습니다. ' +
        '분석이 끝날 때까지 화면을 켠 채로 이 탭에 머물러 주세요.'
      );
    }
    if (err?.name === 'AbortError') {
      throw new Error(
        `응답이 ${Math.round(REQUEST_TIMEOUT_MS / 60000)}분 안에 오지 않아 중단했습니다. ` +
        '문서가 매우 길면 페이지 수를 줄여 다시 시도해 주세요.'
      );
    }
    throw new Error('Gemini에 연결하지 못했습니다. 네트워크 상태를 확인해 주세요.');
  } finally {
    clearTimeout(timer);
    document.removeEventListener('visibilitychange', onHide);
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
  return { text, finishReason: candidate?.finishReason };
}

/**
 * Closes a JSON document that was cut off mid-flight.
 *
 * A long release package can outrun the output ceiling part way through
 * notam_list, and throwing all of it away leaves the pilot with nothing. Walk to
 * the last structurally complete value, then shut the open containers. Anything
 * recovered is flagged so the UI can say the briefing is partial.
 */
function salvageTruncatedJson(raw) {
  const stack = [];
  let inString = false;
  let escaped = false;
  let cut = -1;
  let cutStack = null;

  for (let i = 0; i < raw.length; i += 1) {
    const ch = raw[i];
    if (inString) {
      if (escaped) escaped = false;
      else if (ch === '\\') escaped = true;
      else if (ch === '"') inString = false;
      continue;
    }
    if (ch === '"') { inString = true; continue; }
    if (ch === '{' || ch === '[') { stack.push(ch === '{' ? '}' : ']'); continue; }
    if (ch === '}' || ch === ']') {
      stack.pop();
      // A complete container: everything up to here can stand on its own.
      cut = i + 1;
      cutStack = stack.slice();
    }
  }

  if (cut < 0 || !cutStack || cutStack.length === 0) return null;
  const closers = cutStack.reverse().join('');
  try {
    return JSON.parse(raw.slice(0, cut) + closers);
  } catch {
    return null;
  }
}

/** Gemini occasionally wraps JSON in a markdown fence even in JSON mode. */
function parseJsonResponse(text, finishReason) {
  let cleaned = text.trim();
  if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/, '').trim();
  }
  try {
    return JSON.parse(cleaned);
  } catch {
    // Nearly always this is a document that outran the output ceiling rather
    // than a malformed answer. Recover what completed before saying no.
    const salvaged = salvageTruncatedJson(cleaned);
    if (salvaged) {
      salvaged.__truncated = true;
      return salvaged;
    }
    if (finishReason === 'MAX_TOKENS') {
      throw new Error(
        '문서가 너무 길어 브리핑이 생성 한도를 초과했습니다. NOTAM 묶음을 덜어내거나 ' +
        '필요한 구간만 나눠서 업로드해 주세요.'
      );
    }
    throw new Error(
      `Gemini 응답을 브리핑 데이터로 해석하지 못했습니다${finishReason ? ` (${finishReason})` : ''}. 다시 시도해 주세요.`
    );
  }
}

export async function uploadFlightPdf(file, apiKey = '') {
  // Fail before reading the file, not after. The key lives in this browser's
  // localStorage, so a key entered on another device is not present here.
  if (!apiKey) {
    throw new Error(
      'Gemini API Key가 이 기기에 등록되어 있지 않습니다. 키는 기기마다 따로 저장되므로 ' +
      '우측 상단 [API Key]에서 이 기기에도 입력해 주세요.'
    );
  }

  const name = file?.name || '';
  if (!/\.pdf$/i.test(name) && file?.type !== 'application/pdf') {
    throw new Error('PDF 파일만 분석할 수 있습니다.');
  }
  if (file.size > MAX_PDF_BYTES) {
    throw new Error(
      `PDF 용량이 너무 큽니다 (${(file.size / 1024 / 1024).toFixed(1)}MB). 20MB 이하 파일을 사용해 주세요.`
    );
  }

  const base64 = await fileToBase64(file);

  // The PDF goes to Gemini as-is. Extracting text first (as the old FastAPI backend did)
  // loses the table and column structure that an OFP is almost entirely made of.
  const { text, finishReason } = await callGemini({
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

  const briefing = parseJsonResponse(text, finishReason);

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

  const { text: answer } = await callGemini({
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
