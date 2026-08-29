import os
import json
import logging
from typing import Dict, Any, Optional
from google import genai
from google.genai import types
from services.sample_data import get_aar224_sample_briefing
from services.pdf_parser import parse_ofp_text_locally

logger = logging.getLogger(__name__)

BRIEFING_SYSTEM_PROMPT = """
You are a Senior Airline Captain and Chief Flight Operations Dispatcher with 20+ years of aviation experience.
Your job is to critically analyze aviation flight documents (Operational Flight Plans - OFP, Weather packages, METAR/TAF, SIGMETs, NOTAMs, Fuel & Weight reports) and produce a structured, high-priority, human-friendly Pilot Pre-flight Briefing.

You must output valid JSON ONLY with the following exact schema:
{
  "flight_summary": {
    "callsign": "Flight callsign (e.g. AAR224, KAL001)",
    "flight_number": "Flight number (e.g. OZ224, KE001)",
    "aircraft_type": "Aircraft type and reg (e.g. A380-800 HL7626, B777-300ER HL8274)",
    "flight_date": "Flight date (e.g. 10 AUG 2026)",
    "departure": {
      "icao": "RKSI",
      "iata": "ICN",
      "name": "인천국제공항 (Incheon Intl)",
      "runways": "RWY 15L/15R, 16L/16R"
    },
    "destination": {
      "icao": "KJFK",
      "iata": "JFK",
      "name": "뉴욕 존 F. 케네디 국제공항 (John F. Kennedy Intl)",
      "runways": "RWY 13L/13R, 22L/22R, 31L/31R"
    },
    "alternate": {
      "icao": "KBOS",
      "iata": "BOS",
      "name": "보스턴 로건 국제공항 (Boston Logan Intl)"
    },
    "etd_utc": "12:05Z",
    "etd_lcl": "21:05 L",
    "eta_utc": "01:29Z (+1)",
    "eta_lcl": "21:29 L",
    "arrival_date": "11 AUG (Z) / 10 AUG (L)",
    "flight_time": "13Hr 24Min",
    "total_distance": "6,663 NM",
    "cruising_altitude": "FL310 -> FL350 -> FL370",
    "cost_index": "CI 35",
    "route_summary": "Full waypoint summary",
    "alternate_airports": [
      {
        "icao": "KBOS",
        "iata": "BOS",
        "name": "보스턴 로건 국제공항",
        "role": "FILED DEST ALTERNATE",
        "divertStatus": "AVAILABLE",
        "divertLabel": "DIVERT AVAILABLE (회항 가능)",
        "visRating": "시정 6SM 이상 (최저치 상회)",
        "etaZ": "02:14Z (+1)",
        "etaL": "22:14 L",
        "distTime": "261 NM / 45분 / 22,400 LBS",
        "wxStatus": "GOOD",
        "wxSummary": "Wind 290/10kt, 시정 6SM 이상, SKC. 법정 최저치 상회."
      }
    ]
  },
  "key_alerts": [
    {
      "type": "WEATHER",
      "title": "Alert title in Korean",
      "desc": "Detailed explanation in Korean",
      "level": "CRITICAL",
      "target": "wx"
    }
  ],
  "route_analysis": {
    "filed_route_string": "Full filed route string",
    "alternate_routing": "Filed alternate route string",
    "total_distance": "6,663 NM",
    "flight_time": "13Hr 24Min",
    "fir_crossings": [
      { "fir": "RJJJ (FUKUOKA)", "fix": "ANDOL", "eet": "00:46Z" }
    ],
    "waypoints": [
      { "name": "RKSI", "dist": "0", "fl": "GND", "wind": "200/10kt", "tas": "0", "gs": "0", "eet": "00:00", "fuelRem": "475.8k" }
    ]
  },
  "validation_check": {
    "match_percentage": "100%",
    "cfp_route": "CFP Route description",
    "ats_fpl_route": "ATS ICAO FPL Field 15 text",
    "items": [
      {
        "category": "TOW / AGTOW 여유",
        "detail": "여유 중량 및 구속조건 설명",
        "status": "여유 4,800 LBS",
        "statusType": "OK"
      }
    ]
  },
  "fuel_and_weights": {
    "block_fuel": "475,800 lbs",
    "trip_fuel": "405,900 lbs",
    "contingency_fuel": "12,200 lbs",
    "alternate_fuel": "22,400 lbs",
    "final_reserve": "11,000 lbs",
    "extra_fuel": "22,400 lbs",
    "extra_fuel_reason": "Dispatcher Extra / Disc fuel reason in Korean",
    "estimated_tow": "1,249,600 lbs",
    "max_tow": "1,254,400 lbs",
    "tow_margin": "Within Limits",
    "estimated_law": "843,700 lbs",
    "max_law": "862,000 lbs",
    "payload": {
      "pax_first": "0 / 0",
      "pax_business": "68 / 75",
      "pax_economy": "407 / 416",
      "pax_total_weight": "107,261 LBS (475명)",
      "cargo_weight": "10,142 LBS"
    },
    "fuel_stats": [
      { "label": "MEAN DIFFERENCE (ACTUAL - PLAN)", "val": "+1,134 LBS", "note": "평균 오차" }
    ]
  },
  "weather_briefing": {
    "departure": {
      "icao": "RKSI",
      "name": "인천국제공항",
      "etd": "12:05Z",
      "runway": "RWY 15L/15R",
      "wind": "200° / 10 KT",
      "visibility": "10 KM+ (CAVOK)",
      "ceiling": "SKC / NSC",
      "temp_qnh": "24°C / 1012 hPa",
      "assessment": ["활주로 상태 및 윈드시어 분석"],
      "raw_metar": "METAR raw string",
      "raw_taf": "TAF raw string"
    },
    "destination": {
      "icao": "KJFK",
      "name": "뉴욕 존 F. 케네디",
      "eta": "01:29Z (+1)",
      "runway": "RWY 13L/22L/31L",
      "wind": "180° / 12 KT",
      "visibility": "6 SM -> 3 SM",
      "ceiling": "BKN050CB",
      "temp_altimeter": "22°C / A3002",
      "assessment": ["도착 시간대 뇌우 및 결심고도 영향"],
      "raw_metar": "METAR raw string",
      "raw_taf": "TAF raw string"
    },
    "alternate": {
      "icao": "KBOS",
      "name": "보스턴 로건",
      "eta": "02:14Z (+1)",
      "raw_metar": "METAR raw string",
      "raw_taf": "TAF raw string",
      "suitability": "GOOD",
      "assessment": "회항 적합성 분석"
    },
    "turbulence_timeline": [
      {
        "time": "T+00:45",
        "level": "Light Turb",
        "segment": "[KAE ~ TENAS / FL310~330]",
        "detail": "제트기류 유입에 따른 약한 기체 요동",
        "action": "정상 순항"
      }
    ],
    "turbulence_guidelines": [
      "승객 벨트 사인 점등 및 객실 승무원 서비스 통제 지침"
    ],
    "enroute_airports": [
      {
        "icao": "PANC",
        "name": "앵커리지",
        "tag": "ETP 1&2 (16~20Z)",
        "taf": "TAF string",
        "note": "착륙 최저치 충족"
      }
    ],
    "sigmets": [
      { "fir": "[RJJJ 일본 FIR]", "text": "SIGMET string" }
    ],
    "typhoon_or_storm": {
      "title": "태풍 또는 대형 기상 특보",
      "tag": "MONITORING",
      "detail": "항로 영향 상세 분석"
    }
  },
  "notam_briefing": {
    "general_summary": {
      "departure_hazards": "출발공항 주요 노탐 요약",
      "arrival_hazards": "도착공항 주요 노탐 요약",
      "enroute_hazards": "항로상 주요 노탐 요약"
    },
    "notam_list": [
      {
        "id": "NOTAM ID",
        "station": "KJFK",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": false,
        "shadeReason": "음영 처리 사유",
        "rawText": "Raw NOTAM text",
        "koreanSummary": "조종사용 한국어 핵심 요약"
      }
    ]
  },
  "company_rules_and_mel": {
    "company_advisories": [
      { "id": "COAD ID", "title": "특별 지침 제목", "detail": "지침 상세", "impact": "CRITICAL" }
    ],
    "mel_cdl_items": [
      { "code": "MEL 33-20-05A", "item": "결함 품목", "action": "정비 이연 조치", "status": "CONFIRMED" }
    ]
  },
  "flight_release_report": {
    "flight_no": "AAR224 / 10AUG26",
    "dispatcher": "SEONGHYUNG_LEE (TEL: 02-6101-5503)",
    "release_statement": "I HEREBY RELEASE THE FLIGHT ...",
    "rvsm_status": "RECORDED (OK)"
  },
  "edto_etops": {
    "etp_items": [
      {
        "sector": "ETP 1 : RJCC - PANC",
        "pos": "N53°06.6 E170°27.6",
        "dist1": "2,283 NM to RJCC (04h 39m, Fuel 174,900 lbs)",
        "dist2": "1,355 NM to PANC (03h 48m, Fuel 122,500 lbs)",
        "wind": "RJCC M019 / PANC M005"
      }
    ],
    "designated_eras": "RKSI, RJCC, PANC, KORD, KBOS"
  },
  "ats_icao_fpl": {
    "raw_fpl": "(FPL-...)"
  },
  "flight_crew_briefing": {
    "key_focus": "운항승무원 사전 브리핑 핵심 요약",
    "briefing_topics": [
      "순항 단계별 고도 및 연료 모니터링",
      "도착지 기상 변화 시 회항 판단 시점"
    ]
  },
  "joint_briefing": {
    "key_focus": "운항관리사 및 객실승무원 합동 브리핑 요약",
    "coordination_items": [
      "예상 난류 구간 진입 전 객실 서비스 종료",
      "탑승객 특이사항 및 보안 절차 확인"
    ]
  },
  "threat_and_error_management": {
    "top_threats": [
      { "threat": "위협 요소", "impact": "High", "mitigation": "경감 조치" }
    ],
    "pilot_action_items": ["조종사 액션 아이템"],
    "briefing_points": ["합동 브리핑 포인트"]
  },
  "audio_briefing_script": "안녕하십니까 기장님. 금일 비행 브리핑을 시작하겠습니다..."
}

CRITICAL RULES:
1. Translate cryptic METAR/TAF/NOTAM aviation jargon into plain, actionable Korean.
2. If certain sections are not explicitly provided in the PDF, make standard realistic aviation defaults consistent with the flight route and aircraft type.
3. Output strictly valid JSON without markdown wrapping or backticks.
"""

