'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import { FlightBriefingData, ChatMessage } from '@/types/flight';
import { EfbTab } from '@/types/sidebar';
import { DEMO_FLIGHT_BRIEFING } from '@/lib/demoData';

interface FlightBriefingContextType {
  briefingData: FlightBriefingData | null;
  isLoading: boolean;
  loadingStage: string;
  error: string | null;
  apiKey: string;
  setApiKey: (key: string) => void;
  activeTab: EfbTab;
  setActiveTab: (tab: EfbTab) => void;
  uploadPdf: (file: File) => Promise<void>;
  loadDemo: () => void;
  resetData: () => void;
  updateFlightTime: (newEte: string) => void;
  chatMessages: ChatMessage[];
  isChatLoading: boolean;
  sendChatMessage: (messageText: string) => Promise<void>;
}

const FlightBriefingContext = createContext<FlightBriefingContextType | undefined>(undefined);

export function FlightBriefingProvider({ children }: { children: React.ReactNode }) {
  const [briefingData, setBriefingData] = useState<FlightBriefingData | null>(DEMO_FLIGHT_BRIEFING);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [loadingStage, setLoadingStage] = useState<string>('');
  const [error, setError] = useState<string | null>(null);
  const [apiKey, setApiKeyState] = useState<string>('');
  const [activeTab, setActiveTab] = useState<EfbTab>('BRIEF');
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([
    {
      id: 'welcome-demo',
      sender: 'assistant',
      content: '안녕하십니까 기장님! AAR224 (인천 -> 뉴욕 JFK) 비행 브리핑이 준비되었습니다.',
      timestamp: '09:11',
    },
  ]);
  const [isChatLoading, setIsChatLoading] = useState<boolean>(false);

  useEffect(() => {
    const savedKey = localStorage.getItem('pilot_gemini_api_key');
    if (savedKey) setApiKeyState(savedKey);
  }, []);

  const setApiKey = (key: string) => {
    setApiKeyState(key);
    if (key) {
      localStorage.setItem('pilot_gemini_api_key', key);
    } else {
      localStorage.removeItem('pilot_gemini_api_key');
    }
  };

  const updateFlightTime = (newEte: string) => {
    if (!briefingData) return;
    setBriefingData((prev) => {
      if (!prev) return null;
      return {
        ...prev,
        flightInfo: {
          ...prev.flightInfo,
          ete: newEte,
        },
      };
    });
  };

  const uploadPdf = async (file: File) => {
    setIsLoading(true);
    setError(null);
    setLoadingStage('문서 업로드 및 AI 분석 준비 중...');

    try {
      const formData = new FormData();
      formData.append('file', file);
      if (apiKey) formData.append('apiKey', apiKey);

      setLoadingStage('Gemini AI가 비행계획서, 기상, NOTAM을 심층 분석하고 있습니다...');

      const res = await fetch('/api/analyze-flight', {
        method: 'POST',
        body: formData,
      });

      const json = await res.json();
      if (!res.ok || !json.success) {
        throw new Error(json.error || '문서 분석에 실패했습니다.');
      }

      setBriefingData(json.data);
      setActiveTab('BRIEF');
      setChatMessages([
        {
          id: 'welcome',
          sender: 'assistant',
          content: `안녕하십니까 기장님! 편명 **${json.data.flightInfo.flightNumber || 'FLIGHT'}** 분석이 완료되었습니다. 무엇이든 질문해 주십시오.`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        },
      ]);
    } catch (err: any) {
      console.error(err);
      setError(err.message || '파일 처리 중 오류가 발생했습니다.');
    } finally {
      setIsLoading(false);
      setLoadingStage('');
    }
  };

  const loadDemo = () => {
    setError(null);
    setBriefingData(DEMO_FLIGHT_BRIEFING);
    setActiveTab('BRIEF');
  };

  const resetData = () => {
    setBriefingData(null);
    setError(null);
    setChatMessages([]);
    setActiveTab('BRIEF');
  };

  const sendChatMessage = async (messageText: string) => {
    if (!messageText.trim() || !briefingData) return;

    const userMsg: ChatMessage = {
      id: Date.now().toString(),
      sender: 'user',
      content: messageText,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };

    setChatMessages((prev) => [...prev, userMsg]);
    setIsChatLoading(true);

    try {
      const history = chatMessages.map((m) => ({
        role: (m.sender === 'user' ? 'user' : 'model') as 'user' | 'model',
        text: m.content,
      }));

      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          briefingContext: briefingData,
          question: messageText,
          history,
          apiKey,
        }),
      });

      const json = await res.json();
      if (!res.ok || !json.success) {
        throw new Error(json.error || '답변 수신 실패');
      }

      const botMsg: ChatMessage = {
        id: (Date.now() + 1).toString(),
        sender: 'assistant',
        content: json.answer,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };

      setChatMessages((prev) => [...prev, botMsg]);
    } catch (err: any) {
      setChatMessages((prev) => [
        ...prev,
        {
          id: (Date.now() + 1).toString(),
          sender: 'assistant',
          content: `⚠️ 오류: ${err.message || '답변을 불러오지 못했습니다.'}`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        },
      ]);
    } finally {
      setIsChatLoading(false);
    }
  };

  return (
    <FlightBriefingContext.Provider
      value={{
        briefingData,
        isLoading,
        loadingStage,
        error,
        apiKey,
        setApiKey,
        activeTab,
        setActiveTab,
        uploadPdf,
        loadDemo,
        resetData,
        updateFlightTime,
        chatMessages,
        isChatLoading,
        sendChatMessage,
      }}
    >
      {children}
    </FlightBriefingContext.Provider>
  );
}

export function useFlightBriefing() {
  const context = useContext(FlightBriefingContext);
  if (!context) {
    throw new Error('useFlightBriefing must be used within a FlightBriefingProvider');
  }
  return context;
}
