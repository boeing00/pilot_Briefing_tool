import React from 'react';
import { Plane, Key, UploadCloud } from 'lucide-react';

export default function Navbar({ hasApiKey, onOpenApiKey, onOpenUpload }) {
  return (
    <header className="bg-slate-900/90 backdrop-blur border-b border-slate-800 sticky top-0 z-30 px-4 py-3">
      <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
        {/* Brand & Status */}
        <div className="flex items-center gap-3">
          <div className="p-2 bg-slate-800 text-amber-300 border border-slate-700 rounded-lg flex items-center justify-center">
            <Plane className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-base font-bold tracking-wider text-slate-100 uppercase">
                Pilot Briefing EFB
              </h1>
              <span className="text-2xs px-1.5 py-0.5 bg-slate-800 text-slate-400 border border-slate-700 rounded-lg font-mono font-medium">
                v1.0
              </span>
            </div>
            <p className="text-xs text-slate-400">
              AI-Powered Flight Document Ingestion & Operations Briefing
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2 font-mono">
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

          {/* AI availability pill - the app talks to Gemini directly, so this tracks the key */}
          <div className="hidden md:flex items-center gap-1.5 px-2.5 py-1 bg-slate-800/80 rounded-full border border-slate-700/60 text-sm text-slate-300">
            {hasApiKey ? (
              <>
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>AI READY</span>
              </>
            ) : (
              <>
                <span className="w-2 h-2 rounded-full bg-amber-500"></span>
                <span>API Key 필요</span>
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
