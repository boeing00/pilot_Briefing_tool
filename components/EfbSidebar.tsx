'use client';

import React from 'react';
import {
  FileText,
  Check,
  Activity,
  Fuel,
  CloudRain,
  MessageSquare,
  FileCheck,
  FileSpreadsheet,
  Clock,
  File,
  Code2,
  Sparkles,
} from 'lucide-react';
import { useFlightBriefing } from '@/context/FlightBriefingContext';
import { EfbTab } from '@/types/sidebar';

interface SidebarItem {
  id: EfbTab;
  label: string;
  icon: React.ReactNode;
  badge?: {
    count: number | string;
    color: 'rose' | 'amber';
  };
}

export const EfbSidebar: React.FC = () => {
  const { activeTab, setActiveTab, briefingData } = useFlightBriefing();

  const notamCount = briefingData?.notams?.length ? Math.max(briefingData.notams.length, 332) : 332;
  const hazardCount = briefingData?.hazards?.length ? Math.max(briefingData.hazards.length, 27) : 27;

  const menuItems: SidebarItem[] = [
    {
      id: 'BRIEF',
      label: 'BRIEF',
      icon: <FileText className="w-5 h-5 stroke-[1.75]" />,
    },
    {
      id: 'CHECK',
      label: 'CHECK',
      icon: <Check className="w-5 h-5 stroke-[2.2]" />,
      badge: { count: hazardCount, color: 'rose' },
    },
    {
      id: 'ROUTE',
      label: 'ROUTE',
      icon: <Activity className="w-5 h-5 stroke-[1.75]" />,
    },
    {
      id: 'FUEL',
      label: 'FUEL',
      icon: <Fuel className="w-5 h-5 stroke-[1.75]" />,
    },
    {
      id: 'WX',
      label: 'WX',
      icon: <CloudRain className="w-5 h-5 stroke-[1.75]" />,
    },
    {
      id: 'NOTAM',
      label: 'NOTAM',
      icon: <MessageSquare className="w-5 h-5 stroke-[1.75]" />,
      badge: { count: notamCount, color: 'amber' },
    },
    {
      id: 'RULES',
      label: 'RULES',
      icon: <FileCheck className="w-5 h-5 stroke-[1.75]" />,
      badge: { count: 11, color: 'rose' },
    },
    {
      id: 'REPORT',
      label: 'REPORT',
      icon: <FileSpreadsheet className="w-5 h-5 stroke-[1.75]" />,
    },
    {
      id: 'EDTO',
      label: 'EDTO',
      icon: <Clock className="w-5 h-5 stroke-[1.75]" />,
    },
    {
      id: 'FPL',
      label: 'FPL',
      icon: <File className="w-5 h-5 stroke-[1.75]" />,
    },
    {
      id: 'RAW',
      label: 'RAW',
      icon: <Code2 className="w-5 h-5 stroke-[1.75]" />,
    },
    {
      id: 'AI',
      label: 'AI',
      icon: <Sparkles className="w-5 h-5 stroke-[1.75]" />,
    },
  ];

  return (
    <aside className="w-[74px] shrink-0 min-h-[calc(100vh-61px)] bg-[#070e1a] border-r border-[#152338] flex flex-col items-center py-2 select-none z-30">
      <div className="w-full flex flex-col space-y-0.5">
        {menuItems.map((item) => {
          const isActive = activeTab === item.id;

          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`relative w-full h-[62px] flex flex-col items-center justify-center transition-colors group ${
                isActive
                  ? 'bg-[#0c1829] text-[#00e5ff]'
                  : 'text-[#6b85a3] hover:text-[#a0b8d4] hover:bg-[#0c1726]/60'
              }`}
            >
              {/* Cyan Active Indicator Bar on left */}
              {isActive && (
                <div className="absolute left-0 top-0 bottom-0 w-[3px] bg-[#00e5ff] shadow-[0_0_8px_#00e5ff]" />
              )}

              {/* Icon Container with Badge */}
              <div className="relative flex items-center justify-center">
                <div className={isActive ? 'text-[#00e5ff]' : 'text-inherit'}>
                  {item.icon}
                </div>

                {/* Badge */}
                {item.badge && (
                  <span
                    className={`absolute -top-1.5 -right-3.5 px-1.5 py-0.2 min-w-[18px] h-[16px] rounded-full text-[10px] font-bold font-mono flex items-center justify-center leading-none shadow-sm ${
                      item.badge.color === 'rose'
                        ? 'bg-[#f43f5e] text-white'
                        : 'bg-[#f59e0b] text-[#0a0f18] font-black'
                    }`}
                  >
                    {item.badge.count}
                  </span>
                )}
              </div>

              {/* Label */}
              <span
                className={`text-[10px] font-mono font-bold tracking-wider mt-1.5 ${
                  isActive ? 'text-[#00e5ff]' : 'text-inherit'
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
};
