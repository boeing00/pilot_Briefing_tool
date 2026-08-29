import React from 'react';
import AtsFplCard from '../components/AtsFplCard';

export default function FplPage({ briefing }) {
  return (
    <div className="space-y-6 animate-fade-in">
      <AtsFplCard briefing={briefing} />
    </div>
  );
}
