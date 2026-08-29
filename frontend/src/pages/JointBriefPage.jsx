import React from 'react';
import { UserCheck, Users, ShieldAlert, CheckCircle2 } from 'lucide-react';

export default function JointBriefPage({ briefing }) {
  if (!briefing) return null;

  const fs = briefing.flight_summary || {};
  const jb = briefing.joint_briefing || {
    key_focus: '운항관리사(Dispatcher), 기장(PIC), 객실 사무장(Purser) 간 안전 운항 합동 브리핑',
    coordination_items: [
      '예상 난류 구간 진입 전 객실 서비스 종료 및 카트 고정 프로토콜 공유',
      '도착지 기상에 따른 지연/회항 가능성 기내 방송 프로토콜 공유',
      '총 탑승객 수 및 특이 수하물/화물 무게중심 정상 반영 확인'
    ],
    passenger_cabin_notes: [
      '탑승객 안전벨트 착용 방송 사전 실시',
      '특이 승객 및 응급 장비 위치 점검 완료'
    ],
    operational_limits: [
      '최대 이륙중량(MTOW) 여유 한계 충족 확인',
      '최대 착륙중량(MLDW) 한계 충족 확인'
    ]
  };

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 shadow-lg space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-5 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-3 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <UserCheck className="w-7 h-7" />
            </div>
            <div>
              <h3 className="text-xl sm:text-2xl font-bold text-white uppercase tracking-wide">
                JOINT OPERATIONAL BRIEFING
              </h3>
              <p className="text-sm text-slate-400 mt-1">
                운항관리사(Dispatcher) - 운항승무원(Cockpit) - 객실승무원(Cabin) 합동 브리핑
              </p>
            </div>
          </div>
          <span className="text-xs sm:text-sm font-bold px-3.5 py-1.5 bg-slate-950 border border-amber-500/40 text-amber-300 rounded-lg shadow-sm shrink-0">
            JOINT CREW
          </span>
        </div>

        <div className="bg-slate-950 p-5 rounded-xl border border-slate-800 space-y-2">
          <span className="text-xs text-amber-300 font-bold block uppercase tracking-wider">[KEY FOCUS]</span>
          <p className="text-base text-slate-200 font-bold leading-relaxed">{jb.key_focus}</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
          <div className="bg-slate-950/80 p-5 rounded-xl border border-slate-800 space-y-3">
            <span className="text-xs font-bold text-slate-300 uppercase block pb-2 border-b border-slate-800 flex items-center gap-2">
              <ShieldAlert className="w-4 h-4 text-amber-400" />
              COORDINATION ITEMS
            </span>
            <ul className="space-y-2.5 text-xs sm:text-sm text-slate-300">
              {jb.coordination_items?.map((item, i) => (
                <li key={i} className="flex items-start gap-2">
                  <span className="text-amber-400 font-bold mt-0.5">•</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="bg-slate-950/80 p-5 rounded-xl border border-slate-800 space-y-3">
            <span className="text-xs font-bold text-slate-300 uppercase block pb-2 border-b border-slate-800 flex items-center gap-2">
              <Users className="w-4 h-4 text-slate-300" />
              PASSENGER & CABIN NOTES
            </span>
            <ul className="space-y-2.5 text-xs sm:text-sm text-slate-300">
              {jb.passenger_cabin_notes?.map((item, i) => (
                <li key={i} className="flex items-start gap-2">
                  <span className="text-slate-300 font-bold mt-0.5">•</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="bg-slate-950/80 p-5 rounded-xl border border-slate-800 space-y-3">
          <span className="text-xs font-bold text-slate-300 uppercase block pb-2 border-b border-slate-800 flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            OPERATIONAL LIMITS
          </span>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm text-slate-300">
            {jb.operational_limits?.map((item, i) => (
              <div key={i} className="bg-slate-900 p-3 rounded-lg border border-slate-800 flex items-center gap-2">
                <span className="text-emerald-400 font-bold">✓</span>
                <span>{item}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
