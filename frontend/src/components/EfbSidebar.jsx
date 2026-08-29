import React from 'react';
import {
  Users,
  UserCheck,
  Check,
  TrendingUp,
  Fuel,
  CloudRain,
  MessageSquare,
  FileCheck,
  ClipboardList,
  Clock,
  FileSpreadsheet,
  Code2,
  Sparkles,
} from 'lucide-react';

export default function EfbSidebar({ activeTab, onSelectTab, onOpenAiChat }) {
  const navItems = [
    {
      id: 'flight_crew',
      label: 'FC BRIEF',
      fullLabel: 'Flight Crew Briefing',
      icon: Users,
    },
    {
      id: 'joint_brief',
      label: 'JOINT',
      fullLabel: 'Joint Briefing',
      icon: UserCheck,
    },
    {
      id: 'check',
      label: 'CHECK',
      icon: Check,
    },
    {
      id: 'wx',
      label: 'WX',
      icon: CloudRain,
    },
    {
      id: 'notam',
      label: 'NOTAM',
      icon: MessageSquare,
    },
    {
      id: 'route',
      label: 'ROUTE',
      icon: TrendingUp,
    },
    {
      id: 'fuel',
      label: 'FUEL',
      icon: Fuel,
    },
    {
      id: 'rules',
      label: 'RULES',
      icon: FileCheck,
    },
    {
      id: 'report',
      label: 'REPORT',
      icon: FileSpreadsheet,
    },
    {
      id: 'edto',
      label: 'EDTO',
      icon: Clock,
    },
    {
      id: 'fpl',
      label: 'FPL',
      icon: ClipboardList,
    },
    {
      id: 'raw',
      label: 'RAW',
      icon: Code2,
    },
    {
      id: 'ai',
      label: 'AI',
      icon: Sparkles,
      isAction: true,
      action: onOpenAiChat,
    },
  ];

  const handleClick = (item) => {
    if (item.isAction && item.action) {
      item.action();
      return;
    }
    onSelectTab(item.id);
  };

  return (
    <aside className="fixed left-0 top-[57px] bottom-0 z-40 w-16 bg-[#080d19] border-r border-slate-800/80 flex flex-col justify-start py-2 select-none shadow-xl overflow-y-auto">
      <div className="flex flex-col w-full">
        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;

          return (
            <button
              key={item.id}
              onClick={() => handleClick(item)}
              title={item.fullLabel || item.label}
              className={`relative w-full py-3 flex flex-col items-center justify-center transition-all group ${
                isActive
                  ? 'bg-amber-500/10 text-amber-300'
                  : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900/60'
              }`}
            >
              {isActive && (
                <div className="absolute left-0 top-0 bottom-0 w-1 bg-amber-400 shadow-[0_0_8px_rgba(245,158,11,0.5)]" />
              )}

              <div className="flex items-center justify-center">
                <Icon
                  className={`w-5 h-5 transition-transform duration-150 group-hover:scale-110 ${
                    isActive ? 'text-amber-300 stroke-[2.2]' : 'text-slate-400 group-hover:text-slate-200'
                  }`}
                />
              </div>

              <span
                className={`text-2xs font-mono font-bold tracking-wider mt-1.5 uppercase ${
                  isActive ? 'text-amber-300' : 'text-slate-400 group-hover:text-slate-300'
                }`}
              >
                {item.label}
              </span>
            </button>
          );
        })}
      </div>
    </aside>
  );
}
