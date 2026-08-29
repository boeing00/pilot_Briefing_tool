'use client';

import React, { useState } from 'react';
import { Cloud, Wind, Eye, Compass, Thermometer, CloudRain, AlertTriangle, CheckCircle } from 'lucide-react';
import { WeatherItem } from '@/types/flight';

interface WeatherBriefingProps {
  weather: {
    origin: WeatherItem;
    destination: WeatherItem;
    alternates: WeatherItem[];
    enrouteSignificantWeather: string[];
  };
}

export const WeatherBriefing: React.FC<WeatherBriefingProps> = ({ weather }) => {
  const [selectedStation, setSelectedStation] = useState<'origin' | 'destination' | number>('destination');
  const [showRaw, setShowRaw] = useState<boolean>(false);

  const getActiveStation = (): WeatherItem => {
    if (selectedStation === 'origin') return weather.origin;
    if (selectedStation === 'destination') return weather.destination;
    return weather.alternates[selectedStation] || weather.destination;
  };

  const current = getActiveStation();

  const getFlightCategoryBadge = (category?: string) => {
    switch (category) {
      case 'VFR':
        return 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40';
      case 'MVFR':
        return 'bg-blue-500/20 text-blue-300 border-blue-500/40';
      case 'IFR':
        return 'bg-amber-500/20 text-amber-300 border-amber-500/40';
      case 'LIFR':
        return 'bg-rose-500/20 text-rose-300 border-rose-500/40';
      default:
        return 'bg-slate-800 text-slate-400 border-slate-700';
    }
  };

  return (
    <div className="space-y-6">
      {/* Station Selector & Raw Toggle */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-2 border-b border-slate-800">
        <div className="flex items-center gap-2 flex-wrap">
          <button
            onClick={() => setSelectedStation('origin')}
            className={`px-3 py-1.5 rounded-lg text-xs font-mono font-bold transition flex items-center gap-1.5 ${
              selectedStation === 'origin'
                ? 'bg-cyan-500 text-slate-950 shadow-md'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            <span>출발지:</span>
            <span>{weather.origin.icao}</span>
          </button>

          <button
            onClick={() => setSelectedStation('destination')}
            className={`px-3 py-1.5 rounded-lg text-xs font-mono font-bold transition flex items-center gap-1.5 ${
              selectedStation === 'destination'
                ? 'bg-cyan-500 text-slate-950 shadow-md'
                : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
            }`}
          >
            <span>도착지:</span>
            <span>{weather.destination.icao}</span>
          </button>

          {weather.alternates?.map((alt, idx) => (
            <button
              key={idx}
              onClick={() => setSelectedStation(idx)}
              className={`px-3 py-1.5 rounded-lg text-xs font-mono font-bold transition flex items-center gap-1.5 ${
                selectedStation === idx
                  ? 'bg-cyan-500 text-slate-950 shadow-md'
                  : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
              }`}
            >
              <span>교체:</span>
              <span>{alt.icao}</span>
            </button>
          ))}
        </div>

        <button
          onClick={() => setShowRaw(!showRaw)}
          className="text-xs font-mono text-cyan-400 hover:text-cyan-300 transition underline underline-offset-4"
        >
          {showRaw ? '자연어 해석만 보기' : '원문(Raw METAR/TAF) 함께 보기'}
        </button>
      </div>

      {/* Main Weather Card */}
      <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-blue-500/10 border border-blue-500/30 flex items-center justify-center text-blue-400">
              <Cloud className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xl font-bold font-mono text-slate-100">{current.icao}</span>
                <span className={`px-2 py-0.5 rounded text-xs font-mono font-bold border ${getFlightCategoryBadge(current.flightCategory)}`}>
                  {current.flightCategory || 'VFR'}
                </span>
              </div>
              <p className="text-xs text-slate-400 font-medium">공항 기상 상태 및 예보 요약</p>
            </div>
          </div>

          {current.significantHazards && current.significantHazards.length > 0 && (
            <div className="flex flex-wrap gap-1.5">
              {current.significantHazards.map((haz, i) => (
                <span
                  key={i}
                  className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md text-xs font-mono font-bold bg-rose-950/80 text-rose-300 border border-rose-700/60 animate-pulse"
                >
                  <AlertTriangle className="w-3 h-3 text-rose-400" />
                  {haz}
                </span>
              ))}
            </div>
          )}
        </div>

        {/* Metar & TAF Plain Explanations */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* METAR Card */}
          <div className="p-4 rounded-xl bg-slate-950/70 border border-slate-850 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-mono font-bold text-cyan-400">CURRENT METAR (현재 기상)</span>
            </div>

            {showRaw && current.metarRaw && (
              <pre className="p-2.5 rounded-lg bg-slate-900 text-xs font-mono text-amber-300 overflow-x-auto whitespace-pre-wrap border border-slate-800">
                {current.metarRaw}
              </pre>
            )}

            <p className="text-xs text-slate-200 leading-relaxed font-medium">
              {current.metarTranslated || '기상 관측 정보가 없습니다.'}
            </p>
          </div>

          {/* TAF Card */}
          <div className="p-4 rounded-xl bg-slate-950/70 border border-slate-850 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-mono font-bold text-emerald-400">TAF FORECAST (예보 & 시간대별 추이)</span>
            </div>

            {showRaw && current.tafRaw && (
              <pre className="p-2.5 rounded-lg bg-slate-900 text-xs font-mono text-amber-300 overflow-x-auto whitespace-pre-wrap border border-slate-800">
                {current.tafRaw}
              </pre>
            )}

            <p className="text-xs text-slate-200 leading-relaxed font-medium">
              {current.tafTranslated || '예보 정보가 없습니다.'}
            </p>
          </div>
        </div>

        {/* Quick Weather Metrics Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2">
          <div className="p-3 rounded-xl bg-slate-950/40 border border-slate-850">
            <div className="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
              <Wind className="w-3.5 h-3.5 text-cyan-400" />
              <span>지상풍 (Wind)</span>
            </div>
            <p className="text-sm font-bold font-mono text-slate-100">
              {current.wind ? `${current.wind.direction}° / ${current.wind.speed}kt` : 'N/A'}
              {current.wind?.gust ? <span className="text-rose-400 text-xs ml-1">(G{current.wind.gust})</span> : ''}
            </p>
            {current.wind?.crosswindEstimate && (
              <p className="text-[11px] font-mono text-amber-300 mt-1">{current.wind.crosswindEstimate}</p>
            )}
          </div>

          <div className="p-3 rounded-xl bg-slate-950/40 border border-slate-850">
            <div className="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
              <Eye className="w-3.5 h-3.5 text-cyan-400" />
              <span>시정 (Visibility)</span>
            </div>
            <p className="text-sm font-bold font-mono text-slate-100">{current.visibility || '10km+'}</p>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/40 border border-slate-850">
            <div className="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
              <Cloud className="w-3.5 h-3.5 text-cyan-400" />
              <span>운저고도 (Ceiling)</span>
            </div>
            <p className="text-sm font-bold font-mono text-slate-100">{current.ceiling || 'Unrestricted'}</p>
          </div>

          <div className="p-3 rounded-xl bg-slate-950/40 border border-slate-850">
            <div className="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
              <Thermometer className="w-3.5 h-3.5 text-cyan-400" />
              <span>기온 / 기압</span>
            </div>
            <p className="text-sm font-bold font-mono text-slate-100">
              {current.temperature || 'N/A'} / {current.altimeter || 'QNH'}
            </p>
          </div>
        </div>
      </div>

      {/* En-route Weather Warnings */}
      {weather.enrouteSignificantWeather && weather.enrouteSignificantWeather.length > 0 && (
        <div className="p-5 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-2">
          <h4 className="text-xs font-mono font-bold text-amber-400 uppercase tracking-wider flex items-center gap-2">
            <AlertTriangle className="w-3.5 h-3.5" />
            EN-ROUTE SIGNIFICANT WEATHER (항로 특이기상)
          </h4>
          <ul className="space-y-1.5 text-xs text-slate-200">
            {weather.enrouteSignificantWeather.map((sig, idx) => (
              <li key={idx} className="flex items-start gap-2 bg-slate-950/40 p-2.5 rounded-lg border border-slate-850">
                <span className="text-amber-400 font-bold">•</span>
                <span>{sig}</span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};
