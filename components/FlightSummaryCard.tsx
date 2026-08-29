'use client';

import React, { useState } from 'react';
import {
  Plane,
  Clock,
  CheckCircle,
  AlertTriangle,
  XCircle,
  Navigation,
  MapPin,
  Layers,
  Pencil,
  Check,
  X,
} from 'lucide-react';
import { FlightBriefingData } from '@/types/flight';
import { useFlightBriefing } from '@/context/FlightBriefingContext';

interface FlightSummaryCardProps {
  data: FlightBriefingData;
}

export const FlightSummaryCard: React.FC<FlightSummaryCardProps> = ({ data }) => {
  const { flightInfo, goNoGoAssessment, executiveSummary, weather } = data;
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

  const getStatusBadge = (status: 'GO' | 'CAUTION' | 'NO_GO') => {
    switch (status) {
      case 'GO':
        return {
          icon: <CheckCircle className="w-5 h-5 text-emerald-400" />,
          bg: 'bg-emerald-950/40 border-emerald-500/40 text-emerald-300 shadow-[0_0_15px_rgba(16,185,129,0.15)]',
          badgeBg: 'bg-emerald-500 text-slate-950',
          title: 'GO (운항 양호)',
        };
      case 'CAUTION':
        return {
          icon: <AlertTriangle className="w-5 h-5 text-amber-400 animate-pulse" />,
          bg: 'bg-amber-950/40 border-amber-500/50 text-amber-300 shadow-[0_0_15px_rgba(245,158,11,0.15)]',
          badgeBg: 'bg-amber-400 text-slate-950',
          title: 'CAUTION (운항 주의 필요)',
        };
      case 'NO_GO':
        return {
          icon: <XCircle className="w-5 h-5 text-rose-400 animate-bounce" />,
          bg: 'bg-rose-950/40 border-rose-500/50 text-rose-300 shadow-[0_0_15px_rgba(244,63,94,0.2)]',
          badgeBg: 'bg-rose-500 text-white',
          title: 'NO-GO / HIGH RISK (운항 위험)',
        };
    }
  };

  const statusConfig = getStatusBadge(goNoGoAssessment.status);

  return (
    <div className="space-y-6">
      {/* 1. Main Departure ➔ En-route ➔ Destination Card */}
      <div className="p-6 sm:p-7 rounded-2xl bg-[#09111e] border border-[#162744] shadow-2xl space-y-6">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch">
          {/* Departure Airport Block */}
          <div className="lg:col-span-4 p-5 rounded-2xl bg-[#050b15] border border-[#13223b] flex flex-col justify-between space-y-4 text-center lg:text-left shadow-inner">
            <div className="flex items-center justify-between">
              <span className="inline-flex items-center gap-1.5 text-xs font-mono font-bold text-cyan-400 bg-cyan-950/80 px-2.5 py-1 rounded-lg border border-cyan-800/50">
                <MapPin className="w-3.5 h-3.5" /> DEPARTURE
              </span>
              {weather?.origin?.flightCategory && (
                <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800">
                  {weather.origin.flightCategory}
                </span>
              )}
            </div>

            <div className="space-y-1">
              <div className="text-4xl font-black text-slate-100 font-mono tracking-tight">
                {flightInfo.origin.icao}
                {flightInfo.origin.iata && (
                  <span className="text-xl font-bold text-slate-400 ml-2">/ {flightInfo.origin.iata}</span>
                )}
              </div>
              <p className="text-sm text-slate-300 font-semibold truncate">
                {flightInfo.origin.name}
              </p>
            </div>

            <div className="pt-3 border-t border-[#13223b] grid grid-cols-2 gap-3 text-xs font-mono">
              <div className="p-2 rounded-lg bg-[#081220] border border-[#16253d]">
                <span className="text-slate-400 text-[11px] block font-medium">STD (출발 예정)</span>
                <strong className="text-amber-300 text-sm font-bold">{flightInfo.std || '12:05Z'}</strong>
              </div>
              <div className="p-2 rounded-lg bg-[#081220] border border-[#16253d]">
                <span className="text-slate-400 text-[11px] block font-medium">ELEVATION</span>
                <strong className="text-slate-200 text-sm font-bold">{flightInfo.origin.elevation || '23 FT'}</strong>
              </div>
            </div>
          </div>

          {/* Center Flight Path Graphic (Symmetric & Centered) */}
          <div className="lg:col-span-4 flex flex-col items-center justify-center text-center space-y-3 py-2 px-2">
            <div className="inline-flex items-center gap-2 text-sm font-mono text-slate-300 bg-[#070f1c] px-4 py-1.5 rounded-full border border-[#182a47]">
              <Clock className="w-4 h-4 text-cyan-400" />
              <span>ETE:</span>
              {isEditingEte ? (
                <div className="inline-flex items-center gap-1">
                  <input
                    type="text"
                    value={tempEte}
                    onChange={(e) => setTempEte(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSaveEte()}
                    autoFocus
                    className="w-16 px-1.5 py-0.2 bg-[#0b1c36] border border-cyan-400 rounded text-cyan-300 font-mono text-xs font-bold text-center focus:outline-none"
                  />
                  <button onClick={handleSaveEte} className="text-emerald-400 hover:text-emerald-300">
                    <Check className="w-3.5 h-3.5" />
                  </button>
                  <button onClick={() => setIsEditingEte(false)} className="text-slate-400 hover:text-slate-300">
                    <X className="w-3.5 h-3.5" />
                  </button>
                </div>
              ) : (
                <button
                  onClick={() => {
                    setTempEte(flightInfo.ete);
                    setIsEditingEte(true);
                  }}
                  className="text-cyan-300 font-extrabold text-base hover:underline flex items-center gap-1"
                  title="클릭하여 수정"
                >
                  <span>{flightInfo.ete}</span>
                  <Pencil className="w-3 h-3 opacity-60 hover:opacity-100" />
                </button>
              )}

              {/* Plan Badge */}
              <span className="text-xs font-mono font-bold text-slate-400 bg-slate-900 px-2 py-0.5 rounded border border-slate-800">
                PLN: {plannedTime}
              </span>
            </div>

            <div className="w-full flex items-center gap-3 text-cyan-400">
              <div className="h-[3px] flex-1 bg-gradient-to-r from-cyan-500/20 via-cyan-500/80 to-cyan-500/20" />
              <div className="p-3 rounded-full bg-cyan-950/90 border-2 border-cyan-400/60 text-cyan-300 shadow-[0_0_15px_#00e5ff]">
                <Plane className="w-6 h-6 -rotate-45" />
              </div>
              <div className="h-[3px] flex-1 bg-gradient-to-r from-cyan-500/20 via-cyan-500/80 to-cyan-500/20" />
            </div>

            <div className="flex flex-wrap items-center justify-center gap-2.5 text-xs font-mono">
              <span className="bg-[#0e1b2e] text-slate-100 font-bold px-3 py-1 rounded-lg border border-[#1a3050]">
                {flightInfo.aircraftType}
              </span>
              <span className="bg-[#0e1b2e] text-cyan-300 font-bold px-3 py-1 rounded-lg border border-[#1a3050]">
                {flightInfo.distanceNm?.toLocaleString()} NM
              </span>
              <span className="bg-[#0e1b2e] text-amber-300 font-bold px-3 py-1 rounded-lg border border-[#1a3050]">
                {flightInfo.flightLevel}
              </span>
            </div>
          </div>

          {/* Destination Airport Block */}
          <div className="lg:col-span-4 p-5 rounded-2xl bg-[#050b15] border border-[#13223b] flex flex-col justify-between space-y-4 text-center lg:text-right shadow-inner">
            <div className="flex items-center justify-between lg:justify-end gap-2">
              {weather?.destination?.flightCategory && (
                <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-blue-950 text-blue-300 border border-blue-800">
                  {weather.destination.flightCategory}
                </span>
              )}
              <span className="inline-flex items-center gap-1.5 text-xs font-mono font-bold text-cyan-400 bg-cyan-950/80 px-2.5 py-1 rounded-lg border border-cyan-800/50">
                <MapPin className="w-3.5 h-3.5" /> DESTINATION
              </span>
            </div>

            <div className="space-y-1">
              <div className="text-4xl font-black text-slate-100 font-mono tracking-tight">
                {flightInfo.destination.icao}
                {flightInfo.destination.iata && (
                  <span className="text-xl font-bold text-slate-400 ml-2">/ {flightInfo.destination.iata}</span>
                )}
              </div>
              <p className="text-sm text-slate-300 font-semibold truncate">
                {flightInfo.destination.name}
              </p>
            </div>

            <div className="pt-3 border-t border-[#13223b] grid grid-cols-2 gap-3 text-xs font-mono text-left lg:text-right">
              <div className="p-2 rounded-lg bg-[#081220] border border-[#16253d]">
                <span className="text-slate-400 text-[11px] block font-medium">STA (도착 예정)</span>
                <strong className="text-amber-300 text-sm font-bold">{flightInfo.sta || '01:29Z'}</strong>
              </div>
              <div className="p-2 rounded-lg bg-[#081220] border border-[#16253d]">
                <span className="text-slate-400 text-[11px] block font-medium">ELEVATION</span>
                <strong className="text-slate-200 text-sm font-bold">{flightInfo.destination.elevation || '13 FT'}</strong>
              </div>
            </div>
          </div>
        </div>

        {/* Filed Route String Box (Without Copy button) */}
        {flightInfo.route && (
          <div className="pt-4 border-t border-[#14233c] space-y-2">
            <div className="flex items-center gap-2">
              <Navigation className="w-4 h-4 text-cyan-400" />
              <span className="text-xs font-mono text-slate-300 font-bold">
                FILED IFR ROUTE
              </span>
            </div>
            <div className="p-4 rounded-xl bg-[#050b15] border border-[#15253e] text-xs sm:text-sm font-mono text-cyan-300 leading-relaxed break-all shadow-inner">
              {flightInfo.route}
            </div>
          </div>
        )}

        {/* Alternates List */}
        {flightInfo.alternates && flightInfo.alternates.length > 0 && (
          <div className="pt-3 border-t border-[#14233c] flex flex-wrap items-center gap-2.5 text-xs font-mono">
            <span className="text-slate-400 font-bold text-xs">ALTERNATES:</span>
            {flightInfo.alternates.map((alt, idx) => (
              <div
                key={idx}
                className="inline-flex items-center gap-2 bg-[#050b15] text-slate-200 px-3.5 py-2 rounded-xl border border-[#162744] shadow-sm"
              >
                <span className="text-amber-400 font-black text-sm">{alt.icao}</span>
                {alt.iata && <span className="text-slate-400 font-bold">({alt.iata})</span>}
                <span className="text-slate-300 font-medium">{alt.name}</span>
                {alt.remarks && <span className="text-slate-400 text-xs font-semibold">- {alt.remarks}</span>}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* 2. Executive Pilot Summary Card */}
      <div className="p-6 rounded-2xl bg-[#09111e] border border-[#162744] space-y-3 shadow-xl">
        <h4 className="text-xs font-mono font-bold text-cyan-400 uppercase tracking-wider flex items-center gap-2">
          <Layers className="w-4 h-4 text-cyan-400" />
          EXECUTIVE PRE-FLIGHT BRIEFING SUMMARY
        </h4>
        <p className="text-sm sm:text-base text-slate-200 leading-relaxed font-normal">
          {executiveSummary}
        </p>
      </div>

      {/* 3. Go / No-Go Decision Banner (Caution Card - At Bottom) */}
      <div className={`p-6 rounded-2xl border ${statusConfig.bg} backdrop-blur-sm shadow-xl`}>
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-3">
          <div className="flex items-center gap-3">
            <span className={`px-3 py-1.5 rounded-xl text-xs font-mono font-black ${statusConfig.badgeBg}`}>
              {statusConfig.title}
            </span>
            <span className="text-xs text-slate-300 font-mono font-medium">
              AI 비행 안전성 종합 진단
            </span>
          </div>
        </div>

        <p className="text-sm sm:text-base font-bold text-slate-100 leading-snug">
          {goNoGoAssessment.primaryReason}
        </p>

        {goNoGoAssessment.keyCheckpoints && goNoGoAssessment.keyCheckpoints.length > 0 && (
          <div className="mt-4 pt-4 border-t border-white/10 space-y-2">
            <span className="text-xs font-mono text-slate-300 font-bold uppercase tracking-wider">
              KEY OPERATIONAL CHECKPOINTS:
            </span>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 text-xs sm:text-sm">
              {goNoGoAssessment.keyCheckpoints.map((cp, idx) => (
                <div key={idx} className="flex items-start gap-2.5 bg-black/30 p-3 rounded-xl border border-white/10">
                  <span className="text-cyan-400 font-black">•</span>
                  <span className="text-slate-200 font-medium">{cp}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
