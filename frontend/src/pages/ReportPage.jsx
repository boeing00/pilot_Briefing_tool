import React, { useState } from 'react';
import { FileSpreadsheet, CheckCircle2, PenTool } from 'lucide-react';

export default function ReportPage({ briefing }) {
  const [signed, setSigned] = useState(false);
  const [captName, setCaptName] = useState('KIM / CAPTAIN');

  const rep = briefing?.flight_release_report || {};
  const flightNo = rep.flight_no || `${briefing?.flight_summary?.callsign || 'FLIGHT'} / ${briefing?.flight_summary?.flight_date || 'TODAY'}`;
  const dispatcher = rep.dispatcher || 'OPERATIONS DISPATCHER (TEL: 02-6101-5503 / ocws@flyasiana.com)';
  const releaseStmt = rep.release_statement || `I HEREBY RELEASE THE FLIGHT ${briefing?.flight_summary?.callsign || 'FLIGHT'}, ${briefing?.flight_summary?.departure?.icao || 'RKSI'}/${briefing?.flight_summary?.destination?.icao || 'DEST'}, ${briefing?.flight_summary?.aircraft_type || 'AIRCRAFT'}, ETD ${briefing?.flight_summary?.etd_utc || 'ETD'} UNDER THE CONDITIONS SPECIFIED.`;

  return (
    <div className="space-y-6 animate-fade-in font-mono">
      {/* Dispatch Release Document */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xl space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <FileSpreadsheet className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
                OFFICIAL FLIGHT RELEASE REPORT
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">FLIGHT {flightNo} - DISPATCHER: {dispatcher}</p>
            </div>
          </div>
          <span className="px-3 py-1.5 bg-slate-950 text-slate-300 border border-slate-700 rounded-lg text-xs font-bold shadow-sm">
            RELEASE STATUS: AUTHORIZED
          </span>
        </div>

        {/* Certificate Text Box */}
        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-300 space-y-2 leading-relaxed shadow-inner">
          <p className="text-slate-100 font-bold">
            {releaseStmt}
          </p>
          <p className="text-slate-400">
            - DISPATCHER: {dispatcher}
            <br />
            - COMPLIANCE: CIVIL AVIATION LAW & COMPANY OPERATIONS MANUAL
          </p>
        </div>

        {/* RVSM Altimeter Log Table */}
        <div className="bg-slate-950/80 p-4 rounded-xl border border-slate-800 space-y-2.5 shadow-inner">
          <span className="text-xs font-bold text-slate-200 uppercase tracking-wider block">
            RVSM Altimeter Crosscheck Log (고도계 점검 기록)
          </span>
          <div className="grid grid-cols-3 gap-3 text-xs">
            <div className="bg-slate-900 p-3 rounded-xl border border-slate-800 text-center">
              <span className="text-slate-500 block text-[10px]">CAPT PRIMARY</span>
              <span className="text-slate-200 font-bold block mt-1">RECORDED (OK)</span>
            </div>
            <div className="bg-slate-900 p-3 rounded-xl border border-slate-800 text-center">
              <span className="text-slate-500 block text-[10px]">STANDBY</span>
              <span className="text-slate-200 font-bold block mt-1">RECORDED (OK)</span>
            </div>
            <div className="bg-slate-900 p-3 rounded-xl border border-slate-800 text-center">
              <span className="text-slate-500 block text-[10px]">F/O PRIMARY</span>
              <span className="text-slate-200 font-bold block mt-1">RECORDED (OK)</span>
            </div>
          </div>
        </div>

        {/* Pilot in Command Sign-off */}
        <div className="bg-slate-950/80 p-4 sm:p-5 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-inner">
          <div className="space-y-1 text-xs">
            <span className="font-bold text-slate-200 block">PILOT IN COMMAND (기장 서명 및 수락)</span>
            <p className="text-slate-400">
              본 비행계획서 및 기상/NOTAM 브리핑 내용을 확인하였으며 안전 운항을 위해 수락합니다.
            </p>
          </div>

          <div className="flex items-center gap-3 w-full sm:w-auto justify-end">
            <input
              type="text"
              value={captName}
              onChange={(e) => setCaptName(e.target.value)}
              className="bg-slate-900 border border-slate-700 px-3 py-2 rounded-lg text-xs font-bold text-slate-100 focus:outline-none focus:border-amber-400"
            />
            <button
              onClick={() => setSigned(!signed)}
              className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-1.5 border ${
                signed
                  ? 'bg-slate-900 border-slate-700 text-slate-200'
                  : 'bg-amber-500/20 hover:bg-amber-500/30 border-amber-400/40 text-amber-200 shadow-sm'
              }`}
            >
              {signed ? (
                <>
                  <CheckCircle2 className="w-4 h-4 text-slate-400" /> ACCEPTED
                </>
              ) : (
                <>
                  <PenTool className="w-4 h-4 text-amber-300" /> ACCEPT RELEASE
                </>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
