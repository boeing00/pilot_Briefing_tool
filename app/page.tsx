'use client';

import React from 'react';
import { useFlightBriefing } from '@/context/FlightBriefingContext';
import { Header } from '@/components/Header';
import { EfbSidebar } from '@/components/EfbSidebar';
import { FlightStrip } from '@/components/FlightStrip';
import { UploadZone } from '@/components/UploadZone';
import { FlightSummaryCard } from '@/components/FlightSummaryCard';
import { HazardAlerts } from '@/components/HazardAlerts';
import { WeatherBriefing } from '@/components/WeatherBriefing';
import { NotamBriefing } from '@/components/NotamBriefing';
import { FuelBriefing } from '@/components/FuelBriefing';
import { PilotChat } from '@/components/PilotChat';
import { FileText, ShieldCheck, Clock, FileCode, Code2 } from 'lucide-react';

export default function Home() {
  const { briefingData, activeTab } = useFlightBriefing();

  return (
    <div className="min-h-screen bg-[#050912] text-slate-100 flex flex-col">
      {/* Top Header across entire width */}
      <Header />

      {/* Main Container below Header */}
      <div className="flex-1 flex flex-row min-h-0">
        {/* Left EFB Sidebar Rail */}
        <EfbSidebar />

        {/* Right Section Content */}
        <main className="flex-1 p-4 sm:p-6 lg:p-8 max-w-7xl w-full mx-auto overflow-y-auto">
          {!briefingData ? (
            <UploadZone />
          ) : (
            <div className="space-y-6 animate-in fade-in duration-200">
              {/* Common Top Flight Strip across all EFB tabs */}
              <FlightStrip data={briefingData} />

              {/* Active Tab View */}
              {activeTab === 'BRIEF' && <FlightSummaryCard data={briefingData} />}
              {activeTab === 'CHECK' && <HazardAlerts hazards={briefingData.hazards} />}
              {activeTab === 'ROUTE' && (
                <div className="space-y-4">
                  <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-4">
                    <h3 className="text-base font-bold text-slate-100 font-mono flex items-center gap-2">
                      <span className="text-cyan-400">✈️</span> ROUTE & WAYPOINT ANALYSIS
                    </h3>
                    <div className="p-4 rounded-xl bg-slate-950/70 border border-slate-800 font-mono text-xs text-cyan-300">
                      {briefingData.flightInfo.route}
                    </div>
                    <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs font-mono">
                      <div className="p-3 rounded-lg bg-slate-950/40 border border-slate-800">
                        <span className="text-slate-500 block">TOTAL DISTANCE</span>
                        <span className="font-bold text-slate-200">{briefingData.flightInfo.distanceNm || 694} NM</span>
                      </div>
                      <div className="p-3 rounded-lg bg-slate-950/40 border border-slate-800">
                        <span className="text-slate-500 block">PLANNED FLIGHT LEVEL</span>
                        <span className="font-bold text-amber-300">{briefingData.flightInfo.flightLevel}</span>
                      </div>
                      <div className="p-3 rounded-lg bg-slate-950/40 border border-slate-800">
                        <span className="text-slate-500 block">COST INDEX</span>
                        <span className="font-bold text-slate-200">{briefingData.flightInfo.costIndex || 'CI 35'}</span>
                      </div>
                      <div className="p-3 rounded-lg bg-slate-950/40 border border-slate-800">
                        <span className="text-slate-500 block">EST. TIME ENROUTE</span>
                        <span className="font-bold text-cyan-300">{briefingData.flightInfo.ete}</span>
                      </div>
                    </div>
                  </div>
                </div>
              )}
              {activeTab === 'FUEL' && (
                <FuelBriefing fuel={briefingData.fuel} weightAndBalance={briefingData.weightAndBalance} />
              )}
              {activeTab === 'WX' && <WeatherBriefing weather={briefingData.weather} />}
              {activeTab === 'NOTAM' && <NotamBriefing notams={briefingData.notams} />}
              {activeTab === 'RULES' && (
                <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-4">
                  <div className="flex items-center gap-2">
                    <ShieldCheck className="w-5 h-5 text-emerald-400" />
                    <h3 className="text-base font-bold text-slate-100">운항 규정 & 최저치 (Rules & Minimums)</h3>
                  </div>
                  <p className="text-xs text-slate-400 leading-relaxed">
                    도착지 및 교체공항 IFR 최저치, CAT-II/III 적용 기준 및 운항사 특별 규정 요약입니다.
                  </p>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                    <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 space-y-1">
                      <span className="text-cyan-400 font-bold font-mono">출발 공항 이륙 최저치 (Takeoff Minima)</span>
                      <p className="text-slate-300">{briefingData.flightInfo.origin.icao}: RVR 175m (RWY 33R/15L CAT-IIIb)</p>
                    </div>
                    <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 space-y-1">
                      <span className="text-amber-400 font-bold font-mono">도착 공항 착륙 최저치 (Landing Minima)</span>
                      <p className="text-slate-300">{briefingData.flightInfo.destination.icao}: ILS CAT-I / RNP APCH (RWY 16R/34L)</p>
                    </div>
                  </div>
                </div>
              )}
              {activeTab === 'REPORT' && (
                <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-4">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <FileText className="w-5 h-5 text-cyan-400" />
                      <h3 className="text-base font-bold text-slate-100">조종사 운항 브리핑 리포트 (Briefing Sheet)</h3>
                    </div>
                    <button
                      onClick={() => window.print()}
                      className="px-3 py-1.5 rounded-lg bg-cyan-500 text-slate-950 font-bold text-xs hover:bg-cyan-400 transition"
                    >
                      리포트 인쇄
                    </button>
                  </div>
                  <div className="p-5 rounded-xl bg-slate-950/80 border border-slate-800 space-y-3 font-mono text-xs leading-relaxed text-slate-300">
                    <p className="font-bold text-slate-100 text-sm">{briefingData.flightInfo.flightNumber} PRE-FLIGHT BRIEFING</p>
                    <p>{briefingData.executiveSummary}</p>
                    <div className="pt-2 border-t border-slate-800 text-slate-400">
                      Parsed at: {briefingData.parsedAt} | Doc: {briefingData.documentName || 'OFP.pdf'}
                    </div>
                  </div>
                </div>
              )}
              {activeTab === 'EDTO' && (
                <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-4">
                  <div className="flex items-center gap-2">
                    <Clock className="w-5 h-5 text-cyan-400" />
                    <h3 className="text-base font-bold text-slate-100 font-mono">EDTO / ETOPS DIVERSION ANALYSIS</h3>
                  </div>
                  <div className="p-4 rounded-xl bg-slate-950/60 border border-slate-800 space-y-2 text-xs">
                    <p className="text-slate-200 font-semibold">EDTO 최대 회항시간 기준: 120 / 180 MIN</p>
                    <p className="text-slate-400">항로상 비상 회항 가능한 주요 En-route Alternate 공항 및 기상 여건이 충족됩니다.</p>
                  </div>
                </div>
              )}
              {activeTab === 'FPL' && (
                <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-4">
                  <div className="flex items-center gap-2">
                    <FileCode className="w-5 h-5 text-cyan-400" />
                    <h3 className="text-base font-bold text-slate-100 font-mono">ICAO FLIGHT PLAN (FPL)</h3>
                  </div>
                  <pre className="p-4 rounded-xl bg-slate-950/80 border border-slate-800 font-mono text-xs text-amber-300 overflow-x-auto whitespace-pre-wrap">
{`(FPL-${briefingData.flightInfo.flightNumber}-IS
-${briefingData.flightInfo.aircraftType}/H-SDE3FGHIRWYZ/LB1
-${briefingData.flightInfo.origin.icao}0000
-N0480F370 ${briefingData.flightInfo.route}
-${briefingData.flightInfo.destination.icao}${briefingData.flightInfo.ete.replace(':', '')} ${briefingData.flightInfo.alternates?.[0]?.icao || ''}
-PBN/A1B1C1D1L1O1S2 DOF/260828 REG/${briefingData.flightInfo.registration || 'HL8274'} EET/RJJJ0040 RVR/200 PER/D)`}
                  </pre>
                </div>
              )}
              {activeTab === 'RAW' && (
                <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-4">
                  <div className="flex items-center gap-2">
                    <Code2 className="w-5 h-5 text-cyan-400" />
                    <h3 className="text-base font-bold text-slate-100 font-mono">STRUCTURED RAW JSON DATA</h3>
                  </div>
                  <pre className="p-4 rounded-xl bg-slate-950/80 border border-slate-800 font-mono text-[11px] text-cyan-300 overflow-x-auto max-h-[600px]">
                    {JSON.stringify(briefingData, null, 2)}
                  </pre>
                </div>
              )}
              {activeTab === 'AI' && <PilotChat />}
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
