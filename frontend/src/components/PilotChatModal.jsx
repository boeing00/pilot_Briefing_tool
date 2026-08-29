import React, { useState, useRef, useEffect } from 'react';
import { MessageSquare, Send, X, Bot, User, Loader2, Sparkles } from 'lucide-react';
import { usePilotChat } from '../hooks/usePilotChat';

const QUICK_QUESTIONS = [
  '목적지 착륙 활주로 상태 및 노탐 요약해줘',
  '대체공항 회항 시 연료 마진은 충분한가요?',
  '항로상 난류(CAT) 발생 예상 지점과 권고 고도는?',
  '이 비행에서 가장 주의해야 할 3대 안전 위협 요소는?',
];

export default function PilotChatModal({ isOpen, onClose, briefing, apiKey, onOpenApiKey = () => {} }) {
  const [inputQuestion, setInputQuestion] = useState('');
  const { messages, isSending, askQuestion, clearChat } = usePilotChat();
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isSending]);

  if (!isOpen) return null;

  const handleSend = (q) => {
    const textToSend = q || inputQuestion;
    if (!textToSend.trim() || isSending) return;
    askQuestion({
      question: textToSend,
      briefingContext: briefing,
      apiKey: apiKey || '',
    });
    setInputQuestion('');
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-end bg-slate-950/70 backdrop-blur-sm animate-fade-in">
      <div className="bg-slate-900 border-l border-slate-800 w-full max-w-lg h-full flex flex-col shadow-2xl">
        {/* Header */}
        <div className="p-4 border-b border-slate-800 flex items-center justify-between bg-slate-950/60">
          <div className="flex items-center gap-2.5">
            <div className="p-2 bg-indigo-500/20 text-indigo-400 rounded-lg border border-indigo-500/30">
              <Bot className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-slate-100 uppercase tracking-wide">
                Cockpit AI Assistant Q&A
              </h3>
              <p className="text-xs text-slate-400">운항 문서 및 실시간 비행 질의응답</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-slate-800 rounded-lg text-slate-400 hover:text-slate-200 transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Quick Suggestion Pills */}
        <div className="p-3 bg-slate-950/40 border-b border-slate-800 overflow-x-auto">
          <span className="text-2xs text-slate-400 uppercase font-mono block mb-1.5 flex items-center gap-1">
            <Sparkles className="w-3 h-3 text-amber-400" />
            조종사 추천 질문
          </span>
          <div className="flex flex-wrap gap-1.5">
            {QUICK_QUESTIONS.map((q, idx) => (
              <button
                key={idx}
                onClick={() => handleSend(q)}
                disabled={isSending}
                className="text-xs px-2.5 py-1 bg-slate-800/90 hover:bg-slate-700 text-slate-300 rounded-full border border-slate-700 transition truncate max-w-full text-left"
              >
                {q}
              </button>
            ))}
          </div>
        </div>

        {/* Message Log */}
        <div className="flex-1 p-4 overflow-y-auto space-y-4">
          {messages.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-center text-slate-500 p-6">
              <Bot className="w-12 h-12 mb-3 text-slate-600" />
              <p className="text-sm font-medium text-slate-300">비행 문서에 대해 무엇이든 질문하세요</p>
              <p className="text-xs text-slate-500 mt-1 max-w-xs">
                목적지 기상 최저치, 윈드시어, 활주로 노탐, 대체공항 및 연료 여유량 등에 대해 신속히 답변해 드립니다.
              </p>
            </div>
          ) : (
            messages.map((msg) => (
              <div
                key={msg.id}
                className={`flex gap-3 ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                {msg.role === 'assistant' && (
                  <div className="p-1.5 bg-indigo-900/40 text-indigo-300 border border-indigo-800/50 rounded-lg h-7 w-7 flex items-center justify-center shrink-0 mt-0.5">
                    <Bot className="w-4 h-4" />
                  </div>
                )}
                <div
                  className={`max-w-[82%] rounded-xl p-3 text-xs leading-relaxed ${
                    msg.role === 'user'
                      ? 'bg-blue-600 text-white shadow-md'
                      : msg.isError
                      ? 'bg-rose-950/60 text-rose-200 border border-rose-800/60'
                      : 'bg-slate-800 text-slate-200 border border-slate-700/80 shadow-md'
                  }`}
                >
                  <p className="whitespace-pre-wrap">{msg.text}</p>
                  <span className="text-2xs opacity-60 block mt-1 text-right font-mono">
                    {msg.timestamp}
                  </span>
                </div>
                {msg.role === 'user' && (
                  <div className="p-1.5 bg-blue-900/40 text-blue-300 border border-blue-800/50 rounded-lg h-7 w-7 flex items-center justify-center shrink-0 mt-0.5">
                    <User className="w-4 h-4" />
                  </div>
                )}
              </div>
            ))
          )}

          {isSending && (
            <div className="flex gap-3 justify-start">
              <div className="p-1.5 bg-indigo-900/40 text-indigo-300 border border-indigo-800/50 rounded-lg h-7 w-7 flex items-center justify-center shrink-0">
                <Bot className="w-4 h-4" />
              </div>
              <div className="bg-slate-800 border border-slate-700/80 rounded-xl p-3 text-xs text-slate-300 flex items-center gap-2">
                <Loader2 className="w-4 h-4 animate-spin text-blue-400" />
                <span>운항 문서를 대조하여 답변을 생성 중입니다...</span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Bar */}
        <div className="p-3 border-t border-slate-800 bg-slate-950">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSend();
            }}
            className="flex items-center gap-2"
          >
            <input
              type="text"
              value={inputQuestion}
              onChange={(e) => setInputQuestion(e.target.value)}
              placeholder="조종사용 질문 입력 (예: 목적지 24R ILS 가능 여부)"
              disabled={isSending}
              className="flex-1 bg-slate-900 border border-slate-700 rounded-lg px-3.5 py-2 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-blue-500 transition"
            />
            <button
              type="submit"
              disabled={isSending || !inputQuestion.trim()}
              className="p-2 bg-blue-600 hover:bg-blue-500 text-white rounded-lg transition disabled:opacity-50"
            >
              <Send className="w-4 h-4" />
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
