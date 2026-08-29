'use client';

import React, { useState } from 'react';
import { Volume2, VolumeX, Sparkles } from 'lucide-react';

interface AudioBriefingButtonProps {
  script: string;
}

export const AudioBriefingButton: React.FC<AudioBriefingButtonProps> = ({ script }) => {
  const [isPlaying, setIsPlaying] = useState(false);

  const toggleSpeech = () => {
    if (!('speechSynthesis' in window)) {
      alert('이 브라우저는 음성 합성(TTS)을 지원하지 않습니다.');
      return;
    }

    if (isPlaying) {
      window.speechSynthesis.cancel();
      setIsPlaying(false);
    } else {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(script);
      utterance.lang = 'ko-KR';
      utterance.rate = 1.0;
      utterance.pitch = 1.0;

      utterance.onend = () => setIsPlaying(false);
      utterance.onerror = () => setIsPlaying(false);

      window.speechSynthesis.speak(utterance);
      setIsPlaying(true);
    }
  };

  return (
    <button
      onClick={toggleSpeech}
      className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm font-medium transition-all shadow-sm ${
        isPlaying
          ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40 animate-pulse'
          : 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 hover:bg-emerald-500/20'
      }`}
      title="1분 퀵 오디오 브리핑 듣기"
    >
      {isPlaying ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4 text-emerald-400" />}
      <span>{isPlaying ? '브리핑 중지' : '1분 음성 브리핑'}</span>
      <Sparkles className="w-3.5 h-3.5 text-emerald-300" />
    </button>
  );
};
