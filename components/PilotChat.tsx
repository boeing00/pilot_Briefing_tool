'use client';

import React, { useState, useRef, useEffect } from 'react';
import { MessageSquare, Send, Bot, User, Sparkles, Loader2, Compass } from 'lucide-react';
import { useFlightBriefing } from '@/context/FlightBriefingContext';

export const PilotChat: React.FC = () => {
  const { chatMessages, sendChatMessage, isChatLoading, briefingData } = useFlightBriefing();
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const suggestedQuestions = [
    '도착지 활주로 측풍 및 윈드시어 대비 사항은?',
    '가장 중요한 NOTAM 2개만 요약해 줘',
    '교체공항 기상과 착륙 최저치는 문제없어?',
    '연료 여유량(Extra Fuel)으로 체공 가능한 시간은?',
  ];

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [chatMessages, isChatLoading]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isChatLoading) return;
    sendChatMessage(input.trim());
    setInput('');
  };

  const handleSuggestedClick = (q: string) => {
    if (isChatLoading) return;
    sendChatMessage(q);
  };

  return (
    <div className="flex flex-col h-[650px] bg-slate-900/60 border border-slate-800 rounded-2xl overflow-hidden backdrop-blur-sm shadow-xl">
      {/* Header */}
      <div className="px-5 py-3.5 border-b border-slate-800 bg-slate-950/60 flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400">
            <Bot className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold text-slate-100 flex items-center gap-1.5">
              AI 비행 어시스턴트 (Co-Pilot Q&A)
              <Sparkles className="w-3.5 h-3.5 text-cyan-400" />
            </h3>
            <p className="text-[11px] text-slate-400">
              업로드된 문서 기반 실시간 질의응답
            </p>
          </div>
        </div>
      </div>

      {/* Message List */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {chatMessages.map((msg) => {
          const isUser = msg.sender === 'user';
          return (
            <div
              key={msg.id}
              className={`flex gap-3 ${isUser ? 'justify-end' : 'justify-start'}`}
            >
              {!isUser && (
                <div className="w-7 h-7 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 shrink-0 mt-0.5">
                  <Compass className="w-4 h-4" />
                </div>
              )}

              <div
                className={`max-w-[85%] sm:max-w-[75%] rounded-2xl px-4 py-3 text-xs leading-relaxed ${
                  isUser
                    ? 'bg-cyan-500 text-slate-950 font-medium rounded-tr-none shadow-md'
                    : 'bg-slate-950/80 text-slate-200 border border-slate-800 rounded-tl-none space-y-1.5'
                }`}
              >
                <div className="whitespace-pre-wrap">{msg.content}</div>
                <div
                  className={`text-[10px] font-mono mt-1 ${
                    isUser ? 'text-slate-800' : 'text-slate-500'
                  }`}
                >
                  {msg.timestamp}
                </div>
              </div>

              {isUser && (
                <div className="w-7 h-7 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center text-slate-300 shrink-0 mt-0.5">
                  <User className="w-4 h-4" />
                </div>
              )}
            </div>
          );
        })}

        {isChatLoading && (
          <div className="flex gap-3 justify-start items-center">
            <div className="w-7 h-7 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 shrink-0">
              <Loader2 className="w-4 h-4 animate-spin" />
            </div>
            <div className="px-4 py-2.5 rounded-2xl bg-slate-950/80 border border-slate-800 text-xs text-slate-400 font-mono flex items-center gap-2">
              <span>문서를 분석하여 답변을 작성하고 있습니다...</span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Suggested Prompt Chips */}
      {chatMessages.length <= 2 && (
        <div className="px-4 py-2 border-t border-slate-850 bg-slate-950/40 flex items-center gap-2 overflow-x-auto">
          <span className="text-[11px] font-mono text-slate-500 shrink-0">추천 질문:</span>
          {suggestedQuestions.map((q, idx) => (
            <button
              key={idx}
              onClick={() => handleSuggestedClick(q)}
              className="px-2.5 py-1 rounded-full bg-slate-850 hover:bg-slate-800 text-slate-300 text-[11px] border border-slate-750 transition whitespace-nowrap shrink-0"
            >
              {q}
            </button>
          ))}
        </div>
      )}

      {/* Input Box */}
      <form onSubmit={handleSubmit} className="p-3 bg-slate-950 border-t border-slate-800 flex items-center gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="비행계획, 활주로, 기상, 노탐 관련 질문을 입력하세요..."
          disabled={isChatLoading}
          className="flex-1 px-4 py-2.5 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-cyan-500 transition"
        />
        <button
          type="submit"
          disabled={!input.trim() || isChatLoading}
          className="px-4 py-2.5 bg-cyan-500 hover:bg-cyan-400 disabled:opacity-40 disabled:hover:bg-cyan-500 text-slate-950 rounded-xl text-xs font-bold transition flex items-center gap-1.5 shadow-lg shadow-cyan-500/10"
        >
          <Send className="w-3.5 h-3.5" />
          <span>전송</span>
        </button>
      </form>
    </div>
  );
};
