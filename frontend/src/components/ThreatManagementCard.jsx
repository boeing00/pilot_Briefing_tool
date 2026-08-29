import React from 'react';
import { ShieldAlert, CheckSquare, ArrowRight } from 'lucide-react';

export default function ThreatManagementCard({ data }) {
  if (!data) return null;

  const { top_threats, pilot_action_items, briefing_points } = data;

  return (
    <div id="section-tem" className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-xl space-y-6 font-mono">
      {/* Header */}
      <div className="flex flex-wrap items-center justify-between gap-3 pb-5 border-b border-slate-800">
        <div className="flex items-center gap-3.5">
          <div className="p-3 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
            <ShieldAlert className="w-7 h-7" />
          </div>
          <div>
            <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
              THREAT & ERROR MANAGEMENT (TEM)
            </h3>
          </div>
        </div>
        <span className="text-xs sm:text-sm font-bold px-3.5 py-1.5 bg-slate-950 border border-slate-700 text-slate-300 rounded-lg shadow-sm shrink-0">
          TOP OPERATIONAL RISKS
        </span>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Identified Threats & Mitigations */}
        <div className="space-y-4">
          <span className="text-xs sm:text-sm font-bold text-slate-200 bg-slate-950 border border-slate-700 px-3 py-1.5 rounded-lg uppercase tracking-wider inline-block">
            IDENTIFIED OPERATIONAL THREATS & MITIGATIONS
          </span>

          {top_threats && top_threats.length > 0 ? (
            <div className="space-y-4">
              {top_threats.map((t, idx) => (
                <div
                  key={idx}
                  className="bg-slate-950/80 border border-slate-800 rounded-2xl p-5 space-y-3.5 shadow-inner"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="flex items-start gap-3">
                      <span className="w-7 h-7 rounded-lg bg-slate-900 text-slate-200 border border-slate-700 text-xs sm:text-sm font-bold flex items-center justify-center shrink-0 mt-0.5">
                        {idx + 1}
                      </span>
                      <span className="text-base sm:text-lg font-bold text-white leading-snug">{t.threat}</span>
                    </div>
                    {t.impact && (
                      <span className="px-2.5 py-1 bg-slate-900 border border-slate-700 text-xs font-bold rounded-lg text-slate-300 shrink-0">
                        {t.impact}
                      </span>
                    )}
                  </div>

                  <div className="bg-slate-900 p-4 rounded-xl text-sm sm:text-base text-slate-200 flex items-start gap-3 border border-slate-800">
                    <ArrowRight className="w-5 h-5 text-slate-400 shrink-0 mt-0.5" />
                    <div className="space-y-1">
                      <strong className="text-slate-300 font-bold block text-xs sm:text-sm">[경감 조치 / Mitigation]</strong>
                      <span className="leading-relaxed text-slate-300">{t.mitigation}</span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-sm sm:text-base text-slate-400 italic bg-slate-950/40 p-5 rounded-xl border border-slate-800">
              특이 위험 요소 없음
            </p>
          )}
        </div>

        {/* Pilot Action Items & Crew Briefing */}
        <div className="space-y-5">
          {/* Action Items */}
          <div className="space-y-4">
            <span className="text-xs sm:text-sm font-bold text-slate-200 bg-slate-950 border border-slate-700 px-3 py-1.5 rounded-lg uppercase tracking-wider inline-block">
              PILOT PREFLIGHT ACTION ITEMS
            </span>

            {pilot_action_items && pilot_action_items.length > 0 ? (
              <div className="bg-slate-950/80 border border-slate-800 rounded-2xl p-5 space-y-3 shadow-inner">
                {pilot_action_items.map((item, idx) => (
                  <div key={idx} className="flex items-start gap-3 p-3 rounded-xl bg-slate-900/60 border border-slate-800 text-sm sm:text-base text-slate-200">
                    <CheckSquare className="w-5 h-5 text-slate-400 shrink-0 mt-0.5" />
                    <span className="leading-relaxed">{item}</span>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-sm text-slate-500 italic">표준 절차(SOP) 준수 요망</p>
            )}
          </div>

          {/* Dual Briefing Points */}
          {briefing_points && briefing_points.length > 0 && (
            <div className="space-y-4">
              <span className="text-xs sm:text-sm font-bold text-slate-200 bg-slate-950 border border-slate-700 px-3 py-1.5 rounded-lg uppercase tracking-wider inline-block">
                COCKPIT DUAL BRIEFING FOCUS
              </span>
              <div className="bg-slate-950/80 border border-slate-800 rounded-2xl p-5 space-y-2.5 text-sm sm:text-base text-slate-300 leading-relaxed shadow-inner">
                {briefing_points.map((bp, idx) => (
                  <p key={idx} className="flex items-start gap-3">
                    <span className="text-slate-500 font-bold">•</span>
                    <span>{bp}</span>
                  </p>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
