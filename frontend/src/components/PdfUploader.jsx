import React, { useRef, useState } from 'react';
import { UploadCloud, FileCheck, AlertCircle, Loader2 } from 'lucide-react';

export default function PdfUploader({ onFileUpload, loading, docMeta }) {
  const [isDragOver, setIsDragOver] = useState(false);
  const fileInputRef = useRef(null);

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragOver(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    setIsDragOver(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragOver(false);
    const files = e.dataTransfer.files;
    if (files && files.length > 0) {
      if (files[0].type === 'application/pdf' || files[0].name.endsWith('.pdf')) {
        onFileUpload(files[0]);
      } else {
        alert('PDF 파일만 업로드 가능합니다.');
      }
    }
  };

  const handleFileInputChange = (e) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      onFileUpload(files[0]);
    }
    e.target.value = '';
  };

  return (
    <div className="w-full">
      {docMeta ? (
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 flex flex-col lg:flex-row items-center justify-between gap-4 shadow-lg">
          <div className="flex items-center gap-3 w-full lg:w-auto">
            <div className="p-2.5 bg-amber-500/10 border border-amber-500/30 rounded-lg text-amber-400 shrink-0">
              <FileCheck className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-semibold text-slate-100 text-sm truncate max-w-[280px] sm:max-w-md">
                  {docMeta.filename || '업로드된 비행계획서'}
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                {docMeta.page_count
                  ? `총 ${docMeta.page_count}페이지 문서 파싱 및 브리핑 생성 완료`
                  : '문서 파싱 및 브리핑 생성 완료'}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 w-full lg:w-auto justify-end">
            <button
              onClick={() => fileInputRef.current?.click()}
              disabled={loading}
              className="px-3.5 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-bold rounded-lg transition shadow-sm flex items-center gap-2 disabled:opacity-50"
            >
              {loading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>AI 분석 중...</span>
                </>
              ) : (
                <>
                  <UploadCloud className="w-4 h-4" />
                  <span>새 PDF 업로드</span>
                </>
              )}
            </button>
          </div>
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileInputChange}
            accept=".pdf,application/pdf"
            className="hidden"
          />
        </div>
      ) : (
        <div
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
          className={`border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all duration-200 ${
            isDragOver
              ? 'border-amber-500 bg-amber-950/20 shadow-lg'
              : 'border-slate-700/80 bg-slate-900/60 hover:border-slate-600 hover:bg-slate-900'
          }`}
        >
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileInputChange}
            accept=".pdf,application/pdf"
            className="hidden"
          />
          {loading ? (
            <div className="flex flex-col items-center justify-center gap-3">
              <Loader2 className="w-10 h-10 text-amber-400 animate-spin" />
              <div>
                <p className="font-semibold text-slate-200 text-sm">
                  항공 운항 문서를 정밀 분석하고 있습니다...
                </p>
                <p className="text-xs text-slate-400 mt-1">
                  기상, NOTAM, 연료 및 위험 요소(TEM)를 추출 중입니다.
                </p>
              </div>
            </div>
          ) : (
            <div className="flex flex-col items-center justify-center gap-2.5">
              <div className="p-3 bg-amber-600/10 text-amber-400 border border-amber-500/20 rounded-full">
                <UploadCloud className="w-8 h-8" />
              </div>
              <h3 className="text-base font-semibold text-slate-100">
                비행계획서(OFP), 기상/NOTAM PDF 업로드
              </h3>
              <p className="text-xs text-slate-400 max-w-md">
                PDF 파일을 드래그하여 놓거나 클릭하여 선택하세요.
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
