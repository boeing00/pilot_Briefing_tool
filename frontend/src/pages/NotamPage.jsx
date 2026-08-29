import React, { useState } from 'react';
import { ChevronDown, Search, Copy, Check, Eye, EyeOff } from 'lucide-react';
import { getFallbackNotams } from '../services/api';

export default function NotamPage({ briefing, isSample = true }) {
  const [showAllNotams, setShowAllNotams] = useState(false);
  const [selectedAirportFilter, setSelectedAirportFilter] = useState('ALL');
  const [relevanceFilter, setRelevanceFilter] = useState('ALL');
  const [searchQuery, setSearchQuery] = useState('');
  const [copiedId, setCopiedId] = useState(null);
  const [userShadedOverrides, setUserShadedOverrides] = useState({});

  const fs = briefing?.flight_summary || {};
  const depIcao = fs.departure?.icao || 'RKSI';
  const depName = fs.departure?.name || '인천국제공항';
  const destIcao = fs.destination?.icao || 'KLAX';
  const destName = fs.destination?.name || '로스앤젤레스 국제공항';
  const flightNo = fs.callsign || fs.flight_number || 'AAR202';

  const nb = briefing?.notam_briefing || {};
  const genSum = nb.general_summary || {};
  // NEVER synthesize this section. It renders under a "NOTAM 원문 (Raw ICAO Text)"
  // heading with a copy button, so anything placed here reads as a real NOTAM. The
  // previous hardcoded fallback invented NOTAM numbers (PAZA A0914/26, KZAK A1402/26,
  // CZEG F4091/26 ...) with B)/C) validity dates that did not even match the flight
  // date, and it attached them to uploaded briefings. Show nothing instead.
  const enrouteAnalysis = Array.isArray(nb.enroute_detailed_analysis)
    ? nb.enroute_detailed_analysis
    : [];
  // Each demo flight carries its own NOTAM package. An uploaded briefing gets nothing:
  // showing a demo airport's NOTAMs next to a real flight number is worse than showing none.
  const fallbackNotams = isSample ? getFallbackNotams(destIcao) : [];
  const sourceNotams = (nb.notam_list && nb.notam_list.length > 0)
    ? nb.notam_list
    : fallbackNotams;

  // NOTAM ids are NOT unique across stations (COAD01/21 alone appears at 9 airports),
  // so every per-row piece of state must be keyed by position, never by id.
  const wholeNotams = sourceNotams.map((item, i) => ({ ...item, _uid: String(i) }));

  // Overrides are positional, so they must be dropped whenever the underlying
  // package changes - otherwise row 12 of the KLAX set inherits row 12 of the KJFK set.
  const notamScope = `${destIcao}:${sourceNotams.length}`;
  const [shadingScope, setShadingScope] = useState(notamScope);
  if (shadingScope !== notamScope) {
    setShadingScope(notamScope);
    setUserShadedOverrides({});
  }

  const isItemShaded = (item) => {
    if (userShadedOverrides[item._uid] !== undefined) {
      return userShadedOverrides[item._uid];
    }
    return !!item.isShaded;
  };

  const toggleItemShading = (uid, defaultShaded) => {
    setUserShadedOverrides((prev) => {
      const currentVal = prev[uid] !== undefined ? prev[uid] : defaultShaded;
      return {
        ...prev,
        [uid]: !currentVal,
      };
    });
  };

  const uniqueStations = Array.from(new Set(wholeNotams.map((n) => n.station))).filter(Boolean);
  const activeCount = wholeNotams.filter((n) => !isItemShaded(n)).length;
  const shadedCount = wholeNotams.filter((n) => isItemShaded(n)).length;

  const filteredNotams = wholeNotams.filter((item) => {
    const matchesStation =
      selectedAirportFilter === 'ALL' ||
      item.station === selectedAirportFilter;

    const itemShaded = isItemShaded(item);
    const matchesRelevance =
      relevanceFilter === 'ALL' ||
      (relevanceFilter === 'ACTIVE' && !itemShaded) ||
      (relevanceFilter === 'SHADED' && itemShaded);

    const matchesSearch =
      searchQuery.trim() === '' ||
      (item.id || '').toLowerCase().includes(searchQuery.toLowerCase()) ||
      (item.station || '').toLowerCase().includes(searchQuery.toLowerCase()) ||
      (item.rawText || '').toLowerCase().includes(searchQuery.toLowerCase()) ||
      (item.category || '').toLowerCase().includes(searchQuery.toLowerCase()) ||
      (item.airportName && item.airportName.toLowerCase().includes(searchQuery.toLowerCase())) ||
      (item.shadeReason && item.shadeReason.toLowerCase().includes(searchQuery.toLowerCase()));

    return matchesStation && matchesRelevance && matchesSearch;
  });

  const handleCopyItem = (id, text) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  return (
    <div className="space-y-4 text-slate-100 text-xs sm:text-sm">
      {/* 1. Clean Information Bar */}
      <div className="bg-slate-900 border border-slate-800 rounded-lg p-3 sm:p-4 flex flex-wrap items-center justify-between gap-2">
        <div className="flex flex-wrap items-center gap-3">
          <span className="font-bold text-amber-300 uppercase tracking-wider text-sm sm:text-base">
            NOTAM BRIEFING & PACKAGE
          </span>
          <span className="text-slate-400">|</span>
          <span className="text-slate-300 font-semibold">
            {flightNo} ({depIcao} → {destIcao})
          </span>
          <span className="text-slate-400">|</span>
          <span className="text-slate-400">
            TOTAL {wholeNotams.length} (ACTIVE: {activeCount} / SHADED: {shadedCount})
          </span>
          {isSample && (
            <>
              <span className="text-slate-400">|</span>
              <span className="px-2 py-0.5 bg-amber-950/70 border border-amber-600/70 text-amber-300 rounded-lg font-bold">
                예시 데이터 · 실제 운항에 사용 금지
              </span>
            </>
          )}
        </div>
      </div>

      {/* General Summary Card (3 Core Operational Pillars) */}
      <div className="bg-slate-900 border border-slate-800 rounded-lg p-4 sm:p-5 space-y-4 shadow-sm">
        <div className="pb-2.5 border-b border-slate-800">
          <span className="text-amber-300 font-bold uppercase tracking-wider text-base sm:text-lg lg:text-xl">
            GENERAL SUMMARY
          </span>
        </div>

        <div className="space-y-3">
          {/* 1. 출발 공항 */}
          <div className="bg-slate-950 p-3.5 sm:p-4 rounded-lg border border-slate-800 space-y-2.5">
            <div className="flex items-center justify-between gap-2 pb-1.5 border-b border-slate-800">
              <span className="font-bold text-amber-300 text-xs sm:text-sm uppercase">
                1. 출발공항 ({depIcao} / {depName})
              </span>
              <span className="text-2xs px-2 py-0.5 bg-slate-900 text-slate-400 border border-slate-700 rounded-lg font-bold">
                DEPARTURE
              </span>
            </div>
            <div className="space-y-2 text-xs sm:text-sm leading-relaxed text-slate-200">
              <div>
                <span className="text-slate-400 font-semibold block mb-0.5">◼ 활주로 / Taxiway 상태:</span>
                <p className="text-slate-300 pl-2 border-l-2 border-slate-700">
                  {genSum.departure_hazards?.includes('활주로') 
                    ? genSum.departure_hazards.split('이륙 직후')[0].replace(`${depIcao} (인천):`, '').replace(`${depIcao} :`, '').trim()
                    : '활주로 15R/33L 스위핑 완료 (마른 노면/제동 양호), 유도로 R23/R24 대형기(Code E) 주기장 진입 제한.'}
                </p>
              </div>
              <div>
                <span className="text-slate-400 font-semibold block mb-0.5">◼ 기타 운용 중요 정보:</span>
                <p className="text-slate-300 pl-2 border-l-2 border-amber-500/60">
                  {genSum.departure_hazards?.includes('이륙 직후')
                    ? '이륙 직후 ' + genSum.departure_hazards.split('이륙 직후')[1].trim()
                    : '이륙 직후 400FT AGL 이하 조기 선회 엄격 금지 (FOM 6.4.4 준수), 유사 호출부호(OZ601/KE601 등) 관제 교신 시 복창 철저.'}
                </p>
              </div>
            </div>
          </div>

          {/* 2. 도착 공항 */}
          <div className="bg-slate-950 p-3.5 sm:p-4 rounded-lg border border-slate-800 space-y-2.5">
            <div className="flex items-center justify-between gap-2 pb-1.5 border-b border-slate-800">
              <span className="font-bold text-amber-300 text-xs sm:text-sm uppercase">
                2. 도착공항 ({destIcao} / {destName})
              </span>
              <span className="text-2xs px-2 py-0.5 bg-slate-900 text-slate-400 border border-slate-700 rounded-lg font-bold">
                ARRIVAL
              </span>
            </div>
            <div className="space-y-2 text-xs sm:text-sm leading-relaxed text-slate-200">
              <div>
                <span className="text-slate-400 font-semibold block mb-0.5">◼ 활주로 / Taxiway 상태:</span>
                <p className="text-slate-300 pl-2 border-l-2 border-slate-700">
                  {destIcao === 'KLAX'
                    ? '유도로 E 일부(E6~E7) 공사로 폐쇄 -> TWY C/D 우회 주행 요망, 활주로 24L PAPI 일시 점검.'
                    : (genSum.arrival_hazards?.split('.')[0] || '활주로 및 주요 유도로 지상 이동 지침 준수.')}
                </p>
              </div>
              <div>
                <span className="text-slate-400 font-semibold block mb-0.5">◼ Minimum 변경 & 접근 절차:</span>
                <p className="text-slate-300 pl-2 border-l-2 border-amber-500/60">
                  {destIcao === 'KLAX'
                    ? '활주로 25R 진입등(ALS) 점검 중이나 CAT II/III 정상 접근 가능, 25L ILS 점검 비행 시간대(0400-0800Z) LOC 준비, 톰 브래들리 터미널 크레인(185FT MSL) 주의.'
                    : (genSum.arrival_hazards?.split('.')[1] || '계기착륙시설(ILS) 정상 및 최저치(DA/MDA) 확인.')}
                </p>
              </div>
              <div>
                <span className="text-slate-400 font-semibold block mb-0.5">◼ 기타 운용 중요 정보:</span>
                <p className="text-slate-300 pl-2 border-l-2 border-slate-700">
                  {destIcao === 'KLAX'
                    ? '심야/조기 해안 소음 저감 절차(00:00-06:30L) 준수, 해안가 조류 집중 이동 주의보.'
                    : '터미널 공사 구역 서행 및 소음 저감 절차 준수.'}
                </p>
              </div>
            </div>
          </div>

          {/* 3. 항로 및 비행계획서(FPL) 제약사항 */}
          <div className="bg-slate-950 p-3.5 sm:p-4 rounded-lg border border-slate-800 space-y-3">
            <div className="flex items-center justify-between gap-2 pb-1.5 border-b border-slate-800">
              <span className="font-bold text-amber-300 text-xs sm:text-sm uppercase">
                3. 항로 & FPL 제약사항 (항로상 경로 제약 NOTAM 상세 분석)
              </span>
              <span className="text-2xs px-2 py-0.5 bg-slate-900 text-slate-400 border border-slate-700 rounded-lg font-bold">
                ENROUTE & FPL
              </span>
            </div>

            <div className="space-y-3 text-xs sm:text-sm leading-relaxed text-slate-200">
              <p className="text-slate-400 text-xs font-semibold">
                북태평양 및 주요 통과 공역 수립 최신 항로 제한 규칙 및 당사 비행 연관성 분석:
              </p>

              {enrouteAnalysis.length === 0 && (
                <p className="text-slate-400 text-xs bg-slate-900/70 border border-slate-800 rounded-lg p-3">
                  이 브리핑에는 항로 제약 NOTAM 상세 분석 항목이 없습니다. 항로상 제한사항은
                  아래 전체 NOTAM 목록과 제출된 ATS FPL에서 직접 확인하십시오.
                </p>
              )}

              {enrouteAnalysis.map((item, idx) => {
                const cleanTitle = item.title ? item.title.replace(/^[0-9]+\.[0-9]+\s*/, '') : '';
                const displayTitle = `3.${idx + 1} ${cleanTitle}`;
                return (
                  <div key={idx} className="bg-slate-900/90 border border-slate-800/90 p-3.5 rounded-lg space-y-2.5 shadow-sm">
                    {/* Header Line */}
                    <div className="flex items-center justify-between gap-2 pb-1.5 border-b border-slate-800">
                      <div className="font-bold text-amber-300 text-xs sm:text-sm">
                        {displayTitle}
                      </div>
                      <span className="text-2xs px-1.5 py-0.5 bg-slate-950 text-slate-400 border border-slate-700 rounded-lg font-mono font-bold">
                        {item.fir?.split(' ')[0] || 'ENROUTE'}
                      </span>
                    </div>

                    {/* NOTAM Raw Text (ICAO format) */}
                    {item.raw_text && (
                      <div className="bg-slate-950 border border-slate-800 rounded-lg p-2.5 space-y-1.5">
                        <div className="flex items-center justify-between text-xs text-slate-400 font-semibold">
                          <span className="text-amber-300/90 font-bold">◼ NOTAM 원문 (Raw ICAO Text):</span>
                          <button
                            onClick={() => handleCopyItem(`enroute-${idx}`, item.raw_text)}
                            className="text-slate-400 hover:text-white flex items-center gap-1 text-2xs bg-slate-900 px-2 py-0.5 rounded-lg border border-slate-700 transition"
                          >
                            {copiedId === `enroute-${idx}` ? <Check className="w-2.5 h-2.5 text-emerald-400" /> : <Copy className="w-2.5 h-2.5" />}
                            <span>{copiedId === `enroute-${idx}` ? '복사됨 ✓' : '원문 복사'}</span>
                          </button>
                        </div>
                        <div className="text-slate-200 text-xs font-mono leading-relaxed whitespace-pre-wrap break-words pl-2 border-l-2 border-amber-500/80 bg-slate-900/40 p-2 rounded-lg">
                          {item.raw_text}
                        </div>
                      </div>
                    )}

                    {/* 해당 지점 / 공역 */}
                    <div className="text-slate-400 text-xs">
                      <span className="text-slate-400 font-semibold">◼ 해당 지점 / 공역: </span>
                      <span className="text-slate-300">{item.fir}</span>
                    </div>

                    {/* 상세 제한 조건 */}
                    <div className="text-slate-300 text-xs leading-relaxed pl-2 border-l-2 border-slate-700">
                      <span className="text-slate-400 font-semibold block mb-0.5">◼ 상세 제한 조건:</span>
                      <span>{item.conditions}</span>
                    </div>

                    {/* 우리 비행과의 연관성 */}
                    <div className="text-amber-100/95 text-xs leading-relaxed pl-2 border-l-2 border-amber-500/60 bg-amber-950/20 p-2 rounded-lg">
                      <span className="text-amber-300 font-bold block mb-0.5">◼ 우리 비행({flightNo})과의 연관성:</span>
                      <span>{item.correlation}</span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>

      {/* 2. Controls: Station Dropdown & 전체보기 Toggle */}
      <div className="bg-slate-900 border border-slate-800 rounded-lg p-3 sm:p-4 flex flex-wrap items-center justify-between gap-3">
        {/* Left: Station Drop Down Filter */}
        <div className="flex items-center gap-2">
          <span className="text-slate-400 text-xs sm:text-sm font-semibold shrink-0">
            공항 / FIR 선택:
          </span>
          <div className="relative">
            <select
              value={selectedAirportFilter}
              onChange={(e) => {
                setSelectedAirportFilter(e.target.value);
                setShowAllNotams(true);
              }}
              className="appearance-none bg-slate-950 text-amber-300 font-bold border border-slate-700 hover:border-amber-400 rounded-lg pl-3 pr-8 py-1.5 sm:py-2 text-xs sm:text-sm focus:outline-none focus:border-amber-400 cursor-pointer font-mono"
            >
              <option value="ALL" className="bg-slate-950 text-slate-100 font-mono">
                ALL ({wholeNotams.length})
              </option>
              {uniqueStations.map((station) => {
                const count = wholeNotams.filter((n) => n.station === station).length;
                return (
                  <option key={station} value={station} className="bg-slate-950 text-slate-100 font-mono">
                    {station} ({count})
                  </option>
                );
              })}
            </select>
            <ChevronDown className="w-4 h-4 text-slate-400 absolute right-2.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          </div>
        </div>

        {/* Center/Right: 전체보기 Action Button & Status/Search when open */}
        <div className="flex flex-wrap items-center gap-2.5">
          {showAllNotams && (
            <div className="relative min-w-[160px] sm:min-w-[200px]">
              <Search className="w-3.5 h-3.5 absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="NOTAM 번호, 키워드..."
                className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-7 pr-2.5 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-amber-400"
              />
            </div>
          )}

          {showAllNotams && (
            <div className="flex items-center gap-1">
              <button
                onClick={() => setRelevanceFilter('ACTIVE')}
                className={`px-2.5 py-1 rounded-lg text-xs transition ${
                  relevanceFilter === 'ACTIVE'
                    ? 'bg-slate-800 text-amber-300 border border-slate-700 font-bold'
                    : 'text-slate-400 hover:text-white bg-slate-950 border border-slate-800'
                }`}
              >
                유효 ({activeCount})
              </button>
              <button
                onClick={() => setRelevanceFilter('SHADED')}
                className={`px-2.5 py-1 rounded-lg text-xs transition ${
                  relevanceFilter === 'SHADED'
                    ? 'bg-slate-800 text-slate-300 border border-slate-700 font-bold'
                    : 'text-slate-400 hover:text-white bg-slate-950 border border-slate-800'
                }`}
              >
                음영 ({shadedCount})
              </button>
            </div>
          )}

          {/* Main Toggle Button: 전체보기 */}
          <button
            onClick={() => {
              if (!showAllNotams) {
                setRelevanceFilter('ALL');
                setShowAllNotams(true);
              } else {
                setShowAllNotams(false);
              }
            }}
            className={`px-3.5 py-1.5 sm:py-2 rounded-lg text-xs sm:text-sm font-bold transition flex items-center gap-1.5 shadow-sm ${
              showAllNotams
                ? 'bg-amber-400 text-slate-950 border border-amber-300 hover:bg-amber-300'
                : 'bg-slate-950 text-slate-200 border border-slate-700 hover:text-amber-300 hover:border-amber-400'
            }`}
          >
            <span>{showAllNotams ? '전체보기 닫기 (접기)' : '전체보기 (전문 펼치기)'}</span>
            <ChevronDown className={`w-3.5 h-3.5 transition-transform duration-200 ${showAllNotams ? 'rotate-180' : ''}`} />
          </button>
        </div>
      </div>

      {/* 3. Dropdown-triggered / Toggleable Text NOTAM List */}
      {showAllNotams && (
        <div className="space-y-2.5 animate-fade-in pt-1">
          <div className="flex items-center justify-between text-xs text-slate-400 px-1">
            <span>
              선택 공항: <strong className="text-amber-300">{selectedAirportFilter}</strong> (표시 중: {filteredNotams.length}건)
            </span>
            <button
              onClick={() => {
                const allText = filteredNotams.map((n) => `[#${n.index ?? Number(n._uid) + 1} ${n.station} - ${n.id}] ${n.rawText}`).join('\n\n');
                navigator.clipboard.writeText(allText);
                setCopiedId('ALL');
                setTimeout(() => setCopiedId(null), 2000);
              }}
              className="text-xs text-slate-300 hover:text-white bg-slate-900 border border-slate-800 px-2 py-1 rounded-lg"
            >
              {copiedId === 'ALL' ? '복사 완료 ✓' : '현재 목록 전체 복사'}
            </button>
          </div>

          {filteredNotams.map((item) => {
            const shaded = isItemShaded(item);
            return (
              <div
                key={item._uid}
                className={`p-3 sm:p-4 rounded-lg border transition ${
                  shaded
                    ? 'bg-slate-950/40 border-slate-800 opacity-60'
                    : 'bg-slate-900 border-slate-800'
                }`}
              >
                {/* Header Meta Line */}
                <div className="flex flex-wrap items-center justify-between gap-2 pb-2 border-b border-slate-800 text-xs">
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="text-slate-400 font-bold w-7">#{item.index ?? Number(item._uid) + 1}</span>
                    <span className="font-bold text-amber-300 px-1.5 py-0.5 bg-slate-950 border border-slate-700 rounded-lg">
                      {item.station}
                    </span>
                    <span className="font-bold text-white">{item.id}</span>
                    <span className="text-slate-400">[{item.category}]</span>
                    <span
                      className={`px-1.5 py-0.5 rounded-lg text-xs font-bold ${
                        item.level === 'CRITICAL'
                          ? 'text-rose-400 bg-rose-950/50 border border-rose-900'
                          : 'text-slate-300 bg-slate-950 border border-slate-700'
                      }`}
                    >
                      {item.level}
                    </span>
                    {item.airportName && (
                      <span className="text-slate-400 hidden sm:inline">
                        - {item.airportName}
                      </span>
                    )}
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => toggleItemShading(item._uid, item.isShaded)}
                      className="px-2 py-0.5 text-slate-400 hover:text-white bg-slate-950 rounded-lg border border-slate-800 text-xs flex items-center gap-1"
                      title={shaded ? '음영 해제 (유효화)' : '음영 처리'}
                    >
                      {shaded ? <Eye className="w-3 h-3 text-slate-400" /> : <EyeOff className="w-3 h-3 text-amber-400" />}
                      <span>{shaded ? '음영 해제' : '음영'}</span>
                    </button>
                    <button
                      onClick={() => handleCopyItem(item._uid, item.rawText)}
                      className="p-1 text-slate-400 hover:text-white bg-slate-950 rounded-lg border border-slate-800"
                      title="원문 복사"
                    >
                      {copiedId === item._uid ? <Check className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
                    </button>
                  </div>
                </div>

                {/* Raw NOTAM ICAO Text */}
                <div className="mt-2 text-slate-200 text-xs leading-relaxed whitespace-pre-wrap break-words font-mono">
                  {item.rawText}
                </div>

                {/* Korean Summary Line */}
                {item.koreanSummary && (
                  <div className="mt-2 text-xs font-mono text-amber-200/90 bg-slate-950/70 px-2.5 py-1.5 rounded-lg border border-slate-800/80">
                    [요약] {item.koreanSummary}
                  </div>
                )}

                {/* Shading Reason Note */}
                {shaded && item.shadeReason && (
                  <div className="text-xs font-mono text-slate-400 mt-1 pl-1">
                    (음영 사유: {item.shadeReason})
                  </div>
                )}
              </div>
            );
          })}

          {filteredNotams.length === 0 && (
            <div className="bg-slate-900 border border-slate-800 rounded-lg p-8 text-center text-slate-400 text-xs">
              검색 조건에 일치하는 NOTAM 항목이 없습니다.
            </div>
          )}
        </div>
      )}
    </div>
  );
}
