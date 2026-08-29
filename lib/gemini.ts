import { GoogleGenAI } from '@google/genai';
import { FlightBriefingData } from '../types/flight';

const SYSTEM_INSTRUCTION = `
You are a Senior Airline Captain and Chief Flight Operations Dispatcher with 20+ years of aviation experience (Boeing, Airbus, ICAO, FAA, EASA).
Your role is to critically analyze aviation flight documents (Operational Flight Plans - OFP, Weather packages, METAR/TAF, NOTAMs, Dispatch Releases) and produce a structured, high-priority, human-friendly Pilot Pre-flight Briefing.

CRITICAL GUIDELINES:
1. Identify all critical Go/No-Go items immediately (Runway closures, severe weather, crosswind limits, fuel status).
2. Translate cryptic METAR/TAF/NOTAM aviation jargon into plain Korean explanations for the pilot.
3. Calculate and verify fuel requirements (Trip, Cont, Alt, Final Reserve, Extra, Block).
4. If certain fields are not found in the document, make educated standard aviation defaults or mark them clearly.
5. Provide a 1-minute spoken briefing script in natural, professional Korean cockpit briefing tone ("안녕하십니까 기장님, 금일 ...").
6. Always return VALID JSON matching the FlightBriefingData interface.
`;

const EXTRACTION_PROMPT = `
Analyze the provided flight document (OFP / Weather / NOTAM / Dispatch Release) and extract a complete, structured pilot briefing in the following JSON format:

{
  "flightInfo": {
    "flightNumber": "e.g. KAL701",
    "callsign": "e.g. KOREAN AIR 701",
    "aircraftType": "e.g. B777-300ER or A350-900",
    "registration": "e.g. HL8274",
    "origin": { "icao": "RKSI", "iata": "ICN", "name": "Incheon Intl", "elevation": "23 FT", "runways": ["15L/33R"] },
    "destination": { "icao": "RJAA", "iata": "NRT", "name": "Tokyo Narita", "elevation": "141 FT", "runways": ["16R/34L"] },
    "alternates": [
      { "icao": "RJTT", "iata": "HND", "name": "Tokyo Haneda", "remarks": "Primary" }
    ],
    "std": "Departure time (UTC)",
    "sta": "Arrival time (UTC)",
    "ete": "e.g. 02:20",
    "flightLevel": "e.g. FL370",
    "costIndex": "e.g. 35",
    "route": "Full route waypoints",
    "distanceNm": 694
  },
  "executiveSummary": "A concise, high-level Korean summary of the flight, weather hazards, and operational points for the pilot.",
  "goNoGoAssessment": {
    "status": "GO" | "CAUTION" | "NO_GO",
    "primaryReason": "Key reason for this assessment in Korean",
    "keyCheckpoints": ["Point 1", "Point 2", "Point 3"]
  },
  "hazards": [
    {
      "id": "HAZ-01",
      "level": "CRITICAL" | "WARNING" | "INFO",
      "category": "WEATHER" | "NOTAM" | "AIRPORT" | "EQUIPMENT" | "SECURITY" | "PERFORMANCE",
      "title": "Hazard title in Korean",
      "description": "Hazard details in Korean",
      "recommendation": "Pilot action recommendation in Korean"
    }
  ],
  "weather": {
    "origin": {
      "icao": "RKSI",
      "type": "ORIGIN",
      "metarRaw": "raw METAR if available",
      "metarTranslated": "Korean plain explanation",
      "tafRaw": "raw TAF if available",
      "tafTranslated": "Korean plain explanation",
      "flightCategory": "VFR" | "MVFR" | "IFR" | "LIFR",
      "wind": { "direction": 320, "speed": 8, "gust": 0, "crosswindEstimate": "..." },
      "visibility": "...",
      "ceiling": "...",
      "temperature": "...",
      "altimeter": "..."
    },
    "destination": {
      "icao": "RJAA",
      "type": "DESTINATION",
      "metarRaw": "...",
      "metarTranslated": "...",
      "tafRaw": "...",
      "tafTranslated": "...",
      "flightCategory": "...",
      "wind": { "direction": 210, "speed": 16, "gust": 26, "crosswindEstimate": "..." },
      "visibility": "...",
      "ceiling": "...",
      "temperature": "...",
      "altimeter": "...",
      "significantHazards": ["..."]
    },
    "alternates": [],
    "enrouteSignificantWeather": ["..."]
  },
  "notams": [
    {
      "id": "NOTAM ID",
      "category": "RUNWAY" | "TWY" | "NAVAID" | "AIRSPACE" | "OBSTACLE" | "COMMS" | "GENERAL",
      "rawText": "Raw NOTAM",
      "plainSummary": "Korean plain summary",
      "severity": "HIGH" | "MEDIUM" | "LOW",
      "location": "ICAO",
      "isCritical": true | false
    }
  ],
  "fuel": {
    "tripFuel": 18400,
    "contingencyFuel": 1200,
    "alternateFuel": 3800,
    "finalReserveFuel": 4200,
    "extraFuel": 2400,
    "blockFuel": 30000,
    "minTakeoffFuel": 27600,
    "unit": "KG" | "LBS",
    "burnRatePerHour": 6800,
    "enduranceHours": "04:24"
  },
  "spokenBriefingScript": "Professional Korean spoken briefing script (~1 minute length) for pilot playback",
  "parsedAt": "Current UTC Timestamp",
  "documentName": "File name"
}

Ensure the output is ONLY valid JSON.
`;

