import React, { useState } from 'react';
import { CloudRain, Wind, AlertTriangle, CloudLightning, Eye, Terminal } from 'lucide-react';

export default function WeatherBriefingCard({ data }) {
  const [showRaw, setShowRaw] = useState(false);
  if (!data) return null;

  const { departure, enroute, destination, alternate } = data;

  return (
    <div id="section-wx" className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-lg">
      <div className="flex items-center justify-between pb-4 border-b border-slate-800">
        <div className="flex items-center gap-2.5">
          <div className="p-2 bg-amber-500/10 border border-amber-500/30 rounded-lg text-amber-400">
            <CloudRain className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-100">Weather & Hazards Briefing</h3>
            <p className="text-xs text-slate-400">METAR, TAF, SIGMET & Enroute Turbulence Analysis</p>
          </div>
        </div>

        <button
          onClick={() => setShowRaw(!showRaw)}
          className="flex items-center gap-1.5 px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs rounded-lg border border-slate-700 transition"
        >
          <Terminal className="w-3.5 h-3.5" />
          <span>{showRaw ? 'Raw METAR 숨기기' : 'Raw METAR 보기'}</span>
        </button>
      </div>

      {/* Weather Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
        {/* Departure Weather */}
        <div className="bg-slate-950/60 p-4 rounded-xl border border-slate-800 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-amber-400 uppercase tracking-wider">
                Departure Weather
              </span>
              <span className="text-2xs px-2 py-0.5 bg-amber-950 text-amber-300 border border-amber-800 rounded-lg font-mono">
                ORIGIN
              </span>
            </div>
            <p className="text-sm text-slate-200 leading-relaxed font-medium">
              {departure?.condition_summary || '기상 정보 수신 중'}
            </p>
            {departure?.hazards && departure.hazards.length > 0 && (
              <div className="mt-3 space-y-1">
                {departure.hazards.map((h, i) => (
                  <div key={i} className="flex items-start gap-1.5 text-xs text-amber-300 bg-amber-950/30 p-1.5 rounded-lg border border-amber-900/40">
                    <AlertTriangle className="w-3.5 h-3.5 shrink-0 mt-0.5" />
                    <span>{h}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
          {showRaw && departure?.raw && (
            <div className="mt-3 pt-2 border-t border-slate-800 font-mono text-xs text-slate-400 bg-slate-900/90 p-2 rounded-lg">
              {departure.raw}
            </div>
          )}
        </div>

        {/* Destination Weather */}
        <div className="bg-slate-950/60 p-4 rounded-xl border border-slate-800 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-emerald-400 uppercase tracking-wider">
                Destination Weather
              </span>
              <span className="text-2xs px-2 py-0.5 bg-emerald-950 text-emerald-300 border border-emerald-800 rounded-lg font-mono">
                DESTINATION @ ETA
              </span>
            </div>
            <p className="text-sm text-slate-200 leading-relaxed font-medium">
              {destination?.condition_summary || '도착지 기상 상태'}
            </p>
            {destination?.forecast && (
              <p className="text-xs text-slate-400 mt-2 bg-slate-900/80 p-2 rounded-lg border border-slate-800">
                <span className="text-slate-300 font-semibold">예보(TAF):</span> {destination.forecast}
              </p>
            )}
            {destination?.hazards && destination.hazards.length > 0 && (
              <div className="mt-3 space-y-1">
                {destination.hazards.map((h, i) => (
                  <div key={i} className="flex items-start gap-1.5 text-xs text-amber-300 bg-amber-950/30 p-1.5 rounded-lg border border-amber-900/40">
                    <AlertTriangle className="w-3.5 h-3.5 shrink-0 mt-0.5" />
                    <span>{h}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
          {showRaw && destination?.raw && (
            <div className="mt-3 pt-2 border-t border-slate-800 font-mono text-xs text-slate-400 bg-slate-900/90 p-2 rounded-lg">
              {destination.raw}
            </div>
          )}
        </div>
      </div>

      {/* Enroute Turbulence & Alternate Status */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
        {/* Enroute Turbulence & Jetstream */}
        <div className="md:col-span-2 bg-slate-950/40 p-4 rounded-xl border border-slate-800/80">
          <div className="flex items-center gap-2 mb-2 text-xs font-bold text-amber-400 uppercase tracking-wider">
            <Wind className="w-4 h-4" />
            <span>Enroute Hazards (Turbulence / Icing / Jetstream)</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed mb-2">
            {enroute?.summary || '항로상 기상 정보 없음'}
          </p>
          {enroute?.turbulence_icing && (
            <div className="bg-amber-950/20 border border-amber-900/40 p-2.5 rounded-lg text-xs text-amber-200">
              <span className="font-semibold text-amber-400">Turbulence / Icing: </span>
              {enroute.turbulence_icing}
            </div>
          )}
          {enroute?.sigmet_alerts && enroute.sigmet_alerts.length > 0 && (
            <div className="mt-2 space-y-1">
              {enroute.sigmet_alerts.map((sig, idx) => (
                <div key={idx} className="flex items-start gap-1.5 text-xs text-rose-300 bg-rose-950/30 p-2 rounded-lg border border-rose-900/50">
                  <CloudLightning className="w-3.5 h-3.5 shrink-0 mt-0.5 text-rose-400" />
                  <span className="font-mono text-xs">{sig}</span>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Alternate Status */}
        <div className="bg-slate-950/40 p-4 rounded-xl border border-slate-800/80 flex flex-col justify-between">
          <div>
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-2">
              Alternate Weather
            </span>
            <p className="text-xs text-slate-300 leading-relaxed">
              {alternate?.condition_summary || '대체공항 기상 양호'}
            </p>
            {alternate?.suitability && (
              <div className="mt-3">
                <span className="text-2xs text-slate-400 block mb-1">SUITABILITY</span>
                <span className="px-2.5 py-1 bg-emerald-950 text-emerald-300 border border-emerald-800 rounded-lg font-semibold text-xs inline-block">
                  {alternate.suitability}
                </span>
              </div>
            )}
          </div>
          {showRaw && alternate?.raw && (
            <div className="mt-2 font-mono text-2xs text-slate-400 bg-slate-900 p-1.5 rounded-lg">
              {alternate.raw}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
