import React from 'react';
import { Plane, AlertTriangle, Fuel, CloudRain, Clock, ShieldAlert, ChevronRight, CheckCircle2, Navigation } from 'lucide-react';
import FlightOverviewCard from '../components/FlightOverviewCard';
import ThreatManagementCard from '../components/ThreatManagementCard';

export default function BriefPage({ briefing, onNavigate }) {
  if (!briefing) return null;

  const depIcao = briefing.flight_summary?.departure?.icao || 'DEP';
  const destIcao = briefing.flight_summary?.destination?.icao || 'DEST';
  const altnIcao = briefing.flight_summary?.alternate?.icao || 'ALTN';

  const keyAlerts = briefing.key_alerts && briefing.key_alerts.length > 0
    ? briefing.key_alerts
    : [
        {
          type: 'WEATHER',
          title: `${destIcao} 도착 기상 및 대체공항(${altnIcao}) 점검`,
          desc: `도착 예정 시간대 기상 변화 및 교체공항 상태를 모니터링하십시오. 예비 연료가 정상 반영되어 있습니다.`,
          level: 'HIGH',
          target: 'wx',
        },
        {
          type: 'NOTAM',
          title: `${depIcao} / ${destIcao} 발효 중인 주요 NOTAM 확인`,
          desc: `활주로, 유도로 및 항행안전시설 운영 제한사항을 사전에 확인하십시오.`,
          level: 'HIGH',
          target: 'notam',
        },
        {
          type: 'FUEL & WEIGHT',
          title: `탑재 연료(${briefing.fuel_and_weights?.block_fuel || 'PLAN'}) 및 이륙 중량(TOW) 일치 확인`,
          desc: `비행계획서상의 연료량과 실제 급유량을 상호 대조하고 무게중심(CG) 한계를 확인하십시오.`,
          level: 'MEDIUM',
          target: 'fuel',
        },
        {
          type: 'OPERATION',
          title: `${depIcao} 표준 출항(SID) 및 소음 저감 절차 준수`,
          desc: `초기 상승 고도 및 최저 안전고도(MSA)를 철저히 준수하십시오.`,
          level: 'CRITICAL',
          target: 'rules',
        },
      ];

  const blockFuel = briefing.fuel_and_weights?.block_fuel || '-';
  const estTow = briefing.fuel_and_weights?.estimated_tow || '-';
  const towMargin = briefing.fuel_and_weights?.tow_margin ? ` (${briefing.fuel_and_weights.tow_margin})` : '';
  const fltTime = briefing.flight_summary?.flight_time || '-';
  const edtoEras = briefing.edto_etops?.designated_eras || `${depIcao}, ${altnIcao}, ${destIcao}`;

  return (
    <div className="space-y-7 animate-fade-in">
      {/* Flight Summary Card */}
      <FlightOverviewCard data={briefing.flight_summary} />

      {/* Critical Operational Briefing Alerts */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-lg space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-5 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-3 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <ShieldAlert className="w-7 h-7" />
            </div>
            <div>
              <h3 className="text-xl sm:text-2xl font-bold text-white uppercase tracking-wide">
                KEY OPERATIONAL BRIEFING HIGHLIGHTS
              </h3>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-bold px-3.5 py-1.5 bg-slate-950 border border-slate-700 text-slate-300 rounded-lg shadow-sm shrink-0">
            {keyAlerts.length} CRITICAL ITEM{keyAlerts.length > 1 ? 'S' : ''}
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          {keyAlerts.map((alert, idx) => (
            <div
              key={idx}
              onClick={() => onNavigate(alert.target || 'wx')}
              className="bg-slate-950/80 p-5 sm:p-6 rounded-2xl border border-slate-800 flex flex-col justify-between cursor-pointer transition hover:border-slate-700 hover:bg-slate-900/90 shadow-sm group"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-3">
                  <span className="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-400">
                    [{alert.type}]
                  </span>
                  <span className={`text-xs px-2.5 py-1 rounded-lg border font-bold ${
                    alert.level === 'CRITICAL'
                      ? 'bg-slate-900 text-rose-300 border-rose-600/50'
                      : alert.level === 'HIGH'
                      ? 'bg-slate-900 text-amber-300 border-amber-500/30'
                      : 'bg-slate-900 text-slate-400 border-slate-700'
                  }`}>
                    {alert.level}
                  </span>
                </div>
                <h4 className="text-base sm:text-lg font-bold text-white leading-snug group-hover:text-amber-200 transition-colors">
                  {alert.title}
                </h4>
                <p className="text-sm sm:text-base text-slate-300 mt-2.5 leading-relaxed">
                  {alert.desc}
                </p>
              </div>

              <div className="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between text-xs sm:text-sm font-bold text-slate-400 group-hover:text-slate-200 transition">
                <span>상세 브리핑 페이지 확인</span>
                <ChevronRight className="w-4 h-4 text-slate-400 group-hover:text-slate-200" />
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Quick EFB Metrics Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        {/* Block Fuel */}
        <div
          onClick={() => onNavigate('fuel')}
          className="bg-slate-900 hover:bg-slate-800 border border-slate-800 p-5 rounded-2xl cursor-pointer transition flex items-center gap-4 shadow-sm group"
        >
          <div className="p-3 bg-slate-800 border border-slate-700 text-slate-300 rounded-xl group-hover:text-amber-300 transition">
            <Fuel className="w-6 h-6" />
          </div>
          <div>
            <span className="text-xs sm:text-sm text-slate-400 uppercase font-bold block">BLOCK FUEL</span>
            <span className="text-base sm:text-lg font-bold text-white">{blockFuel}</span>
          </div>
        </div>

        {/* Takeoff Weight */}
        <div
          onClick={() => onNavigate('fuel')}
          className="bg-slate-900 hover:bg-slate-800 border border-slate-800 p-5 rounded-2xl cursor-pointer transition flex items-center gap-4 shadow-sm group"
        >
          <div className="p-3 bg-slate-800 border border-slate-700 text-slate-300 rounded-xl group-hover:text-amber-300 transition">
            <CheckCircle2 className="w-6 h-6" />
          </div>
          <div>
            <span className="text-xs sm:text-sm text-slate-400 uppercase font-bold block">EST TOW</span>
            <span className="text-base sm:text-lg font-bold text-white">{estTow}{towMargin}</span>
          </div>
        </div>

        {/* Flight Time */}
        <div
          onClick={() => onNavigate('route')}
          className="bg-slate-900 hover:bg-slate-800 border border-slate-800 p-5 rounded-2xl cursor-pointer transition flex items-center gap-4 shadow-sm group"
        >
          <div className="p-3 bg-slate-800 border border-slate-700 text-slate-300 rounded-xl group-hover:text-amber-300 transition">
            <Clock className="w-6 h-6" />
          </div>
          <div>
            <span className="text-xs sm:text-sm text-slate-400 uppercase font-bold block">EST FLIGHT TIME</span>
            <span className="text-base sm:text-lg font-bold text-white">{fltTime}</span>
          </div>
        </div>

        {/* ETOPS / EDTO */}
        <div
          onClick={() => onNavigate('edto')}
          className="bg-slate-900 hover:bg-slate-800 border border-slate-800 p-5 rounded-2xl cursor-pointer transition flex items-center gap-4 shadow-sm group"
        >
          <div className="p-3 bg-slate-800 border border-slate-700 text-slate-300 rounded-xl group-hover:text-amber-300 transition">
            <Navigation className="w-6 h-6" />
          </div>
          <div>
            <span className="text-xs sm:text-sm text-slate-400 uppercase font-bold block">EDTO ERAS</span>
            <span className="text-base sm:text-lg font-bold text-white">{edtoEras}</span>
          </div>
        </div>
      </div>

      {/* Threat & Error Management (TEM) Card */}
      <ThreatManagementCard data={briefing?.threat_and_error_management} />
    </div>
  );
}

