'use client';

import React, { useState, useRef } from 'react';
import { Upload, FileUp, AlertCircle, Plane, Compass } from 'lucide-react';
import { useFlightBriefing } from '@/context/FlightBriefingContext';

export const UploadZone: React.FC = () => {
  const { uploadPdf, isLoading, loadingStage, error } = useFlightBriefing();
  const [isDragOver, setIsDragOver] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFile = (file: File) => {
    if (file && (file.type === 'application/pdf' || file.name.endsWith('.pdf'))) {
      uploadPdf(file);
    } else {
      alert('PDF 파일만 업로드할 수 있습니다.');
    }
  };

  const onDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const onDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragOver(true);
  };

  const onDragLeave = () => {
    setIsDragOver(false);
  };

  return (
    <div className="w-full max-w-2xl mx-auto py-16 px-4">
      {/* Intro Banner */}
      <div className="text-center mb-8 space-y-2">
        <h2 className="text-3xl sm:text-4xl font-extrabold text-slate-100 tracking-tight">
          Pilot Briefing
        </h2>
        <p className="text-sm text-slate-400 max-w-md mx-auto leading-relaxed">
          PDF 비행 문서를 업로드하여 브리핑을 시작하세요.
        </p>
      </div>

      {/* Upload Box */}
      <div
        onDrop={onDrop}
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        onClick={() => !isLoading && fileInputRef.current?.click()}
        className={`relative border-2 border-dashed rounded-3xl p-12 sm:p-16 text-center cursor-pointer transition-all duration-300 ${
          isDragOver
            ? 'border-cyan-400 bg-cyan-950/30 scale-[1.01] shadow-2xl shadow-cyan-900/20'
            : 'border-slate-800 bg-slate-900/50 hover:border-slate-700 hover:bg-slate-900/80 shadow-xl'
        } ${isLoading ? 'pointer-events-none opacity-80' : ''}`}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept=".pdf,application/pdf"
          className="hidden"
          onChange={(e) => e.target.files?.[0] && handleFile(e.target.files[0])}
        />

        {isLoading ? (
          <div className="flex flex-col items-center justify-center space-y-4 py-6">
            <div className="relative">
              <div className="w-16 h-16 rounded-full border-4 border-cyan-500/20 border-t-cyan-400 animate-spin" />
              <Compass className="w-7 h-7 text-cyan-400 absolute inset-0 m-auto animate-pulse" />
            </div>
            <div className="space-y-1 text-center">
              <h3 className="text-base font-bold text-slate-200">비행 문서 분석 중</h3>
              <p className="text-xs font-mono text-cyan-400 max-w-md animate-pulse">
                {loadingStage || '문서의 주요 데이터를 추출하고 있습니다...'}
              </p>
            </div>
          </div>
        ) : (
          <div className="flex flex-col items-center justify-center space-y-4">
            <div className="w-16 h-16 rounded-2xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-400 group-hover:scale-110 transition">
              <FileUp className="w-8 h-8" />
            </div>

            <div className="space-y-1">
              <p className="text-base font-semibold text-slate-200">
                PDF 비행 문서를 여기에 드래그하거나 클릭
              </p>
              <p className="text-xs text-slate-400">
                OFP, 기상 차트, NOTAM 브리핑 패키지 (PDF)
              </p>
            </div>

            <div className="pt-2 flex items-center justify-center">
              <button
                type="button"
                className="px-6 py-2.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold text-xs transition shadow-lg shadow-cyan-500/15 flex items-center gap-2"
              >
                <Upload className="w-3.5 h-3.5" />
                <span>PDF 파일 선택</span>
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Error Message */}
      {error && (
        <div className="mt-4 p-4 rounded-2xl bg-rose-950/50 border border-rose-800/60 text-rose-300 text-xs flex items-start gap-3">
          <AlertCircle className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
          <div>
            <p className="font-bold">분석 실패</p>
            <p className="mt-0.5 opacity-90">{error}</p>
          </div>
        </div>
      )}
    </div>
  );
};