def get_gemini_client(api_key: Optional[str] = None) -> genai.Client:
    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY is not set. Please provide an API key.")
    return genai.Client(api_key=key)

def generate_flight_briefing(pdf_text: str, api_key: Optional[str] = None, filename: str = "") -> Dict[str, Any]:
    key = api_key or os.environ.get("GEMINI_API_KEY")
    full_context_text = f"FILENAME: {filename}\n\n{pdf_text}" if filename else pdf_text
    
    if not key:
        logger.info("No GEMINI_API_KEY provided, parsing uploaded PDF locally")
        return parse_ofp_text_locally(full_context_text)
        
    try:
        client = get_gemini_client(api_key=key)
        
        prompt = f"""
Analyze the following flight operation document text and generate the structured pilot briefing JSON:

=== FLIGHT DOCUMENT CONTENT ===
{pdf_text[:55000]}
=== END OF CONTENT ===
"""
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=BRIEFING_SYSTEM_PROMPT,
                response_mime_type="application/json",
                temperature=0.2,
            )
        )
        
        result_text = response.text.strip()
        if result_text.startswith("```json"):
            result_text = result_text[7:]
        if result_text.startswith("```"):
            result_text = result_text[3:]
        if result_text.endswith("```"):
            result_text = result_text[:-3]
            
        data = json.loads(result_text.strip())
        return data
        
    except Exception as e:
        logger.error(f"Gemini API generation failed ({e}), falling back to local OFP parser", exc_info=True)
        fallback_data = parse_ofp_text_locally(pdf_text)
        fallback_data["_api_warning"] = f"Gemini API Key 오류 또는 호출 실패 ({str(e)}). 로컬 파서로 분석되었습니다."
        return fallback_data

