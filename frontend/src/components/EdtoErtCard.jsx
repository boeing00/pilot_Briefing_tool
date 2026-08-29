import React from 'react';
import { Clock, ShieldCheck } from 'lucide-react';

export default function EdtoErtCard({ briefing }) {
  const edto = briefing?.edto_etops || {};
  const etpData = edto.etp_items || [
    {
      sector: 'ETP 1 : RJCC (신치토세) - PANC (앵커리지)',
      pos: 'N53°06.6 E170°27.6 (웨이포인트 ETP1 인근)',
      dist1: '2,283 NM to RJCC (04h 39m, Fuel 174,900 LBS)',
      dist2: '1,355 NM to PANC (03h 48m, Fuel 122,500 LBS)',
      wind: 'RJCC M019 / PANC M005',
    },
    {
      sector: 'ETP 2 : PANC (앵커리지) - KORD (시카고)',
      pos: 'N58°48.0 W109°09.6 (웨이포인트 ETP2 인근)',
      dist1: '4,853 NM to PANC (09h 49m, Fuel 322,300 LBS)',
      dist2: '1,287 NM to KORD (03h 24m, Fuel 101,400 LBS)',
      wind: 'PANC M002 / KORD P018',
    },
  ];

  const eras = edto.designated_eras || 'RKSI, RJCC, PANC, KORD, CYEG, CYWG, KBOS';

  return (
    <div id="section-edto" className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xl space-y-5">
      <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
        <div className="flex items-center gap-3.5">
          <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
            <Clock className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-xl sm:text-2xl font-black text-white font-mono uppercase tracking-wide">
              EDTO / ETOPS & EQUAL TIME POINTS (ETP)
            </h3>
            <p className="text-xs text-slate-400 font-mono mt-0.5">
              대양 및 극항로 비행 등시점(ETP) 및 회항공항 분기 정보
            </p>
          </div>
        </div>
        <span className="text-xs font-mono font-bold px-3 py-1.5 bg-slate-950 border border-slate-700 text-slate-300 rounded-lg shadow-sm shrink-0">
          ETP ACTIVE ({etpData.length} SECTORS)
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 font-mono">
        {etpData.map((etp, idx) => (
          <div key={idx} className="bg-slate-950/80 border border-slate-800 p-4 rounded-xl space-y-2.5 shadow-inner">
            <div className="flex items-center justify-between gap-2">
              <span className="text-xs font-bold text-slate-200">{etp.sector}</span>
              <span className="px-2 py-0.5 bg-slate-900 text-slate-300 border border-slate-700 rounded text-[10px]">
                CRZ FL350
              </span>
            </div>
            <div className="bg-slate-900/80 p-3 rounded-lg border border-slate-800 text-xs space-y-1.5 leading-relaxed">
              <p className="text-slate-300">
                <span className="text-slate-500 font-bold">ETP POSITION:</span> {etp.pos}
              </p>
              <p className="text-slate-300">
                <span className="text-slate-500 font-bold">DIVERT 1:</span> {etp.dist1}
              </p>
              <p className="text-slate-300">
                <span className="text-slate-500 font-bold">DIVERT 2:</span> {etp.dist2}
              </p>
              {etp.wind && (
                <p className="text-slate-400">
                  <span className="text-slate-500 font-bold">WIND FACTOR:</span> {etp.wind}
                </p>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Enroute Alternates (ERA) */}
      <div className="pt-2 border-t border-slate-800 flex flex-wrap items-center justify-between gap-2 text-xs font-mono text-slate-400">
        <div>
          <span className="text-slate-500 font-bold">DESIGNATED ERAs:</span>{' '}
          <span className="text-slate-200">{eras}</span>
        </div>
        <div className="text-slate-300 flex items-center gap-1.5 bg-slate-950 px-2.5 py-1 rounded border border-slate-700">
          <ShieldCheck className="w-4 h-4 text-emerald-400" />
          <span>3% CONTINGENCY ERA VALIDATED</span>
        </div>
      </div>
    </div>
  );
}
