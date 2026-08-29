'use client';

import React from 'react';
import { Fuel, Scale, Clock, AlertCircle, CheckCircle } from 'lucide-react';
import { FuelItem, WeightAndBalance } from '@/types/flight';

interface FuelBriefingProps {
  fuel: FuelItem;
  weightAndBalance?: WeightAndBalance;
}

export const FuelBriefing: React.FC<FuelBriefingProps> = ({ fuel, weightAndBalance }) => {
  const { tripFuel, contingencyFuel, alternateFuel, finalReserveFuel, extraFuel, blockFuel, unit } = fuel;

  const totalRequired = tripFuel + contingencyFuel + alternateFuel + finalReserveFuel;
  const isExtraPositive = extraFuel > 0;

  return (
    <div className="space-y-6">
      {/* Fuel Overview Card */}
      <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
              <Fuel className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xl font-bold font-mono text-slate-100">
                  {blockFuel?.toLocaleString()} {unit}
                </span>
                <span className="px-2 py-0.5 rounded text-xs font-mono font-bold bg-amber-950 text-amber-300 border border-amber-800">
                  BLOCK FUEL
                </span>
              </div>
              <p className="text-xs text-slate-400 font-medium">연료 탑재량 및 법정 요구치 비교</p>
            </div>
          </div>

          {fuel.enduranceHours && (
            <div className="flex items-center gap-2 text-xs font-mono bg-slate-950/60 px-3 py-1.5 rounded-lg border border-slate-800 text-slate-300">
              <Clock className="w-4 h-4 text-cyan-400" />
              <span>TOTAL ENDURANCE: <strong className="text-cyan-300">{fuel.enduranceHours}</strong></span>
            </div>
          )}
        </div>

        {/* Visual Fuel Bar */}
        <div className="space-y-2">
          <div className="flex justify-between text-xs font-mono text-slate-400">
            <span>법정 필요 연료: {totalRequired.toLocaleString()} {unit}</span>
            <span>여유 연료 (Extra): <strong className={isExtraPositive ? 'text-emerald-400' : 'text-rose-400'}>{extraFuel?.toLocaleString()} {unit}</strong></span>
          </div>

          <div className="h-6 w-full rounded-xl bg-slate-950 overflow-hidden flex border border-slate-800 text-[10px] font-mono font-bold text-slate-950">
            <div
              style={{ width: `${(tripFuel / blockFuel) * 100}%` }}
              className="bg-cyan-500 flex items-center justify-center truncate px-1"
              title={`Trip Fuel: ${tripFuel} ${unit}`}
            >
              TRIP
            </div>
            <div
              style={{ width: `${(contingencyFuel / blockFuel) * 100}%` }}
              className="bg-blue-400 flex items-center justify-center truncate px-1"
              title={`Contingency: ${contingencyFuel} ${unit}`}
            >
              CONT
            </div>
            <div
              style={{ width: `${(alternateFuel / blockFuel) * 100}%` }}
              className="bg-amber-400 flex items-center justify-center truncate px-1"
              title={`Alternate: ${alternateFuel} ${unit}`}
            >
              ALT
            </div>
            <div
              style={{ width: `${(finalReserveFuel / blockFuel) * 100}%` }}
              className="bg-rose-400 flex items-center justify-center truncate px-1"
              title={`Final Reserve: ${finalReserveFuel} ${unit}`}
            >
              RSV
            </div>
            {extraFuel > 0 && (
              <div
                style={{ width: `${(extraFuel / blockFuel) * 100}%` }}
                className="bg-emerald-400 flex items-center justify-center truncate px-1"
                title={`Extra Fuel: ${extraFuel} ${unit}`}
              >
                EXTRA
              </div>
            )}
          </div>

          <div className="flex flex-wrap gap-4 text-[11px] font-mono text-slate-400 pt-1">
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-sm bg-cyan-500"></span> Trip ({tripFuel.toLocaleString()})</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-sm bg-blue-400"></span> Cont ({contingencyFuel.toLocaleString()})</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-sm bg-amber-400"></span> Alt ({alternateFuel.toLocaleString()})</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-sm bg-rose-400"></span> Reserve ({finalReserveFuel.toLocaleString()})</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-sm bg-emerald-400"></span> Extra ({extraFuel.toLocaleString()})</span>
          </div>
        </div>

        {/* Detailed Fuel Table */}
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2.5 pt-2 text-center">
          <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-850">
            <span className="text-[11px] font-mono text-slate-500 block">TRIP FUEL</span>
            <span className="text-sm font-bold font-mono text-cyan-300">{tripFuel?.toLocaleString()}</span>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-850">
            <span className="text-[11px] font-mono text-slate-500 block">CONTINGENCY</span>
            <span className="text-sm font-bold font-mono text-blue-300">{contingencyFuel?.toLocaleString()}</span>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-850">
            <span className="text-[11px] font-mono text-slate-500 block">ALTERNATE</span>
            <span className="text-sm font-bold font-mono text-amber-300">{alternateFuel?.toLocaleString()}</span>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-850">
            <span className="text-[11px] font-mono text-slate-500 block">FINAL RESERVE</span>
            <span className="text-sm font-bold font-mono text-rose-300">{finalReserveFuel?.toLocaleString()}</span>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-850">
            <span className="text-[11px] font-mono text-slate-500 block">EXTRA FUEL</span>
            <span className="text-sm font-bold font-mono text-emerald-300">+{extraFuel?.toLocaleString()}</span>
          </div>
          <div className="p-3 rounded-xl bg-slate-950/50 border border-slate-850">
            <span className="text-[11px] font-mono text-slate-500 block">MIN T/O FUEL</span>
            <span className="text-sm font-bold font-mono text-slate-100">{fuel.minTakeoffFuel?.toLocaleString() || 'N/A'}</span>
          </div>
        </div>
      </div>

      {/* Weight & Balance (If Available) */}
      {weightAndBalance && (
        <div className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-4">
          <div className="flex items-center gap-2">
            <Scale className="w-5 h-5 text-cyan-400" />
            <h4 className="text-base font-bold text-slate-100">Weight & Balance (중량 계산)</h4>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div className="p-4 rounded-xl bg-slate-950/50 border border-slate-850 space-y-1">
              <span className="text-xs font-mono text-slate-500">EST. ZERO FUEL WT (ZFW)</span>
              <div className="text-base font-bold font-mono text-slate-100">
                {weightAndBalance.ezfw?.toLocaleString()} <span className="text-xs text-slate-400">{weightAndBalance.unit}</span>
              </div>
              {weightAndBalance.maxZfw && (
                <div className="text-[11px] font-mono text-slate-400">
                  MAX: {weightAndBalance.maxZfw.toLocaleString()} {weightAndBalance.unit}
                </div>
              )}
            </div>

            <div className="p-4 rounded-xl bg-slate-950/50 border border-slate-850 space-y-1">
              <span className="text-xs font-mono text-slate-500">EST. TAKEOFF WT (TOW)</span>
              <div className="text-base font-bold font-mono text-slate-100">
                {weightAndBalance.estTow?.toLocaleString()} <span className="text-xs text-slate-400">{weightAndBalance.unit}</span>
              </div>
              {weightAndBalance.maxTow && (
                <div className="text-[11px] font-mono text-slate-400">
                  MAX: {weightAndBalance.maxTow.toLocaleString()} {weightAndBalance.unit}
                </div>
              )}
            </div>

            <div className="p-4 rounded-xl bg-slate-950/50 border border-slate-850 space-y-1">
              <span className="text-xs font-mono text-slate-500">EST. LANDING WT (LDW)</span>
              <div className="text-base font-bold font-mono text-slate-100">
                {weightAndBalance.estLdw?.toLocaleString()} <span className="text-xs text-slate-400">{weightAndBalance.unit}</span>
              </div>
              {weightAndBalance.maxLdw && (
                <div className="text-[11px] font-mono text-slate-400">
                  MAX: {weightAndBalance.maxLdw.toLocaleString()} {weightAndBalance.unit}
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