def chat_with_flight_docs(question: str, briefing_context: Dict[str, Any], raw_text: str, api_key: Optional[str] = None) -> str:
    key = api_key or os.environ.get("GEMINI_API_KEY")
    callsign = briefing_context.get("flight_summary", {}).get("callsign", "FLIGHT")
    
    if not key:
        return f"[{callsign} 콕핏 브리핑 모드] 운항 비행계획서 기반 안내: '{question}'에 대해 로컬 문서 및 브리핑 데이터에서 안전 운항 지침을 확인하였습니다. (실시간 심층 대화형 답변을 위해 우측 상단에서 GEMINI_API_KEY를 설정해 주세요.)"
        
    try:
        client = get_gemini_client(api_key=key)
        prompt = f"""
You are an expert Flight Operations Assistant & Dispatcher helping a pilot in the cockpit.
Flight Callsign: {callsign}
The pilot is asking a question regarding their flight documents.

=== STRUCTURED BRIEFING CONTEXT ===
{json.dumps(briefing_context, ensure_ascii=False, indent=2)}

=== RAW FLIGHT DOCUMENT SNIPPETS ===
{raw_text[:25000]}

=== PILOT'S QUESTION ===
{question}

Answer concisely, accurately, and authoritatively in Korean, citing relevant ICAO/flight plan data where applicable. Focus on flight safety, fuel management, and operational practicality.
"""
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.3,
            )
        )
        return response.text.strip()
    except Exception as e:
        logger.error(f"Chat failed: {e}")
        return f"답변 생성 중 오류가 발생했습니다: {str(e)}"

def get_mock_briefing_data(pdf_text: str = "") -> Dict[str, Any]:
    return get_aar224_sample_briefing()

