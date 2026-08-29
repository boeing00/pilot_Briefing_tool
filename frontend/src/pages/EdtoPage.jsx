import React from 'react';
import EdtoErtCard from '../components/EdtoErtCard';

export default function EdtoPage({ briefing }) {
  return (
    <div className="space-y-6 animate-fade-in">
      <EdtoErtCard briefing={briefing} />
    </div>
  );
}
