import { useState, useEffect, useCallback } from 'react';
import { uploadFlightPdf, getSampleBriefing } from '../services/api';

const STORAGE_KEY_API_KEY = 'PILOT_BRIEFING_GEMINI_KEY';

export function useBriefing() {
  const [briefing, setBriefing] = useState(null);
  const [docMeta, setDocMeta] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [currentFlight, setCurrentFlight] = useState('KLAX');
  const [apiKey, setApiKeyState] = useState(() => {
    try {
      return localStorage.getItem(STORAGE_KEY_API_KEY) || '';
    } catch {
      return '';
    }
  });

  const setApiKey = useCallback((key) => {
    setApiKeyState(key);
    try {
      if (key) {
        localStorage.setItem(STORAGE_KEY_API_KEY, key);
      } else {
        localStorage.removeItem(STORAGE_KEY_API_KEY);
      }
    } catch (e) {
      console.warn('LocalStorage access failed:', e);
    }
  }, []);

  // Sample briefings are bundled JSON - no network, no key, no spinner worth showing.
  const loadSample = useCallback((flightCode = 'KLAX') => {
    setError(null);
    const data = getSampleBriefing(flightCode);
    setBriefing(data.briefing);
    setDocMeta(data.document_meta);
    setCurrentFlight(flightCode);
  }, []);

  const handleFileUpload = useCallback(async (file) => {
    if (!file) return;
    setLoading(true);
    setError(null);
    try {
      const data = await uploadFlightPdf(file, apiKey);
      setBriefing(data.briefing);
      setDocMeta(data.document_meta);
      const dest = data.briefing?.flight_summary?.destination?.icao;
      if (dest) setCurrentFlight(dest);
    } catch (err) {
      console.error('Failed to process flight PDF:', err);
      setError(err.message || 'PDF 분석 중 오류가 발생했습니다.');
    } finally {
      setLoading(false);
    }
  }, [apiKey]);

  const clearBriefing = useCallback(() => {
    setBriefing(null);
    setDocMeta(null);
    setError(null);
  }, []);

  useEffect(() => {
    loadSample('KLAX');
  }, [loadSample]);

  return {
    briefing,
    docMeta,
    loading,
    error,
    currentFlight,
    apiKey,
    setApiKey,
    hasApiKey: Boolean(apiKey),
    loadSample,
    handleFileUpload,
    clearBriefing,
  };
}
