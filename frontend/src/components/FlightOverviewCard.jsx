import React, { useState, useEffect } from 'react';
import {
  Plane,
  Clock,
  MapPin,
  Edit3,
  Check,
  X,
  RotateCcw,
  CloudSun,
  Sun,
  CloudRain,
  CloudLightning,
  Cloud,
  CloudFog,
  Snowflake,
  Wind,
  Wrench,
  AlertTriangle,
  FileText,
  ShieldCheck
} from 'lucide-react';

export default function FlightOverviewCard({ data, weather, melItems }) {
  const {
    callsign,
    flight_number,
    aircraft_type,
    flight_date,
    departure,
    destination,
    alternate,
    etd_utc,
    etd_lcl,
    eta_utc,
    eta_lcl,
    arrival_date,
    flight_time,
    cruising_altitude,
    alternate_airports,
  } = data || {};

  const planTime = flight_time || '10Hr 42Min';
  const [customTime, setCustomTime] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [inputVal, setInputVal] = useState(planTime);

  useEffect(() => {
    setCustomTime(null);
    setInputVal(flight_time || '');
  }, [flight_time, callsign, destination?.icao]);

  // Every hook above runs unconditionally; only bail out afterwards.
  if (!data) return null;

  const handleSave = (e) => {
    e.preventDefault();
    if (inputVal.trim() && inputVal.trim() !== planTime) {
      setCustomTime(inputVal.trim());
    } else {
      setCustomTime(null);
    }
    setIsEditing(false);
  };

  const handleReset = () => {
    setCustomTime(null);
    setInputVal(planTime);
    setIsEditing(false);
  };

  const cleanName = (name) => {
    if (!name) return '';
    return name.replace(/\s*\([^)]*\)/g, '').trim();
  };

  const dynamicAlternates = alternate_airports && alternate_airports.length > 0
    ? alternate_airports
    : [
        {
          icao: alternate?.icao || 'KBOS',
          // Blank beats a wrong identifier: only fall back to the demo IATA when there is no real alternate.
          iata: alternate?.iata || (alternate?.icao ? '' : 'BOS'),
          name: cleanName(alternate?.name) || '제1 지정 교체공항 (Alternate Airport)',
          role: 'FILED DEST ALTERNATE',
          divertStatus: 'AVAILABLE',
          divertLabel: 'DIVERT AVAILABLE (회항 가능)',
          visRating: '시정 6SM 이상 (최저치 상회)',
          etaZ: eta_utc ? `${eta_utc} (+45m)` : '02:14Z (+1)',
          etaL: eta_lcl ? `${eta_lcl} (+45m)` : '22:14 L',
          distTime: '260 NM / 45분 / 22,400 LBS',
          wxStatus: 'GOOD',
          wxSummary: `${alternate?.name || alternate?.icao || '교체공항'} 법정 최저치 상회 만족, 안전 회항 가용.`,
        }
      ];

  const depIcao = departure?.icao || 'RKSI';
  const depIata = departure?.iata || 'ICN';
  const depName = cleanName(departure?.name) || '인천국제공항 (Incheon Intl)';
  const destIcao = destination?.icao || 'KJFK';
  const destIata = destination?.iata || 'JFK';
  const destName = cleanName(destination?.name) || '뉴욕 존 F. 케네디 국제공항 (John F. Kennedy Intl)';

  const depWx = weather?.departure || {};
  const destWx = weather?.destination || {};

  // Helper to render contextual weather icon
  const renderWxIcon = (text, size = "w-7 h-7") => {
    const s = (text || '').toUpperCase();
    if (s.includes('TS') || s.includes('THUNDER') || s.includes('CB') || s.includes('LIGHTNING')) {
      return <CloudLightning className={`${size} text-amber-400 stroke-[2.2] animate-pulse`} title="뇌우/적란운 주의" />;
    }
    if (s.includes('RA') || s.includes('RAIN') || s.includes('SH') || s.includes('DRIZZLE')) {
      return <CloudRain className={`${size} text-slate-300 stroke-[2.2]`} title="비/강수" />;
    }
    if (s.includes('SN') || s.includes('SNOW')) {
      return <Snowflake className={`${size} text-slate-300 stroke-[2.2]`} title="강설" />;
    }
    if (s.includes('FG') || s.includes('FOG') || s.includes('BR') || s.includes('MIST') || s.includes('HZ')) {
      return <CloudFog className={`${size} text-slate-300 stroke-[2.2]`} title="안개/박무" />;
    }
    if (s.includes('CAVOK') || s.includes('SKC') || s.includes('CLR') || s.includes('GOOD') || s.includes('SUN') || s.includes('CLEAR')) {
      return <Sun className={`${size} text-amber-300 stroke-[2.2]`} title="맑음/CAVOK" />;
    }
    return <CloudSun className={`${size} text-amber-200 stroke-[2.2]`} title="구름 조금/양호" />;
  };

  const effectiveMelItems = melItems || [
    {
      code: 'MEL 33-20-05A',
      item: '32K, 51K WINDOW LIGHT OUT',
      action: 'DEFERRED IAW MEL 33-20-05A (비행계획 후 발부)',
      status: 'CONFIRMED'
    },
    {
      code: 'CDL 27-32',
      item: 'LH WING NO 1 DROOP NOSE INBD LATERAL D-S',
      action: '좌측 날개 1번 드룹 노즈 CDL 적용 (운항 성능 반영 완료)',
      status: 'APPLIED'
    }
  ];

  return (
    <div id="section-overview" className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-lg space-y-6">
      {/* 1. Top Header Row (Callsign & Badges) */}
      <div className="flex flex-wrap items-center justify-between gap-4 pb-5 border-b border-slate-800">
        <div className="flex items-center gap-4">
          <div className="p-3 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
            <Plane className="w-7 h-7" />
          </div>
          <div className="px-4 py-2 bg-amber-500/15 border border-amber-400/40 rounded-xl text-amber-200 font-mono font-bold text-2xl sm:text-3xl tracking-wider leading-none shadow-[0_0_15px_rgba(245,158,11,0.15)]">
            {callsign || flight_number || 'AAR224'}
          </div>
          <div className="flex flex-col">
            <span className="text-xs sm:text-sm text-slate-400 font-mono font-bold uppercase tracking-wider">AIRCRAFT TYPE</span>
            <p className="text-lg sm:text-xl font-bold text-white leading-tight tracking-wide">
              {aircraft_type || 'A380-800 / Trent 970'}
            </p>
          </div>
        </div>

        <div className="flex items-center gap-3 text-sm sm:text-base font-mono">
          <div className="bg-slate-950 px-4 py-2.5 rounded-xl border border-slate-800 flex items-center gap-2.5">
            <span className="text-slate-400 font-bold text-xs sm:text-sm">PLAN TIME:</span>
            <span className="text-white font-bold text-base sm:text-lg">{planTime}</span>
          </div>
          <div className="bg-slate-950 px-4 py-2.5 rounded-xl border border-slate-800 flex items-center gap-2.5">
            <span className="text-slate-400 font-bold text-xs sm:text-sm">CRZ ALT:</span>
            <span className="text-white font-bold text-base sm:text-lg">{cruising_altitude || 'FL310~370'}</span>
          </div>
        </div>
      </div>

      {/* 2. Unified 1-Card Flight Sector (Departure -> Flight Time -> Destination Stacked Vertically with Weather Icons) */}
      <div className="bg-slate-950 p-5 sm:p-7 rounded-2xl border border-amber-500/30 space-y-4">
        {/* Row 1: Departure Card with Weather Icon */}
        <div className="bg-slate-900/90 p-5 rounded-xl border border-slate-800 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="space-y-1.5 min-w-0">
            <div className="flex items-center gap-3 flex-wrap">
              <span className="font-mono text-xs sm:text-sm font-bold uppercase tracking-wider text-amber-300 bg-amber-500/15 border border-amber-400/30 px-2.5 py-1 rounded-lg">
                DEPARTURE (출발지)
              </span>
              <span className="text-xs text-slate-400 font-mono">RUNWAYS: {departure?.runways || '15L/15R, 16L/16R'}</span>
            </div>
            <div className="flex items-center gap-3 pt-1">
              <div className="p-2 bg-slate-950 border border-slate-800 rounded-xl flex items-center justify-center">
                {renderWxIcon(depWx.condition_summary || depWx.raw_metar || 'CAVOK', 'w-8 h-8')}
              </div>
              <div className="min-w-0">
                <div className="flex items-baseline gap-2.5">
                  <span className="text-4xl sm:text-5xl font-bold font-mono text-amber-200 tracking-wider">{depIcao}</span>
                  {depIata && <span className="text-2xl font-bold text-amber-300/90 font-mono">({depIata})</span>}
                </div>
                <span className="block text-base sm:text-lg font-bold text-slate-300 mt-0.5 break-keep">{depName}</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 font-mono shadow-sm shrink-0">
            <div className="grid grid-cols-[auto_auto] gap-x-3 gap-y-1 items-center text-left">
              <span className="text-xs font-bold text-slate-400">ETD (UTC) :</span>
              <span className="font-bold text-amber-200 text-sm sm:text-base">{etd_utc || '12:05Z'}</span>
              <span className="text-xs font-bold text-slate-400">LCL TIME  :</span>
              <span className="font-bold text-amber-300/90 text-sm sm:text-base">{etd_lcl || '21:05 L'}</span>
              <span className="text-xs font-bold text-slate-400">DATE      :</span>
              <span className="font-bold text-slate-300 text-xs">{flight_date || 'TODAY'}</span>
            </div>
          </div>
        </div>

        {/* Row 2: Center Flight Time & Direct Route Info */}
        <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800/80 flex flex-col md:flex-row items-center justify-between gap-4 px-6">
          <div className="flex items-center gap-3 text-slate-400 text-sm shrink-0">
            <Plane className="w-5 h-5 text-amber-400 transform rotate-90 shrink-0" />
            <span className="whitespace-nowrap">비행 소요시간 및 계획 정보</span>
          </div>

          <div className="flex items-center gap-3">
            {isEditing ? (
              <form onSubmit={handleSave} className="flex items-center gap-2 bg-slate-950 p-1.5 rounded-xl border border-slate-700 shadow-lg">
                <input
                  type="text"
                  value={inputVal}
                  onChange={(e) => setInputVal(e.target.value)}
                  placeholder="예: 13Hr 24Min"
                  autoFocus
                  className="bg-slate-900 border border-slate-700 rounded-lg px-3 py-1 text-base font-bold font-mono text-white w-40 focus:outline-none focus:border-amber-400 text-center"
                />
                <button type="submit" className="p-1.5 bg-amber-400 text-slate-950 font-bold rounded-lg" title="저장">
                  <Check className="w-4 h-4 stroke-[3]" />
                </button>
                <button type="button" onClick={() => setIsEditing(false)} className="p-1.5 bg-slate-800 text-slate-400 rounded-lg" title="취소">
                  <X className="w-4 h-4" />
                </button>
              </form>
            ) : customTime ? (
              <div className="flex items-center gap-2.5">
                <span className="text-xs px-2 py-0.5 bg-slate-800 border border-slate-700 text-white font-mono font-bold rounded-lg uppercase">수정</span>
                <span className="text-2xl sm:text-3xl font-bold font-mono text-white">{customTime}</span>
                <button onClick={() => { setInputVal(customTime); setIsEditing(true); }} className="p-1 text-slate-400 hover:text-white" title="재수정">
                  <Edit3 className="w-4 h-4" />
                </button>
                <button onClick={handleReset} className="p-1 text-slate-400 hover:text-white" title="초기화">
                  <RotateCcw className="w-4 h-4" />
                </button>
                <span className="text-xs text-slate-400 font-mono ml-2">(PLAN: {planTime})</span>
              </div>
            ) : (
              <div className="flex items-center gap-3 group">
                <Clock className="w-6 h-6 text-slate-400 shrink-0" />
                <span className="text-2xl sm:text-3xl font-bold font-mono text-white">{planTime}</span>
                <button onClick={() => { setInputVal(planTime); setIsEditing(true); }} className="text-slate-400 group-hover:text-white p-1 hover:bg-slate-800 rounded-lg transition" title="수정">
                  <Edit3 className="w-4 h-4" />
                </button>
              </div>
            )}
          </div>

          <div className="text-xs sm:text-sm text-slate-300 flex flex-wrap items-center gap-x-4 gap-y-1">
            <span className="whitespace-nowrap">거리: <strong className="text-white font-mono">{data.total_distance || '6,663 NM'}</strong></span>
            <span>순항고도: <strong className="text-amber-200 font-mono">{cruising_altitude || 'FL310~370'}</strong></span>
          </div>
        </div>

        {/* Row 3: Destination Card with Weather Icon */}
        <div className="bg-slate-900/90 p-5 rounded-xl border border-slate-800 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="space-y-1.5 min-w-0">
            <div className="flex items-center gap-3 flex-wrap">
              <span className="font-mono text-xs sm:text-sm font-bold uppercase tracking-wider text-amber-300 bg-amber-500/15 border border-amber-400/30 px-2.5 py-1 rounded-lg">
                DESTINATION (도착지)
              </span>
              <span className="text-xs text-slate-400 font-mono">RUNWAYS: {destination?.runways || '13L/13R, 22L/22R, 31L/31R'}</span>
            </div>
            <div className="flex items-center gap-3 pt-1">
              <div className="p-2 bg-slate-950 border border-slate-800 rounded-xl flex items-center justify-center">
                {renderWxIcon(destWx.forecast || destWx.condition_summary || destWx.raw_metar || 'PROB30 TSRA', 'w-8 h-8')}
              </div>
              <div className="min-w-0">
                <div className="flex items-baseline gap-2.5">
                  <span className="text-4xl sm:text-5xl font-bold font-mono text-amber-200 tracking-wider">{destIcao}</span>
                  {destIata && <span className="text-2xl font-bold text-amber-300/90 font-mono">({destIata})</span>}
                </div>
                <span className="block text-base sm:text-lg font-bold text-slate-300 mt-0.5 break-keep">{destName}</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 font-mono shadow-sm shrink-0">
            <div className="grid grid-cols-[auto_auto] gap-x-3 gap-y-1 items-center text-left">
              <span className="text-xs font-bold text-slate-400">ETA (UTC) :</span>
              <span className="font-bold text-amber-200 text-sm sm:text-base">{eta_utc || '01:29Z (+1)'}</span>
              <span className="text-xs font-bold text-slate-400">LCL TIME  :</span>
              <span className="font-bold text-amber-300/90 text-sm sm:text-base">{eta_lcl || '21:29 L'}</span>
              <span className="text-xs font-bold text-slate-400">DATE      :</span>
              <span className="font-bold text-slate-300 text-xs">{arrival_date || `${flight_date || 'TODAY'} (+1)`}</span>
            </div>
          </div>
        </div>
      </div>

      {/* 3. Origin & Destination Weather Card (with Weather Icons next to Airport Names) */}
      <div className="bg-slate-950 rounded-2xl p-5 sm:p-7 border border-slate-800 shadow-lg space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <CloudSun className="w-6 h-6" />
            </div>
            <div>
              <h4 className="text-xl sm:text-2xl font-bold text-white font-mono uppercase tracking-wide">
                ORIGIN & DESTINATION WEATHER
              </h4>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-mono font-bold px-3.5 py-1.5 bg-slate-900 text-slate-300 border border-slate-700 rounded-lg shadow-sm shrink-0">
            METAR / TAF LIVE
          </span>
        </div>

        {/* Vertical Stack: 1. Origin Weather then 2. Destination Weather */}
        <div className="space-y-5">
          {/* 1. Origin Weather */}
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 space-y-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between pb-3 border-b border-slate-800 gap-2">
              <div className="flex items-center gap-3">
                <span className="text-xs font-mono font-bold px-2.5 py-1 rounded-lg bg-slate-950 border border-slate-700 text-slate-300 uppercase tracking-wider">
                  1. ORIGIN WEATHER (출발지)
                </span>
                <div className="flex items-center gap-2">
                  {renderWxIcon(depWx.condition_summary || depWx.raw_metar || 'CAVOK', 'w-6 h-6')}
                  <span className="text-2xl font-bold text-amber-200 font-mono">{depIcao}</span>
                  {depIata && <span className="text-lg font-bold text-amber-300 font-mono">({depIata})</span>}
                  <span className="text-sm font-bold text-slate-300">{depName}</span>
                </div>
              </div>
              <span className="text-xs font-mono font-bold px-3 py-1 rounded-lg border border-emerald-500/40 bg-slate-950 text-emerald-300 flex items-center gap-1.5">
                {renderWxIcon('CAVOK', 'w-4 h-4')}
                <span>GOOD (CAVOK)</span>
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-4 gap-3 font-mono text-center">
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span className="text-xs text-slate-400 font-bold block uppercase">이륙예정 (ETD)</span>
                <span className="font-bold text-sm sm:text-base text-amber-200 mt-1 block">{etd_utc || '12:05Z'} ({etd_lcl || '21:05 L'})</span>
              </div>
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span className="text-xs text-slate-400 font-bold block uppercase">WIND</span>
                <span className="font-bold text-sm sm:text-base text-white mt-1 block">{depWx.wind || '200° / 10 KT'}</span>
              </div>
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span className="text-xs text-slate-400 font-bold block uppercase">VISIBILITY</span>
                <span className="font-bold text-sm sm:text-base text-white mt-1 block">{depWx.visibility || '10 KM+ (CAVOK)'}</span>
              </div>
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span className="text-xs text-slate-400 font-bold block uppercase">TEMP / QNH</span>
                <span className="font-bold text-sm sm:text-base text-white mt-1 block">{depWx.temp_qnh || '24°C / 1012 hPa'}</span>
              </div>
            </div>

            <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-sm font-mono text-slate-300">
              <strong className="text-amber-200 block mb-1">[운항 판단]</strong>
              {depWx.assessment?.[0] || '출발지 기상 양호, 마른 활주로(Dry) 이륙 최저치 만족하여 정시 출발 가능.'}
            </div>
          </div>

          {/* 2. Destination Weather */}
          <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 space-y-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between pb-3 border-b border-slate-800 gap-2">
              <div className="flex items-center gap-3">
                <span className="text-xs font-mono font-bold px-2.5 py-1 rounded-lg bg-slate-950 border border-slate-700 text-slate-300 uppercase tracking-wider">
                  2. DESTINATION WEATHER (도착지)
                </span>
                <div className="flex items-center gap-2">
                  {renderWxIcon(destWx.forecast || destWx.condition_summary || destWx.raw_metar || 'PROB30 TSRA', 'w-6 h-6')}
                  <span className="text-2xl font-bold text-amber-200 font-mono">{destIcao}</span>
                  {destIata && <span className="text-lg font-bold text-amber-300 font-mono">({destIata})</span>}
                  <span className="text-sm font-bold text-slate-300">{destName}</span>
                </div>
              </div>
              <span className="text-xs font-mono font-bold px-3 py-1 rounded-lg border border-amber-500/40 bg-slate-950 text-amber-300 flex items-center gap-1.5">
                {renderWxIcon('TSRA', 'w-4 h-4')}
                <span>STANDARD / CAUTION</span>
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-4 gap-3 font-mono text-center">
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span className="text-xs text-slate-400 font-bold block uppercase">도착예정 (ETA)</span>
                <span className="font-bold text-sm sm:text-base text-amber-200 mt-1 block">{eta_utc || '01:29Z (+1)'} ({eta_lcl || '21:29 L'})</span>
              </div>
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span className="text-xs text-slate-400 font-bold block uppercase">WIND</span>
                <span className="font-bold text-sm sm:text-base text-white mt-1 block">{destWx.wind || '180° / 12 KT'}</span>
              </div>
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span className="text-xs text-slate-400 font-bold block uppercase">VISIBILITY</span>
                <span className="font-bold text-sm sm:text-base text-amber-200 mt-1 block">{destWx.visibility || '6 SM 이상 (강수 3SM)'}</span>
              </div>
              <div className="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span className="text-xs text-slate-400 font-bold block uppercase">TEMP / ALTIMETER</span>
                <span className="font-bold text-sm sm:text-base text-white mt-1 block">{destWx.temp_altimeter || '22°C / A3002'}</span>
              </div>
            </div>

            <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-sm font-mono text-slate-300">
              <strong className="text-amber-200 block mb-1">[운항 판단]</strong>
              {destWx.assessment?.[0] || `도착 시간대 적란운(CB) 및 소나기 예보(PROB30)로 접근 지연 가능성. 대체공항(${alternate?.icao || 'KBOS'}) 회항 계획 및 예비연료 확인 완료.`}
            </div>
          </div>
        </div>
      </div>

      {/* 4. All Alternate & Diversion Airports Card (with Weather Icons next to each airport) */}
      <div className="bg-slate-950 rounded-2xl p-5 sm:p-7 border border-slate-800 shadow-lg space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <MapPin className="w-6 h-6" />
            </div>
            <div>
              <h4 className="text-xl sm:text-2xl font-bold text-white font-mono uppercase tracking-wide">
                ALL ALTERNATE & ENROUTE DIVERSION AIRPORTS
              </h4>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-mono font-bold px-3.5 py-1.5 bg-slate-900 text-slate-300 border border-slate-700 rounded-lg shadow-sm shrink-0">
            {dynamicAlternates.length} AIRFIELD{dynamicAlternates.length > 1 ? 'S' : ''} ACTIVE
          </span>
        </div>

        <div className="divide-y divide-slate-800">
          {dynamicAlternates.map((alt, idx) => (
            <div key={idx} className={`py-5 space-y-3.5 transition ${idx === 0 ? 'pt-1' : ''} ${idx === dynamicAlternates.length - 1 ? 'pb-1' : ''}`}>
              <div className="flex flex-wrap items-center justify-between gap-3">
                <div className="flex flex-wrap items-center gap-3.5">
                  <span className="text-xs sm:text-sm font-mono font-bold px-3 py-1 rounded-lg bg-slate-900 border border-slate-700 text-slate-300 uppercase tracking-wider shrink-0">
                    {alt.role || 'ALTERNATE'}
                  </span>
                  <div className="flex items-center gap-2">
                    {renderWxIcon(alt.wxSummary || alt.visRating || 'GOOD', 'w-6 h-6')}
                    <div className="flex items-baseline gap-2 font-mono">
                      <span className="text-2xl sm:text-3xl font-bold text-white">{alt.icao}</span>
                      {alt.iata && <span className="text-lg font-bold text-slate-400">({alt.iata})</span>}
                    </div>
                    <span className="text-lg sm:text-xl font-bold text-slate-100">{cleanName(alt.name)}</span>
                  </div>
                </div>

                <span className="text-xs sm:text-sm font-mono font-bold px-3.5 py-1.5 rounded-lg border border-slate-700 bg-slate-900 text-slate-200 flex items-center gap-2 shrink-0">
                  <Check className="w-4 h-4 text-emerald-400 stroke-[3]" />
                  {alt.divertLabel || 'DIVERT AVAILABLE'}
                </span>
              </div>

              <div className="bg-slate-900 border border-slate-800 px-5 py-3.5 rounded-xl flex flex-wrap items-center justify-between gap-4 text-sm sm:text-base font-mono">
                <div className="flex items-center gap-2.5">
                  <span className="text-slate-400 font-bold">회항 ETA:</span>
                  <span className="text-white font-bold">{alt.etaZ || 'N/A'}</span>
                  {alt.etaL && <span className="text-slate-400">({alt.etaL})</span>}
                </div>
                <div className="flex items-center gap-2.5 text-slate-200 font-bold">
                  <span className="text-slate-400 font-bold">거리/시간/연료:</span>
                  <span>{alt.distTime || 'STANDBY'}</span>
                </div>
                <div className="flex items-center gap-2 bg-slate-950 px-3 py-1.5 rounded-lg border border-slate-800 text-xs sm:text-sm text-slate-300">
                  <span className="text-slate-400 font-bold">시정:</span>
                  <strong className="text-slate-200 font-bold">{alt.visRating || '시정 양호'}</strong>
                </div>
              </div>

              <div className="bg-slate-950 px-5 py-3.5 rounded-xl border border-slate-800 flex items-start gap-3.5 text-sm sm:text-base font-mono leading-relaxed">
                <span className="text-xs sm:text-sm font-bold px-2.5 py-1 rounded-lg border border-slate-700 bg-slate-900 text-slate-300 shrink-0 mt-0.5">
                  {alt.wxStatus || 'GOOD'}
                </span>
                <span className="text-slate-300 font-normal">
                  {alt.wxSummary || `${alt.name || alt.icao} 교체공항 기상 상태 적합.`}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 5. NEW DEDICATED MEL / CDL CARD */}
      <div className="bg-slate-950 rounded-2xl p-5 sm:p-7 border border-slate-800 shadow-lg space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <Wrench className="w-6 h-6" />
            </div>
            <div>
              <h4 className="text-xl sm:text-2xl font-bold text-white font-mono uppercase tracking-wide">
                DEFERRED DEFECTS & CONFIGURATION DEVIATION (MEL / CDL)
              </h4>
              <p className="text-xs sm:text-sm text-slate-400 font-mono mt-0.5">
                당해 항공기({aircraft_type || 'A380 HL7626'}) 적용 이연 정비 및 형상 변경 항목
              </p>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-mono font-bold px-3.5 py-1.5 bg-slate-900 text-amber-300 border border-amber-500/40 rounded-lg shadow-sm shrink-0">
            {effectiveMelItems.length} ITEMS APPLIED
          </span>
        </div>

        <div className="space-y-3">
          {effectiveMelItems.map((item, idx) => (
            <div
              key={idx}
              className="bg-slate-900 border border-slate-800 p-4 sm:p-5 rounded-xl flex flex-col md:flex-row items-start md:items-center justify-between gap-4 shadow-sm"
            >
              <div className="space-y-1 flex-1">
                <div className="flex items-center gap-3">
                  <span className="text-xs font-bold px-2.5 py-1 rounded-lg bg-slate-950 border border-slate-700 text-amber-300 uppercase">
                    {item.code}
                  </span>
                  <span className="text-base sm:text-lg font-bold text-white">
                    {item.item}
                  </span>
                </div>
                <p className="text-xs sm:text-sm text-slate-300 pl-1">
                  {item.action}
                </p>
              </div>

              <div className="shrink-0 self-end md:self-center">
                <span className={`text-xs sm:text-sm font-bold px-3 py-1.5 rounded-lg border flex items-center gap-2 ${
                  item.status === 'APPLIED' || item.status === 'CONFIRMED'
                    ? 'bg-slate-950 text-emerald-300 border-emerald-600/40'
                    : 'bg-slate-950 text-amber-300 border-amber-500/40'
                }`}>
                  <ShieldCheck className="w-4 h-4 text-emerald-400 stroke-[2.5]" />
                  {item.status}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
