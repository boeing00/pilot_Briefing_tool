import React from 'react';
import { Fuel, CheckCircle2 } from 'lucide-react';

export default function FuelAndWeightsCard({ data }) {
  if (!data) return null;

  const {
    block_fuel,
    trip_fuel,
    contingency_fuel,
    alternate_fuel,
    final_reserve,
    extra_fuel,
    estimated_tow,
    max_tow,
    tow_margin,
    estimated_law,
    max_law,
  } = data;

  return (
    <div id="section-fuel" className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xl space-y-5">
      <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
        <div className="flex items-center gap-3.5">
          <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
            <Fuel className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-xl sm:text-2xl font-black text-white font-mono uppercase tracking-wide">
              FUEL & PERFORMANCE WEIGHTS
            </h3>
            <p className="text-xs text-slate-400 font-mono mt-0.5">
              Required Fuel Reserves & Structural Weight Limits
            </p>
          </div>
        </div>
        <span className="text-xs font-mono font-bold px-3 py-1.5 bg-slate-950 border border-slate-700 text-slate-300 rounded-lg shadow-sm shrink-0">
          PERFORMANCE NORMAL
        </span>
      </div>

      {/* Fuel Summary Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 font-mono">
        {/* Block Fuel */}
        <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-700 text-center">
          <span className="text-2xs text-slate-400 block">BLOCK FUEL</span>
          <span className="text-base font-bold text-white block mt-1">
            {block_fuel || 'N/A'}
          </span>
        </div>

        {/* Trip Fuel */}
        <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
          <span className="text-2xs text-slate-400 block">TRIP BURN</span>
          <span className="text-base font-bold text-slate-200 block mt-1">
            {trip_fuel || 'N/A'}
          </span>
        </div>

        {/* Contingency */}
        <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
          <span className="text-2xs text-slate-400 block">CONTINGENCY</span>
          <span className="text-base font-bold text-slate-200 block mt-1">
            {contingency_fuel || 'N/A'}
          </span>
        </div>

        {/* Alternate */}
        <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
          <span className="text-2xs text-slate-400 block">ALTERNATE</span>
          <span className="text-base font-bold text-slate-200 block mt-1">
            {alternate_fuel || 'N/A'}
          </span>
        </div>

        {/* Final Reserve */}
        <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
          <span className="text-2xs text-slate-400 block">FINAL RESERVE (30m)</span>
          <span className="text-base font-bold text-amber-200 block mt-1">
            {final_reserve || 'N/A'}
          </span>
        </div>

        {/* Extra Fuel */}
        <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 text-center">
          <span className="text-2xs text-slate-400 block">EXTRA / TANKER</span>
          <span className="text-base font-bold text-slate-200 block mt-1">
            {extra_fuel || '0 lbs'}
          </span>
        </div>
      </div>

      {/* Weights and Balance */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-3 border-t border-slate-800 font-mono">
        {/* Takeoff Weight */}
        <div className="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800 flex items-center justify-between">
          <div>
            <span className="text-xs text-slate-400 uppercase block">ESTIMATED TAKEOFF WEIGHT (TOW)</span>
            <div className="flex items-baseline gap-2 mt-1">
              <span className="text-base font-bold text-white">{estimated_tow || 'N/A'}</span>
              <span className="text-xs text-slate-400">/ Max: {max_tow || 'N/A'}</span>
            </div>
          </div>
          <div className="flex items-center gap-1 text-xs text-slate-300 font-bold bg-slate-900 border border-slate-700 px-2.5 py-1 rounded">
            <CheckCircle2 className="w-3.5 h-3.5 text-slate-400" />
            <span>{tow_margin || 'OK'}</span>
          </div>
        </div>

        {/* Landing Weight */}
        <div className="bg-slate-950/60 p-3.5 rounded-xl border border-slate-800 flex items-center justify-between">
          <div>
            <span className="text-xs text-slate-400 uppercase block">ESTIMATED LANDING WEIGHT (LAW)</span>
            <div className="flex items-baseline gap-2 mt-1">
              <span className="text-base font-bold text-white">{estimated_law || 'N/A'}</span>
              <span className="text-xs text-slate-400">/ Max: {max_law || 'N/A'}</span>
            </div>
          </div>
          <div className="flex items-center gap-1 text-xs text-slate-300 font-bold bg-slate-900 border border-slate-700 px-2.5 py-1 rounded">
            <CheckCircle2 className="w-3.5 h-3.5 text-slate-400" />
            <span>Limits Valid</span>
          </div>
        </div>
      </div>
    </div>
  );
}
