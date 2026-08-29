# Pilot Briefing EFB

조종사용 EFB 웹앱. OFP/기상/NOTAM PDF를 올리면 Gemini가 구조화된 브리핑을 만들어
12개 탭으로 보여준다. 실사용 기기는 **iPad**(조종실, 밝은 빛, 한 손 조작).

라이브: https://boeing00.github.io/pilot_Briefing_tool/

## 무엇이 실제로 배포되는가

**`frontend/` (Vite + React) 하나뿐이다.** `.github/workflows/deploy.yml`이 `frontend/`만
빌드해 GitHub Pages로 올린다. main에 푸시하면 약 1분 뒤 반영된다.

저장소에 있지만 **배포되지 않는 것**:

| 경로 | 상태 |
|---|---|
| `app/`, `components/`, `lib/`, `next.config.ts` | 루트 Next.js 앱. 사용 안 함 |
| `backend/` | 구 FastAPI. 서버는 더 이상 없음. **단, 삭제 금지** — 아래 참조 |
| `AGENTS.md` | `next dev`가 자동 생성한 Next.js 규칙. **이 앱과 무관하니 따르지 말 것** |

`backend/services/sample_data.py`는 번들 샘플 브리핑
(`frontend/src/data/sample_*.json`)의 원본이다. 샘플을 고치려면 여기서 고치고 다시
추출한다. 그래서 `backend/`를 지우면 안 된다.

## 아키텍처: 백엔드 없음

정적 호스팅이라 서버가 없다. **브라우저에서 Gemini를 직접 호출한다.**
사용자가 자기 API Key를 UI에 입력 → 해당 브라우저 localStorage → 브라우저에서
Google로 직행. 제3자 서버를 거치지 않는다.

- 키는 **기기마다 별도**다. PC에서 넣은 키는 iPad에 없다.
- PDF는 텍스트 추출 없이 `inlineData`로 통째로 보낸다. 표와 단으로 된 OFP는
  추출본보다 원본 인식이 낫다.
- `/api/*` 경로를 되살리지 말 것. 정적 호스팅에서 전부 404다.

## 하지 말아야 할 것

**NOTAM 데이터를 절대 합성하지 말 것.** 과거에 항로 NOTAM 4건을 하드코딩해두고
브리핑에 없으면 대신 보여주는 코드가 있었다. 존재하지 않는 NOTAM 번호에 비행
날짜와 맞지 않는 유효기간이었고, "NOTAM 원문 (Raw ICAO Text)" 제목과 복사 버튼
아래에 렌더링되어 진짜 전문과 구분이 되지 않았다. 데이터가 없으면 **빈 상태를
보여준다.** 번들 샘플에는 "예시 데이터 · 실제 운항에 사용 금지" 표식을 유지한다.

**NOTAM ID는 공항 간 유일하지 않다.** `COAD01/21` 하나가 9개 공항에 존재한다.
행 단위 상태(음영 처리 등)는 반드시 위치 기반 키를 쓸 것. id로 키잉하면 한 건을
접었을 때 다른 공항 NOTAM까지 함께 사라진다.

**루트 `postcss.config.mjs`가 Vite 빌드로 새어 들어온다.** Next.js용이고
`@tailwindcss/postcss`를 요구하는데 `frontend/`에는 없어서 빌드가 깨진다.
`frontend/vite.config.js`의 `css.postcss: {}`가 이걸 막고 있으니 지우지 말 것.

## Gemini 호출 (`frontend/src/services/api.js`)

API에서 직접 조회한 `gemini-2.5-flash` 한계:

```
inputTokenLimit   1,048,576
outputTokenLimit     65,536   ← thinking과 공유
thinking             기본 ON
```

- 문서에 적힌 `thinking_level`(REST `thinkingLevel`)은 v1beta generateContent에서
  **400 Unknown name**을 반환한다. 실제로 동작하는 건 `thinkingConfig.thinkingBudget`뿐.
- thinking을 묶지 않으면 OFP 1건에 4천 토큰을 먼저 먹는다. 현재 4096으로 제한.
- `candidate.content.parts`에는 `{ text, thought: true }` 파트가 섞여 올 수 있다.
  **반드시 걸러낼 것.** 안 그러면 추론 산문이 JSON 앞에 붙는다.
- 응답 파싱은 4단계 복구를 거친다(원본 → 펜스 제거 → 최외곽 `{...}` 추출 →
  절단 복구). 부분 복구된 브리핑은 `__truncated` 표식을 달고 화면에 경고를 띄운다.
  **조종사가 부분 자료를 전체로 오인하면 안 된다.**

## 디자인 규칙 (`frontend/src/index.css`)

iPad에서 팔 길이만큼 떨어져 읽는다는 전제로 잡혀 있다.

- **타입**: `@theme`에 12~36px 스케일. `text-2xs`(12px)가 바닥이며 그 아래로 내리지
  말 것. 한글 산문은 Pretendard, 수치는 Inter.
- **숫자**: Inter + `tabular-nums`. 모노스페이스 계열은 전부 0에 점/슬래시가 있어
  쓰지 않는다. 단 `.font-code`(IBM Plex Mono)는 ATS FPL·RAW OFP·JSON 뷰어처럼
  문자 그리드가 의미를 갖는 전문에만 남긴다.
- **색**: 4역할만. `slate`=표면·본문, `amber`=브랜드·상호작용, `emerald`=정상,
  `rose`=경고. 다른 계열을 새로 들이지 말 것.
- **터치 타깃**: 최소 36px, `pointer: coarse`에서 44px.
- **한글 줄바꿈**: `word-break: keep-all`. 좁은 칸에서 한 글자씩 세로로 깨진다.
- **깊이는 테두리로.** 근흑색 바탕에서 drop shadow는 보이지 않는다.

## 작업 후 확인

```bash
cd frontend && npm run build && npx oxlint
```

UI를 건드렸다면 820×1180(iPad)에서 가로 오버플로 0, 최소 폰트 12px, 명암비
4.5:1 이상을 실측해 확인할 것. 이 세션에서 837개 요소 기준 최저 5.28:1이었다.
