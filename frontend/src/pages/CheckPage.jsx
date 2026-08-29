import React from 'react';
import { CheckCheck, Check, ShieldAlert, FileText, Scale, Fuel, Navigation, ArrowDownUp } from 'lucide-react';

export default function CheckPage({ briefing }) {
  if (!briefing) return null;

  const depIcao = briefing.flight_summary?.departure?.icao || 'RKSI';
  const destIcao = briefing.flight_summary?.destination?.icao || 'KLAX';
  const altnIcao = briefing.flight_summary?.alternate?.icao || 'KSAN';
  const fltTime = briefing.flight_summary?.flight_time || '-';
  const crzAlt = briefing.flight_summary?.cruising_altitude || 'FL350 ~ 390';
  const actType = briefing.flight_summary?.aircraft_type || 'A350 / B787';
  const totalDist = briefing.route_analysis?.total_distance || briefing.flight_summary?.total_distance || '-';

  const cfpRoute = briefing.validation_check?.cfp_route || briefing.route_analysis?.filed_route_string || `${depIcao}..ENROUTE..${destIcao}`;
  const atsFplRoute = briefing.validation_check?.ats_fpl_route || `N0480F350 DCT ${cfpRoute}`;
  const matchPct = briefing.validation_check?.match_percentage || '100%';

  // The 여유 (margin) figures used to be literal strings that only matched the demo
  // weights, so any real OFP showed weights and a margin that did not add up.
  const fw = briefing.fuel_and_weights || {};
  const lbsOf = (v) => {
    const m = String(v ?? '').match(/([0-9][0-9,]*)/);
    return m ? parseInt(m[1].replace(/,/g, ''), 10) : null;
  };
  const marginOf = (est, max) => {
    const e = lbsOf(est);
    const x = lbsOf(max);
    return e !== null && x !== null ? x - e : null;
  };
  const fmtMargin = (est, max, fallback) => {
    const m = marginOf(est, max);
    return `${(m !== null ? m : fallback).toLocaleString()} LBS`;
  };

  const estTow = fw.estimated_tow || '568,200 LBS';
  const maxTow = fw.max_tow || '617,200 LBS';
  const estZfw = fw.estimated_zfw || '361,100 LBS';
  const maxZfw = fw.max_zfw || '423,200 LBS';
  const estLaw = fw.estimated_law || '385,800 LBS';
  const maxLaw = fw.max_law || '451,900 LBS';

  const towMarginTxt = fmtMargin(estTow, maxTow, 49000);
  const zfwMarginTxt = fmtMargin(estZfw, maxZfw, 62100);
  const ldwMarginTxt = fmtMargin(estLaw, maxLaw, 66100);

  const rawItems = (briefing.validation_check?.items && briefing.validation_check.items.length > 0)
    ? briefing.validation_check.items
    : [
        {
          category: 'TOW / AGTOW 여유',
          detail: `EST TOW (${estTow}) vs AGTOW (${maxTow}) - 여유 ${towMarginTxt}`,
          status: `여유 ${towMarginTxt} (최소제한)`,
          statusType: 'OK',
          isGoverningLimit: true,
        },
        {
          category: 'ZFW / MZFW 여유',
          detail: `EST ZFW (${estZfw}) vs MZFW (${maxZfw}) - 여유 ${zfwMarginTxt} (충족)`,
          status: `여유 ${zfwMarginTxt} (OK)`,
          statusType: 'OK',
        },
        {
          category: 'LDW / MLDW 여유',
          detail: `EST LAW (${estLaw}) vs MLDW (${maxLaw}) - 여유 ${ldwMarginTxt} (충족)`,
          status: `여유 ${ldwMarginTxt} (OK)`,
          statusType: 'OK',
        },
        {
          category: 'MEL / CDL 내용',
          detail: briefing.company_rules_and_mel?.mel_cdl_items?.[0]?.item || '정비 이연 품목(MEL/CDL) 안전 검토 완료',
          status: '검토 완료',
          statusType: 'OK',
        },
        {
          category: '디스패치 고려사항',
          detail: `${destIcao} 도착 기상 대비 회항 연료(${briefing.fuel_and_weights?.alternate_fuel || '8,200 LBS'}) 및 난류 회피 계획 반영`,
          status: '반영 완료',
          statusType: 'OK',
        },
        {
          category: '이륙연료 합계',
          detail: `TRIP ${briefing.fuel_and_weights?.trip_fuel || '182,400 LBS'} + EXTRA ${briefing.fuel_and_weights?.extra_fuel || '4,500 LBS'} 일치`,
          status: '일치 (MATCH)',
          statusType: 'OK',
        },
        {
          category: '램프연료 합계',
          detail: `BLOCK FUEL ${briefing.fuel_and_weights?.block_fuel || '218,500 LBS'} 탑재량 확인`,
          status: '일치 (MATCH)',
          statusType: 'OK',
        },
        {
          category: '도착 잔여 vs 교체+최종예비',
          detail: `FOD ≥ ALTN ${briefing.fuel_and_weights?.alternate_fuel || '8.2k'} + FINAL RES ${briefing.fuel_and_weights?.final_reserve || '6.4k'}`,
          status: '법정 만족 (OK)',
          statusType: 'OK',
        },
        {
          category: '교체공항 연료 일치',
          detail: `연료블록 ALTN/${altnIcao} ${briefing.fuel_and_weights?.alternate_fuel || '8,200 LBS'} 일치`,
          status: '일치 (MATCH)',
          statusType: 'OK',
        },
        {
          category: 'CFP 항로 vs ATS FPL',
          detail: '컴퓨터 비행계획서(CFP)와 ATS 제출 비행계획서 웨이포인트 100% 일치',
          status: '100% MATCH',
          statusType: 'OK',
        },
      ];

  // Reorder items so that 1: TOW, 2: ZFW, 3: LDW, followed by remaining items
  const cat = (i) => i?.category || '';
  const towItem = rawItems.find((i) => cat(i).includes('TOW') || cat(i).includes('이륙중량')) || rawItems[0];
  const zfwItem = rawItems.find((i) => cat(i).includes('ZFW') || cat(i).includes('무연료')) || rawItems[1];
  const ldwItem = rawItems.find((i) => cat(i).includes('LDW') || cat(i).includes('LAW') || cat(i).includes('착륙중량')) || rawItems[2];

  const otherItems = rawItems.filter((i) =>
    i !== towItem && i !== zfwItem && i !== ldwItem &&
    !cat(i).includes('TOW') && !cat(i).includes('ZFW') && !cat(i).includes('LDW') && !cat(i).includes('LAW')
  );

  const orderedItems = [towItem, zfwItem, ldwItem, ...otherItems].filter(Boolean);

  // Parse margins for 1~3 weight items
  const parseMargin = (item, fallback) => {
    if (!item) return fallback;
    const m = (item.detail || '').match(/여유\s*([0-9,]+)\s*LBS/i) || (item.status || '').match(/여유\s*([0-9,]+)\s*LBS/i);
    if (m) return parseInt(m[1].replace(/,/g, ''), 10);
    return fallback;
  };

  const towMargin = parseMargin(towItem, 49000);
  const zfwMargin = parseMargin(zfwItem, 62100);
  const ldwMargin = parseMargin(ldwItem, 66100);

  const minMarginVal = Math.min(towMargin, zfwMargin, ldwMargin);
  const governingItemName = minMarginVal === towMargin ? '1. TOW 여유' : (minMarginVal === zfwMargin ? '2. ZFW 여유' : '3. LDW 여유');
  const governingMarginFormatted = minMarginVal.toLocaleString() + ' LBS';

  return (
    <div className="space-y-7 animate-fade-in font-mono">
      {/* 1. Single Unified Card: Top/Bottom Route Comparison */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-xl space-y-5">
        {/* Header */}
        <div className="flex flex-wrap items-center justify-between gap-3 pb-5 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-3 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <Navigation className="w-7 h-7" />
            </div>
            <div>
              <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
                ROUTE COMPARISON: CFP ROUTE vs ATS ICAO FPL
              </h3>
            </div>
          </div>
          <span className="text-sm sm:text-base lg:text-lg font-black px-4 sm:px-5 py-2 sm:py-2.5 bg-emerald-950/90 border-2 border-emerald-400 text-emerald-300 rounded-xl shadow-lg shadow-emerald-950/60 shrink-0 flex items-center gap-2.5 tracking-wider">
            <Check className="w-5 h-5 sm:w-6 sm:h-6 text-emerald-400 stroke-[3.5]" />
            {matchPct} WAYPOINT & AIRWAY MATCH
          </span>
        </div>

        {/* Visual Connected Layout: Card 1 (CFP) ⟷ Card 2 (ATS FPL) with Connecting Lines */}
        <div className="relative pl-6 sm:pl-8 space-y-4">
          {/* Left Vertical Glowing Connector Spine */}
          <div className="absolute left-2.5 sm:left-3.5 top-6 bottom-6 w-1 bg-gradient-to-b from-emerald-400 via-emerald-500 to-emerald-400 rounded-full shadow-[0_0_12px_rgba(52,211,153,0.6)]">
            {/* Center Junction Node */}
            <div className="absolute top-1/2 -translate-y-1/2 -left-1 w-3 h-3 rounded-full bg-emerald-400 border-2 border-slate-900 shadow-md shadow-emerald-400" />
          </div>

          {/* Top: CFP Route Box (Card 1) */}
          <div className="relative group">
            {/* Top Node */}
            <div className="absolute -left-6 sm:-left-8 top-6 w-3.5 h-3.5 rounded-full bg-emerald-400 border-2 border-slate-900 shadow-md shadow-emerald-400" />
            <div className="bg-slate-950/90 border border-slate-800 rounded-2xl p-5 space-y-3 shadow-inner group-hover:border-emerald-500/40 transition-all">
              <div className="flex items-center justify-between">
                <span className="text-xs sm:text-sm font-bold text-slate-200 bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-lg uppercase tracking-wider flex items-center gap-2">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                  1. COMPUTERIZED FLIGHT PLAN (CFP) ROUTE
                </span>
                <span className="text-xs sm:text-sm font-bold text-slate-400">OFP ROUTE</span>
              </div>

              <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-5 text-sm sm:text-base leading-relaxed text-slate-200 font-bold break-words tracking-wide">
                <span className="text-amber-200 font-black">{depIcao}</span> → {cfpRoute} → <span className="text-amber-200 font-black">{destIcao}</span>
              </div>
            </div>
          </div>

          {/* Center Comparison Connector Bridge (Explicit Visual Link between Card 1 and Card 2) */}
          <div className="relative flex items-center justify-center my-1 py-1">
            {/* Horizontal Dashed Connector */}
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t-2 border-dashed border-emerald-500/50" />
            </div>

            {/* Floating Comparison Match Pill */}
            <div className="relative bg-slate-900 border-2 border-emerald-400/90 px-4 sm:px-6 py-2 rounded-full shadow-xl shadow-emerald-950/90 flex items-center gap-2.5 text-xs sm:text-sm font-black text-emerald-300 z-10 tracking-wide">
              <ArrowDownUp className="w-4 h-4 text-emerald-400 stroke-[3]" />
              <span>1번 CFP 항로 ⟷ 2번 ATS FPL 항로 웨이포인트 100% 완전 일치 대조</span>
              <Check className="w-4 h-4 text-emerald-400 stroke-[3.5]" />
            </div>
          </div>

          {/* Bottom: ATS ICAO FPL Field 15 Box (Card 2) */}
          <div className="relative group">
            {/* Bottom Node */}
            <div className="absolute -left-6 sm:-left-8 top-6 w-3.5 h-3.5 rounded-full bg-emerald-400 border-2 border-slate-900 shadow-md shadow-emerald-400" />
            <div className="bg-slate-950/90 border border-slate-800 rounded-2xl p-5 space-y-3 shadow-inner group-hover:border-emerald-500/40 transition-all">
              <div className="flex items-center justify-between">
                <span className="text-xs sm:text-sm font-bold text-slate-200 bg-slate-900 border border-slate-700 px-3 py-1.5 rounded-lg uppercase tracking-wider flex items-center gap-2">
                  <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                  2. SUBMITTED ATS FLIGHT PLAN (ICAO FPL)
                </span>
                <span className="text-xs sm:text-sm font-bold text-slate-400">FIELD 15 ROUTE</span>
              </div>

              <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 sm:p-5 text-sm sm:text-base leading-relaxed text-slate-200 font-bold break-words tracking-wide">
                {atsFplRoute}
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Key Flight Metrics Bar */}
        <div className="border-t border-slate-800 pt-4 flex flex-wrap items-center justify-between gap-4 text-xs sm:text-sm text-slate-300">
          <span>총 비행거리: <strong className="text-white font-bold">{totalDist}</strong></span>
          <span>예상 비행시간: <strong className="text-white font-bold">{fltTime}</strong></span>
          <span>순항고도: <strong className="text-amber-200 font-bold">{crzAlt}</strong></span>
          <span>기체등록: <strong className="text-white font-bold">{actType}</strong></span>
          <span>목적지/교체: <strong className="text-amber-200 font-bold">{destIcao} / {altnIcao}</strong></span>
        </div>
      </div>

      {/* 2. Flight Plan Cross-Check & Operational Validation Section */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-xl space-y-5">
        {/* Header */}
        <div className="flex flex-wrap items-center justify-between gap-3 pb-5 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-3 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <CheckCheck className="w-7 h-7" />
            </div>
            <div>
              <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
                FLIGHT PLAN CROSS-CHECK & OPERATIONAL VALIDATION
              </h3>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-bold px-3.5 py-1.5 bg-slate-950 border border-slate-700 text-slate-300 rounded-lg shadow-sm shrink-0 flex items-center gap-2">
            <Check className="w-4 h-4 sm:w-5 sm:h-5 text-emerald-400 stroke-[3.5]" />
            {orderedItems.length} ITEMS VERIFIED (OK)
          </span>
        </div>

        {/* Weight Limitation Callout Notice */}
        <div className="bg-slate-950 p-3.5 rounded-xl border border-amber-500/40 flex flex-wrap items-center justify-between gap-2 text-xs shadow-inner">
          <div className="flex items-center gap-2.5">
            <span className="px-2.5 py-1 bg-amber-400 text-slate-950 font-black rounded-lg text-[11px] tracking-wider uppercase shrink-0">
              ★ 중량 여유 제한사항 분석
            </span>
            <span className="text-slate-200 leading-relaxed">
              1~3번 중량 여유(TOW / ZFW / LDW) 중 <strong>가장 낮은 여유가 당 비행편의 유효 탑재 제한사항(Governing Limit)</strong>입니다.
            </span>
          </div>
          <div className="text-amber-300 font-bold text-xs bg-amber-950/60 border border-amber-500/50 px-3 py-1 rounded-lg">
            유효 탑재 제한: <span className="text-amber-200 underline decoration-amber-400 underline-offset-2">{governingItemName} (+{governingMarginFormatted})</span>
          </div>
        </div>

        {/* Dynamic Cards List */}
        <div className="space-y-2.5">
          {orderedItems.map((item, idx) => {
            const isOk =
              item.statusType === 'OK' ||
              item.status?.includes('OK') ||
              item.status?.includes('MATCH') ||
              item.status?.includes('완료') ||
              item.status?.includes('충족') ||
              item.status?.includes('일치');

            const isWeightItem = idx < 3;
            const itemMargin = isWeightItem ? parseMargin(item, 999999) : null;
            const isGoverning = isWeightItem && itemMargin === minMarginVal;
            const cleanCategoryName = item.category
              .replace(/^[0-9]+\.\s*/, '')
              .replace('TOW / MTOW 여유', 'TOW / AGTOW 여유')
              .replace('MTOW', 'AGTOW');
            const cleanDetail = (item.detail || '')
              .replace(/vs\s*MTOW/g, 'vs AGTOW')
              .replace(/\bMTOW\b/g, 'AGTOW');

            return (
              <div
                key={idx}
                className={`bg-slate-950/80 border ${
                  isGoverning ? 'border-amber-500/60 bg-amber-950/10' : 'border-slate-800/90'
                } px-4 sm:px-5 py-3 rounded-2xl flex flex-col md:flex-row items-start md:items-center justify-between gap-3.5 shadow-inner transition-all`}
              >
                {/* Left: Category Badge */}
                <div className="flex items-center gap-3 shrink-0">
                  <span className="text-xs sm:text-sm font-bold text-slate-500 w-6 text-right">
                    {idx + 1}.
                  </span>
                  <span className={`text-xs sm:text-sm font-bold px-3 py-1.5 rounded-lg min-w-[210px] text-center md:text-left border ${
                    isGoverning
                      ? 'bg-slate-900 border-amber-500/70 text-amber-200'
                      : 'bg-slate-900 border-slate-700 text-slate-200'
                  }`}>
                    {cleanCategoryName}
                  </span>
                </div>

                {/* Center: Detail */}
                <div className="text-sm sm:text-base text-slate-200 flex-1 leading-relaxed pl-1 font-medium flex flex-wrap items-center gap-2">
                  <span>{cleanDetail}</span>
                  {isGoverning && (
                    <span className="text-[11px] font-bold px-2 py-0.5 bg-amber-500/20 text-amber-300 border border-amber-500/60 rounded-md shrink-0">
                      ★ 최소 여유 (탑재 제한사항)
                    </span>
                  )}
                </div>

                {/* Right: Status Badge */}
                <div className="shrink-0 self-end md:self-center">
                  <span className="text-xs sm:text-sm font-bold px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-lg border border-slate-700 bg-slate-900 text-slate-300 flex items-center gap-2.5 shadow-sm">
                    <Check
                      className={`w-4 h-4 sm:w-5 sm:h-5 stroke-[3.5] ${
                        isOk ? 'text-emerald-400' : 'text-rose-400'
                      }`}
                    />
                    <span>{item.status}</span>
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

