import React from 'react';
import RawDocViewerCard from '../components/RawDocViewerCard';

export default function RawPage({ docMeta }) {
  return (
    <div className="space-y-6 animate-fade-in">
      <RawDocViewerCard rawText={docMeta?.raw_text} />
    </div>
  );
}
