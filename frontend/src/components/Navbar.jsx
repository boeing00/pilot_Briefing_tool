import React from 'react';
import { Plane, Key, UploadCloud, RefreshCw } from 'lucide-react';

export default function Navbar({
  serverHealth,
  onOpenApiKey,
  onOpenUpload,
  currentFlight,
  onSelectFlight,
  loading,
  hasBriefing,
}) {
  return (
    <header className="bg-slate-900/90 backdrop-blur border-b border-slate-800 sticky top-0 z-30 px-4 py-3">
      <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
        {/* Brand & Status */}
        <div className="flex items-center gap-3">
          <div className="p-2 bg-slate-800 text-amber-300 border border-slate-700 rounded-lg flex items-center justify-center shadow-inner">
            <Plane className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-base font-bold tracking-wider text-slate-100 uppercase">
                Pilot Briefing EFB
              </h1>
              <span className="text-[10px] px-1.5 py-0.5 bg-slate-800 text-slate-400 border border-slate-700 rounded font-mono font-medium">
                v1.0
              </span>
            </div>
            <p className="text-xs text-slate-400">
              AI-Powered Flight Document Ingestion & Operations Briefing
            </p>
          </div>
        </div>

        {/* Flight Preset Selector & Tools */}
        <div className="flex items-center gap-2 font-mono">
          {/* Preset Buttons */}
          <div className="flex items-center bg-slate-950 p-1 rounded-xl border border-slate-800 text-xs">
            <button
              onClick={() => onSelectFlight('KLAX')}
              disabled={loading}
              className={`px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1.5 ${
                currentFlight === 'KLAX'
                  ? 'bg-amber-500/20 text-amber-300 border border-amber-400/40 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <span>✈️ RKSI ➔ KLAX (AAR202)</span>
            </button>
            <button
              onClick={() => onSelectFlight('KJFK')}
              disabled={loading}
              className={`px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1.5 ${
                currentFlight === 'KJFK'
                  ? 'bg-amber-500/20 text-amber-300 border border-amber-400/40 shadow-sm'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <span>✈️ RKSI ➔ KJFK (AAR224)</span>
            </button>
          </div>

          {/* Upload PDF Button */}
          {onOpenUpload && (
            <button
              onClick={onOpenUpload}
              className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-amber-200 text-xs font-bold rounded-lg border border-slate-700 transition"
              title="PDF 비행계획서 업로드"
            >
              <UploadCloud className="w-4 h-4 text-amber-400" />
              <span className="hidden sm:inline">PDF 업로드</span>
            </button>
          )}

          {/* Server status pill */}
          <div className="hidden md:flex items-center gap-1.5 px-2.5 py-1 bg-slate-800/80 rounded-full border border-slate-700/60 text-xs text-slate-300">
            {serverHealth?.status === 'online' ? (
              <>
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>API Online</span>
              </>
            ) : (
              <>
                <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                <span>Connecting...</span>
              </>
            )}
          </div>

          {/* API Key Modal Button */}
          <button
            onClick={onOpenApiKey}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-medium rounded-lg border border-slate-700 transition"
            title="Gemini API Key Settings"
          >
            <Key className="w-3.5 h-3.5 text-amber-400" />
            <span className="hidden sm:inline">API Key</span>
          </button>
        </div>
      </div>
    </header>
  );
}
