import React from 'react';
import RulesAndMelCard from '../components/RulesAndMelCard';

export default function RulesPage({ briefing }) {
  return (
    <div className="space-y-6 animate-fade-in font-mono">
      <RulesAndMelCard briefing={briefing} />
    </div>
  );
}
