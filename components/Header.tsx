'use client';

import React, { useState } from 'react';
import { Plane, Key, RefreshCw } from 'lucide-react';
import { useFlightBriefing } from '@/context/FlightBriefingContext';
import { AudioBriefingButton } from './AudioBriefingButton';

export const Header: React.FC = () => {
  const { briefingData, resetData, apiKey, setApiKey } = useFlightBriefing();
  const [showKeyModal, setShowKeyModal] = useState(false);
  const [tempKey, setTempKey] = useState(apiKey);

  const handleSaveKey = () => {
    setApiKey(tempKey.trim());
    setShowKeyModal(false);
  };

  return (
    <>
      <header className="sticky top-0 z-40 w-full border-b border-slate-800 bg-slate-950/85 backdrop-blur-md px-4 lg:px-8 py-3.5">
        <div className="max-w-7xl mx-auto flex items-center justify-between gap-4">
          {/* Logo & Title */}
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 shadow-inner">
              <Plane className="w-5 h-5 -rotate-45" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-lg font-bold text-slate-100 tracking-tight">
                  Pilot Briefing
                </h1>
                {briefingData && (
                  <span className="font-mono text-xs font-bold text-amber-300 bg-amber-950/60 px-2 py-0.5 rounded border border-amber-800/40">
                    {briefingData.flightInfo.flightNumber}
                  </span>
                )}
              </div>
              <p className="text-[11px] text-slate-400 font-medium">
                {briefingData
                  ? `${briefingData.flightInfo.origin.icao} → ${briefingData.flightInfo.destination.icao} • FLIGHT BRIEFING`
                  : 'AI 비행 문서 분석 및 운항 브리핑'}
              </p>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex items-center gap-2">
            {briefingData?.spokenBriefingScript && (
              <AudioBriefingButton script={briefingData.spokenBriefingScript} />
            )}

            {briefingData && (
              <button
                onClick={resetData}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800 transition"
              >
                <RefreshCw className="w-3.5 h-3.5 text-slate-400" />
                <span>새 문서 분석</span>
              </button>
            )}

            <button
              onClick={() => {
                setTempKey(apiKey);
                setShowKeyModal(true);
              }}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition border ${
                apiKey
                  ? 'bg-slate-900 text-emerald-400 border-emerald-500/30 hover:bg-slate-800'
                  : 'bg-slate-900 text-slate-300 border-slate-750 hover:bg-slate-800'
              }`}
              title="Gemini API Key 설정"
            >
              <Key className="w-3.5 h-3.5 text-amber-400" />
              <span>{apiKey ? 'API 키 등록됨' : 'API 키 설정'}</span>
            </button>
          </div>
        </div>
      </header>

      {/* API Key Modal */}
      {showKeyModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4 animate-in fade-in">
          <div className="w-full max-w-md bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-2xl text-slate-100">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2 text-cyan-400">
                <Key className="w-5 h-5 text-amber-400" />
                <h3 className="text-lg font-bold text-slate-100">Gemini API Key 설정</h3>
              </div>
              <button
                onClick={() => setShowKeyModal(false)}
                className="text-slate-400 hover:text-slate-200 text-sm"
              >
                ✕
              </button>
            </div>

            <p className="text-xs text-slate-400 mb-4 leading-relaxed">
              Google AI Studio에서 발급받은 Gemini API 키를 입력하세요. 브라우저 로컬 스토리지에 안전하게 저장됩니다.
            </p>

            <div className="space-y-3">
              <input
                type="password"
                value={tempKey}
                onChange={(e) => setTempKey(e.target.value)}
                placeholder="AIzaSy..."
                className="w-full px-3.5 py-2.5 bg-slate-950 border border-slate-750 rounded-xl text-sm font-mono text-slate-100 focus:outline-none focus:border-cyan-500 transition"
              />

              <div className="flex justify-end gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowKeyModal(false)}
                  className="px-4 py-2 rounded-xl text-xs font-medium text-slate-400 hover:bg-slate-800"
                >
                  취소
                </button>
                <button
                  type="button"
                  onClick={handleSaveKey}
                  className="px-4 py-2 rounded-xl text-xs font-semibold bg-cyan-500 hover:bg-cyan-400 text-slate-950 transition"
                >
                  저장하기
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};
