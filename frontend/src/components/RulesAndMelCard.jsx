import React from 'react';
import { Shield, Wrench, ShieldCheck } from 'lucide-react';

export default function RulesAndMelCard({ briefing }) {
  const comp = briefing?.company_rules_and_mel || {};
  const companyAdvisories = comp.company_advisories || [
    {
      id: 'COMPANY ADVISORY 01',
      title: '표준 계기 출항(SID) 및 소음 저감 지침 준수',
      detail: '400FT AGL 이하 조기 선회 금지 및 초기 상승 프로파일 준수',
      impact: 'CRITICAL',
    },
    {
      id: 'COMPANY ADVISORY 02',
      title: '유사 편명 (Similar Call Signs) 주의',
      detail: '관제 교신 시 유사 호출부호 혼선 방지를 위한 복창 철저',
      impact: 'CAUTION',
    },
  ];

  const melCdlItems = comp.mel_cdl_items || [
    {
      code: 'MEL 33-20-05A',
      item: 'CABIN / WINDOW LIGHT DEFERRAL',
      action: 'DEFERRED IAW MEL 33-20-05A (운항 성능 반영 완료)',
      status: 'CONFIRMED',
    },
    {
      code: 'CDL 27-32',
      item: 'SECONDARY FLAP / SLAT FAIRING D-S',
      action: 'CDL 성능 패널티 반영 완료 (연료 계산 일치)',
      status: 'APPLIED',
    },
  ];

  const actType = briefing?.flight_summary?.aircraft_type || 'AIRCRAFT';

  return (
    <div id="section-rules" className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xl space-y-5">
      <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
        <div className="flex items-center gap-3.5">
          <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
            <Shield className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-xl sm:text-2xl font-black text-white font-mono uppercase tracking-wide">
              COMPANY RULES & MEL / CDL DEFERRALS
            </h3>
            <p className="text-xs text-slate-400 font-mono mt-0.5">
              운항사 특별 지침(Company Advisories) 및 항공기 이연 정비 항목
            </p>
          </div>
        </div>
        <span className="text-xs font-mono font-bold px-3 py-1.5 bg-slate-950 border border-slate-700 text-slate-300 rounded-lg shadow-sm shrink-0">
          {companyAdvisories.length + melCdlItems.length} NOTICES ACTIVE
        </span>
      </div>

      {/* Advisories Grid */}
      <div className="space-y-3 font-mono">
        <span className="text-xs font-bold text-slate-200 bg-slate-950 border border-slate-700 px-2.5 py-1 rounded uppercase tracking-wider inline-block">
          COMPANY OPERATIONAL ADVISORIES
        </span>
        <div className="space-y-2">
          {companyAdvisories.map((adv, idx) => (
            <div key={idx} className="bg-slate-950/80 border border-slate-800 p-3.5 rounded-xl space-y-1.5 shadow-inner">
              <div className="flex items-center justify-between gap-2">
                <span className="text-xs sm:text-sm font-bold text-slate-200">{adv.id} : {adv.title}</span>
                <span className={`text-2xs px-2 py-0.5 rounded border font-mono font-bold shrink-0 ${
                  adv.impact === 'CRITICAL'
                    ? 'bg-slate-900 text-rose-300 border-rose-600/50'
                    : adv.impact === 'CAUTION'
                    ? 'bg-slate-900 text-amber-300 border-amber-500/30'
                    : 'bg-slate-900 text-slate-400 border-slate-700'
                }`}>
                  {adv.impact}
                </span>
              </div>
              <p className="text-xs text-slate-300 leading-relaxed">{adv.detail}</p>
            </div>
          ))}
        </div>
      </div>

      {/* MEL / CDL Table */}
      <div className="pt-2 border-t border-slate-800 space-y-3 font-mono">
        <span className="text-xs font-bold text-slate-200 bg-slate-950 border border-slate-700 px-2.5 py-1 rounded uppercase tracking-wider inline-block">
          APPLIED MEL / CDL ITEMS ({actType})
        </span>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
          {melCdlItems.map((item, idx) => (
            <div key={idx} className="bg-slate-950/80 border border-slate-800 p-3.5 rounded-xl flex items-start gap-3 shadow-inner">
              <Wrench className="w-4 h-4 text-slate-400 shrink-0 mt-0.5" />
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-xs font-bold text-amber-200">{item.code}</span>
                  <span className="text-2xs px-1.5 py-0.5 bg-slate-900 text-slate-400 rounded border border-slate-800 font-mono">
                    {item.status}
                  </span>
                </div>
                <p className="text-xs font-bold text-slate-200">{item.item}</p>
                <p className="text-xs text-slate-400">{item.action}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
