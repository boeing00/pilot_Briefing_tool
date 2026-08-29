import React from 'react';
import { Navigation, Globe, Table } from 'lucide-react';

export default function RoutePage({ briefing }) {
  if (!briefing) return null;

  const depIcao = briefing.flight_summary?.departure?.icao || 'RKSI';
  const depIata = briefing.flight_summary?.departure?.iata || 'ICN';
  const destIcao = briefing.flight_summary?.destination?.icao || 'KJFK';
  const destIata = briefing.flight_summary?.destination?.iata || 'JFK';
  const altnIcao = briefing.flight_summary?.alternate?.icao || 'KBOS';
  const fltTime = briefing.flight_summary?.flight_time || '13Hr 24Min';
  const totalDist = briefing.route_analysis?.total_distance || briefing.flight_summary?.total_distance || '6,663 NM';
  const filedRoute = briefing.route_analysis?.filed_route_string || briefing.flight_summary?.route_summary || `${depIcao} SID ... ENROUTE ... STAR ${destIcao}`;
  const altnRoute = briefing.route_analysis?.alternate_routing || `${destIcao}..DIRECT..${altnIcao}`;

  const waypoints = (briefing.route_analysis?.waypoints && briefing.route_analysis.waypoints.length > 0)
    ? briefing.route_analysis.waypoints
    : [
        { name: `${depIcao} (${depIata})`, dist: '0', fl: 'GND', wind: '200/10kt', tas: '0', gs: '0', eet: '00:00', fuelRem: briefing.fuel_and_weights?.block_fuel || '475.8k' },
        { name: 'CLIMB / ENROUTE', dist: '120', fl: 'FL310', wind: '280/25kt', tas: '480', gs: '495', eet: '00:20', fuelRem: '95%' },
        { name: 'MID CRUISE', dist: '1,450', fl: 'FL350', wind: '290/40kt', tas: '490', gs: '520', eet: '03:15', fuelRem: '75%' },
        { name: 'TOP OF DESCENT', dist: '5,600', fl: 'FL370', wind: '270/35kt', tas: '480', gs: '500', eet: '11:30', fuelRem: '25%' },
        { name: `${destIcao} (${destIata})`, dist: totalDist.replace(' NM', ''), fl: 'GND', wind: '180/12kt', tas: '-', gs: '-', eet: fltTime, fuelRem: briefing.fuel_and_weights?.final_reserve || '68.0k' },
      ];

  const firCrossings = (briefing.route_analysis?.fir_crossings && briefing.route_analysis.fir_crossings.length > 0)
    ? briefing.route_analysis.fir_crossings
    : [
        { fir: `${depIcao} FIR`, fix: 'DEP_FIX', eet: '00:30Z' },
        { fir: 'OCEANIC / ENROUTE FIR', fix: 'MID_FIX', eet: '04:15Z' },
        { fir: `${destIcao} FIR`, fix: 'ARR_FIX', eet: '11:45Z' },
      ];

  return (
    <div className="space-y-6 animate-fade-in font-mono">
      {/* Route Header Banner */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xl space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800">
          <div className="flex items-center gap-3.5">
            <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
              <Navigation className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-xl sm:text-2xl font-black text-white uppercase tracking-wide">
                FLIGHT ROUTE & NAVIGATION LOG
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">
                {depIcao} ({depIata}) ➡️ {destIcao} ({destIata})
              </p>
            </div>
          </div>
          <span className="text-xs font-bold px-3 py-1.5 bg-slate-950 text-slate-300 border border-slate-700 rounded-lg shadow-sm">
            {totalDist} / {fltTime}
          </span>
        </div>

        {/* Route String */}
        <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-200 leading-relaxed overflow-x-auto shadow-inner">
          <span className="text-slate-500 block text-[10px] mb-1 font-bold">FILED ROUTE STRING:</span>
          {filedRoute}
        </div>

        {/* Alternate Routing */}
        <div className="bg-slate-950/60 p-3 rounded-xl border border-slate-800 text-xs flex items-center justify-between">
          <span className="text-slate-400 font-bold">FILED ALTERNATE TO {altnIcao}:</span>
          <span className="text-amber-200 font-bold">{altnRoute}</span>
        </div>
      </div>

      {/* FIR Crossing Schedule */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xl space-y-4">
        <div className="flex items-center gap-2 text-xs font-bold text-slate-200 uppercase tracking-wider pb-2 border-b border-slate-800">
          <Globe className="w-4 h-4 text-slate-400" />
          <span>FIR Boundary Crossing Times (관제구역 진입 시간)</span>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2.5">
          {firCrossings.map((fir, idx) => (
            <div key={idx} className="bg-slate-950/80 border border-slate-800 p-3 rounded-xl text-center shadow-inner">
              <span className="text-[10px] text-slate-500 block truncate">{fir.fir}</span>
              <span className="text-xs font-bold text-white block mt-0.5">{fir.fix}</span>
              <span className="text-xs text-amber-200 font-bold block mt-0.5">{fir.eet}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Full Waypoint Log Table */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-xl space-y-4">
        <div className="flex items-center gap-2 text-xs font-bold text-slate-200 uppercase tracking-wider pb-2 border-b border-slate-800">
          <Table className="w-4 h-4 text-slate-400" />
          <span>Waypoint Navigation Log & Fuel Burn Progression</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse text-xs">
            <thead>
              <tr className="border-b border-slate-800 text-slate-400 text-[10px] uppercase bg-slate-950/80">
                <th className="py-2.5 px-3">WAYPOINT</th>
                <th className="py-2.5 px-2">CUM DIST</th>
                <th className="py-2.5 px-2">ALTITUDE</th>
                <th className="py-2.5 px-2">WIND/TEMP</th>
                <th className="py-2.5 px-2">TAS</th>
                <th className="py-2.5 px-2">GS</th>
                <th className="py-2.5 px-2">EET</th>
                <th className="py-2.5 px-3 text-right">REM FUEL</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {waypoints.map((wp, idx) => (
                <tr key={idx} className="hover:bg-slate-800/30 transition">
                  <td className="py-2 px-3 font-bold text-white">{wp.name}</td>
                  <td className="py-2 px-2 text-slate-400">{wp.dist} NM</td>
                  <td className="py-2 px-2 text-slate-200 font-bold">{wp.fl}</td>
                  <td className="py-2 px-2 text-slate-400">{wp.wind}</td>
                  <td className="py-2 px-2 text-slate-400">{wp.tas}</td>
                  <td className="py-2 px-2 text-slate-200">{wp.gs}</td>
                  <td className="py-2 px-2 text-slate-300">{wp.eet}</td>
                  <td className="py-2 px-3 text-right font-bold text-amber-200">{wp.fuelRem}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
