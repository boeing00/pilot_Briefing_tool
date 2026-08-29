import { useState, useEffect, useCallback } from 'react';
import { uploadFlightPdf, getSampleBriefing, checkHealth } from '../services/api';

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
  const [serverHealth, setServerHealth] = useState(null);

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

  const loadSample = useCallback(async (flightCode = 'KLAX') => {
    setLoading(true);
    setError(null);
    try {
      const data = await getSampleBriefing(flightCode);
      setBriefing(data.briefing);
      setDocMeta(data.document_meta);
      setCurrentFlight(flightCode);
    } catch (err) {
      console.error('Failed to load sample briefing:', err);
      setError(err.message || '샘플 브리핑 로드 실패');
    } finally {
      setLoading(false);
    }
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
    checkHealth()
      .then((res) => setServerHealth(res))
      .catch((err) => console.warn('Server health check error:', err));

    // Auto load the initial flight briefing on mount
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
    serverHealth,
    loadSample,
    handleFileUpload,
    clearBriefing,
  };
}
