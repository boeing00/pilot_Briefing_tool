import React from 'react';
import { Fuel, BarChart3, Users } from 'lucide-react';
import FuelAndWeightsCard from '../components/FuelAndWeightsCard';

export default function FuelPage({ briefing }) {
  if (!briefing) return null;

  const fw = briefing.fuel_and_weights || {};
  const blockFuel = fw.block_fuel || '-';
  const tripFuel = fw.trip_fuel || '-';
  const altnFuel = fw.alternate_fuel || '-';
  const discFuel = fw.extra_fuel || '-';
  const finalRes = fw.final_reserve || '-';
  const altnIcao = briefing.flight_summary?.alternate?.icao || 'ALTN';
  const fltTime = briefing.flight_summary?.flight_time || '-';

  const extraReason = fw.extra_fuel_reason || `목적지(${briefing.flight_summary?.destination?.icao || 'DEST'}) 기상 변화 대응 및 관제 대기(Holding), 교체공항(${altnIcao}) 회항 안전 마진 확보를 위해 추가 탑재.`;

  const payload = fw.payload || {
    pax_first: '0 / 0',
    pax_business: '68 / 75',
    pax_economy: '407 / 416',
    pax_total_weight: '107,261 LBS (475명)',
    cargo_weight: '10,142 LBS',
  };

  const fuelStats = fw.fuel_stats && fw.fuel_stats.length > 0
    ? fw.fuel_stats
    : [
        { label: 'MEAN DIFFERENCE (ACTUAL - PLAN)', val: '+1,134 LBS', note: '평균 오차' },
        { label: '95% STATISTICAL CONFIDENCE', val: '+6,700 LBS', note: '95% 신뢰구간' },
        { label: '99% STATISTICAL CONFIDENCE', val: '+9,006 LBS', note: '99% 최대 보수치' },
      ];

  return (
    <div className="space-y-6 animate-fade-in font-mono">
      {/* Main Fuel and Weights Card */}
      <FuelAndWeightsCard data={briefing.fuel_and_weights} />

      {/* Fuel Composition Breakdown & Visual Bar */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xl space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <Fuel className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
                DETAILED FUEL PLANNING BREAKDOWN
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">OFP 기준 총 탑재량: {blockFuel}</p>
            </div>
          </div>
          <span className="text-xs font-bold px-3 py-1.5 bg-slate-950 text-slate-300 border border-slate-700 rounded-lg shadow-sm">
            RAMP {blockFuel}
          </span>
        </div>

        {/* Visual Fuel Bar */}
        <div className="space-y-2.5">
          <div className="h-6 w-full bg-slate-950 rounded-lg overflow-hidden flex border border-slate-800 text-[10px] text-white font-bold text-center">
            <div style={{ width: '84%' }} className="bg-slate-700 flex items-center justify-center truncate" title={`Trip Fuel: ${tripFuel}`}>
              TRIP (84%)
            </div>
            <div style={{ width: '6%' }} className="bg-slate-800 border-l border-slate-700 flex items-center justify-center truncate" title={`Alternate: ${altnFuel}`}>
              ALT
            </div>
            <div style={{ width: '5%' }} className="bg-amber-600/70 border-l border-slate-700 flex items-center justify-center truncate text-amber-100" title={`DISC: ${discFuel}`}>
              DISC
            </div>
            <div style={{ width: '5%' }} className="bg-slate-800 border-l border-slate-700 flex items-center justify-center truncate" title={`Reserve: ${finalRes}`}>
              RES
            </div>
          </div>
          <div className="flex flex-wrap items-center justify-between text-xs text-slate-400">
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 bg-slate-700 rounded-sm inline-block"></span> Trip Burn: {tripFuel} ({fltTime})</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 bg-slate-800 rounded-sm inline-block"></span> Alternate: {altnFuel} ({altnIcao})</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 bg-amber-600/70 rounded-sm inline-block"></span> DISC Fuel: {discFuel} (버퍼/기상)</span>
            <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 bg-slate-800 rounded-sm inline-block"></span> Final Reserve: {finalRes} (30m)</span>
          </div>
        </div>

        {/* Discretionary Fuel Justification */}
        <div className="bg-slate-950/80 border border-slate-800 p-4 rounded-xl text-xs space-y-1.5 shadow-inner">
          <span className="font-bold text-amber-200 uppercase block">
            DISPATCHER EXTRA FUEL REASON (DISC FUEL 사유)
          </span>
          <p className="text-slate-300 leading-relaxed whitespace-pre-line">
            {extraReason}
          </p>
        </div>
      </div>

      {/* Passenger & Cargo Load Distribution */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Pax and Cargo */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-4">
          <div className="flex items-center gap-2 text-xs font-bold text-slate-200 uppercase tracking-wider pb-2 border-b border-slate-800">
            <Users className="w-4 h-4 text-slate-400" />
            <span>Payload & Passenger Manifest (탑승객 및 화물)</span>
          </div>
          <div className="grid grid-cols-3 gap-2.5 text-center">
            <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 shadow-inner">
              <span className="text-[10px] text-slate-500 block">FIRST</span>
              <span className="text-base font-bold text-slate-200 block mt-1">{payload.pax_first}</span>
            </div>
            <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 shadow-inner">
              <span className="text-[10px] text-slate-500 block">BUSINESS</span>
              <span className="text-base font-bold text-white block mt-1">{payload.pax_business}</span>
            </div>
            <div className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 shadow-inner">
              <span className="text-[10px] text-slate-500 block">ECONOMY</span>
              <span className="text-base font-bold text-white block mt-1">{payload.pax_economy}</span>
            </div>
          </div>
          <div className="bg-slate-950/60 p-3 rounded-xl border border-slate-800 text-xs flex justify-between text-slate-300">
            <span>PAX TOTAL: {payload.pax_total_weight}</span>
            <span>CARGO: {payload.cargo_weight}</span>
          </div>
        </div>

        {/* Route Fuel Burn History Stats */}
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-4">
          <div className="flex items-center gap-2 text-xs font-bold text-slate-200 uppercase tracking-wider pb-2 border-b border-slate-800">
            <BarChart3 className="w-4 h-4 text-slate-400" />
            <span>Route Fuel Consumption Statistics</span>
          </div>
          <div className="space-y-2">
            {fuelStats.map((stat, idx) => (
              <div key={idx} className="bg-slate-950/80 p-3 rounded-xl border border-slate-800 flex justify-between items-center text-xs shadow-inner">
                <span className="text-slate-400">{stat.label}</span>
                <span className="text-slate-200 font-bold">{stat.val}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

