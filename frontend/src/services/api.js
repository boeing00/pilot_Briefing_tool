/**
 * API Service for Pilot Briefing Backend
 */

const API_BASE = import.meta.env.VITE_API_BASE_URL
  ? `${import.meta.env.VITE_API_BASE_URL.replace(/\/$/, '')}/api`
  : '/api';

export async function checkHealth() {
  try {
    const res = await fetch(`${API_BASE}/health`);
    if (!res.ok) throw new Error('Health check failed');
    return await res.json();
  } catch (e) {
    return { status: 'offline', local_demo: true };
  }
}

export async function getSampleBriefing(flight = 'KLAX') {
  try {
    const res = await fetch(`${API_BASE}/briefing/sample?flight=${flight}`);
    if (res.ok) {
      return await res.json();
    }
  } catch (err) {
    console.warn('Backend unavailable, using static client demo data:', err);
  }
  
  // Return rich mock fallback if static host
  return {
    filename: `${flight}_SAMPLE_RELEASE.pdf`,
    document_meta: {
      callsign: flight === 'KLAX' ? 'AAR202' : 'AAR224',
      origin: 'RKSI',
      destination: flight,
      aircraft: flight === 'KLAX' ? 'A350-900 (HL8078)' : 'A380-800 (HL7625)',
      pages_analyzed: 42,
    },
    briefing: {
      flight_summary: {
        flight_number: flight === 'KLAX' ? 'AAR202' : 'AAR224',
        aircraft_type: flight === 'KLAX' ? 'A350-900 (HL8078)' : 'A380-800 (HL7625)',
        departure: { icao: 'RKSI', iata: 'ICN', name: 'Incheon Intl', scheduled_out: '05:30Z' },
        destination: { icao: flight, iata: flight === 'KLAX' ? 'LAX' : 'JFK', name: flight === 'KLAX' ? 'Los Angeles Intl' : 'John F Kennedy Intl', scheduled_in: '10:42Z' },
        alternate: { icao: flight === 'KLAX' ? 'KSAN' : 'KBOS', name: flight === 'KLAX' ? 'San Diego Intl' : 'Boston Logan Intl' },
        cruising_altitude: 'FL350 ~ 390',
        flight_time: flight === 'KLAX' ? '10Hr 42Min' : '13Hr 24Min',
        total_distance: flight === 'KLAX' ? '5,980 NM' : '6,663 NM',
      }
    }
  };
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
