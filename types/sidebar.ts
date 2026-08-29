export type EfbTab =
  | 'BRIEF'
  | 'CHECK'
  | 'ROUTE'
  | 'FUEL'
  | 'WX'
  | 'NOTAM'
  | 'RULES'
  | 'REPORT'
  | 'EDTO'
  | 'FPL'
  | 'RAW'
  | 'AI';

export interface SidebarItemConfig {
  id: EfbTab;
  label: string;
  badge?: {
    count: number | string;
    color: 'rose' | 'amber';
  };
}
