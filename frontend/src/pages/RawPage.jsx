import React from 'react';
import RawDocViewerCard from '../components/RawDocViewerCard';

export default function RawPage({ docMeta }) {
  const isSample = docMeta?.is_sample !== false;

  return (
    <div className="space-y-6 animate-fade-in">
      {!isSample && (
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 text-base text-slate-300 leading-relaxed">
          업로드하신 PDF는 Gemini로 직접 전달되어 분석됩니다. 원문 텍스트 추출 단계를 거치지
          않으므로 이 탭에는 표시할 원문이 없습니다. 아래는 참고용 CFP 서식 예시입니다.
        </div>
      )}
      <RawDocViewerCard rawText={isSample ? docMeta?.raw_text : ''} />
    </div>
  );
}
