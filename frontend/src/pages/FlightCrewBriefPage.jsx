import React from 'react';
import {
  Users,
  Plane,
  AlertTriangle,
  Fuel,
  CloudRain,
  Clock,
  ShieldAlert,
  ChevronRight,
  CheckCircle2,
  Navigation,
  FileCheck,
  CheckSquare,
  Volume2
} from 'lucide-react';
import FlightOverviewCard from '../components/FlightOverviewCard';
import ThreatManagementCard from '../components/ThreatManagementCard';

export default function FlightCrewBriefPage({ briefing, onNavigate = () => {} }) {
  if (!briefing) return null;

  const depIcao = briefing.flight_summary?.departure?.icao || 'RKSI';
  const destIcao = briefing.flight_summary?.destination?.icao || 'KJFK';
  const altnIcao = briefing.flight_summary?.alternate?.icao || 'KBOS';

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

  const fcBrief = briefing.flight_crew_briefing || {
    key_focus: '장거리 비행에 따른 순항 고도 관리 및 도착지 뇌우 회피 절차',
    briefing_topics: [
      '출발 시 400ft AGL 이하 조기 선회 금지 지침 준수',
      '태평양/항로상 난류 예상 구간 승객 벨트 사인 사전 점등',
      '도착지 기상 악화 시 교체공항 회항 연료 마진 확인'
    ],
    crew_coordination: [
      '단계별 연료 소모율 및 FOD 잔여 연료 상호 교차 점검',
      '도착 전 레이더 틸트 조절 및 기상 우회 경로 ATC 사전 조율'
    ],
    checklist_action_items: [
      '출발 전 METAR/TAF 및 NOTAM 최종 업데이트 확인',
      '탑재 연료량과 OFP 일치 서명 확인',
      '항공기 결함(MEL/CDL) 적용 내역 확인'
    ]
  };

  return (
    <div className="space-y-7 animate-fade-in">

      {/* Flight Summary Card with Vertically Aligned Dep/Center/Dest + Weather + Alternates + MEL/CDL */}
      <FlightOverviewCard
        data={briefing.flight_summary}
        weather={briefing.weather_briefing}
        melItems={briefing.company_rules_and_mel?.mel_cdl_items}
      />

      {/* Critical Operational Briefing Highlights */}
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

      {/* Flight Crew Specific Briefing Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-lg space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-5 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-3 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <Users className="w-7 h-7" />
            </div>
            <div>
              <h3 className="text-xl sm:text-2xl font-bold text-white uppercase tracking-wide">
                FLIGHT CREW OPERATIONAL BRIEFING
              </h3>
              <p className="text-xs sm:text-sm text-slate-400 mt-0.5">
                운항승무원 전용 핵심 토픽 및 상호 협조 체크리스트
              </p>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-bold px-3.5 py-1.5 bg-slate-950 border border-amber-500/40 text-amber-300 rounded-lg shadow-sm shrink-0">
            CREW ACTIONS
          </span>
        </div>

        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
          <span className="text-xs text-amber-300 font-bold block mb-1 uppercase tracking-wider">[KEY FOCUS]</span>
          <p className="text-sm sm:text-base text-slate-200 font-bold leading-relaxed">{fcBrief.key_focus}</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {/* Topics */}
          <div className="bg-slate-950/80 p-5 rounded-xl border border-slate-800 space-y-3">
            <span className="text-xs font-bold text-slate-300 uppercase block pb-2 border-b border-slate-800 flex items-center gap-2">
              <FileCheck className="w-4 h-4 text-amber-400" />
              BRIEFING TOPICS
            </span>
            <ul className="space-y-2.5 text-xs sm:text-sm text-slate-300">
              {fcBrief.briefing_topics?.map((topic, i) => (
                <li key={i} className="flex items-start gap-2">
                  <span className="text-amber-400 font-bold mt-0.5">•</span>
                  <span>{topic}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Coordination */}
          <div className="bg-slate-950/80 p-5 rounded-xl border border-slate-800 space-y-3">
            <span className="text-xs font-bold text-slate-300 uppercase block pb-2 border-b border-slate-800 flex items-center gap-2">
              <Users className="w-4 h-4 text-amber-400" />
              CREW COORDINATION
            </span>
            <ul className="space-y-2.5 text-xs sm:text-sm text-slate-300">
              {fcBrief.crew_coordination?.map((item, i) => (
                <li key={i} className="flex items-start gap-2">
                  <span className="text-amber-400 font-bold mt-0.5">•</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Action Items */}
          <div className="bg-slate-950/80 p-5 rounded-xl border border-slate-800 space-y-3">
            <span className="text-xs font-bold text-slate-300 uppercase block pb-2 border-b border-slate-800 flex items-center gap-2">
              <CheckSquare className="w-4 h-4 text-emerald-400" />
              ACTION CHECKLIST
            </span>
            <ul className="space-y-2.5 text-xs sm:text-sm text-slate-300">
              {fcBrief.checklist_action_items?.map((item, i) => (
                <li key={i} className="flex items-start gap-2">
                  <span className="text-emerald-400 font-bold mt-0.5">✓</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      {/* Quick EFB Metrics Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
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
