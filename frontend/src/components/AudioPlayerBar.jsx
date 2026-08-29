import React, { useState } from 'react';
import { Play, Pause, Square, Volume2, ChevronDown, ChevronUp, FastForward } from 'lucide-react';
import { useAudioBriefing } from '../hooks/useAudioBriefing';

export default function AudioPlayerBar({ scriptText }) {
  const [showScript, setShowScript] = useState(false);
  const {
    isPlaying,
    isPaused,
    rate,
    setRate,
    togglePlay,
    stop,
  } = useAudioBriefing(scriptText);

  if (!scriptText) return null;

  return (
    <div className="bg-gradient-to-r from-amber-950/60 via-slate-900 to-amber-950/60 border border-amber-800/40 rounded-xl p-4 shadow-lg backdrop-blur">
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
        {/* Title & Status */}
        <div className="flex items-center gap-3 w-full sm:w-auto">
          <div className={`p-2.5 rounded-full ${
            isPlaying ? 'bg-amber-600 text-white animate-pulse' : 'bg-slate-800 text-amber-400'
          }`}>
            <Volume2 className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-sm font-bold text-slate-100 uppercase tracking-wide">
                Voice Briefing Player
              </h3>
              <span className={`text-2xs px-2 py-0.5 rounded-lg font-mono font-semibold ${
                isPlaying
                  ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40'
                  : 'bg-slate-800 text-slate-400'
              }`}>
                {isPlaying ? 'PLAYING' : isPaused ? 'PAUSED' : 'READY'}
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              조종사용 표준 음성 운항 브리핑 (Web Speech Engine)
            </p>
          </div>
        </div>

        {/* Controls */}
        <div className="flex items-center gap-3 w-full sm:w-auto justify-end">
          {/* Speed Selector */}
          <div className="flex items-center gap-1 bg-slate-800/80 p-1 rounded-lg border border-slate-700/60 text-xs">
            {[0.9, 1.0, 1.2, 1.4].map((speed) => (
              <button
                key={speed}
                onClick={() => setRate(speed)}
                className={`px-2 py-0.5 rounded-lg text-xs font-medium transition ${
                  rate === speed
                    ? 'bg-amber-600 text-white shadow'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                {speed}x
              </button>
            ))}
          </div>

          {/* Play/Pause Button */}
          <button
            onClick={togglePlay}
            className="flex items-center gap-2 px-4 py-2 bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold rounded-lg shadow-lg transition transform active:scale-95"
          >
            {isPlaying ? (
              <>
                <Pause className="w-4 h-4 fill-white" />
                일시정지
              </>
            ) : (
              <>
                <Play className="w-4 h-4 fill-white" />
                브리핑 재생
              </>
            )}
          </button>

          {/* Stop Button */}
          {(isPlaying || isPaused) && (
            <button
              onClick={stop}
              className="p-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg border border-slate-700 transition"
              title="Stop"
            >
              <Square className="w-4 h-4" />
            </button>
          )}

          {/* Script Drawer Toggle */}
          <button
            onClick={() => setShowScript(!showScript)}
            className="flex items-center gap-1 px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium rounded-lg border border-slate-700 transition"
          >
            대본 {showScript ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
          </button>
        </div>
      </div>

      {/* Spoken Script Drawer */}
      {showScript && (
        <div className="mt-4 pt-4 border-t border-slate-800">
          <div className="bg-slate-950/80 p-3.5 rounded-lg border border-slate-800/80 text-xs text-slate-300 leading-relaxed max-h-48 overflow-y-auto">
            <p className="font-mono text-slate-200">{scriptText}</p>
          </div>
        </div>
      )}
    </div>
  );
}
