'use client';

import React, { useState } from 'react';
import { ShieldAlert, AlertTriangle, AlertCircle, Info, Filter, CheckCircle2, ChevronRight } from 'lucide-react';
import { HazardItem, HazardLevel, HazardCategory } from '@/types/flight';

interface HazardAlertsProps {
  hazards: HazardItem[];
}

export const HazardAlerts: React.FC<HazardAlertsProps> = ({ hazards }) => {
  const [filterLevel, setFilterLevel] = useState<string>('ALL');

  const filteredHazards = hazards.filter((h) => {
    if (filterLevel === 'ALL') return true;
    return h.level === filterLevel;
  });

  const getLevelStyle = (level: HazardLevel) => {
    switch (level) {
      case 'CRITICAL':
        return {
          badge: 'bg-rose-500/20 text-rose-300 border-rose-500/40',
          border: 'border-rose-800/80 bg-rose-950/20',
          icon: <AlertCircle className="w-5 h-5 text-rose-400 shrink-0" />,
        };
      case 'WARNING':
        return {
          badge: 'bg-amber-500/20 text-amber-300 border-amber-500/40',
          border: 'border-amber-800/80 bg-amber-950/20',
          icon: <AlertTriangle className="w-5 h-5 text-amber-400 shrink-0" />,
        };
      case 'INFO':
        return {
          badge: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/40',
          border: 'border-cyan-800/80 bg-cyan-950/20',
          icon: <Info className="w-5 h-5 text-cyan-400 shrink-0" />,
        };
    }
  };

  const getCategoryBadge = (category: HazardCategory) => {
    switch (category) {
      case 'WEATHER':
        return 'bg-blue-950 text-blue-300 border-blue-800';
      case 'NOTAM':
        return 'bg-purple-950 text-purple-300 border-purple-800';
      case 'AIRPORT':
        return 'bg-emerald-950 text-emerald-300 border-emerald-800';
      case 'EQUIPMENT':
        return 'bg-orange-950 text-orange-300 border-orange-800';
      default:
        return 'bg-slate-800 text-slate-300 border-slate-700';
    }
  };

  return (
    <div className="space-y-4">
      {/* Header & Filter */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-2 border-b border-slate-800">
        <div className="flex items-center gap-2">
          <ShieldAlert className="w-5 h-5 text-amber-400" />
          <h3 className="text-base font-bold text-slate-100">위험 및 주의사항 (Hazards & Alerts)</h3>
          <span className="px-2 py-0.5 rounded-full text-xs font-mono font-bold bg-slate-800 text-slate-300">
            {hazards.length}건
          </span>
        </div>

        <div className="flex items-center gap-1.5 text-xs font-mono">
          <Filter className="w-3.5 h-3.5 text-slate-400" />
          {['ALL', 'CRITICAL', 'WARNING', 'INFO'].map((lvl) => (
            <button
              key={lvl}
              onClick={() => setFilterLevel(lvl)}
              className={`px-2.5 py-1 rounded-md transition ${
                filterLevel === lvl
                  ? 'bg-cyan-500 text-slate-950 font-bold'
                  : 'bg-slate-800 text-slate-400 hover:bg-slate-700'
              }`}
            >
              {lvl}
            </button>
          ))}
        </div>
      </div>

      {/* Hazard Cards Grid */}
      {filteredHazards.length === 0 ? (
        <div className="p-8 text-center bg-slate-900/30 rounded-2xl border border-slate-800 text-slate-400 text-xs">
          선택한 필터 조건에 해당하는 위험 항목이 없습니다.
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-3.5">
          {filteredHazards.map((item) => {
            const style = getLevelStyle(item.level);
            return (
              <div
                key={item.id}
                className={`p-4 rounded-xl border ${style.border} transition-all duration-200 hover:border-slate-700 space-y-2`}
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="flex items-center gap-2 flex-wrap">
                    {style.icon}
                    <span className={`px-2 py-0.5 rounded text-[11px] font-mono font-bold border ${style.badge}`}>
                      {item.level}
                    </span>
                    <span className={`px-2 py-0.5 rounded text-[11px] font-mono border ${getCategoryBadge(item.category)}`}>
                      {item.category}
                    </span>
                    <h4 className="text-sm font-bold text-slate-100">{item.title}</h4>
                  </div>
                  <span className="text-[11px] font-mono text-slate-500 shrink-0">{item.id}</span>
                </div>

                <p className="text-xs text-slate-300 leading-relaxed pl-7">
                  {item.description}
                </p>

                {item.recommendation && (
                  <div className="ml-7 mt-2 p-2.5 rounded-lg bg-slate-950/60 border border-slate-850 flex items-start gap-2 text-xs">
                    <CheckCircle2 className="w-3.5 h-3.5 text-cyan-400 shrink-0 mt-0.5" />
                    <div>
                      <span className="text-cyan-400 font-semibold font-mono text-[11px]">권장 조치: </span>
                      <span className="text-slate-300">{item.recommendation}</span>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
