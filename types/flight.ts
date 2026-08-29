export type HazardLevel = 'CRITICAL' | 'WARNING' | 'INFO';
export type HazardCategory = 'WEATHER' | 'NOTAM' | 'AIRPORT' | 'EQUIPMENT' | 'SECURITY' | 'PERFORMANCE';

export interface HazardItem {
  id: string;
  level: HazardLevel;
  category: HazardCategory;
  title: string;
  description: string;
  recommendation?: string;
  sourceDoc?: string;
}

export interface AirportInfo {
  icao: string;
  iata?: string;
  name: string;
  elevation?: string;
  runways?: string[];
  weather?: WeatherItem;
  remarks?: string;
}

export interface WeatherItem {
  icao: string;
  type: 'ORIGIN' | 'DESTINATION' | 'ALTERNATE' | 'ENROUTE';
  metarRaw?: string;
  metarTranslated?: string;
  tafRaw?: string;
  tafTranslated?: string;
  flightCategory?: 'VFR' | 'MVFR' | 'IFR' | 'LIFR';
  wind?: {
    direction: number | string;
    speed: number;
    gust?: number;
    crosswindEstimate?: string;
  };
  visibility?: string;
  ceiling?: string;
  temperature?: string;
  altimeter?: string;
  significantHazards?: string[];
}

export interface NotamItem {
  id: string;
  category: 'RUNWAY' | 'TWY' | 'NAVAID' | 'AIRSPACE' | 'OBSTACLE' | 'COMMS' | 'GENERAL';
  rawText: string;
  plainSummary: string;
  severity: 'HIGH' | 'MEDIUM' | 'LOW';
  location: string;
  effectivePeriod?: string;
  isCritical: boolean;
}

export interface WaypointItem {
  name: string;
  airway?: string;
  level?: string;
  windTemp?: string;
  timeRemaining?: string;
  fuelRemaining?: string;
}

export interface FuelItem {
  tripFuel: number;
  contingencyFuel: number;
  alternateFuel: number;
  finalReserveFuel: number;
  extraFuel: number;
  blockFuel: number;
  minTakeoffFuel?: number;
  unit: 'LBS' | 'KG' | 'LBS/KG';
  burnRatePerHour?: number;
  enduranceHours?: string;
}

export interface WeightAndBalance {
  ezfw?: number;
  maxZfw?: number;
  estTow?: number;
  maxTow?: number;
  estLdw?: number;
  maxLdw?: number;
  unit?: 'LBS' | 'KG';
  payload?: number;
}

export interface FlightBriefingData {
  flightInfo: {
    flightNumber: string;
    callsign?: string;
    aircraftType: string;
    registration?: string;
    origin: AirportInfo;
    destination: AirportInfo;
    alternates: AirportInfo[];
    std: string;
    sta: string;
    ete: string; // Current/Adjusted ETE
    plannedEte?: string; // Original Plan ETE (e.g. 13:24)
    flightLevel: string;
    costIndex?: string;
    route: string;
    distanceNm?: number;
  };
  executiveSummary: string;
  goNoGoAssessment: {
    status: 'GO' | 'CAUTION' | 'NO_GO';
    primaryReason: string;
    keyCheckpoints: string[];
  };
  hazards: HazardItem[];
  weather: {
    origin: WeatherItem;
    destination: WeatherItem;
    alternates: WeatherItem[];
    enrouteSignificantWeather: string[];
  };
  notams: NotamItem[];
  fuel: FuelItem;
  weightAndBalance?: WeightAndBalance;
  waypoints?: WaypointItem[];
  spokenBriefingScript: string;
  parsedAt: string;
  documentName?: string;
}

export interface ChatMessage {
  id: string;
  sender: 'user' | 'assistant';
  content: string;
  timestamp: string;
  referencedSection?: string;
}
