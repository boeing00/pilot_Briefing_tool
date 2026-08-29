# ✈️ Pilot Briefing Web App (조종사용 PDF 운항 브리핑 웹앱)

항공 비행계획서(OFP, Operational Flight Plan), 기상(METAR/TAF/SIGMET), NOTAM(고시보) 등이 포함된 PDF 문서를 업로드하면, AI(Google Gemini)가 핵심 운항 정보를 구조화하여 **음성 브리핑(TTS)**, **조종사 EFB 대시보드**, **실시간 콕핏 Q&A**를 제공하는 웹 애플리케이션입니다.

---

## 🛠️ 빠른 시작 가이드 (Quick Start)

### 1. 백엔드 (FastAPI) 실행
```bash
cd backend
# 가상환경 활성화 (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# 서버 실행 (포트 8000)
uvicorn main:app --reload --port 8000
```
- Swagger API 문서: http://localhost:8000/docs
- 헬스체크: http://localhost:8000/api/health

*(선택사항) Gemini API Key 설정: `.env` 파일에 `GEMINI_API_KEY=your_key`를 추가하거나 웹 화면 상단 'API Key' 버튼으로 브라우저에서 직접 등록 가능합니다.*

---

### 2. 프론트엔드 (React + Vite) 실행
새 터미널을 열고 다음 명령어를 실행합니다:
```bash
cd frontend
npm run dev
```
- 웹 애플리케이션 접속: http://localhost:5173

---

## 🎨 UI/UX 직접 디자인 가이드

사용자님께서 자유롭게 UI/UX를 디자인하실 수 있도록, **데이터 레이어(Hook/API)**와 **화면 레이어(Components)**가 명확하게 분리되어 있습니다.

### 1. 주요 커스텀 훅 (State & Actions)
| Hook | 위치 | 설명 |
|---|---|---|
| `useBriefing()` | `src/hooks/useBriefing.js` | PDF 업로드, 샘플 로드, 브리핑 데이터 상태 관리 |
| `useAudioBriefing()` | `src/hooks/useAudioBriefing.js` | Web Speech 기반 음성 브리핑 재생/일시정지/속도 조절 |
| `usePilotChat()` | `src/hooks/usePilotChat.js` | 비행 문서 기반 조종사 실시간 질의응답 (Q&A) |

### 2. 모듈형 컴포넌트 구조
`frontend/src/components/` 폴더 내 각 컴포넌트의 HTML/Tailwind 클래스를 원하시는 디자인에 맞게 자유롭게 수정하세요:
- `FlightOverviewCard.jsx`: 편명, 기종, 출발/도착/대체공항, 비행시간, 순항고도
- `WeatherBriefingCard.jsx`: 출발지/도착지 기상, 항로상 난류(CAT)/착빙, SIGMET 알림
- `NotamBriefingCard.jsx`: 활주로/유도로 폐쇄, 항법시설 점검 등 영향도(Critical/Caution)별 노탐
- `FuelAndWeightsCard.jsx`: Block/Trip/Alternate/Reserve 연료 및 이착륙 중량 한계
- `ThreatManagementCard.jsx`: 3대 안전 위협 요소(TEM) 및 경감 조치, 체크리스트
- `AudioPlayerBar.jsx`: 음성 브리핑 재생 바 및 대본 서랍
- `PilotChatModal.jsx`: 조종사용 콕핏 대화형 챗봇 모달

---

## 📋 표준 브리핑 JSON 데이터 규격

웹 상단의 **[JSON 보기]** 버튼을 누르거나 `/api/briefing/sample` 엔드포인트를 호출하여 언제든지 실제 데이터 구조를 확인할 수 있습니다:

```json
{
  "flight_summary": {
    "callsign": "KAL001",
    "aircraft_type": "B777-300ER",
    "departure": { "icao": "RKSI", "iata": "ICN", "name": "인천국제공항" },
    "destination": { "icao": "KLAX", "iata": "LAX", "name": "로스앤젤레스" },
    "alternate": { "icao": "KSAN", "iata": "SAN", "name": "샌디에이고" },
    "etd_utc": "14:30Z",
    "flight_time": "10시간 45분",
    "cruising_altitude": "FL330 -> FL350 -> FL370"
  },
  "weather_briefing": { ... },
  "notam_briefing": { ... },
  "fuel_and_weights": { ... },
  "threat_and_error_management": { ... },
  "audio_briefing_script": "안녕하십니까 기장님..."
}
```
