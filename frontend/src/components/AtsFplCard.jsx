import React, { useState } from 'react';
import { ClipboardList, Copy, Check } from 'lucide-react';

export default function AtsFplCard({ briefing }) {
  const [copied, setCopied] = useState(false);

  const rawFpl = briefing?.ats_icao_fpl?.raw_fpl || `(FPL-${briefing?.flight_summary?.callsign || 'FLIGHT'}-IS
-${briefing?.flight_summary?.aircraft_type || 'A359'}-...
-${briefing?.flight_summary?.departure?.icao || 'RKSI'}${briefing?.flight_summary?.etd_utc?.replace(':', '')?.replace('Z', '') || '0530'}
-${briefing?.route_analysis?.filed_route_string || 'DIRECT'}
-${briefing?.flight_summary?.destination?.icao || 'DEST'}${briefing?.flight_summary?.flight_time?.replace('Hr ', '')?.replace('Min', '') || '1042'} ${briefing?.flight_summary?.alternate?.icao || 'ALTN'})`;

  const handleCopy = () => {
    navigator.clipboard.writeText(rawFpl);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div id="section-fpl" className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-lg space-y-5">
      <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
        <div className="flex items-center gap-3.5">
          <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
            <ClipboardList className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-xl sm:text-2xl font-bold text-white uppercase tracking-wide">
              SUBMITTED ATS FLIGHT PLAN (ICAO FPL)
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">항공교통관제소(ATS) 공식 제출 비행계획 전문</p>
          </div>
        </div>

        <button
          onClick={handleCopy}
          className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-950 hover:bg-slate-800 text-slate-200 text-xs font-bold rounded-lg border border-slate-700 transition"
        >
          {copied ? <Check className="w-3.5 h-3.5 text-slate-300" /> : <Copy className="w-3.5 h-3.5 text-slate-400" />}
          <span>{copied ? '복사 완료' : 'FPL 전문 복사'}</span>
        </button>
      </div>

      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-200 leading-relaxed overflow-x-auto select-all font-mono">
        <pre>{rawFpl}</pre>
      </div>
    </div>
  );
}
