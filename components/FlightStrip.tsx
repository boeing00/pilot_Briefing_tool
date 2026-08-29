'use client';

import React, { useState } from 'react';
import { Plane, Pencil, Check, X } from 'lucide-react';
import { FlightBriefingData } from '@/types/flight';
import { useFlightBriefing } from '@/context/FlightBriefingContext';

interface FlightStripProps {
  data: FlightBriefingData;
}

export const FlightStrip: React.FC<FlightStripProps> = ({ data }) => {
  const { flightInfo, fuel } = data;
  const { updateFlightTime } = useFlightBriefing();

  const [isEditingEte, setIsEditingEte] = useState(false);
  const [tempEte, setTempEte] = useState(flightInfo.ete || '13:24');

  const plannedTime = flightInfo.plannedEte || '13:24';
  const isTimeModified = flightInfo.ete !== plannedTime;

  const handleSaveEte = () => {
    if (tempEte.trim()) {
      updateFlightTime(tempEte.trim());
    }
    setIsEditingEte(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSaveEte();
    } else if (e.key === 'Escape') {
      setTempEte(flightInfo.ete);
      setIsEditingEte(false);
    }
  };

  return (
    <div className="w-full bg-[#08101e] border border-[#182c4d] rounded-2xl p-5 shadow-2xl mb-6 select-none">
      <div className="flex flex-col xl:flex-row xl:items-center justify-between gap-5">
        {/* Left Side: Flight Identity & Aircraft Details */}
        <div className="flex items-center gap-4">
          {/* Flight Number Badge */}
          <div className="px-4 py-3 rounded-2xl bg-gradient-to-br from-cyan-500/25 to-blue-600/10 border-2 border-cyan-400/50 text-cyan-300 font-mono font-black text-2xl sm:text-3xl tracking-tight shadow-[0_0_20px_rgba(0,229,255,0.2)] flex items-center gap-2.5 shrink-0">
            <Plane className="w-6 h-6 -rotate-45 text-cyan-400" />
            <span>{flightInfo.flightNumber || 'AAR224'}</span>
          </div>

          <div className="space-y-1.5">
            <div className="flex items-center gap-2.5 flex-wrap">
              {flightInfo.callsign && (
                <span className="text-sm font-mono font-bold text-slate-100 bg-[#0d1d36] px-3 py-1 rounded-lg border border-[#1f3d6b] tracking-wide">
                  {flightInfo.callsign}
                </span>
              )}
              <span className="inline-flex items-center gap-1.5 text-xs font-mono font-bold text-emerald-300 bg-emerald-950/90 px-3 py-1 rounded-lg border border-emerald-600/60 shadow-sm">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                DISPATCH RELEASED
              </span>
            </div>

            {/* Aircraft & Config Meta */}
            <div className="flex items-center gap-3 text-sm font-mono text-slate-300 pt-0.5">
              <span>
                A/C: <strong className="text-slate-100 font-extrabold">{flightInfo.aircraftType}</strong>
              </span>
              <span className="text-slate-600 font-bold">•</span>
              <span>
                REG: <strong className="text-cyan-300 font-extrabold">{flightInfo.registration}</strong>
              </span>
              <span className="text-slate-600 font-bold">•</span>
              <span>
                CI: <strong className="text-amber-300 font-extrabold">{flightInfo.costIndex || '65'}</strong>
              </span>
            </div>
          </div>
        </div>

        {/* Right Side: Key Operational Parameters */}
        <div className="grid grid-cols-3 gap-3 sm:gap-6 bg-[#040813] px-6 py-3.5 rounded-2xl border border-[#162744] shadow-inner items-center">
          {/* Planned Cruise */}
          <div className="flex flex-col items-center xl:items-end text-center xl:text-right">
            <span className="text-[11px] font-mono font-bold text-slate-400 uppercase tracking-wider mb-0.5">
              순항고도 (CRZ)
            </span>
            <span className="text-xl sm:text-2xl font-black font-mono text-amber-300 tracking-tight">
              {flightInfo.flightLevel}
            </span>
          </div>

          {/* ETE (Shows both Plan & Adjusted ETE) */}
          <div className="flex flex-col items-center xl:items-end text-center xl:text-right border-x border-[#1a2e4c] px-3 sm:px-6 relative group">
            <div className="flex items-center gap-1 mb-0.5">
              <span className="text-[11px] font-mono font-bold text-slate-400 uppercase tracking-wider">
                {isTimeModified ? '수정 비행시간' : '비행시간 (ETE)'}
              </span>
              {!isEditingEte && (
                <button
                  onClick={() => {
                    setTempEte(flightInfo.ete);
                    setIsEditingEte(true);
                  }}
                  className="opacity-60 hover:opacity-100 text-cyan-400 transition"
                  title="비행시간 직접 수정"
                >
                  <Pencil className="w-3 h-3" />
                </button>
              )}
            </div>

            {isEditingEte ? (
              <div className="flex items-center gap-1.5 mt-0.5">
                <input
                  type="text"
                  value={tempEte}
                  onChange={(e) => setTempEte(e.target.value)}
                  onKeyDown={handleKeyDown}
                  autoFocus
                  placeholder="13:24"
                  className="w-20 px-2 py-0.5 bg-[#0b1c36] border-2 border-cyan-400 rounded-lg text-cyan-300 font-mono text-lg font-black text-center focus:outline-none shadow-[0_0_10px_#00e5ff]"
                />
                <button
                  onClick={handleSaveEte}
                  className="p-1 rounded-md bg-emerald-500 hover:bg-emerald-400 text-slate-950 transition"
                  title="저장"
                >
                  <Check className="w-3.5 h-3.5 stroke-[3]" />
                </button>
                <button
                  onClick={() => setIsEditingEte(false)}
                  className="p-1 rounded-md bg-slate-800 hover:bg-slate-700 text-slate-300 transition"
                  title="취소"
                >
                  <X className="w-3.5 h-3.5" />
                </button>
              </div>
            ) : (
              <div className="flex flex-col items-center xl:items-end">
                <button
                  onClick={() => {
                    setTempEte(flightInfo.ete);
                    setIsEditingEte(true);
                  }}
                  className="text-xl sm:text-2xl font-black font-mono text-cyan-300 tracking-tight hover:text-cyan-200 transition"
                  title="클릭하여 비행시간 수정"
                >
                  {flightInfo.ete}
                </button>
                {/* Plan Time Always Displayed */}
                <span className="text-[10px] font-mono font-bold text-slate-400 mt-0.5">
                  PLN: <strong className="text-slate-300 font-bold">{plannedTime}</strong>
                  {isTimeModified && (
                    <span className="text-amber-400 ml-1">(수정됨)</span>
                  )}
                </span>
              </div>
            )}
          </div>

          {/* Block Fuel */}
          <div className="flex flex-col items-center xl:items-end text-center xl:text-right">
            <span className="text-[11px] font-mono font-bold text-slate-400 uppercase tracking-wider mb-0.5">
              블록 연료 (BLOCK)
            </span>
            <span className="text-xl sm:text-2xl font-black font-mono text-emerald-300 tracking-tight">
              {fuel?.blockFuel?.toLocaleString()} <span className="text-xs font-bold text-emerald-400">{fuel?.unit || 'LBS'}</span>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};