export async function analyzeFlightDocument(
  fileBase64: string,
  mimeType: string,
  fileName: string,
  customApiKey?: string
): Promise<FlightBriefingData> {
  const apiKey = customApiKey || process.env.GEMINI_API_KEY;
  if (!apiKey) {
    throw new Error('GEMINI_API_KEY is not configured. Please provide an API key.');
  }

  const ai = new GoogleGenAI({ apiKey });

  const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: [
      {
        inlineData: {
          data: fileBase64,
          mimeType: mimeType || 'application/pdf',
        },
      },
      {
        text: `${SYSTEM_INSTRUCTION}\n\n${EXTRACTION_PROMPT}\nDocument filename: ${fileName}`,
      },
    ],
    config: {
      responseMimeType: 'application/json',
    },
  });

  const text = response.text?.trim();
  if (!text) {
    throw new Error('Gemini API returned an empty response.');
  }

  // Remove potential markdown code fences if present
  const cleanedJson = text.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '');
  const parsedData = JSON.parse(cleanedJson) as FlightBriefingData;
  parsedData.documentName = fileName;
  parsedData.parsedAt = new Date().toISOString();

  return parsedData;
}

export async function askFlightAssistant(
  briefingContext: FlightBriefingData,
  userQuestion: string,
  chatHistory: Array<{ role: 'user' | 'model'; text: string }>,
  customApiKey?: string
): Promise<string> {
  const apiKey = customApiKey || process.env.GEMINI_API_KEY;
  if (!apiKey) {
    throw new Error('GEMINI_API_KEY is not configured. Please provide an API key.');
  }

  const ai = new GoogleGenAI({ apiKey });

  const systemPrompt = `
You are an expert Co-pilot / Aviation Dispatch Assistant.
You have full access to the current flight's briefing data:
${JSON.stringify(briefingContext, null, 2)}

Answer the pilot's questions accurately, concisely, and professionally in Korean.
When referencing runway numbers, wind directions, fuel figures, or NOTAMs, cite exact data from the briefing.
If information is not present in the briefing, state so clearly and offer relevant standard operational wisdom.
`;

  const contents = [
    { text: systemPrompt },
    ...chatHistory.map((msg) => ({
      role: msg.role === 'user' ? 'user' : 'model',
      parts: [{ text: msg.text }],
    })),
    { role: 'user', parts: [{ text: userQuestion }] },
  ];

  const response = await ai.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: contents as any,
  });

  return response.text || '답변을 생성하지 못했습니다.';
}
