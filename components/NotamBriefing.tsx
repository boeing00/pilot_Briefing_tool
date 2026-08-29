'use client';

import React, { useState } from 'react';
import { FileWarning, Search, Filter, AlertCircle, ChevronDown, ChevronUp } from 'lucide-react';
import { NotamItem } from '@/types/flight';

interface NotamBriefingProps {
  notams: NotamItem[];
}

export const NotamBriefing: React.FC<NotamBriefingProps> = ({ notams }) => {
  const [categoryFilter, setCategoryFilter] = useState<string>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [expandedId, setExpandedId] = useState<string | null>(null);

  const categories = ['ALL', 'RUNWAY', 'TWY', 'NAVAID', 'AIRSPACE', 'GENERAL'];

  const filteredNotams = notams.filter((n) => {
    const matchesCategory = categoryFilter === 'ALL' || n.category === categoryFilter;
    const matchesQuery =
      searchQuery === '' ||
      n.id.toLowerCase().includes(searchQuery.toLowerCase()) ||
      n.plainSummary.toLowerCase().includes(searchQuery.toLowerCase()) ||
      n.location.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesQuery;
  });

  const getSeverityBadge = (severity: 'HIGH' | 'MEDIUM' | 'LOW') => {
    switch (severity) {
      case 'HIGH':
        return 'bg-rose-500/20 text-rose-300 border-rose-500/40';
      case 'MEDIUM':
        return 'bg-amber-500/20 text-amber-300 border-amber-500/40';
      case 'LOW':
        return 'bg-slate-800 text-slate-300 border-slate-700';
    }
  };

  return (
    <div className="space-y-4">
      {/* Filters & Search */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-2 border-b border-slate-800">
        <div className="flex items-center gap-2">
          <FileWarning className="w-5 h-5 text-purple-400" />
          <h3 className="text-base font-bold text-slate-100">NOTAM 스마트 분석</h3>
          <span className="px-2 py-0.5 rounded-full text-xs font-mono font-bold bg-slate-800 text-slate-300">
            총 {notams.length}건
          </span>
        </div>

        <div className="flex items-center gap-2">
          <div className="relative">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="검색어 또는 공항 ICAO..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-8 pr-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-200 focus:outline-none focus:border-cyan-500 w-48 sm:w-60"
            />
          </div>
        </div>
      </div>

      {/* Category Pills */}
      <div className="flex items-center gap-1.5 overflow-x-auto pb-1 text-xs font-mono">
        <Filter className="w-3.5 h-3.5 text-slate-400 shrink-0" />
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => setCategoryFilter(cat)}
            className={`px-2.5 py-1 rounded-md transition shrink-0 ${
              categoryFilter === cat
                ? 'bg-purple-600 text-white font-bold'
                : 'bg-slate-850 text-slate-400 hover:bg-slate-800'
            }`}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* NOTAM Cards */}
      {filteredNotams.length === 0 ? (
        <div className="p-8 text-center bg-slate-900/30 rounded-2xl border border-slate-800 text-slate-400 text-xs">
          해당 조건의 NOTAM이 없습니다.
        </div>
      ) : (
        <div className="space-y-3">
          {filteredNotams.map((notam) => {
            const isExpanded = expandedId === notam.id;
            return (
              <div
                key={notam.id}
                className={`p-4 rounded-xl border transition-all ${
                  notam.isCritical
                    ? 'border-rose-800/80 bg-rose-950/20 shadow-md'
                    : 'border-slate-800 bg-slate-900/50 hover:border-slate-750'
                }`}
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="space-y-1">
                    <div className="flex items-center gap-2 flex-wrap">
                      <span className="px-2 py-0.5 rounded text-[11px] font-mono font-bold bg-slate-800 text-cyan-300 border border-slate-700">
                        {notam.location}
                      </span>
                      <span className={`px-2 py-0.5 rounded text-[11px] font-mono font-bold border ${getSeverityBadge(notam.severity)}`}>
                        {notam.severity}
                      </span>
                      <span className="px-2 py-0.5 rounded text-[11px] font-mono bg-purple-950 text-purple-300 border border-purple-800/60">
                        {notam.category}
                      </span>
                      <span className="text-xs font-mono font-semibold text-slate-300">{notam.id}</span>
                    </div>

                    <p className="text-sm font-semibold text-slate-100 pt-1 leading-snug">
                      {notam.plainSummary}
                    </p>
                  </div>

                  <button
                    onClick={() => setExpandedId(isExpanded ? null : notam.id)}
                    className="text-slate-400 hover:text-slate-200 p-1 rounded hover:bg-slate-800 transition shrink-0"
                    title="원문 보기"
                  >
                    {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                  </button>
                </div>

                {/* Raw Text Accordion */}
                {isExpanded && (
                  <div className="mt-3 pt-3 border-t border-slate-800/80 space-y-1">
                    <span className="text-[11px] font-mono text-slate-500 font-semibold">RAW NOTAM TEXT:</span>
                    <pre className="p-3 rounded-lg bg-slate-950 text-xs font-mono text-amber-300 whitespace-pre-wrap border border-slate-850">
                      {notam.rawText}
                    </pre>
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
