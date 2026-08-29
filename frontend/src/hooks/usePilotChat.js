import { useState, useCallback } from 'react';
import { sendPilotQuestion } from '../services/api';

export function usePilotChat() {
  const [messages, setMessages] = useState([]);
  const [isSending, setIsSending] = useState(false);
  const [error, setError] = useState(null);

  const askQuestion = useCallback(async ({ question, briefingContext, apiKey }) => {
    if (!question.trim()) return;

    const userMessageId = Date.now().toString();
    const userMsg = {
      id: userMessageId,
      role: 'user',
      text: question,
      timestamp: new Date().toLocaleTimeString(),
    };

    setMessages((prev) => [...prev, userMsg]);
    setIsSending(true);
    setError(null);

    try {
      const res = await sendPilotQuestion({
        question,
        briefingContext,
        apiKey,
      });

      const assistantMsg = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        text: res.answer,
        timestamp: new Date().toLocaleTimeString(),
      };

      setMessages((prev) => [...prev, assistantMsg]);
    } catch (err) {
      const errorMsg = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        text: `[오류] 답변을 불러오지 못했습니다: ${err.message}`,
        timestamp: new Date().toLocaleTimeString(),
        isError: true,
      };
      setMessages((prev) => [...prev, errorMsg]);
      setError(err.message);
    } finally {
      setIsSending(false);
    }
  }, []);

  const clearChat = useCallback(() => {
    setMessages([]);
    setError(null);
  }, []);

  return {
    messages,
    isSending,
    error,
    askQuestion,
    clearChat,
  };
}
