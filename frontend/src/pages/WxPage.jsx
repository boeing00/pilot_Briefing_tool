import React, { useState } from 'react';
import {
  CloudRain,
  Wind,
  AlertTriangle,
  CloudLightning,
  Eye,
  Terminal,
  Compass,
  Thermometer,
  PlaneTakeoff,
  PlaneLanding,
  Check,
  Gauge,
  Clock,
  Sun,
  CloudSun,
  Cloud,
  CloudFog,
  Snowflake,
  MapPin,
} from 'lucide-react';
import WeatherBriefingCard from '../components/WeatherBriefingCard';

export default function WxPage({ briefing }) {
  if (!briefing) return null;

  const wx = briefing.weather_briefing || {};
  const fs = briefing.flight_summary || {};
  const dep = wx.departure || {};
  const dest = wx.destination || {};
  const altn = wx.alternate || {};

  const depIcao = dep.icao || fs.departure?.icao || 'RKSI';
  const depName = dep.name || fs.departure?.name || '인천국제공항';
  const depEtd = dep.etd || fs.etd_utc || '12:05Z';
  const depRwy = dep.runway || fs.departure?.runways || 'RWY 15L/15R';
  const depWind = dep.wind || '200° / 10 KT';
  const depVis = dep.visibility || '10 KM+';
  const depCeil = dep.ceiling || 'SKC / NSC';
  const depTemp = dep.temp_qnh || '24°C / 1012 hPa';
  const depAssess = dep.assessment || [
    '출발지 기상 양호, 마른 노면(Dry) 상태 유지로 정상 출발 가능.',
    '이륙 시간대 윈드시어(WS) 및 대류성 위험 없음.',
  ];
  const depMetar = dep.raw_metar || `METAR ${depIcao} 100500Z 20010KT CAVOK 24/19 Q1012 NOSIG=`;
  const depTaf = dep.raw_taf || `TAF ${depIcao} 100500Z 1006/1112 20010KT CAVOK=`;

  const destIcao = dest.icao || fs.destination?.icao || 'KJFK';
  const destName = dest.name || fs.destination?.name || '뉴욕 존 F. 케네디 국제공항';
  const destEta = dest.eta || fs.eta_utc || '01:29Z (+1)';
  const destRwy = dest.runway || fs.destination?.runways || 'RWY 13L/22L/31L';
  const destWind = dest.wind || '180° / 12 KT';
  const destVis = dest.visibility || '6 SM 이상';
  const destCeil = dest.ceiling || 'SCT050';
  const destTemp = dest.temp_altimeter || '22°C / A3002';
  const destAssess = dest.assessment || [
    '도착 시간대 착륙 최저치 만족, 정상 접근 가능.',
    `예비연료 및 교체공항(${altn.icao || fs.alternate?.icao || 'ALTN'}) 회항 계획 확인.`,
  ];
  const destMetar = dest.raw_metar || `METAR ${destIcao} 100551Z 18012KT 10SM CLR 22/16 A3002=`;
  const destTaf = dest.raw_taf || `TAF ${destIcao} 100522Z 1006/1112 18012KT P6SM SCT060=`;

  const altnIcao = altn.icao || fs.alternate?.icao || 'KBOS';
  const altnName = altn.name || fs.alternate?.name || '보스턴 로건 국제공항';
  const altnEta = altn.eta || '02:14Z (+1)';
  const altnMetar = altn.raw_metar || `METAR ${altnIcao} 100554Z 29010KT 10SM FEW250=`;
  const altnTaf = altn.raw_taf || `TAF ${altnIcao} 100534Z 1006/1112 29010KT P6SM FEW250=`;
  const altnSuitability = altn.suitability || 'GOOD';
  const altnAssess = altn.assessment || `${altnName} 법정 대체공항 최저치 상회 만족, 안전 회항 보장.`;

  const fltTime = fs.flight_time || '-';

  const renderWxIcon = (text, size = "w-7 h-7") => {
    const s = (text || '').toUpperCase();
    if (s.includes('TS') || s.includes('THUNDER') || s.includes('CB') || s.includes('LIGHTNING')) {
      return <CloudLightning className={`${size} text-amber-400 stroke-[2.2] animate-pulse`} title="뇌우/적란운 주의" />;
    }
    if (s.includes('RA') || s.includes('RAIN') || s.includes('SH') || s.includes('DRIZZLE')) {
      return <CloudRain className={`${size} text-cyan-400 stroke-[2.2]`} title="비/강수" />;
    }
    if (s.includes('SN') || s.includes('SNOW')) {
      return <Snowflake className={`${size} text-sky-200 stroke-[2.2]`} title="강설" />;
    }
    if (s.includes('FG') || s.includes('FOG') || s.includes('BR') || s.includes('MIST') || s.includes('HZ')) {
      return <CloudFog className={`${size} text-slate-300 stroke-[2.2]`} title="안개/박무" />;
    }
    if (s.includes('CAVOK') || s.includes('SKC') || s.includes('CLR') || s.includes('GOOD') || s.includes('SUN')) {
      return <Sun className={`${size} text-amber-300 stroke-[2.2]`} title="맑음/CAVOK" />;
    }
    return <CloudSun className={`${size} text-amber-200 stroke-[2.2]`} title="구름 조금/양호" />;
  };

  const turbulenceTimeline = (wx.turbulence_timeline && wx.turbulence_timeline.length > 0)
    ? wx.turbulence_timeline
    : [
        {
          time: 'T+00:45',
          level: 'Light Turb',
          segment: 'CLIMB / DEPARTURE CORRIDOR',
          detail: '상승 및 순항고도 진입 구간 기류 요동 (정상 순항)',
          action: '정상 순항',
        },
        {
          time: 'T+04:30',
          level: 'Moderate Turb',
          segment: 'OCEANIC / ENROUTE JETSTREAM',
          detail: '제트기류 전단대(Jetstream Shearing) 통과',
          action: '벨트 사인 사전 점등',
        },
        {
          time: 'T+11:15',
          level: 'Light to Moderate',
          segment: 'DESCENT TRANSITION',
          detail: '강하 전 고고도 난류 구역 통과',
          action: '착륙 준비 사전 착수',
        },
      ];

  const turbulenceGuidelines = (wx.turbulence_guidelines && wx.turbulence_guidelines.length > 0)
    ? wx.turbulence_guidelines
    : [
        '난류 예상 구간 진입 15분 전 승객 좌석벨트 사인 사전 점등',
        'Moderate CAT 예상 시 객실 승무원 서비스 일시 중단 및 카트 래치 고정',
        '기상 레이더 적절한 Tilt 조절 및 스텝클라임 고도 최적화',
      ];

  const enrouteAirports = (wx.enroute_airports && wx.enroute_airports.length > 0)
    ? wx.enroute_airports
    : [
        {
          icao: altnIcao,
          name: altnName,
          tag: 'FILED ALTERNATE',
          taf: altnTaf,
          note: '시정 6SM 이상, 착륙 최저치 만족',
        },
        {
          icao: 'PANC',
          name: '앵커리지 테드 스티븐스 공항',
          tag: 'ENROUTE ERA / ETP',
          taf: 'TAF PANC 100500Z 1006/1112 16008KT P6SM SCT040',
          note: '기상 양호, 착륙 기준 충족',
        },
      ];

  const sigmets = (wx.sigmets && wx.sigmets.length > 0)
    ? wx.sigmets
    : [
        {
          fir: '[PAZA / CZEG FIR]',
          text: 'SIGMET VALID FOR HIGH ALTITUDE MODERATE TURBULENCE FL340-FL380.',
        },
        {
          fir: '[RJJJ 일본 FIR]',
          text: 'TYPHOON CHAN-HOM LOCATED 280NM SE OF TOKYO, MOVING NE AT 15KT. NO DIRECT IMPACT ON FILED ROUTE.',
        },
      ];

  const typhoon = wx.typhoon_or_storm || {
    title: '15호 태풍 찬홈(Chan-hom) 및 대류 활동 모니터링',
    tag: 'MONITORING',
    detail: '15호 태풍 찬홈이 일본 남동쪽 해상을 지나 북동진 중이나 당사 계획 항로 남측 200NM 이상 이격되어 직접 영향은 없습니다. 다만 일본 열도 통과 시 외곽 기류 수렴에 따른 약한 요동에 주의하십시오.',
  };

  return (
    <div className="space-y-7 animate-fade-in font-mono">
      {/* 1. Departure Weather Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-xl space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <PlaneTakeoff className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-3">
                {renderWxIcon(dep.condition_summary || depMetar, 'w-7 h-7')}
                <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
                  출발지 기상: {depIcao} ({depName})
                </h3>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                DEPARTURE AIRPORT METAR & TAF / ETD: {depEtd} / {depRwy}
              </p>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-bold px-3.5 py-1.5 bg-slate-950 border border-slate-700 text-slate-300 rounded-lg shadow-sm shrink-0 flex items-center gap-1.5">
            {renderWxIcon('CAVOK', 'w-4 h-4')}
            <span>GOOD (CAVOK)</span>
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs text-slate-400 font-bold block uppercase">WIND</span>
            <span className="font-bold text-lg text-white mt-1 block">{depWind}</span>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs text-slate-400 font-bold block uppercase">VISIBILITY</span>
            <span className="font-bold text-lg text-white mt-1 block">{depVis}</span>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs text-slate-400 font-bold block uppercase">CEILING / CLOUD</span>
            <span className="font-bold text-lg text-white mt-1 block">{depCeil}</span>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs text-slate-400 font-bold block uppercase">TEMP / QNH</span>
            <span className="font-bold text-lg text-white mt-1 block">{depTemp}</span>
          </div>
        </div>

        <div className="bg-slate-950 p-4 sm:p-5 rounded-xl border border-slate-800 space-y-2 shadow-inner">
          <span className="text-xs font-bold text-slate-200 uppercase tracking-wider block">
            [운항 승무원 기상 판단 요약]
          </span>
          <ul className="space-y-1.5 text-xs sm:text-sm text-slate-300">
            {depAssess.map((item, idx) => (
              <li key={idx} className="flex items-start gap-2">
                <span className="text-amber-400 font-bold">•</span>
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="space-y-2 text-xs">
          <div className="bg-slate-950 p-3 rounded-lg border border-slate-850 text-slate-300 break-words">
            <span className="text-slate-500 font-bold block mb-1">METAR:</span>
            <code>{depMetar}</code>
          </div>
          <div className="bg-slate-950 p-3 rounded-lg border border-slate-850 text-slate-300 break-words">
            <span className="text-slate-500 font-bold block mb-1">TAF:</span>
            <code>{depTaf}</code>
          </div>
        </div>
      </div>

      {/* 2. Destination Weather Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-xl space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <PlaneLanding className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-3">
                {renderWxIcon(dest.forecast || dest.condition_summary || destMetar, 'w-7 h-7')}
                <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
                  목적지 기상: {destIcao} ({destName})
                </h3>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                DESTINATION AIRPORT METAR & TAF / ETA: {destEta} / {destRwy}
              </p>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-bold px-3.5 py-1.5 bg-slate-950 border border-amber-500/40 text-amber-300 rounded-lg shadow-sm shrink-0 flex items-center gap-1.5">
            {renderWxIcon('TSRA', 'w-4 h-4')}
            <span>PROB30 TSRA / CAUTION</span>
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs text-slate-400 font-bold block uppercase">WIND</span>
            <span className="font-bold text-lg text-white mt-1 block">{destWind}</span>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs text-slate-400 font-bold block uppercase">VISIBILITY</span>
            <span className="font-bold text-lg text-amber-200 mt-1 block">{destVis}</span>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs text-slate-400 font-bold block uppercase">CEILING / CLOUD</span>
            <span className="font-bold text-lg text-white mt-1 block">{destCeil}</span>
          </div>
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 shadow-inner">
            <span className="text-xs text-slate-400 font-bold block uppercase">TEMP / ALTIMETER</span>
            <span className="font-bold text-lg text-white mt-1 block">{destTemp}</span>
          </div>
        </div>

        <div className="bg-slate-950 p-4 sm:p-5 rounded-xl border border-slate-800 space-y-2 shadow-inner">
          <span className="text-xs font-bold text-slate-200 uppercase tracking-wider block">
            [운항 승무원 기상 판단 요약]
          </span>
          <ul className="space-y-1.5 text-xs sm:text-sm text-slate-300">
            {destAssess.map((item, idx) => (
              <li key={idx} className="flex items-start gap-2">
                <span className="text-amber-400 font-bold">•</span>
                <span>{item}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="space-y-2 text-xs">
          <div className="bg-slate-950 p-3 rounded-lg border border-slate-850 text-slate-300 break-words">
            <span className="text-slate-500 font-bold block mb-1">METAR:</span>
            <code>{destMetar}</code>
          </div>
          <div className="bg-slate-950 p-3 rounded-lg border border-slate-850 text-slate-300 break-words">
            <span className="text-slate-500 font-bold block mb-1">TAF:</span>
            <code>{destTaf}</code>
          </div>
        </div>
      </div>

      {/* 3. Filed Alternate Weather Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-xl space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <MapPin className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-3">
                {renderWxIcon(altnAssess || altnMetar, 'w-7 h-7')}
                <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
                  지정 교체공항: {altnIcao} ({altnName})
                </h3>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                FILED ALTERNATE AIRPORT / ETA: {altnEta}
              </p>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-bold px-3.5 py-1.5 bg-slate-950 border border-slate-700 text-slate-300 rounded-lg shadow-sm shrink-0 flex items-center gap-1.5">
            {renderWxIcon('GOOD', 'w-4 h-4')}
            <span>{altnSuitability}</span>
          </span>
        </div>

        <div className="bg-slate-950 p-4 sm:p-5 rounded-xl border border-slate-800 space-y-2 shadow-inner">
          <span className="text-xs font-bold text-slate-200 uppercase tracking-wider block">
            [교체공항 법정 최저치 적합성 판단]
          </span>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            {altnAssess}
          </p>
        </div>

        <div className="space-y-2 text-xs">
          <div className="bg-slate-950 p-3 rounded-lg border border-slate-850 text-slate-300 break-words">
            <span className="text-slate-500 font-bold block mb-1">METAR:</span>
            <code>{altnMetar}</code>
          </div>
          <div className="bg-slate-950 p-3 rounded-lg border border-slate-850 text-slate-300 break-words">
            <span className="text-slate-500 font-bold block mb-1">TAF:</span>
            <code>{altnTaf}</code>
          </div>
        </div>
      </div>
    </div>
  );
}
