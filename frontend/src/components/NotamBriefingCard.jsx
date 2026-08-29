import React from 'react';
import { AlertOctagon, Radio, Info, AlertTriangle } from 'lucide-react';

function ImpactBadge({ impact }) {
  const imp = (impact || 'low').toLowerCase();
  if (imp === 'high') {
    return (
      <span className="px-2 py-0.5 bg-rose-950 text-rose-300 border border-rose-800 rounded-lg text-2xs font-bold uppercase font-mono">
        CRITICAL
      </span>
    );
  }
  if (imp === 'medium') {
    return (
      <span className="px-2 py-0.5 bg-amber-950 text-amber-300 border border-amber-800 rounded-lg text-2xs font-bold uppercase font-mono">
        CAUTION
      </span>
    );
  }
  return (
    <span className="px-2 py-0.5 bg-slate-800 text-slate-400 border border-slate-700 rounded-lg text-2xs font-mono">
      INFO
    </span>
  );
}

export default function NotamBriefingCard({ data }) {
  if (!data) return null;

  const { critical_runway_taxiway, nav_aids_airspace, general_hazards } = data;

  return (
    <div id="section-notam" className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg">
      <div className="flex items-center gap-2.5 pb-4 border-b border-slate-800">
        <div className="p-2 bg-amber-500/10 border border-amber-500/30 rounded-lg text-amber-400">
          <AlertOctagon className="w-5 h-5" />
        </div>
        <div>
          <h3 className="text-base font-bold text-slate-100">Critical NOTAMs & Airport Notices</h3>
          <p className="text-xs text-slate-400">Runway/Taxiway closures, NAVAIDs, Restrictions</p>
        </div>
      </div>

      <div className="space-y-4 mt-4">
        {/* Runway & Taxiway Closures */}
        <div>
          <div className="flex items-center gap-2 text-xs font-bold text-rose-400 uppercase tracking-wider mb-2">
            <AlertOctagon className="w-4 h-4" />
            <span>Runway / Taxiway Closures (운항 직결)</span>
          </div>

          {critical_runway_taxiway && critical_runway_taxiway.length > 0 ? (
            <div className="space-y-2">
              {critical_runway_taxiway.map((item, idx) => (
                <div
                  key={idx}
                  className="bg-slate-950/70 border border-rose-900/40 p-3 rounded-lg flex flex-col sm:flex-row sm:items-center justify-between gap-2"
                >
                  <div className="space-y-1">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-bold text-rose-300">
                        {item.item}
                      </span>
                      {item.id && (
                        <span className="text-2xs text-slate-400 font-mono">[{item.id}]</span>
                      )}
                    </div>
                    <p className="text-xs text-slate-300">{item.detail}</p>
                  </div>
                  <div className="shrink-0 self-start sm:self-center">
                    <ImpactBadge impact={item.impact} />
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-slate-400 italic bg-slate-950/40 p-3 rounded-lg border border-slate-800">
              특이 활주로/유도로 폐쇄 노탐 없음
            </p>
          )}
        </div>

        {/* NAVAIDS / Airspace */}
        <div>
          <div className="flex items-center gap-2 text-xs font-bold text-amber-400 uppercase tracking-wider mb-2">
            <Radio className="w-4 h-4" />
            <span>NAVAIDs & Airspace Procedures (항법/절차)</span>
          </div>

          {nav_aids_airspace && nav_aids_airspace.length > 0 ? (
            <div className="space-y-2">
              {nav_aids_airspace.map((item, idx) => (
                <div
                  key={idx}
                  className="bg-slate-950/70 border border-slate-800 p-3 rounded-lg flex flex-col sm:flex-row sm:items-center justify-between gap-2"
                >
                  <div className="space-y-1">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-xs font-semibold text-slate-200">
                        {item.item}
                      </span>
                      {item.id && (
                        <span className="text-2xs text-slate-400 font-mono">[{item.id}]</span>
                      )}
                    </div>
                    <p className="text-xs text-slate-400">{item.detail}</p>
                  </div>
                  <div className="shrink-0 self-start sm:self-center">
                    <ImpactBadge impact={item.impact} />
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-xs text-slate-400 italic bg-slate-950/40 p-3 rounded-lg border border-slate-800">
              항법 장비 및 공역 제한사항 없음
            </p>
          )}
        </div>

        {/* General Hazards */}
        {general_hazards && general_hazards.length > 0 && (
          <div>
            <div className="flex items-center gap-2 text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">
              <Info className="w-4 h-4" />
              <span>General Hazards (조류/장애물 등)</span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {general_hazards.map((item, idx) => (
                <div key={idx} className="bg-slate-950/40 border border-slate-800/80 p-2.5 rounded-lg text-xs">
                  <span className="font-mono font-medium text-slate-300 block">{item.item}</span>
                  <span className="text-slate-400 mt-0.5 block">{item.detail}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
