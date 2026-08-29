import { FlightBriefingData } from '../types/flight';

export const DEMO_FLIGHT_BRIEFING: FlightBriefingData = {
  flightInfo: {
    flightNumber: "AAR224",
    callsign: "ASIANA 224",
    aircraftType: "A380-800",
    registration: "HL7626",
    origin: {
      icao: "RKSI",
      iata: "ICN",
      name: "Incheon International Airport, Seoul",
      elevation: "23 FT",
      runways: ["15L/33R", "15R/33L", "16L/34R", "16R/34L"],
      remarks: "Company Radio: 129.35 MHz"
    },
    destination: {
      icao: "KJFK",
      iata: "JFK",
      name: "John F. Kennedy International Airport, New York",
      elevation: "13 FT",
      runways: ["04L/22R", "04R/22L", "13L/31R", "13R/31L"],
      remarks: "Company Radio: 130.925 MHz (Asiana New York)"
    },
    alternates: [
      {
        icao: "KBOS",
        iata: "BOS",
        name: "Boston Edward L Logan Intl Airport",
        elevation: "19 FT",
        remarks: "Primary ALTN (Dist: 261 NM, Time: 00:45, Req Fuel: 22,400 LBS)"
      },
      {
        icao: "KORD",
        iata: "ORD",
        name: "Chicago O'Hare International Airport",
        remarks: "3% ERA / ETP Alternate"
      },
      {
        icao: "PANC",
        iata: "ANC",
        name: "Anchorage Ted Stevens Intl",
        remarks: "ETP Alternate"
      },
      {
        icao: "RJCC",
        iata: "CTS",
        name: "Sapporo New Chitose Airport",
        remarks: "ETP Alternate"
      }
    ],
    std: "2026-08-10 12:05 UTC",
    sta: "2026-08-11 01:29 UTC",
    ete: "13:24",
    plannedEte: "13:24",
    flightLevel: "FL310 ~ FL370 (Step Climb)",
    costIndex: "65",
    route: "RKSI..EGOBA Y697 KAE Y437 TENAS L512 GTC Y512 OATIS R580 ORCCA.. SQA..GKN..GAHAM..N62W130..N61W120..N59W110..N56W100..N51W090.. N46W080..NOVON..YODAA PUCKY1 KJFK",
    distanceNm: 6663
  },
  executiveSummary: "인천(RKSI)발 뉴욕 JFK(KJFK)행 아시아나항공 AAR224편(A380-800 / HL7626) 운항 브리핑입니다. 비행시간은 13시간 24분, 비행거리는 6,663NM이며 순항고도는 FL310에서 단계적 상승(Step Climb)하여 FL370까지 운영됩니다. 15호 태풍 찬홈(CHAN-HOM)의 일본 인근 접근 및 JFK 도착 시간대 국지성 뇌우(TSRA) 가능성에 대비하여 1시간 분량(22,400 LBS)의 추가 연료(DISC FUEL)가 반영되어 총 475,800 LBS의 블록 연료가 탑재됩니다. 인천 FIR GPS 교란 주의보, 캄차카 화산활동 경보, JFK 활주로 및 접근 크레인 NOTAM을 숙지하시기 바랍니다.",
  goNoGoAssessment: {
    status: "CAUTION",
    primaryReason: "15호 태풍 찬홈 항로 인접 및 JFK 도착 시 뇌우(TSRA) 가능성, DISC FUEL(1시간) 반영됨",
    keyCheckpoints: [
      "15호 태풍 찬홈(CHAN-HOM) 일본 통과 구간 항로 및 기상 모니터링",
      "JFK 도착 예정 시간대(01:29Z) PROB30 TSRA(뇌우) 및 강수 회피(DETOUR) 대비",
      "인천 FIR 내 GPS 신호 불안정(GPS Interference) 및 400ft 미만 선회 금지 주의",
      "캄차카 반도 Sheveluch 화산활동 주의보(Color Code ORANGE) 확인",
      "교체공항 보스턴(KBOS) RWY 14/32 및 15L/33R 폐쇄 NOTAM 확인"
    ]
  },
  hazards: [
    {
      id: "HAZ-01",
      level: "WARNING",
      category: "WEATHER",
      title: "15호 태풍 찬홈(CHAN-HOM) 접근 및 항로 영향",
      description: "태풍 찬홈이 일본 도쿄 방면으로 북상 중. 비행계획 항로상 직접적인 위험은 낮으나 주변 기류 불안정 및 난기류 가능성 있음. 디스패치에서 1시간 DISC FUEL 반영 완료.",
      recommendation: "일본 영공 통과 시 기상 레이더 상시 작동 및 승무원 벨트 사인 관리."
    },
    {
      id: "HAZ-02",
      level: "WARNING",
      category: "WEATHER",
      title: "도착지 뉴욕 JFK 뇌우(TSRA) 및 CB 발달 예보",
      description: "KJFK TAF: 1021/1101 PROB30 3SM TSRA BKN050CB 및 1101/1105 PROB30 4SM SHRA 예보됨. 도착 시점에 회피 및 홀딩 가능성 존재.",
      recommendation: "접근 브리핑 시 복행 및 필요시 주 교체공항(KBOS) 또는 KORD 회항 절차 사전 점검."
    },
    {
      id: "HAZ-03",
      level: "WARNING",
      category: "NOTAM",
      title: "인천 FIR GPS 신호 불안정 경보 (GPS Interference)",
      description: "RKSI Z0511/24 NOTAM: 인천/서울 지역 GPS 간헐적 신호 유실 보고. Nuisance GPWS 경고 발생 가능성 있음.",
      recommendation: "이륙 및 초기 상승 시 기존 재래식 계기 및 FMS 모니터링 철저."
    },
    {
      id: "HAZ-04",
      level: "INFO",
      category: "EQUIPMENT",
      title: "MEL / CDL 발행 항목 (HL7626)",
      description: "MEL 25-20-04A (좌석 3K/2A 리클라인 불량), CDL 27-32 (LH WING NO.1 DROOP NOSE LATERAL D-S), MEL 33-20-05A (81F,G / 32K, 51K 조명 불량).",
      recommendation: "운항상 성능 제한 없음. CDL 항목 외부 점검 시 확인 요망."
    },
    {
      id: "HAZ-05",
      level: "INFO",
      category: "NOTAM",
      title: "캄차카 Sheveluch 화산활동 경보 (Color Code ORANGE)",
      description: "PAZA A2278/26: 캄차카 반도 Sheveluch 화산 지진활동 증가로 화산재 분출 가능성. 항로 통과 시 주의.",
      recommendation: "화산재 보고 발생 시 즉시 ATC와 협의하여 회피 항로 요청."
    }
  ],
  weather: {
    origin: {
      icao: "RKSI",
      type: "ORIGIN",
      metarRaw: "TAF RKSI 100500Z 1006/1112 20010KT CAVOK TN24/1020Z TX33/1106Z BECMG 1010/1012 14010KT",
      metarTranslated: "출발 시 풍향 200도 10노트, CAVOK(시정 10km 이상 및 구름 없음), 기온 24~33°C. 양호한 VFR 출발 기상.",
      tafRaw: "TAF RKSI 100500Z 1006/1112 20010KT CAVOK BECMG 1010/1012 14010KT BECMG 1013/1015 08007KT=",
      tafTranslated: "출발 후 야간 시간대 풍향 140도 10노트 -> 080도 7노트로 완만하게 변화, 안정적인 기상 지속.",
      flightCategory: "VFR",
      wind: { direction: 200, speed: 10, gust: 0 },
      visibility: "10km+",
      ceiling: "CAVOK",
      temperature: "33°C",
      altimeter: "1012 hPa"
    },
    destination: {
      icao: "KJFK",
      type: "DESTINATION",
      metarRaw: "TAF KJFK 100522Z 1006/1112 02004KT P6SM SKC FM101800 18012KT P6SM SCT060 BKN250 PROB30 1021/1101 3SM TSRA BKN050CB",
      metarTranslated: "도착 시간대(01:29Z) 남서풍 250도 8kt, 시정 6마일 이상, 운저고도 5,000ft 파손운(BKN). 일시적 소나기(SHRA) 및 뇌우(TSRA) 가능성 고려 필요.",
      tafRaw: "FM110100 25008KT P6SM SCT050 BKN250 PROB30 1101/1105 4SM SHRA BKN050=",
      tafTranslated: "01~05Z 도착 시간대에 30% 확률로 4마일 시정의 비(SHRA) 및 운저 5000ft 예상.",
      flightCategory: "MVFR",
      wind: { direction: 250, speed: 8, gust: 0, crosswindEstimate: "RWY 31L/22R 기준 안정적인 착륙풍" },
      visibility: "6 SM (PROB30 3-4 SM)",
      ceiling: "5,000 FT (BKN050CB)",
      temperature: "26°C",
      altimeter: "29.92 inHg",
      significantHazards: ["PROB30 TSRA", "CB CLOUD", "WET RUNWAY"]
    },
    alternates: [
      {
        icao: "KBOS",
        type: "ALTERNATE",
        metarRaw: "TAF KBOS 100534Z 1006/1112 29010KT P6SM FEW250 FM102100 21009KT P6SM SCT050 BKN200",
        metarTranslated: "보스턴(KBOS) 풍향 210도 9노트, 시정 6마일 이상, 구름 5,000ft 소량. 매우 양호한 회항 조건 유지.",
        flightCategory: "VFR",
        wind: { direction: 210, speed: 9 },
        visibility: "6 SM+",
        ceiling: "5,000 FT"
      }
    ],
    enrouteSignificantWeather: [
      "일본 열도 동쪽 해상: 15호 태풍 찬홈(CHAN-HOM) 영향으로 FL300~FL360 난기류 주의",
      "알래스카 및 캐나다 통과 구간: FL370 순항 중 Moderate CAT(청천난기류) 구역 존재",
      "미국 북동부 진입(CZYZ/KZBW/KZNY): 국지성 대류운(CB) 형성 가능성"
    ]
  },
  notams: [
    {
      id: "A5872/26",
      category: "RUNWAY",
      rawText: "26JUN26 13:52 - 26AUG26 23:59 KJFK A5872/26 E) RWY 31L TKOF HOLD LGT U/S",
      plainSummary: "뉴욕 JFK RWY 31L 이륙대기정지등(Takeoff Hold Light) 고장/불작동",
      severity: "MEDIUM",
      location: "KJFK",
      isCritical: false
    },
    {
      id: "A6513/26",
      category: "NAVAID",
      rawText: "27JUL26 20:45 - 08MAR27 20:45 KJFK A6513/26 E) IAP JOHN F KENNEDY INTL. ILS OR LOC RWY 31L S-ILS 31L DA 304/HAT 291. TEMPORARY CRANE 256FT MSL 4985FT NW OF RWY 31L.",
      plainSummary: "JFK RWY 31L 북서쪽 4,985ft 지점 크레인 설치로 ILS 결심고도(DA) 304ft로 상향 조정됨",
      severity: "HIGH",
      location: "KJFK",
      effectivePeriod: "2026-07-27 ~ 2027-03-08",
      isCritical: true
    },
    {
      id: "Z0511/24",
      category: "GENERAL",
      rawText: "30MAY24 01:15 - UFN RKSI Z0511/24 E) CAUTIONARY INFO FOR ACFT OPERATING IN INCHEON FIR : PILOTS HAVE REPORTED GPS SIGNALS ARE UNRELIABLE IN INCHEON FIR.",
      plainSummary: "인천 FIR 내 군 훈련 등으로 인한 GPS 신호 교란/불안정 주의보 발효 중",
      severity: "HIGH",
      location: "RKSI",
      isCritical: true
    },
    {
      id: "A0654/26",
      category: "RUNWAY",
      rawText: "10AUG26 01:15 - 15AUG26 12:00 KBOS A0654/26 E) RWY 14/32 CLSD EXC TAX 30MIN PPR",
      plainSummary: "교체공항 보스턴(KBOS) RWY 14/32 활주로 공사로 폐쇄됨",
      severity: "MEDIUM",
      location: "KBOS",
      isCritical: false
    },
    {
      id: "A2278/26",
      category: "AIRSPACE",
      rawText: "15JUL26 11:41 - 15JUL27 16:00 PAZA A2278/26 E) VOLCANIC ACTIVITY ADVISORY FOR SHEVELUCH VOLCANO (COLOR CODE ORANGE)",
      plainSummary: "캄차카 반도 Sheveluch 화산활동 증가(Color Code ORANGE) - 화산재 구름 주의",
      severity: "MEDIUM",
      location: "PAZA",
      isCritical: false
    }
  ],
  fuel: {
    tripFuel: 405900,
    contingencyFuel: 12200,
    alternateFuel: 22400,
    finalReserveFuel: 11000,
    extraFuel: 22400,
    blockFuel: 475800,
    minTakeoffFuel: 451500,
    unit: "LBS",
    burnRatePerHour: 30200,
    enduranceHours: "16:12"
  },
  weightAndBalance: {
    ezfw: 775700,
    maxZfw: 806800,
    estTow: 1249600,
    maxTow: 1254400,
    estLdw: 843700,
    maxLdw: 862000,
    unit: "LBS",
    payload: 117000
  },
  spokenBriefingScript: "안녕하십니까 기장님, 금일 인천발 뉴욕 JFK행 아시아나항공 AAR224편 비행 브리핑입니다. 비행시간은 13시간 24분, 비행거리 6,663NM이며 A380-800(HL7626) 기종입니다. 순항고도는 FL310에서 시작해 FL370까지 단계적으로 상승합니다. 주요 위험 요소로는 15호 태풍 찬홈의 일본 인접 영향과 뉴욕 JFK 도착 시간대 뇌우(TSRA) 가능성이 있어 1시간 분량(22,400 LBS)의 추가 연료가 반영되었습니다. 총 블록 연료는 475,800 LBS 탑재됩니다. 인천 FIR GPS 주의보와 캄차카 화산활동, JFK 31L 접근 크레인 NOTAM을 확인해 주시기 바랍니다.",
  parsedAt: "2026-08-10 09:11 UTC",
  documentName: "AAR224_RKSI_KJFK_10AUG2026.pdf"
};
