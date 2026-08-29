/**
 * API Service for Pilot Briefing Backend
 */

const API_BASE = '/api';

export async function checkHealth() {
  const res = await fetch(`${API_BASE}/health`);
  if (!res.ok) throw new Error('Health check failed');
  return res.json();
}

export async function getSampleBriefing(flight = 'KJFK') {
  const res = await fetch(`${API_BASE}/briefing/sample?flight=${flight}`);
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Failed to fetch sample briefing');
  }
  return res.json();
}

export async function uploadFlightPdf(file, apiKey = '') {
  const formData = new FormData();
  formData.append('file', file);
  if (apiKey) {
    formData.append('api_key', apiKey);
  }

  const res = await fetch(`${API_BASE}/briefing/upload`, {
    method: 'POST',
    body: formData,
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Failed to upload and parse flight PDF');
  }
  return res.json();
}

export async function sendPilotQuestion({ question, briefingContext, rawText = '', apiKey = '' }) {
  const res = await fetch(`${API_BASE}/briefing/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      question,
      briefing_context: briefingContext,
      raw_text: rawText,
      api_key: apiKey || undefined,
    }),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail || 'Failed to submit question');
  }
  return res.json();
}
