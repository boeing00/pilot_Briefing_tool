import json
import os

_klax_notams_path = os.path.join(os.path.dirname(__file__), "klax_notams.json")
if os.path.exists(_klax_notams_path):
    with open(_klax_notams_path, "r", encoding="utf-8") as _f:
        ALL_KLAX_NOTAMS = json.load(_f)
else:
    ALL_KLAX_NOTAMS = []

ALL_414_NOTAMS = [
    {
        "index": 1,
        "id": "COAD03/26",
        "station": "RKSI",
        "airportName": "인천국제공항 (출발지)",
        "validPeriod": "01APR26 00:00 - 31OCT26 14:59",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 01APR26 00:00 - 31OCT26 14:59 RKSI COAD03/26\n[ SIMILAR CALL SIGNS]\nPLZ PAY MORE ATTENTION TO ATC COMMUNICATION\n- OZ335 AND OZ3355 IN SEOUL APPROACH, BY SELOV\n- OZ601 (ICN-SYD) AND KE601 (ICN CEB) DURING ICN APRON & EN-ROUTE,\nBY SELOB\n- OZ756 (DAD-ICN) AND OZ356 (CAN-ICN) DURING APPROACH, BY SELOV\n- OZ349 (ICN-NKG) AND OZ339 (ICN-HRB) DURING DEPARTURE, BY SELOB\n-- BY SELOP--"
    },
    {
        "index": 2,
        "id": "COAD05/26",
        "station": "RKSI",
        "airportName": "인천국제공항 (출발지)",
        "validPeriod": "01JUN26 00:00 - UFN",
        "category": "TAXIWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 01JUN26 00:00 - UFN RKSI COAD05/26\n// RKSI SID UPDATE DUE TO NDB CHANGES //\n- BACKGROUND : AFTER FEB NDB UPDATE, CERTAIN FMS ROUTES NOW DIRECT\nTHE A/C STRAIGHT TO THE FIRST RNAV WAYPOINT.\n- A321F, A330, A350, A380, B777\nTHE FD MAY COMMAND A TURN BELOW 400FT AGL DURING DEPARTURE.\nDO NOT COMMENCE ANY TURN BELOW 400FT AGL.\n(EXCEPTION : REFER TO FOM 6.4.4)\n-- BY SELOC--\n◼ TAXIWAY"
    },
    {
        "index": 3,
        "id": "A1073/26",
        "station": "RKSI",
        "airportName": "인천국제공항 (출발지)",
        "validPeriod": "31JUL26 04:34 - 30SEP26 16:00",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "31JUL26 04:34 - 30SEP26 16:00 RKSI A1073/26\nE) TXL R23, R24 AVBL FOR ACFT UP TO ICAO CODE E WHEN TAXIING\nTO STAND\n208R, 290R\n◼ RAMP"
    },
    {
        "index": 4,
        "id": "Z0286/26",
        "station": "RKSI",
        "airportName": "인천국제공항 (출발지)",
        "validPeriod": "10JUN26 16:00 - 24DEC26 00:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "행정/AIP SUP 발효 고지 (차트 반영 완료)",
        "rawText": "10JUN26 16:00 - 24DEC26 00:00 RKSI Z0286/26\nE) TRIGGER NOTAM - AIRAC AIP SUP 41/26\nWEF 1600 UTC 10 JUN 2026 TIL 0000 UTC 24 DEC 2026\n- ACFT STAND NR 711 WILL BE CLOSED AS FOLLOWS DUE TO\nCONSTRUCTION\nFOR TEMPORARY FACILITY."
    },
    {
        "index": 5,
        "id": "Z1294/25",
        "station": "RKSI",
        "airportName": "인천국제공항 (출발지)",
        "validPeriod": "24DEC25 16:00 - 12JAN27 15:00",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24DEC25 16:00 - 12JAN27 15:00 RKSI Z1294/25\nE) TRIGGER NOTAM - AIRAC AIP SUP 102/25\nPage 26\nWEF 1600 UTC 24 DEC 2025 TO 1500 UTC 12 JAN 2027\n- OPERATIONAL RESTRICTION\n- AIRCRAFT STAND NR 505 CLSD DUE TO OPERATIONAL USE.\nCOMMENT) REFER TO LATEST NOTAM FOR ANY CHANGE.\n◼ GPS"
    },
    {
        "index": 6,
        "id": "Z0511/24",
        "station": "RKSI",
        "airportName": "인천국제공항 (출발지)",
        "validPeriod": "30MAY24 01:15 - UFN",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30MAY24 01:15 - UFN RKSI Z0511/24\nE) CAUTIONARY INFO FOR ACFT OPERATING IN INCHEON FIR :\nPILOTS HAVE REPORTED THAT GPS SIGNALS ARE UNRELIABLE OR LOST\nINTERMITTENTLY IN INCHEON FIR(AROUND INCHEON AND SEOUL AREA).\nEXERCISE EXTREME CAUTION WHEN USING GPS.\nCOMMENT) WITHIN ICN/GMP AREA,  NUISANCE GPWS\nTERRAIN WARNINGS ARE OCCURRED BY GPS INTERFERENCE.\nREVIEW RELATED PROCEDURE - OPERATION SAFETY ASSURANCE TEAM.\n[DEST]KJFK/ JFK/ John F Kennedy International Airport, New York,\nUS\n1. RUNWAY : 13R/31L : 14511FT X 200FT 04L/22R : 12079FT X 200FT\n13L/31R : 10000FT X 200FT 04R/22L : 8400FT X 200FT\n2. COMPANY RADIO : 130.925 ASIANA NEW YORK\n◼ COMPANY ADVISORY"
    },
    {
        "index": 7,
        "id": "COAD01/23",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "30APR23 00:00 - UFN",
        "category": "COMPANY ADVISORY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 30APR23 00:00 - UFN KJFK COAD01/23\nPAX TERMINAL 1 GATE DOOR OPERATIONS\n1) A350\n  - ARR GATE 5,7,8 : L1, GATE 2,3,4,6 : L2\n  - DEP GATE ALL : L2\n2) A380\n - UL1, ML1\n3) RMK : MAY CHG WITHOUT NOTICE. PLS CHK OZ STAFF AT JETBRIDGE\n-- BY JFKOC--"
    },
    {
        "index": 8,
        "id": "COAD02/23",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "30APR23 00:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 30APR23 00:00 - UFN KJFK COAD02/23\n1) GATE 4,6 : EXPECT P/B TO SPOT 1 (SPOT 2 AVBL AS SECONDARY STARTUP\nPOS) DUE TO NEW TERMINAL CONSTRUCTION\n2) RMK : P/B PROCEDURES ARE SUBJECT TO CHANGE; STRICTLY FOLLOW RAMP\nTOWER INSTRUCTIONS.\n-- BY JFKOC--"
    },
    {
        "index": 9,
        "id": "COAD01/21",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "3. 14JAN21 00:00 - UFN KJFK COAD01/21\n** DE/ANTI-ICING CURRENT STATE OF FLUIDS **\nFLUID : TYPE 1 (DOW-UCAR PG ADF DILUTE 55/45), TYPE 4 (DOW-UCAR\nFLIGHTGUARD AD-49)\nWORKING TYPE : 2 STEP\n-- BY --\n◼ RUNWAY"
    },
    {
        "index": 10,
        "id": "A5872/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "26JUN26 13:52 - 26AUG26 23:59",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "26JUN26 13:52 - 26AUG26 23:59 KJFK A5872/26\nE) RWY 31L TKOF HOLD LGT U/S"
    },
    {
        "index": 11,
        "id": "A3783/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "31MAR26 11:18 - 31AUG26 23:59",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "31MAR26 11:18 - 31AUG26 23:59 KJFK A3783/26\nE) JFK RWY 31L LEAD ON LGT AT TWY KE U/S"
    },
    {
        "index": 12,
        "id": "A3773/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "31MAR26 06:59 - 31AUG26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "31MAR26 06:59 - 31AUG26 23:00 KJFK A3773/26\nE) JFK RWY 13R LEAD OFF LGT AT TWY KE U/S\nPage 27\n◼ RUNWAY LIGHT"
    },
    {
        "index": 13,
        "id": "A4688/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "06MAY26 15:49 - 04MAY27 23:59",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "06MAY26 15:49 - 04MAY27 23:59 KJFK A4688/26\nE) TWY A CL LGT BTN TWY N AND TWY MB NOT STD\n◼ TAXIWAY"
    },
    {
        "index": 14,
        "id": "A6730/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "05AUG26 09:44 - 31DEC26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "05AUG26 09:44 - 31DEC26 23:00 KJFK A6730/26\nE) TWY K IN PAVEMENT RWY GUARD LGT AT RWY 13R/31L U/S"
    },
    {
        "index": 15,
        "id": "A6654/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "03AUG26 10:00 - 15AUG26 03:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "03AUG26 10:00 - 15AUG26 03:00 KJFK A6654/26\nE) TWY E BTN APCH END RWY 22R AND TWY Y CLSD"
    },
    {
        "index": 16,
        "id": "A6146/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "10JUL26 13:45 - 30OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "10JUL26 13:45 - 30OCT26 23:00 KJFK A6146/26\nE) TWY PB LGT BTN TWY P AND TWY Q U/S"
    },
    {
        "index": 17,
        "id": "A6145/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "10JUL26 13:44 - 30OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "10JUL26 13:44 - 30OCT26 23:00 KJFK A6145/26\nE) TWY PA LGT BTN TWY P AND TWY Q U/S"
    },
    {
        "index": 18,
        "id": "A6144/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "10JUL26 13:42 - 30OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "10JUL26 13:42 - 30OCT26 23:00 KJFK A6144/26\nE) TWY Q2 LGT U/S"
    },
    {
        "index": 19,
        "id": "A6140/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "10JUL26 13:11 - 30OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "10JUL26 13:11 - 30OCT26 23:00 KJFK A6140/26\nE) TWY Q1 LGT U/S"
    },
    {
        "index": 20,
        "id": "A6136/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "10JUL26 13:03 - 30OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "10JUL26 13:03 - 30OCT26 23:00 KJFK A6136/26\nE) TWY Q LGT BTN HANGAR 19 RAMP AND TWY PF U/S"
    },
    {
        "index": 21,
        "id": "A6132/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "10JUL26 12:52 - 30OCT26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "10JUL26 12:52 - 30OCT26 23:00 KJFK A6132/26\nE) TWY KE LGT BTN RWY 13R/31L AND TWY A U/S"
    },
    {
        "index": 22,
        "id": "A5877/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "26JUN26 14:30 - UFN",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "26JUN26 14:30 - UFN KJFK A5877/26\nE) TWY VV CLSD"
    },
    {
        "index": 23,
        "id": "A5839/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "26JUN26 12:01 - UFN",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "26JUN26 12:01 - UFN KJFK A5839/26\nE) TWY LA BTN TWY A AND TWY B COMMISSIONED ASPH NOT LGTD"
    },
    {
        "index": 24,
        "id": "A5838/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "26JUN26 04:01 - UFN",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "26JUN26 04:01 - UFN KJFK A5838/26\nE) TWY A14 BTN TWY A AND TWY B COMMISSIONED ASPH NOT LGTD\nCOMMENT) TWY A14 IS NEW TWY BTN M AND LA (NOT IN JPSN CHRT)"
    },
    {
        "index": 25,
        "id": "A5837/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "26JUN26 04:01 - UFN",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "26JUN26 04:01 - UFN KJFK A5837/26\nE) TWY LA BTN TERMINAL 1 RAMP AND TWY A CHANGED TO TWY A14\nASPH NOT\nLGTD\nCOMMENT) TWY A14 IS NEW TWY BTN M AND LA (NOT IN JPSN CHRT)"
    },
    {
        "index": 26,
        "id": "A5792/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "24JUN26 14:28 - 31DEC26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "24JUN26 14:28 - 31DEC26 23:00 KJFK A5792/26\nE) TWY KG CLR BAR LGT AT TERMINAL 4 RAMP U/S"
    },
    {
        "index": 27,
        "id": "A5525/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "11JUN26 18:09 - UFN",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "11JUN26 18:09 - UFN KJFK A5525/26\nE) TWY LL COMMISSIONED BTN TWY A AND TWY B ASPH NOT LGTD\nCOMMENT) TWY LL LOCATED BTN TWY L AND TWY KG"
    },
    {
        "index": 28,
        "id": "A5482/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "10JUN26 17:32 - UFN",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10JUN26 17:32 - UFN KJFK A5482/26\nE) TWY L BTN TWY A AND TWY B CLSD\nPage 28"
    },
    {
        "index": 29,
        "id": "A5026/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "20MAY26 08:25 - 31DEC26 23:00",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "20MAY26 08:25 - 31DEC26 23:00 KJFK A5026/26\nE) TWY KF TWY DIRECTION SIGN FOR TERMINAL 4 RAMP MISSING"
    },
    {
        "index": 30,
        "id": "A4724/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "08MAY26 09:44 - 31OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "08MAY26 09:44 - 31OCT26 23:00 KJFK A4724/26\nE) TWY KF TWY DIRECTION SIGN FOR TWY A LGT U/S"
    },
    {
        "index": 31,
        "id": "A4532/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "29APR26 18:49 - 31OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "29APR26 18:49 - 31OCT26 23:00 KJFK A4532/26\nE) TWY Q SIGNS BTN HANGAR 19 RAMP AND TWY N LGT U/S"
    },
    {
        "index": 32,
        "id": "A4512/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "29APR26 12:32 - 31OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "29APR26 12:32 - 31OCT26 23:00 KJFK A4512/26\nE) TWY KG TWY DIRECTION SIGN FOR TWY A LGT U/S"
    },
    {
        "index": 33,
        "id": "A4373/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "24APR26 09:43 - 30SEP26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "24APR26 09:43 - 30SEP26 23:00 KJFK A4373/26\nE) TWY J LGT BTN TWY B AND TWY A U/S"
    },
    {
        "index": 34,
        "id": "A4306/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "22APR26 10:10 - 30SEP26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "22APR26 10:10 - 30SEP26 23:00 KJFK A4306/26\nE) TWY B TWY DIRECTION SIGN SOUTH SIDE FOR TWY EA LGT U/S"
    },
    {
        "index": 35,
        "id": "A3912/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "06APR26 16:08 - 30OCT26 19:00",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "06APR26 16:08 - 30OCT26 19:00 KJFK A3912/26\nE) JFK TWY A4 BTN TWY A AND TERMINAL 5 RAMP CLSD"
    },
    {
        "index": 36,
        "id": "A2350/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "18FEB26 21:18 - 31DEC27 23:59",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "18FEB26 21:18 - 31DEC27 23:59 KJFK A2350/26\nE) JFK TWY VA BTN TERMINAL 7 RAMP AND TWY A CLSD"
    },
    {
        "index": 37,
        "id": "A0398/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "08JAN26 15:36 - 31DEC26 23:00",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "08JAN26 15:36 - 31DEC26 23:00 KJFK A0398/26\nE) JFK TWY TB BTN TERMINAL 8 RAMP AND TWY A CLSD"
    },
    {
        "index": 38,
        "id": "A9155/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "10DEC25 19:44 - UFN",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10DEC25 19:44 - UFN KJFK A9155/25\nE) JFK TWY PB BTN HANGAR 12 RAMP AND TWY Q CLSD"
    },
    {
        "index": 39,
        "id": "A8968/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "03DEC25 16:20 - 31DEC26 23:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "03DEC25 16:20 - 31DEC26 23:00 KJFK A8968/25\nE) JFK TWY Z BTN RWY 04L/22R AND TWY Y CLSD"
    },
    {
        "index": 40,
        "id": "A8688/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "19NOV25 21:00 - UFN",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "19NOV25 21:00 - UFN KJFK A8688/25\nE) JFK TWY KG BTN TWY A AND TWY B CLSD\n◼ TAXIWAY LIGHT"
    },
    {
        "index": 41,
        "id": "A6609/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "31JUL26 07:49 - 30NOV26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "31JUL26 07:49 - 30NOV26 23:00 KJFK A6609/26\nE) TWY Y CL LGT BTN TWY FB AND TWY E U/S"
    },
    {
        "index": 42,
        "id": "A6608/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "31JUL26 07:44 - 30NOV26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "31JUL26 07:44 - 30NOV26 23:00 KJFK A6608/26\nE) TWY E CL LGT BTN APCH END RWY 22R AND TWY Y U/S"
    },
    {
        "index": 43,
        "id": "A5938/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "29JUN26 12:55 - 31DEC26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "29JUN26 12:55 - 31DEC26 23:00 KJFK A5938/26\nE) TWY KD BTN RWY 13R/31L AND TWY A LGT U/S"
    },
    {
        "index": 44,
        "id": "A5937/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "29JUN26 12:53 - 31DEC26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "29JUN26 12:53 - 31DEC26 23:00 KJFK A5937/26\nE) TWY Q5 LGT U/S"
    },
    {
        "index": 45,
        "id": "A5799/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "24JUN26 15:21 - 31DEC26 23:59",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "24JUN26 15:21 - 31DEC26 23:59 KJFK A5799/26\nE) TWY L CL LGT BTN RWY 13R/31L AND TWY A U/S"
    },
    {
        "index": 46,
        "id": "A5173/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "27MAY26 03:45 - 04DEC26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "27MAY26 03:45 - 04DEC26 23:00 KJFK A5173/26\nE) TWY G CL LGT BTN TWY B AND RWY 04L/22R U/S\nPage 29"
    },
    {
        "index": 47,
        "id": "A4535/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "29APR26 19:05 - 11NOV26 23:59",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "29APR26 19:05 - 11NOV26 23:59 KJFK A4535/26\nE) TWY B CL LGT BTN TWY J AND TWY MA U/S"
    },
    {
        "index": 48,
        "id": "A4368/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "24APR26 06:49 - 30SEP26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "24APR26 06:49 - 30SEP26 23:00 KJFK A4368/26\nE) TWY D CL LGT BTN RWY 13L/31R AND TWY A U/S"
    },
    {
        "index": 49,
        "id": "A4145/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "15APR26 15:51 - 31DEC26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "15APR26 15:51 - 31DEC26 23:00 KJFK A4145/26\nE) JFK TWY B CL LGT BTN TWY M AND TWY MB NOT STD"
    },
    {
        "index": 50,
        "id": "A4139/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "15APR26 08:31 - 31OCT26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "15APR26 08:31 - 31OCT26 23:00 KJFK A4139/26\nE) JFK TWY YA CL LGT BTN TWY B AND TWY ZA U/S"
    },
    {
        "index": 51,
        "id": "A3964/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "07APR26 21:39 - 31AUG27 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "07APR26 21:39 - 31AUG27 23:00 KJFK A3964/26\nE) JFK TWY E CL LGT BTN TWY B AND TWY YA NOT STD"
    },
    {
        "index": 52,
        "id": "A8975/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "03DEC25 16:30 - 31DEC26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "03DEC25 16:30 - 31DEC26 23:00 KJFK A8975/25\nE) JFK TWY A CL LGT BTN TWY M AND TWY MA NOT STD"
    },
    {
        "index": 53,
        "id": "A8974/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "03DEC25 16:25 - 31DEC26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "03DEC25 16:25 - 31DEC26 23:00 KJFK A8974/25\nE) JFK TWY H CL LGT BTN TWY Y AND TWY Z NOT STD\n◼ RAMP"
    },
    {
        "index": 54,
        "id": "A5072/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "21MAY26 18:23 - 30APR27 23:59",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "21MAY26 18:23 - 30APR27 23:59 KJFK A5072/26\nE) APRON TERMINAL 5 RAMP WIP CONST ADJ NW SIDE BARRICADED"
    },
    {
        "index": 55,
        "id": "A5070/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "21MAY26 18:10 - 30APR27 23:59",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "21MAY26 18:10 - 30APR27 23:59 KJFK A5070/26\nE) APRON TERMINAL 7 RAMP WIP CONST ADJ SE SIDE LGTD AND\nBARRICADED"
    },
    {
        "index": 56,
        "id": "A4509/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "18JUN25 03:34 - 05SEP26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "18JUN25 03:34 - 05SEP26 23:00 KJFK A4509/25\nE) JFK APRON TERMINAL 1 RAMP WIP CONST LGTD AND BARRICADED\n◼ NAVAID"
    },
    {
        "index": 57,
        "id": "A3778/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "31MAR26 08:57 - 30SEP26 20:00",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "31MAR26 08:57 - 30SEP26 20:00 KJFK A3778/26\nE) /HTO/ NAV VOR U/S\n◼ DEPARTURE"
    },
    {
        "index": 58,
        "id": "A6769/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "07AUG26 01:01 - 06SEP26 01:01",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 01:01 - 06SEP26 01:01 KJFK A6769/26\nE) SID JOHN F KENNEDY INTL, NEW YORK, NY. KENNEDY FIVE\nDEPARTURE...\nBREEZY POINT CLIMB, CANARSIE CLIMB, GATEWAY CLIMB, IDLEWILD\nCLIMB: NA\nEXCEPT FOR AIRCRAFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH\nGPS, JFK\nDME OUT OF SERVICE."
    },
    {
        "index": 59,
        "id": "A2290/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "17FEB26 14:23 - 29SEP26 14:23",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "17FEB26 14:23 - 29SEP26 14:23 KJFK A2290/26\nE) JFK SID JOHN F KENNEDY INTL, NEW YORK, NY.\nKENNEDY FIVE DEPARTURE...\nNOTE: COATE DEPARTURES NA EXCEPT FOR AIRCRAFT EQUIPPED WITH\nSUITABLE RNAV SYSTEM WITH GPS,\nSAX VORTAC OUT OF SERVICE.\n◼ APPROACH"
    },
    {
        "index": 60,
        "id": "A6768/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "07AUG26 01:01 - 06SEP26 01:01",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 01:01 - 06SEP26 01:01 KJFK A6768/26\nPage 30\nE) IAP JOHN F KENNEDY INTL, NEW YORK, NY. ILS OR LOC RWY 31L,\nAMDT\n11B... VOR RWY 31L, ORIG-B... VOR RWY 4R, ORIG-B... VDP NA,\nJFK DME\nOUT OF SERVICE."
    },
    {
        "index": 61,
        "id": "A6516/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "27JUL26 21:10 - 08MAR27 21:10",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27JUL26 21:10 - 08MAR27 21:10 KJFK A6516/26\nE) ODP JOHN F KENNEDY INTL, NEW YORK, NY. TAKEOFF MINIMUMS AND\n(OBSTACLE) DEPARTURE PROCEDURES AMDT 9A... ADD TAKEOFF\nOBSTACLE NOTE:\nRWY 31R, TEMPORARY CRANE 4276FT FROM DER, 1540FT LEFT OF\nCENTERLINE,\n125FT AGL/138FT MSL (2024-AEA-5111-NRA). ADD TAKEOFF OBSTACLE\nNOTE:\nRWY 4L, TEMPORARY CONSTRUCTION EQUIPMENT 563FT FROM DER, 218FT\nRIGHT\nOF CENTERLINE, 45FT AGL/60FT MSL (2022-AEA-1418-NRA). TEMPORARY\nCONSTRUCTION EQUIPMENT 1055FT FROM DER, 121FT RIGHT OF\nCENTERLINE,\n45FT AGL/57FT MSL (2022-AEA-1421-NRA)."
    },
    {
        "index": 62,
        "id": "A6514/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "27JUL26 20:45 - 08MAR27 20:45",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27JUL26 20:45 - 08MAR27 20:45 KJFK A6514/26\nE) IAP JOHN F KENNEDY INTL, NEW YORK, NY. RNAV (GPS) RWY 31L,\nAMDT\n2C... LPV DA 297/HAT 284 ALL CATS. VISIBILITY ALL CATS RVR\n4500.\nEXCEPT WHEN ADVISED BY ATCT THAT THIS CRANE IS DOWN. TEMPORARY\nCRANE\n256FT MSL 4985FT NORTHWEST OF RWY 31L (2023-AEA-5122-NRA).\nTEMPORARY\nCRANE 180FT MSL 4798FT NORTHWEST OF RWY 31L (2023-AEA-5112-\nNRA).\nTEMPORARY CRANE 197FT MSL 5432 NORTHWEST OF RWY 31L\n(2023-AEA-5132-NRA). TEMPORARY CRANE 247FT MSL 5512FT\nNORTHWEST OF\nRWY 31L (2023-AEA-5108-NRA). TEMPORARY CRANE 247FT MSL 4995FT\nNORTHWEST OF RWY 31L (2023-AEA-5107-NRA). TEMPORARY CRANE\n302FT MSL\n4238FT NORTHWEST OF RWY 31L (2023-AEA-475-NRA). TEMPORARY\nCRANE 256FT\nMSL 1.02NM NORTHWEST OF RWY 31L (2023-AEA-2934-NRA). TEMPORARY\nCRANE\n256FT MSL 1.03NM NORTHWEST OF RWY 31L (2023-AEA-2935-NRA)."
    },
    {
        "index": 63,
        "id": "A6513/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "27JUL26 20:45 - 08MAR27 20:45",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27JUL26 20:45 - 08MAR27 20:45 KJFK A6513/26\nE) IAP JOHN F KENNEDY INTL, NEW YORK, NY. ILS OR LOC RWY 31L,\nAMDT\n11B... S-ILS 31L DA 304/HAT 291 ALL CATS. VISIBILITY ALL CATS\nRVR\n4500. S-LOC 31L MDA 480/HAT 467 ALL CATS. VISIBILITY CATS C/D\n1 3/8.\nVDP AT JFK VOR/DME 0.87 DME? DISTANCE VDP TO THLD 1.23NM.\nEXCEPT WHEN\nADVISED BY ATCT THAT THIS CRANE IS DOWN. TEMPORARY CRANE 256FT\nMSL\n4985FT NORTHWEST OF RWY 31L (2023-AEA-5122-NRA). TEMPORARY\nCRANE\nPage 31\n180FT MSL 4798FT NORTHWEST OF RWY 31L (2023-AEA-5112-NRA).\nTEMPORARY\nCRANE 197FT MSL 5432 NORTHWEST OF RWY 31L (2023-AEA-5132-NRA).\nTEMPORARY CRANE 247FT MSL 5512FT NORTHWEST OF RWY 31L\n(2023-AEA-5108-NRA). TEMPORARY CRANE 247FT MSL 4995FT\nNORTHWEST OF\nRWY 31L (2023-AEA-5107-NRA). TEMPORARY CRANE 302FT MSL 4238FT\nNORTHWEST OF RWY 31L (2023-AEA-475-NRA). TEMPORARY CRANE 256FT\nMSL\n1.02NM NORTHWEST OF RWY 31L (2023-AEA-2934-NRA). TEMPORARY\nCRANE\n256FT MSL 1.03NM NORTHWEST OF RWY 31L (2023-AEA-2935-NRA)."
    },
    {
        "index": 64,
        "id": "A5946/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "29JUN26 16:56 - 29JUN28 16:56",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "29JUN26 16:56 - 29JUN28 16:56 KJFK A5946/26\nE) IAP JOHN F KENNEDY INTL, NEW YORK, NY. VOR RWY 4R, ORIG-\nB... S-4R\nCAT C VISIBILITY RVR 5500. NOTE: FOR INOPERATIVE ALS, INCREASE\nS-4R\nCAT D VISIBILITY TO 1 1/2 SM."
    },
    {
        "index": 65,
        "id": "A5540/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "12JUN26 13:24 - 24DEC26 09:01",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "12JUN26 13:24 - 24DEC26 09:01 KJFK A5540/26\nE) IAP JOHN F KENNEDY INTL, NEW YORK, NY. VOR RWY 4R, ORIG-C...\nPROCEDURE NA."
    },
    {
        "index": 66,
        "id": "A4843/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "13MAY26 16:30 - 31AUG26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "13MAY26 16:30 - 31AUG26 23:59 KJFK A4843/26\nE) NAV ILS RWY 22L IM U/S"
    },
    {
        "index": 67,
        "id": "A4842/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "13MAY26 16:30 - 31AUG26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "13MAY26 16:30 - 31AUG26 23:59 KJFK A4842/26\nE) NAV ILS RWY 04R IM U/S"
    },
    {
        "index": 68,
        "id": "A2296/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "17FEB26 16:33 - 05OCT27 16:33",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "17FEB26 16:33 - 05OCT27 16:33 KJFK A2296/26\nE) JFK IAP JOHN F KENNEDY INTL, NEW YORK, NY.\nCOPTER RNAV (GPS) 027, ORIG-C...\nLNAV MDA 680/HAS 647. NUMEROUS OFFSHORE TEMPORARY BARGE\nCRANES/WIND\nTURBINES 345FT MSL 10NM SOUTHWEST OF JFK AIRPORT (2024-WTE-4148\nTHRU 4149-OE, 2024-WTE-4196 THRU 4197-OE, 2024-WTE-4236 THRU\n4344-OE)."
    },
    {
        "index": 69,
        "id": "A2086/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "12FEB26 14:13 - 24SEP26 14:13",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "12FEB26 14:13 - 24SEP26 14:13 KJFK A2086/26\nE) JFK IAP JOHN F KENNEDY INTL, NEW YORK, NY.\nILS OR LOC RWY 31R, AMDT 16B...\nS-ILS 31R DA 217/HAT 204 ALL CATS.\nS-LOC 31R MDA 460/HAT 447 ALL CATS. VISIBILITY  CATS C/D RVR\n4500.\nVDP AT I-RTH 0.87 DME? DISTANCE VDP TO THLD 1.23 NM.\nEXCEPT WHEN ADVISED BY ATCT THAT THESE CRANES ARE DOWN.\nTEMPORARY CRANES 261 MSL 4630 FT W OF RWY 31R (2023-AEA-2063\nTHRU\n2068-NRA)..\nCOMMENT) NO IMPACT ON TAKEOFF PERFORMANCE"
    },
    {
        "index": 70,
        "id": "A2085/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "12FEB26 14:14 - 24SEP26 14:14",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "12FEB26 14:14 - 24SEP26 14:14 KJFK A2085/26\nE) JFK IAP JOHN F KENNEDY INTL, NEW YORK, NY.\nILS RWY 13L (CAT II) AMDT 18D ...\nPROCEDURE NA.\nEXCEPT WHEN ADVISED BY ATCT THAT THESE CRANES ARE DOWN.\nPage 32\nTEMPORARY CRANES 261 MSL 3037 FT SE OF RWY 13L (2023-AEA-2063\nTHRU\n2068-NRA).\nCOMMENT) NO IMPACT ON TAKEOFF PERFORMANCE"
    },
    {
        "index": 71,
        "id": "A2084/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "12FEB26 14:13 - 24SEP26 14:13",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "12FEB26 14:13 - 24SEP26 14:13 KJFK A2084/26\nE) JFK IAP JOHN F KENNEDY INTL, NEW YORK, NY.\nILS OR LOC  RWY 13L, AMDT 18D...\nS-ILS 13L DA 278/HAT 265 ALL CATS. VISIBILITY ALL CATS RVR\n2000.\nUXHUB FIX MINIMUMS:\nS-LOC 13L MDA 460/HAT 447 ALL CATS. VISIBILITY CATS C/D RVR\n4500.\nVDP AT I-TLK 2.86 DME? DISTANCE VDP TO THLD 1.17 NM.\nEXCEPT WHEN ADVISED BY ATCT THAT THESE CRANES ARE DOWN.\nTEMPORARY CRANES 261 MSL 3037 FT SE OF RWY 13L (2023-AEA-2063\nTHRU\n2068-NRA).\nCOMMENT) NO IMPACT ON TAKEOFF PERFORMANCE"
    },
    {
        "index": 72,
        "id": "A2083/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "12FEB26 14:12 - 24SEP26 14:12",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "12FEB26 14:12 - 24SEP26 14:12 KJFK A2083/26\nE) JFK IAP JOHN F KENNEDY INTL, NEW YORK, NY.\nRNAV (GPS) RWY 31R, AMDT 2D...\nLPV DA 218/HAT 205 ALL CATS.\nEXCEPT WHEN ADVISED BY ATCT THAT THESE CRANES ARE DOWN.\nTEMPORARY CRANES 261 MSL 4630 FT W OF RWY 31R (2023-AEA-2063\nTHRU\n2068-NRA).\nCOMMENT) NO IMPACT ON TAKEOFF PERFORMANCE"
    },
    {
        "index": 73,
        "id": "A7708/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "21OCT25 14:21 - 21OCT27 14:21",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "21OCT25 14:21 - 21OCT27 14:21 KJFK A7708/25\nE) JFK IAP JOHN F KENNEDY INTL, NEW YORK, NY.\nILS OR LOC RWY 4L, AMDT 11E...\nCHANGE NOTE: AUTOPILOT COUPLED APPROACH NA BELOW 200 FEET MSL\nTO\nREAD AUTOPILOT COUPLED APPROACH NA BELOW 500 MSL."
    },
    {
        "index": 74,
        "id": "A7069/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "29SEP25 20:49 - 26DEC27 20:48",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "29SEP25 20:49 - 26DEC27 20:48 KJFK A7069/25\nE) JFK IAP JOHN F KENNEDY INTL, NEW YORK, NY.\nILS OR LOC RWY 22L, AMDT 26...\nILS OR LOC RWY 22R, AMDT 4...\nILS OR LOC RWY 31L, AMDT 11B...\nILS OR LOC RWY 31R, AMDT 16B...\nILS OR LOC RWY 4R, AMDT 30B...\nRNAV (GPS) RWY 22R, AMDT 1G...\nRNAV (GPS) X RWY 22L, ORIG-A...\nRNAV (GPS) Y RWY 22L, AMDT 1F...\nRNAV (GPS) Y RWY 4L, AMDT 3B...\nRNAV (GPS) Y RWY 4R, AMDT 2B...\nVOR RWY 31L, ORIG-B...\nVOR RWY 4R, ORIG-B...\nCIRCLING MDA CATS C/D 700/HAA 687. VISIBILITY CAT C 2, CAT D 2\n1/4."
    },
    {
        "index": 75,
        "id": "A5023/25",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "05JUL25 22:28 - 05JUL27 22:28",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "05JUL25 22:28 - 05JUL27 22:28 KJFK A5023/25\nE) JFK IAP JOHN F KENNEDY INTL, NEW YORK, NY.\nILS OR LOC RWY 22R, AMDT 4...\nPage 33\nS-LOC 22R MDA 580/HAT 567 ALL CATS. VISIBILITY CAT C/D 1 5/8.\nPERMANENT BUILDING 266FT MSL 4.7NM NORTH OF RWY 22R\n(2024-AEA-9867-OE).\n◼ OBSTRUCTION"
    },
    {
        "index": 76,
        "id": "A5284/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "01JUN26 13:38 - 03SEP26 23:59",
        "category": "COM / RADAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "01JUN26 13:38 - 03SEP26 23:59 KJFK A5284/26\nE) OBST CRANE (ASN 2022-AEA-1423-NRA) 403907N0734542W (1.1NM\nNE JFK)\n56FT (45FT AGL) FLAGGED AND LGTD\nCOMMENT) REF TO TECH INFO"
    },
    {
        "index": 77,
        "id": "A5283/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "01JUN26 13:36 - 03SEP26 23:59",
        "category": "COM / RADAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "01JUN26 13:36 - 03SEP26 23:59 KJFK A5283/26\nE) OBST CRANE (ASN 2022-AEA-1418-NRA) 403906N0734542W (1.1NM\nNE JFK)\n60FT (45FT AGL) FLAGGED AND LGTD\nCOMMENT) REF TO TECH INFO"
    },
    {
        "index": 78,
        "id": "A0947/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "21JAN26 19:40 - 03SEP26 18:00",
        "category": "COM / RADAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "21JAN26 19:40 - 03SEP26 18:00 KJFK A0947/26\nE) JFK OBST CRANE (ASN 2022-AEA-1421-NRA) 403910N0734540W\n(1.1NM NE\nJFK) 57FT (45FT AGL) FLAGGED AND LGTD\nCOMMENT) REF TO TECH INFO\n◼ GPS"
    },
    {
        "index": 79,
        "id": "J1287/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "09AUG26 16:00 - 12AUG26 16:00",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 16:00 - 12AUG26 16:00 KJFK J1287/26\nE)  GPS RAIM OUTAGES PREDICTED FOR RNP-0.3 AS FLW\n   NO GPS OUTAGES PREDICTED)\n◼ OTHER"
    },
    {
        "index": 80,
        "id": "A5028/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "20MAY26 08:30 - 31DEC26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "20MAY26 08:30 - 31DEC26 23:00 KJFK A5028/26\nE) TWY K LGT BTN RWY 13R/31L AND TWY A U/S"
    },
    {
        "index": 81,
        "id": "A4504/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "29APR26 09:12 - 31OCT26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "29APR26 09:12 - 31OCT26 23:00 KJFK A4504/26\nE) RWY 13R LEAD OFF LGT AT TWY M U/S"
    },
    {
        "index": 82,
        "id": "A4370/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "24APR26 09:22 - 30SEP26 23:00",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24APR26 09:22 - 30SEP26 23:00 KJFK A4370/26\nE) TWY B TWY DIRECTION SIGN EAST SIDE FOR TWY J MISSING"
    },
    {
        "index": 83,
        "id": "A4366/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "24APR26 05:52 - 30SEP26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "24APR26 05:52 - 30SEP26 23:00 KJFK A4366/26\nE) TWY A TWY DIRECTION SIGN SOUTH SIDE FOR TWY EA LGT U/S"
    },
    {
        "index": 84,
        "id": "A4365/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "24APR26 05:49 - 30SEP26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "24APR26 05:49 - 30SEP26 23:00 KJFK A4365/26\nE) TWY DB TWY DIRECTION SIGN FOR TWY B LGT U/S"
    },
    {
        "index": 85,
        "id": "A3853/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "02APR26 07:00 - 31AUG26 23:59",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "02APR26 07:00 - 31AUG26 23:59 KJFK A3853/26\nE) JFK RWY 31L LEAD ON LGT AT TWY K U/S"
    },
    {
        "index": 86,
        "id": "A3852/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "02APR26 06:53 - 31AUG26 23:59",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "02APR26 06:53 - 31AUG26 23:59 KJFK A3852/26\nE) JFK RWY 13R LEAD OFF LGT AT TWY K U/S"
    },
    {
        "index": 87,
        "id": "A3641/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "25MAR26 08:09 - 05SEP26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "25MAR26 08:09 - 05SEP26 23:00 KJFK A3641/26\nE) JFK TWY KF LGT BTN TERMINAL 4 RAMP AND TWY B U/S"
    },
    {
        "index": 88,
        "id": "A3637/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "25MAR26 07:36 - 05SEP26 23:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "25MAR26 07:36 - 05SEP26 23:00 KJFK A3637/26\nPage 34\nE) JFK TWY HB LGT BTN TERMINAL 4 RAMP AND TWY B U/S"
    },
    {
        "index": 89,
        "id": "A3489/26",
        "station": "KJFK",
        "airportName": "뉴욕 존 F. 케네디 국제공항 (목적지)",
        "validPeriod": "18MAR26 21:40 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "18MAR26 21:40 - UFN KJFK A3489/26\nE) JFK SVC AUTOMATED WX BCST SYSTEM CHANGED TO 347-588-1609\n[ALTN]KBOS/ BOS/ Boston Edward L Logan Intl Airport, Boston, US\n1. RUNWAY : 15R/33L : 10083FT X 150FT 04R/22L : 10006FT X 150FT\n04L/22R : 7864FT X 150FT 09/27 : 7001FT X 150FT\n◼ RUNWAY"
    },
    {
        "index": 90,
        "id": "A5772/26",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "21APR26 04:01 - 30OCT26 03:59",
        "category": "GENERAL",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "일반항공(GA)/헬리포트/드론 전용 (상업 정기 여객편 비적용)",
        "rawText": "21APR26 04:01 - 30OCT26 03:59 KBOS A5772/26\nE) BOS AD AP CLSD TO NON-SKED TRANSIENT GA ACFT EXC 24HR\nPPR 617-561-2500"
    },
    {
        "index": 91,
        "id": "A0654/26",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "10AUG26 01:15 - 15AUG26 12:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 01:15 - 15AUG26 12:00 KBOS A0654/26\nE) RWY 14/32 CLSD EXC TAX 30MIN PPR 617-561-1919\nCOMMENT)   14 / 32 : 5000FT"
    },
    {
        "index": 92,
        "id": "A0649/26",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "09AUG26 17:52 - 16AUG26 12:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 17:52 - 16AUG26 12:00 KBOS A0649/26\nE) RWY 15L/33R CLSD EXC TAX 30MIN PPR 131.1\n◼ DEPARTURE"
    },
    {
        "index": 93,
        "id": "A9800/25",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "08OCT25 14:05 - 08OCT27 14:05",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "08OCT25 14:05 - 08OCT27 14:05 KBOS A9800/25\nE) BOS ODP GENERAL EDWARD LAWRENCE LOGAN\nINTL, BOSTON, MA.\nTAKEOFF MINIMUMS AND (OBSTACLE) DEPARTURE PROCEDURES AMDT 15...\nNOTE: RWY 04L IN ADDITION TO EXISTING TAKEOFF OBSTACLE NOTES,\nADD:\nTREE 3930 FT FROM DER, 1367 FT LEFT OF CENTERLINE, 172 FT MSL.\nTREES, SMOKESTACKS, POLES, BUILDINGS, TRAVERSE WAY BEGINNING\n3972\nFT FROM DER, 476 FT LEFT OF CENTERLINE, UP TO 74 FT AGL/198 FT\nMSL.\nTREES, POLE BEGINNING 4344 FT FROM DER, 1034 FT LEFT OF\nCENTERLINE,\nUP TO 202 FT MSL. TREES, POLE, BUILDING BEGINNING 4386 FT FROM\nDER,\n755 FT LEFT OF CENTERLINE, UP TO 183 FT MSL."
    },
    {
        "index": 94,
        "id": "A3012/25",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "05MAR25 21:58 - 05MAR27 21:58",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "05MAR25 21:58 - 05MAR27 21:58 KBOS A3012/25\nE) BOS ODP GENERAL EDWARD LAWRENCE LOGAN\nINTL, BOSTON, MA.\nDIVERSE VECTOR AREA (RADAR VECTORS), ORIG ...\nRWY 22R, REQUIRES MINIMUM CLIMB OF 406 FT PER NM TO 1000. ALL\nOTHER\nDATA REMAINS AS PUBLISHED"
    },
    {
        "index": 95,
        "id": "A0917/25",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "13NOV25 19:14 - 13NOV27 19:14",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "13NOV25 19:14 - 13NOV27 19:14 KBOS A0917/25\nE) BOS SID GENERAL EDWARD LAWRENCE LOGAN\nINTL, BOSTON, MA.\nLOGAN FOUR DEPARTURE...\nTAKEOFF MINIMUMS: RWY 33L: CHANGE TO READ: STANDARD WITH\nMINIMUM\nCLIMB OF 300 FT/NM TO 1200. ALL OTHER DATA REMAINS AS\nPUBLISHED..\nPage 35\n◼ APPROACH"
    },
    {
        "index": 96,
        "id": "A0380/25",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "24OCT25 14:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24OCT25 14:00 - UFN KBOS A0380/25\nE) BOS STAR GENERAL EDWARD LAWRENCE LOGAN INTL, BOSTON, MA.\nROBUC THREE ARRIVAL...\nMERIT ROUTE INCREASE MOCA FROM ALWIN TO ROBUC 1900 TO 2100,\nWINDMILL AT 1002 OBS"
    },
    {
        "index": 97,
        "id": "A0379/25",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "24OCT25 14:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24OCT25 14:00 - UFN KBOS A0379/25\nE) BOS STAR GENERAL EDWARD LAWRENCE LOGAN INTL, BOSTON, MA.\nROBUC THREE ARRIVAL...\nKENNEDY ROUTE INCREASE MOCA FROM ALWIN TO ROBUC 1900 TO 2100,\nWINDMILL AT 1002 OBS"
    },
    {
        "index": 98,
        "id": "A0375/25",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "24OCT25 14:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24OCT25 14:00 - UFN KBOS A0375/25\nE) BOS STAR GENERAL EDWARD LAWRENCE LOGAN INTL, BOSTON, MA.\nROBUC THREE ARRIVAL...\nRUIZE ROUTE INCREASE MOCA FROM ALWIN TO ROBUC 1900 TO 2100,\nWINDMILL AT 1002 OBS"
    },
    {
        "index": 99,
        "id": "A0372/25",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "30OCT25 15:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30OCT25 15:00 - UFN KBOS A0372/25\nE) BOS STAR GENERAL EDWARD LAWRENCE LOGAN INTL, BOSTON, MA.\nOOSHN FIVE ARRIVAL...\nRIFLE ROUTE INCREASE MOCA FROM CUTOX TO CUJKE 1200 TO 1900,\nWINDMILL AT 873 OBS (25-077159\n◼ GPS"
    },
    {
        "index": 100,
        "id": "J1287/26",
        "station": "KBOS",
        "airportName": "보스턴 로건 국제공항 (교체공항)",
        "validPeriod": "09AUG26 16:00 - 12AUG26 16:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 16:00 - 12AUG26 16:00 KBOS J1287/26\nE)  GPS RAIM OUTAGES PREDICTED FOR RNP-0.3 AS FLW\n   NO GPS OUTAGES PREDICTED)\nEND OF PACKAGE 1 FOR OZ 224 ICN/JFK .\nPage 36\nOZ 224 ICN/JFK PRINTED AT 10AUG26 0726Z\nETP: RJCC   PANC   KORD\n3% ERA: KORD\nERA: RKSI   RKPC   RJAA   RJBB   RJGG   ROAH   RORS   RJAW  \nRJTT   RJCC   PASY   PADK   PACD   PAKN   PAFA   CYXY   CYZF  \nCYEG   CYYC   CYWG   CYYQ   CYXE   KDLH   CYYZ   KBOS   KJFK\n[ETP]RJCC/ CTS/ Sapporo New Chitose Airport, Sapporo, JP\n1. RUNWAY : 01L/19R : 9843FT X 197FT 01R/19L : 9843FT X 197FT\n2. COMPANY RADIO : 132.05 CHITOSE ANA OPERATION\n◼ COMPANY ADVISORY"
    },
    {
        "index": 101,
        "id": "COAD01/24",
        "station": "RJCC",
        "airportName": "삿포로 신치토세 공항 (ETP/ERA)",
        "validPeriod": "26JUN24 15:00 - UFN",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 26JUN24 15:00 - UFN RJCC COAD01/24\n- FREQUENCY : 132.05MHZ\n- PLEASE SET 132.05MHZ DURING PREPARATION ON THE GROUND\n-- BY NRTKKW--"
    },
    {
        "index": 102,
        "id": "COAD01/21",
        "station": "RJCC",
        "airportName": "삿포로 신치토세 공항 (ETP/ERA)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 14JAN21 00:00 - UFN RJCC COAD01/21\n** DE/ANTI-ICING CURRENT STATE OF FLUIDS **\nFLUID : TYPE 1 (SAFEWING MP I ECO PLUS(80))\n        TYPE 4 (KILFROST ABC-S PLUS)\nWORKING TYPE : 2 STEP\n-- BY --\n◼ RUNWAY"
    },
    {
        "index": 103,
        "id": "C2096/26",
        "station": "RJCC",
        "airportName": "삿포로 신치토세 공항 (ETP/ERA)",
        "validPeriod": "07AUG26 15:00 - 16AUG26 15:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 15:00 - 16AUG26 15:00 RJCC C2096/26\nE) TEMPO OPS WILL APPLY AS FLW\nRWY01L OR RWY01R PREFERRED WHEN TAILWIND COMPONENT IS LESS\nTHAN 10KT.\nRMK:\n(1) OPS MAY BE SUSPENDED FOR OPR REASONS.\n(2) PILOTS SHOULD NOTIFY ATC IF UNA TO COMPLY.\n(3) CONTACT INFORMATION:\nOPERATIONAL FOUNDATION DIVISION, BUREAU OF DEFENSE POLICY,\nMINISTRY\nOF DEFENSE JAPAN\n03-3268-3111\n[ETP]PANC/ ANC/ Anchorage Ted Stevens Intl Airport, Anchorage,\nUS\n1. RUNWAY : 07R/25L : 12400FT X 200FT 15/33 : 10960FT X 200FT\n07L/25R : 10865FT X 150FT\n◼ COMPANY ADVISORY"
    },
    {
        "index": 104,
        "id": "COAD01/21",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "1. 14JAN21 00:00 - UFN PANC COAD01/21\n** DE/ANTI-ICING CURRENT STATE OF FLUIDS **\nFLUID TYPE : TYPE 1(UCAR-PG-ADF, DOW CHEMICAL COMPANY), TYPE\nPage 37\n4(UCAR FLIGHTGUARD AD-49, DOW CHEMICAL COMPANY)\nWORKING TYPE : 2STEP\n-- BY SELOC--"
    },
    {
        "index": 105,
        "id": "COAD02/21",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "COMPANY ADVISORY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 14JAN21 00:00 - UFN PANC COAD02/21\nCONTACT POINT\nOFFICE : TEL 1-907-243-3100\n-- BY JFKKKW--"
    },
    {
        "index": 106,
        "id": "COAD03/21",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "18FEB21 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "3. 18FEB21 00:00 - UFN PANC COAD03/21\nAIRCRAFT LARGER THAN WING SPAN 196FT MUST BE TOWED TO THE GATE\n-- BY SELKI--\n◼ RUNWAY"
    },
    {
        "index": 107,
        "id": "A4914/26",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "10AUG26 15:00 - 10AUG26 23:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 15:00 - 10AUG26 23:00 PANC A4914/26\nE) RWY 07L/25R CLSD EXC XNG\nCOMMENT) CODE F A/C USING RWY\n◼ APPROACH"
    },
    {
        "index": 108,
        "id": "A4832/26",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "10AUG26 15:30 - 10AUG26 23:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 15:30 - 10AUG26 23:00 PANC A4832/26\nE) ANC ILS RWY 07L LOC/GP/DME U/S"
    },
    {
        "index": 109,
        "id": "A4802/26",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "04AUG26 14:23 - 31AUG26 15:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "04AUG26 14:23 - 31AUG26 15:00 PANC A4802/26\nE) RWY 15 PAPI U/S"
    },
    {
        "index": 110,
        "id": "A4415/26",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "09JUL26 12:05 - 30SEP27 12:05",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 12:05 - 30SEP27 12:05 PANC A4415/26\nE) IAP TED STEVENS ANCHORAGE INTL, ANCHORAGE, AK. ILS OR LOC\nRWY 7R,\nAMDT 5A... ILS RWY 7R (SA CAT I), AMDT 5A... ILS RWY 7R (CAT\nII-III),\nAMDT 5A ... MISSED APPROACH: CLIMB TO 780 THEN CLIMBING RIGHT\nTURN TO\n3000 ON HEADING 230 AND ON TED VOR/DME R-210 TO JUKEP/TED\n15.00 DME\nAND HOLD. (TACAN AIRCRAFT CLIMB TO 780 THEN CLIMBING RIGHT\nTURN TO\n3000 ON HEADING 230 AND EDF TACAN R-213 TO JUKEP/EDF 22.63\nDME AND\nHOLD?HOLDING, NE, RT, 212.63 INBOUND)."
    },
    {
        "index": 111,
        "id": "A4414/26",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "09JUL26 12:04 - 30SEP27 12:03",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 12:04 - 30SEP27 12:03 PANC A4414/26\nE) IAP TED STEVENS ANCHORAGE INTL, ANCHORAGE, AK. ILS OR LOC\nRWY 7L,\nAMDT 5A... ILS RWY 7L (SA CAT I-II), AMDT 5A ... MISSED\nAPPROACH:\nCLIMB TO 600 THEN CLIMBING RIGHT TURN TO 3000 ON HEADING 230\nAND TED\nVOR/DME R-210 TO JUKEP/TED 15.00 DME AND HOLD. (TACAN\nAIRCRAFT CLIMB\nTO 600 THEN CLIMBING RIGHT TURN TO 3000 ON HEADING 230 AND\nEDF TACAN\nR-213 TO JUKEP/EDF 22.63 DME AND HOLD? HOLDING, NE JUKEP/EDF\n22.63\nDME, RT, 212.63 INBOUND)."
    },
    {
        "index": 112,
        "id": "A4413/26",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "09JUL26 12:02 - 30SEP27 12:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 12:02 - 30SEP27 12:00 PANC A4413/26\nPage 38\nE) IAP TED STEVENS ANCHORAGE INTL, ANCHORAGE, AK. ILS OR LOC\nRWY 7L,\nAMDT 5A... MISSED APPROACH: CLIMB TO 600 THEN CLIMBING RIGHT\nTURN TO\n3000 ON HEADING 230 AND TED VOR/DME R-210 TO JUKEP/TED 15.00\nDME AND\nHOLD. (TACAN AIRCRAFT CLIMB TO 600 THEN CLIMBING RIGHT TURN\nTO 3000\nON HEADING 230 AND EDF TACAN R-213 TO JUKEP/EDF 22.63 DME AND\nHOLD?\nHOLDING, NE JUKEP/EDF 22.63 DME, RT, 212.63 INBOUND)."
    },
    {
        "index": 113,
        "id": "A4412/26",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "09JUL26 12:02 - 30SEP27 12:02",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 12:02 - 30SEP27 12:02 PANC A4412/26\nE) IAP TED STEVENS ANCHORAGE INTL, ANCHORAGE, AK. ILS OR LOC\nRWY 7R,\nAMDT 5A... MISSED APPROACH: CLIMB TO 780 THEN CLIMBING RIGHT\nTURN TO\n3000 ON HEADING 230 AND ON TED VOR/DME R-210 TO JUKEP/TED\n15.00 DME\nAND HOLD. (TACAN AIRCRAFT CLIMB TO 780 THEN CLIMBING RIGHT\nTURN TO\n3000 ON HEADING 230 AND EDF TACAN R-213 TO JUKEP/EDF 22.63\nDME AND\nHOLD?HOLDING, NE, RT, 212.63 INBOUND."
    },
    {
        "index": 114,
        "id": "A4189/25",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "28OCT25 14:09 - 28OCT27 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "28OCT25 14:09 - 28OCT27 23:59 PANC A4189/25\nE) ANC IAP TED STEVENS ANCHORAGE INTL,\nANCHORAGE, AK.\nRNAV (GPS) RWY 7L, AMDT 3...\nLNAV MDA 620/HAT 492 ALL CATS."
    },
    {
        "index": 115,
        "id": "A4133/25",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "22OCT25 14:55 - 22OCT27 14:54",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22OCT25 14:55 - 22OCT27 14:54 PANC A4133/25\nE) ANC IAP TED STEVENS ANCHORAGE INTL,\nANCHORAGE, AK.\nRNAV (GPS) Y RWY 7R, AMDT 5...\nLPV DA 369/HAT 237 ALL CATS."
    },
    {
        "index": 116,
        "id": "A4115/25",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "20OCT25 18:49 - 20OCT27 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "20OCT25 18:49 - 20OCT27 23:59 PANC A4115/25\nE) ANC IAP TED STEVENS ANCHORAGE INTL,\nANCHORAGE, AK.\nRNAV (GPS) RWY 15, AMDT 3...\nLNAV/VNAV MDA 406/HAT 255 ALL CATS."
    },
    {
        "index": 117,
        "id": "A4082/25",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "15OCT25 13:04 - 15OCT27 13:04",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "15OCT25 13:04 - 15OCT27 13:04 PANC A4082/25\nE) ANC IAP TED STEVENS ANCHORAGE INTL,\nANCHORAGE, AK.\nRNAV (RNP) RWY 33, AMDT 1A...\nRNP 0.11 DA 465/HAT 344 ALL CATS. RNP 0.20 DA 542/HAT 421 ALL\nCATS,\nVISIBILITY ALL CATS 1 1/4.."
    },
    {
        "index": 118,
        "id": "A3981/25",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "02OCT25 09:01 - 02OCT26 09:01",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02OCT25 09:01 - 02OCT26 09:01 PANC A3981/25\nE) ANC STAR TED STEVENS ANCHORAGE INTL, ANCHORAGE,\nAK..TAGER NINE ARRIVAL..MC GRATH TRANSITION (MCG.TAGER9) NOT\nAUTH\nEXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nMCG VOR R-102 UNUSABLE BEYOND 20NM.\nPage 39"
    },
    {
        "index": 119,
        "id": "A3975/25",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "29SEP25 16:22 - 30SEP27 16:22",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "29SEP25 16:22 - 30SEP27 16:22 PANC A3975/25\nE) ANC IAP TED STEVENS ANCHORAGE INTL,\nANCHORAGE, AK.\nILS OR LOC RWY 7L, AMDT 5...\nS-LOC 7L VISIBILITY CATS C/D/E RVR 3500.\n◼ APPROACH LIGHT"
    },
    {
        "index": 120,
        "id": "A4778/26",
        "station": "PANC",
        "airportName": "앵커리지 테드 스티븐스 국제공항 (ETP/ERA)",
        "validPeriod": "31JUL26 19:05 - 03OCT26 15:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "31JUL26 19:05 - 03OCT26 15:00 PANC A4778/26\nE) RWY 15 SEQUENCED FLG LGT U/S\n[ETP]KORD/ ORD/ Chicago O`Hare International Airport, Chicago,\nUS\n1. RUNWAY : 10L/28R : 13000FT X 150FT 09R/27L : 11260FT X 150FT\n09C/27C : 11245FT X 200FT 10C/28C : 10800FT X 200FT\n04R/22L : 8075FT X 150FT\n2. COMPANY RADIO : 131.40MHZ SUNLINE OPS\n◼ COMPANY ADVISORY"
    },
    {
        "index": 121,
        "id": "COAD01/20",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "01MAY20 00:00 - UFN",
        "category": "COMPANY ADVISORY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 01MAY20 00:00 - UFN KORD COAD01/20\n** DE/ANTI-ICING FLUIDS FOR PAX/CGO FLTS **\nTYPE 1 (CRYOTECH POLAR PLUS LT)\nTYPE 4 (CRYOTECH POLAR GUARD EXTEND)\nWORKING TYPE : 2 STEP\n-- BY JFKKKW--"
    },
    {
        "index": 122,
        "id": "COAD02/20",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "01MAY20 16:01 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 01MAY20 16:01 - UFN KORD COAD02/20\nNIGHT TIME (2201-0559L) AIRPORT OPERATION INFO\nATC CONTACT : 121.9MHZ FOR CLEARANCE DELIVERY, METERING, GROUND\nRMK : RAMP IS AN UNCONTROLLED AREA AND PUSH-BACK IS AT YOUR OWN\nRISK (AT YOUR DISCRETION)\n-- BY JFKKKW--\n◼ RUNWAY"
    },
    {
        "index": 123,
        "id": "A7007/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "10AUG26 05:52 - 11AUG26 05:52",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 05:52 - 11AUG26 05:52 KORD A7007/26\nE) RWY 04R FICON 5/5/5 100 PCT WET OBS AT 2608100552."
    },
    {
        "index": 124,
        "id": "A7002/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "10AUG26 05:09 - 10AUG26 11:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 05:09 - 10AUG26 11:30 KORD A7002/26\nE) RWY 10C/28C CLSD\nCOMMENT) CODE F A/C USING RWY"
    },
    {
        "index": 125,
        "id": "A6995/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "10AUG26 04:18 - 10AUG26 11:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 04:18 - 10AUG26 11:30 KORD A6995/26\nE) RWY 09L/27R CLSD"
    },
    {
        "index": 126,
        "id": "A6993/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "10AUG26 04:06 - 11AUG26 04:06",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 04:06 - 11AUG26 04:06 KORD A6993/26\nE) RWY 10L FICON 5/5/5 100 PCT WET OBS AT 2608100406."
    },
    {
        "index": 127,
        "id": "A6990/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "10AUG26 04:05 - 11AUG26 04:05",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 04:05 - 11AUG26 04:05 KORD A6990/26\nE) RWY 09R FICON 5/5/5 100 PCT WET OBS AT 2608100405."
    },
    {
        "index": 128,
        "id": "A6985/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "10AUG26 03:42 - 10AUG26 11:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 03:42 - 10AUG26 11:30 KORD A6985/26\nE) RWY 10R/28L CLSD"
    },
    {
        "index": 129,
        "id": "A6505/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "03AUG26 07:34 - 05SEP26 11:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "03AUG26 07:34 - 05SEP26 11:00 KORD A6505/26\nE) RWY 09R/27L SAFETY AREA IRREGULAR SFC N SIDE BTN TWY M AND\nPage 40\nTWY TT"
    },
    {
        "index": 130,
        "id": "A6364/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "31JUL26 16:09 - 30SEP26 16:00",
        "category": "OBSTACLE / CRANE",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "원거리 장애물/크레인 (비행경로 보호구역 외곽)",
        "rawText": "31JUL26 16:09 - 30SEP26 16:00 KORD A6364/26\nE) AD AP BIRD ACT INCREASED GEESE AND CRANES"
    },
    {
        "index": 131,
        "id": "A0010/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "01JAN26 01:59 - 11SEP26 23:59",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "01JAN26 01:59 - 11SEP26 23:59 KORD A0010/26\nE) ORD RWY 28R TKOF HOLD LGT AT ARRAY 2 U/S\n◼ APPROACH"
    },
    {
        "index": 132,
        "id": "A8777/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "27APR26 22:08 - 09NOV26 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27APR26 22:08 - 09NOV26 23:55 KORD A8777/26\nE) IAP CHICAGO O'HARE INTL, CHICAGO, IL. RNAV (GPS) RWY 4R,\nAMDT\n1D... LNAV/VNAV DA 1056/HAT 395 ALL CATS, VISIBILITY RVR 3500\nALL\nCATS. LNAV MDA 1160/HAT 499 ALL CATS, VDP 1.35 NM TO RW04R.\nFOR\nINOPERATIVE ALS, INCREASE LNAV CATS C/D VISIBILITY TO 1 3/8.\nTEMPORARY CRANE 845 MSL, 4873FT W OF RWY 4R\n(2024-AGL-15027/15028/15029-NRA). TEMPORARY CRANE 822 MSL\n7342FT SW\nOF 10R (2025-AGL-8827-OE). TEMPORARY CRANE 788 MSL, 5934FT SW\nOF RWY\n4R (2024-AGL-13315-OE). TEMPORARY CRANE 841 MSL 5090FT SW OF\nRWY 4R\n(2024-AGL-15026-15033-NRA)."
    },
    {
        "index": 133,
        "id": "A6997/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "11AUG26 03:00 - 11AUG26 09:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "11AUG26 03:00 - 11AUG26 09:00 KORD A6997/26\nE) NAV ILS RWY 27C U/S"
    },
    {
        "index": 134,
        "id": "A6983/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "10AUG26 23:00 - 11AUG26 05:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 23:00 - 11AUG26 05:00 KORD A6983/26\nE) NAV ILS RWY 10R DME U/S"
    },
    {
        "index": 135,
        "id": "A6962/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "09AUG26 17:36 - 16AUG26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 17:36 - 16AUG26 23:59 KORD A6962/26\nE) RWY 27L PAPI UNUSABLE"
    },
    {
        "index": 136,
        "id": "A6476/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "30MAR26 12:18 - 09NOV26 12:18",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30MAR26 12:18 - 09NOV26 12:18 KORD A6476/26\nE) ORD IAP CHICAGO O'HARE INTL, CHICAGO, IL.\nRNAV (GPS) RWY 9L, AMDT 4...\nLNAV/VNAV DA 1100/HAT 432 ALL CATS, VIS ALL CATS RVR 4000.\nEXCEPT\nWHEN ADVISED BY ATCT THAT THIS CRANE IS DOWN. TEMPORARY CRANE\n840\nMSL, 6911 FT W OF RWY 9L (2025-AGL-3331-OE)."
    },
    {
        "index": 137,
        "id": "A5950/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "27JUL26 20:53 - 08MAR27 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27JUL26 20:53 - 08MAR27 23:55 KORD A5950/26\nE) IAP CHICAGO O'HARE INTL, CHICAGO, IL. RNAV (GPS) Y RWY 10R,\nORIG-B... LNAV MDA 1160/HAT 480 ALL CATS, VIS CAT C/D RVR\n5000. VDP\nNA. FOR INOP ALS, INCREASE LNAV/VNAV ALL CATS VISIBILITY AND\nLNAV\nCATS C/D VISIBILITY TO 1 3/8 SM. TEMPORARY CRANES, UP TO 846\nMSL,\n1808FT SE OF RWY 10R (2024-AGL-15036 THRU 15042-NRA)."
    },
    {
        "index": 138,
        "id": "A5435/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "22JUL26 11:00 - 13AUG26 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22JUL26 11:00 - 13AUG26 23:55 KORD A5435/26\nE) ODP CHICAGO O'HARE INTL, CHICAGO, IL. TAKEOFF MINIMUMS AND\nPage 41\n(OBSTACLE) DEPARTURE PROCEDURES AMDT 23... TAKEOFF OBSTACLE\nNOTES:\nRWY 9C, TEMPORARY CRANE, 3280FT FROM DER, 633FT LEFT OF\nCENTERLINE,\n115 AGL/749 MSL, (2025-AGL-7270-OE). EXCEPT WHEN ADVISED BY\nATCT THAT\nTHIS CRANE IS DOWN. ALL OTHER DATA REMAINS AS PUBLISHED."
    },
    {
        "index": 139,
        "id": "A5363/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "19JUL26 22:56 - 15AUG26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "19JUL26 22:56 - 15AUG26 23:59 KORD A5363/26\nE) ORD ILS RWY 28L GP U/S"
    },
    {
        "index": 140,
        "id": "A5362/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "19JUL26 22:55 - 15AUG26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "19JUL26 22:55 - 15AUG26 23:59 KORD A5362/26\nE) ORD ILS RWY 28L CAT II/III NA"
    },
    {
        "index": 141,
        "id": "A4646/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "09JUL26 19:12 - 09NOV26 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 19:12 - 09NOV26 23:55 KORD A4646/26\nE) IAP CHICAGO O'HARE INTL, CHICAGO, IL. ILS Z OR LOC Z RWY\n10R,\nORIG-C... S-ILS 10R DA 945/HAT 265 ALL CATS. VIS RVR 2000 ALL\nCATS.\nTEMPORARY CRANES, UP TO 846 MSL, 1808FT SE OF RWY 10R (2024-\nAGL-15026\nTHRU 15039-NRA)."
    },
    {
        "index": 142,
        "id": "A4645/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "09JUL26 19:07 - 09NOV26 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 19:07 - 09NOV26 23:55 KORD A4645/26\nE) IAP CHICAGO O'HARE INTL, CHICAGO, IL. ILS Z RWY 10R (SA\nCAT I),\nORIG-C ... ILS Z RWY 10R (SA CAT II AND III), ORIG-C ...\nPROCEDURE\nNA. TEMPORARY CRANES, UP TO 846 MSL, 1808FT SE OF RWY 10R\n(2024-AGL-15026 THRU 15039-NRA"
    },
    {
        "index": 143,
        "id": "A4627/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "09JUL26 13:18 - 18FEB27 13:18",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 13:18 - 18FEB27 13:18 KORD A4627/26\nE) IAP CHICAGO O'HARE INTL, CHICAGO, IL. ILS RWY 9C (CAT II-\nIII),\nAMDT ORIG-B ... NOTE: OYG ILS LLZ RWY 9C UNUSABLE FOR ROLLOUT\nGUIDANCE."
    },
    {
        "index": 144,
        "id": "A4566/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "04MAR26 12:53 - 24OCT27 21:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "04MAR26 12:53 - 24OCT27 21:11 KORD A4566/26\nE) ORD NAV ILS RWY 27R IM U/S"
    },
    {
        "index": 145,
        "id": "A2754/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "15JUN26 19:27 - 22NOV27 21:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "15JUN26 19:27 - 22NOV27 21:11 KORD A2754/26\nE) NAV ILS RWY 27C IM U/S"
    },
    {
        "index": 146,
        "id": "A1704/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "01JUN26 19:33 - 31DEC26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01JUN26 19:33 - 31DEC26 23:59 KORD A1704/26\nE) NAV ILS RWY 28L IM U/S"
    },
    {
        "index": 147,
        "id": "A1622/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "22JAN26 14:44 - 31DEC26 21:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22JAN26 14:44 - 31DEC26 21:11 KORD A1622/26\nE) ORD NAV ILS RWY 28R IM U/S"
    },
    {
        "index": 148,
        "id": "A1621/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "22JAN26 14:43 - 31DEC26 21:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22JAN26 14:43 - 31DEC26 21:11 KORD A1621/26\nE) ORD NAV ILS RWY 28C IM U/S"
    },
    {
        "index": 149,
        "id": "A1619/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "22JAN26 14:42 - 31DEC26 21:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22JAN26 14:42 - 31DEC26 21:11 KORD A1619/26\nE) ORD NAV ILS RWY 27L IM U/S"
    },
    {
        "index": 150,
        "id": "A1613/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "22JAN26 12:51 - 30DEC26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22JAN26 12:51 - 30DEC26 23:59 KORD A1613/26\nPage 42\nE) ORD NAV ILS RWY 10R(Z) IM U/S"
    },
    {
        "index": 151,
        "id": "A1611/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "22JAN26 12:45 - 30DEC26 21:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22JAN26 12:45 - 30DEC26 21:11 KORD A1611/26\nE) ORD NAV ILS RWY 10L IM U/S"
    },
    {
        "index": 152,
        "id": "A0194/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "14MAY26 12:53 - 14MAY28 12:53",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14MAY26 12:53 - 14MAY28 12:53 KORD A0194/26\nE) IAP CHICAGO O'HARE INTL, CHICAGO, IL. RNAV (GPS) RWY 9L,\nAMDT 4...\nPROFILE NOTE: VGSI AND RNAV GLIDEPATH NOT COINCIDENT (VGSI\nANGLE\n3.00/TCH 69)."
    },
    {
        "index": 153,
        "id": "A0193/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "14MAY26 12:53 - 14MAY28 12:53",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14MAY26 12:53 - 14MAY28 12:53 KORD A0193/26\nE) IAP CHICAGO O'HARE INTL, CHICAGO, IL. RNAV (GPS) RWY 4R,\nAMDT\n1D... PROFILE NOTE: VGSI AND RNAV GLIDEPATH NOT COINCIDENT\n(VGSI\nANGLE 3.00/TCH 67)."
    },
    {
        "index": 154,
        "id": "A0192/26",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "14MAY26 12:53 - 14MAY28 12:53",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14MAY26 12:53 - 14MAY28 12:53 KORD A0192/26\nE) IAP CHICAGO O'HARE INTL, CHICAGO, IL. ILS OR LOC RWY 9L,\nAMDT\n4B... ILS RWY 9L SA CAT I, AMDT 4B... ILS RWY 9L CAT II/III,\nAMDT\n4B... PROFILE NOTE: VGSI AND ILS GLIDEPATH NOT COINCIDENT\n(VGSI ANGLE\n3.00/TCH 69)."
    },
    {
        "index": 155,
        "id": "A8816/25",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "30DEC25 13:07 - 31DEC26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30DEC25 13:07 - 31DEC26 23:59 KORD A8816/25\nE) ORD NAV ILS RWY 10C IM U/S"
    },
    {
        "index": 156,
        "id": "A8813/25",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "30DEC25 12:33 - 31DEC26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30DEC25 12:33 - 31DEC26 23:59 KORD A8813/25\nE) ORD NAV ILS RWY 09C IM U/S"
    },
    {
        "index": 157,
        "id": "A8811/25",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "30DEC25 12:20 - 31DEC26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30DEC25 12:20 - 31DEC26 23:59 KORD A8811/25\nE) ORD NAV ILS RWY 09L IM U/S"
    },
    {
        "index": 158,
        "id": "A8810/25",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "30DEC25 12:17 - 31DEC26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30DEC25 12:17 - 31DEC26 23:59 KORD A8810/25\nE) ORD RWY 09L PAPI U/S"
    },
    {
        "index": 159,
        "id": "A8809/25",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "30DEC25 12:15 - 31DEC26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30DEC25 12:15 - 31DEC26 23:59 KORD A8809/25\nE) ORD RWY 27R PAPI U/S"
    },
    {
        "index": 160,
        "id": "A8434/25",
        "station": "KORD",
        "airportName": "시카고 오헤어 국제공항 (3% ERA)",
        "validPeriod": "22DEC25 14:44 - 31DEC26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22DEC25 14:44 - 31DEC26 23:59 KORD A8434/25\nE) ORD NAV ILS RWY 09R IM U/S\n[3% ERA]KORD/ ORD/ Chicago O`Hare International Airport,\nChicago, US\nSEE THE SAME AIRPORT IN PACKAGE 2\n[ERA]RKSI/ ICN/ Seoul Incheon International Airport, Seoul, KR\nSEE THE SAME AIRPORT IN PACKAGE 1\n[ERA]RKPC/ CJU/ Jeju Intl., Jeju, KR\n1. RUNWAY : 07/25 : 10433FT X 148FT 13/31 : 6234FT X 148FT\nPage 43\n2. COMPANY RADIO : 129.85 ASIANA JEJU\n◼ COMPANY ADVISORY"
    },
    {
        "index": 161,
        "id": "COAD01/26",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "01MAR26 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 01MAR26 00:00 - UFN RKPC COAD01/26\nCERTIFIED A/C TYPE : A350\nCERTIFIED APPROACHES :  RNP Z RWY 07 (AR), RNP Z RWY 25 (AR)\n-- BY SELOO--"
    },
    {
        "index": 162,
        "id": "COAD01/25",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "05FEB25 00:00 - 30DEC26 00:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 05FEB25 00:00 - 30DEC26 00:00 RKPC COAD01/25\nAIP SUP 109/25\nA H-BEAM STRUCTURE EXISTS UNDER LOC ANTENNA 305 METERS FROM END OF\nRWY 07\n-- BY SELOP--"
    },
    {
        "index": 163,
        "id": "COAD02/25",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "01AUG25 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "3. 01AUG25 00:00 - UFN RKPC COAD02/25\nRWY 31 OPS : AVBL A321 ONLY\n1)RWY 31 TKOF : WHEN DEP RWY25 AND 31 ON ATIS\n2)RWY 13 TKOF : NOT AVBL\n3)RWY 31 LDG : NOT AVBL\n4)RWY 13 LDG : NOT AVBL\n-- BY CJUKKW--"
    },
    {
        "index": 164,
        "id": "COAD03/25",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "01AUG25 00:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "4. 01AUG25 00:00 - UFN RKPC COAD03/25\nCHANGES TO CJUOC OPERATIONS (25.8.1~)\n1)CONTACT DETAILS\n- PHONE : +82-64-800-6676\n- E-MAIL : AACJUOC@FLYASIANA.COM\n2)KEY CHANGES\n- STAFFING : 1 PERSONNEL\n- OPERATING HOURS : MON-FRA(0830-1730KST, DAY SHIFT ONLY)\nOPERATING HOURS ARE SUBJECT TO CHANGE WITHOUT PRIOR NOTICE.\n3)FLIGHT PLAN APPROVAL : HQ(OCC) : 0000-2359KST\n4)COMPANY RADIO\n\"ASIANA JEJU\" CONTINUES\nHQ(OCC) SUPPORTS DURING NON-WORKING HOURS\n5)SUPPORT FOR DOMESTIC AIRPORTS\nHQ(OCC) SUPPORTS DURING NON-OPERATING HOURS OF THE CJUOC.\n-- BY CJUOC--"
    },
    {
        "index": 165,
        "id": "COAD04/25",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "24DEC25 16:49 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "5. 24DEC25 16:49 - UFN RKPC COAD04/25\nCERTIFIED A/C TYPE : A321(HL8510, HL8534, HL8511, HL8533, HL8582)\nCERTIFIED APPROACHES : RNP Z RWY 07 (AR), RNP Z RWY 25 (AR)\n-- BY SELOO--"
    },
    {
        "index": 166,
        "id": "COAD01/20",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "01MAY20 00:00 - UFN",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "6. 01MAY20 00:00 - UFN RKPC COAD01/20\nPUSH BACK PROC IN CASE OF APU SHUT DOWN : ONE ENG START WITH ASU -\nPUSH BACK\n - TWO ENG START - TAXI (ST51-57,60-62,64,65)\n-- BY CJUKKW--"
    },
    {
        "index": 167,
        "id": "COAD01/18",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "07AUG18 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "7. 07AUG18 00:00 - UFN RKPC COAD01/18\nFLOCKS OF BIRDS VICINITY AIRPORT USE CAUTION WHEN LANDING AND DEP\n-- BY SELOP--\n◼ RUNWAY"
    },
    {
        "index": 168,
        "id": "A1100/26",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "06AUG26 14:00 - 02NOV26 21:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "06AUG26 14:00 - 02NOV26 21:00 RKPC A1100/26\nD) 1400-2100\nE) RWY 07/25 CLSD DUE TO WIP\nPage 44\nRMK:\n1. RWY 07/25 CLSD START TIMES MAY BE ADJUSTED AFTER THE END OF\nSKED FLT OPS\n2. 60MIN PN FOR NML OPS\n◼ APPROACH"
    },
    {
        "index": 169,
        "id": "Z0446/26",
        "station": "RKPC",
        "airportName": "제주국제공항 (ERA)",
        "validPeriod": "05AUG26 16:00 - 14APR27 16:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "05AUG26 16:00 - 14APR27 16:00 RKPC Z0446/26\nE) TRIGGER NOTAM - AIRAC AIP SUP 56/26 WEF 1600 UTC 5 AUG\n2026 TIL\n1600 UTC 14 APR 2027\n- THE ILS/DME FOR RWY 07 AT JEJU INTL AIRPORT WILL BE\nUNSERVICEABLE\nDUE TO REPLACEMENT.\nCOMMENT) 1) DURING THE PERIOD, FOLLOW PROC U/S  \n    • ILS Z or LOC Z RWY 07 CAT I & II\n    • ILS Y or LOC Y RWY 07 CAT I & II\n2) TAKE-OFF FROM RWY 07 WITH CERTIFIED TGS(TAKE-OFF GUIDANCE\nSYSTEM)\nNOT AVBL.\n3) TAKE-OFF FROM RWY 07 PROHIBITED IN VIS LESS THAN RVR 150M.\n[ERA]RJAA/ NRT/ Tokyo Narita Intl, Tokyo, JP\n1. RUNWAY : 16R/34L : 13123FT X 197FT 16L/34R : 8202FT X 197FT\n2. COMPANY RADIO : 130.55 ANA OPERATON\n◼ COMPANY ADVISORY"
    },
    {
        "index": 170,
        "id": "COAD01/26",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "06MAY26 00:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 06MAY26 00:00 - UFN RJAA COAD01/26\nPLZ PAY MORE ATTENTION TO ATC COMMUNICATION.\nCAUTION: SIMILAR CALL SIGNS (DURING APPROACH TO NRT)\nOZ102 (ICN-NRT) AND GK102 (CTS-NRT)\n-- BY SELOB--"
    },
    {
        "index": 171,
        "id": "COAD01/25",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "19AUG25 00:00 - UFN",
        "category": "COMPANY ADVISORY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 19AUG25 00:00 - UFN RJAA COAD01/25\nCURFEW INFO\nAD CURFEW : 1500-2100Z\nA330(MMTOW APPLIED) : 1400-2100Z\n-- BY NRTKKW--"
    },
    {
        "index": 172,
        "id": "COAD02/25",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "26NOV25 00:00 - 31DEC27 00:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "3. 26NOV25 00:00 - 31DEC27 00:00 RJAA COAD02/25\nRJAA AIP SUP 224/25\nTEMPO APCH PROC IN USE DUE TO CRANE. (AIP SUP 184/25 SUPERSEDED.)\n1) 13 FEB 2026 1500 UTC ~ 30 MAR 2026 1500 UTC\n- SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n- RNP RWY 34R LNAV MDA(H) CHANGED.\n- RNP RWY 16L LNAV/VNAV DA(H) AND LNAV MDA(H) CHANGED.\n2) 30 MAR 2026 1500 UTC ~ 5 AUG 2026 1500 UTC\n- SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n- RNP RWY 34R LNAV MDA(H) CHANGED.\n- RNP RWY 16L LNAV/VNAV DA(H) AND LNAV MDA(H) CHANGED.\n3) 5 AUG 2026 1500 UTC ~ 15 JUN 2027 1500 UTC\n- SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n- VOR RWY 34L MDA(H) AND RVR CHANGED.\n- RNP RWY 34R LNAV/VNAV DA(H), RVR AND LNAV MDA(H), RVR CHANGED.\n- VOR RWY 16R MDA(H) AND RVR CHANGED.\n- RNP RWY 16L LNAV/VNAV DA(H), RVR AND LNAV MDA(H), RVR CHANGED.\nPage 45\n4) 15 JUN 2027 1500 UTC ~ 31 DEC 2027 1500 UTC\n-SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n- ILS RWY 34L DA(H) AND RVR CHANGED.\n- LOC RWY 34L MDA(H) AND RVR CHANGED.\n- VOR RWY 34L MDA(H) AND RVR CHANGED.\n- RNP RWY 34R LNAV/VNAV DA(H), RVR AND LNAV MDA(H), RVR CHANGED.\n- VOR RWY 16R MDA(H) AND RVR CHANGED.\n- RNP RWY 16L LNAV/VNAV DA(H), RVR AND LNAV MDA(H), RVR CHANGED.\nCOMMENT) REFER TO JPSN CHART.\nREFER TO LATEST NOTAM FOR ANY CHANGE.\n-- BY SELOC--"
    },
    {
        "index": 173,
        "id": "COAD02/24",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "09SEP24 00:00 - UFN",
        "category": "COMPANY ADVISORY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "4. 09SEP24 00:00 - UFN RJAA COAD02/24\nFUEL ORDER PROCEDURE\n- FUEL ORDER PROCEDURE AT NRT\n- IF EXTRA FUEL IS NEEDED, PLEASE LET OCC KNOW IT VIA AVIATOR\n-- BY NRTOC--"
    },
    {
        "index": 174,
        "id": "COAD01/21",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "COMPANY ADVISORY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "5. 14JAN21 00:00 - UFN RJAA COAD01/21\n** DE/ANTI-ICING CURRENT STATE OF FLUIDS **\nFLUID : TYPE 1(KILFROST DF PLUS), TYPE 4(KILFROST ABC-S PLUS)\nWORKING TYPE : 2 STEP\n-- BY --"
    },
    {
        "index": 175,
        "id": "COAD01/20",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "01MAY20 16:01 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "6. 01MAY20 16:01 - UFN RJAA COAD01/20\nRWY USE INFO\n2100-1400Z : USE RWY INSTRUCTED BY ATC\n1400-1500Z : RWY 34L/16R ONLY AVAILABLE\n-- BY NRTKKW--\n◼ RUNWAY"
    },
    {
        "index": 176,
        "id": "A1179/26",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "31JUL26 20:20 - 30OCT26 20:20",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "31JUL26 20:20 - 30OCT26 20:20 RJAA A1179/26\nE) GROOVING FOR RWY 16R/34L PARTLY ERASED DUE TO CONST\nLEN: 25.0M (BTN 241.15M AND 266.15M FM RWY 16R THR)\nWID: 6.0M (BTN 2.0M AND 8.0M ON THE WEST SIDE OF RCL)"
    },
    {
        "index": 177,
        "id": "A1127/26",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "01AUG26 15:10 - 31AUG26 20:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 15:10 - 31AUG26 20:30 RJAA A1127/26\nD) 1510/2030\nE) RWY 16R/34L CLSD DUE TO MAINT\n1.EXC ACFT IN AIC051/19 ITEM3\n2.EXC EMERG ACFT WITH PRIOR PERMISSION AT LEAST 1HR BFR\nCOMMENT) CODE F A/C USING RWY"
    },
    {
        "index": 178,
        "id": "A1126/26",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "01AUG26 14:10 - 31AUG26 20:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:10 - 31AUG26 20:30 RJAA A1126/26\nD) 1410/2030\nE) RWY 16L/34R CLSD DUE TO MAINT\nCOMMENT) CODE F A/C USING RWY (B748)\n◼ RUNWAY LIGHT"
    },
    {
        "index": 179,
        "id": "A1095/26",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "08JUL26 15:00 - 06OCT26 15:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "08JUL26 15:00 - 06OCT26 15:00 RJAA A1095/26\nE) STOP-BAR-LGT FOR TWY B1 THRU B9 U/S\nRMK:(1)REF AIP SUP 165/26 ITEM TWY:5\n(2)THE EXACT TIME OF NEXT PERIOD WILL BE NOTIFIED BY FURTHER\nNOTAM"
    },
    {
        "index": 180,
        "id": "A1091/26",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "08JUL26 15:00 - 06OCT26 15:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "08JUL26 15:00 - 06OCT26 15:00 RJAA A1091/26\nPage 46\nE) FLW LGT U/S\nPALS FOR RWY 16L\nSEQUENCED-FLG-LGT FOR RWY 16L\nRMK:(1)REF AIP SUP 165/26 ITEM RWY:1,2\n(2)THE EXACT TIME OF NEXT PERIOD WILL BE NOTIFIED BY FURTHER\nNOTAM\n◼ APPROACH"
    },
    {
        "index": 181,
        "id": "AIP",
        "station": "RJAA",
        "airportName": "도쿄 나리타 국제공항 (ERA)",
        "validPeriod": "26NOV25 15:00 - 31DEC27 15:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "26NOV25 15:00 - 31DEC27 15:00 RJAA AIP SUP 224/25\nE) TEMPO APCH PROC IN USE DUE TO CRANE. (AIP SUP 184/25\nSUPERSEDED.)\n1) 26 NOV 2025 1500 UTC – 24 JAN 2026 1500 UTC\nREF JPSN 21-0A.\n• VOR RWY 34L MDA(H) CHANGED.\n• RNP RWY 16L LNAV MDA(H) CHANGED.\n2) 24 JAN 2026 1500 UTC – 13 FEB 2026 1500 UTC\nREF JPSN 21-0A, 21-0B, 21-0C, 21-0D.\n• SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n• VOR RWY 34L MDA(H) CHANGED.\n• RNP RWY 34R LNAV MDA(H) CHANGED.\n• RNP RWY 16L LNAV/VNAV DA(H) AND LNAV MDA(H) CHANGED.\n3) 13 FEB 2026 1500 UTC – 30 MAR 2026 1500 UTC\n• SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n• RNP RWY 34R LNAV MDA(H) CHANGED.\n• RNP RWY 16L LNAV/VNAV DA(H) AND LNAV MDA(H) CHANGED.\n4) 30 MAR 2026 1500 UTC – 5 AUG 2026 1500 UTC\n• SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n• RNP RWY 34R LNAV MDA(H) CHANGED.\n• RNP RWY 16L LNAV/VNAV DA(H) AND LNAV MDA(H) CHANGED.\n5) 5 AUG 2026 1500 UTC – 15 JUN 2027 1500 UTC\n• SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n• VOR RWY 34L MDA(H) AND RVR CHANGED.\n• RNP RWY 34R LNAV/VNAV DA(H), RVR AND LNAV MDA(H), RVR\nCHANGED.\n• VOR RWY 16R MDA(H) AND RVR CHANGED.\n• RNP RWY 16L LNAV/VNAV DA(H), RVR AND LNAV MDA(H), RVR\nCHANGED.\n6) 15 JUN 2027 1500 UTC – 31 DEC 2027 1500 UTC\n• SOME CIRCLING PROCEDURES MDA(H) CHANGED.\n• ILS RWY 34L DA(H) AND RVR CHANGED.\n• LOC RWY 34L MDA(H) AND RVR CHANGED.\n• VOR RWY 34L MDA(H) AND RVR CHANGED.\n• RNP RWY 34R LNAV/VNAV DA(H), RVR AND LNAV MDA(H), RVR\nCHANGED.\n• VOR RWY 16R MDA(H) AND RVR CHANGED.\n• RNP RWY 16L LNAV/VNAV DA(H), RVR AND LNAV MDA(H), RVR\nCHANGED.\nCOMMENT) REFER TO JPSN CHART.\nREFER TO LATEST NOTAM FOR ANY CHANGE.\n[ERA]RJBB/ KIX/ Osaka Kansai International Airport, Osaka, JP\nPage 47\n1. RUNWAY : 06L/24R : 13123FT X 197FT 06R/24L : 11483FT X 197FT\n2. COMPANY RADIO : 130.95 ALL NIPPON KANSAI OPS\n◼ COMPANY ADVISORY"
    },
    {
        "index": 182,
        "id": "COAD01/21",
        "station": "RJBB",
        "airportName": "오사카 간사이 국제공항 (ERA)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "COMPANY ADVISORY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 14JAN21 00:00 - UFN RJBB COAD01/21\n** DE/ANTI-ICING CURRENT STATE OF FLUIDS **\nFLUID : TYPE 1(KILFROST DF PLUS)\n        TYPE 4(KILFROST ABC-S PLUS)\nWORKING TYPE : 2 STEP\n-- BY --"
    },
    {
        "index": 183,
        "id": "COAD01/20",
        "station": "RJBB",
        "airportName": "오사카 간사이 국제공항 (ERA)",
        "validPeriod": "01MAY20 16:01 - UFN",
        "category": "COMPANY ADVISORY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 01MAY20 16:01 - UFN RJBB COAD01/20\nCONTACT POINT\nTEL : 81-72-456-7537\n-- BY NRTKKW--"
    },
    {
        "index": 184,
        "id": "COAD02/20",
        "station": "RJBB",
        "airportName": "오사카 간사이 국제공항 (ERA)",
        "validPeriod": "01MAY20 16:01 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "3. 01MAY20 16:01 - UFN RJBB COAD02/20\nILS Y RWY 24L APPROACH\nILS Y RWY 24L (JPSN 21-6) IS FOR NON-RNAV AIRCRAFT ONLY.\nRNAV CAPABLE AIRCRAFT SHOULD USE ILS Z RWY 24L WHEN APPROACHING\nRWY 24L BY ILS.\n-- BY NRTKKW--\n◼ RUNWAY"
    },
    {
        "index": 185,
        "id": "B2078/26",
        "station": "RJBB",
        "airportName": "오사카 간사이 국제공항 (ERA)",
        "validPeriod": "10AUG26 14:00 - 31AUG26 23:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 14:00 - 31AUG26 23:30 RJBB B2078/26\nD) 10 13 17 20 22-24 27 29-31 1400/2330\nE) RWY 06L/24R CLSD DUE TO MAINT"
    },
    {
        "index": 186,
        "id": "B1129/26",
        "station": "RJBB",
        "airportName": "오사카 간사이 국제공항 (ERA)",
        "validPeriod": "08JUL26 15:00 - 04AUG27 15:00",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "행정/AIP SUP 발효 고지 (차트 반영 완료)",
        "rawText": "08JUL26 15:00 - 04AUG27 15:00 RJBB B1129/26\nE) TRIGGER NOTAM-AIRAC AIP SUP 099/26\nWEF 09 JUL 2026 TIL 04 AUG 2027\nUNSERVICEABILITY OF KANSAI ILS-GP 06L AND KANSAI IM 06L\n◼ APPROACH"
    },
    {
        "index": 187,
        "id": "B0360/26",
        "station": "RJBB",
        "airportName": "오사카 간사이 국제공항 (ERA)",
        "validPeriod": "15APR26 15:00 - 29SEP27 15:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "행정/AIP SUP 발효 고지 (차트 반영 완료)",
        "rawText": "15APR26 15:00 - 29SEP27 15:00 RJBB B0360/26\nE) TRIGGER NOTAM-AIRAC AIP SUP 019/26\nWEF 16 APR 2026 TIL 29 SEP 2027\nUNSERVICEABILITY OF KANSAI ILS 24R(LOC,GP,DME) AND KANSAI IM\n24R\nCOMMENT) ILS 24R(LOC,DME) AND KANSAI IM 24R U/S\n(2026.04.15 1500 ~2026.11.25 1500)\nILS 24R GP U/S (2026.04.15 1500~2027.09.29 1500)\n[ERA]RJGG/ NGO/ Nagoya Chubu Centrair International Airport,\nNagoya, JP\n1. RUNWAY : 36/18 : 11483FT X 197FT\n2. COMPANY RADIO : 132.05 CENTRAIR OPERATION\n◼ COMPANY ADVISORY"
    },
    {
        "index": 188,
        "id": "COAD01/21",
        "station": "RJGG",
        "airportName": "나고야 츄부 국제공항 (ERA)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 14JAN21 00:00 - UFN RJGG COAD01/21\n** DE/ANTI-ICING CURRENT STATE OF FLUIDS **\nFLUID : TYPE 1(KILFROST DF PLUS)\n        TYPE 4(KILFROST ABC-S PLUS)\nWORKING TYPE : 2 STEP\n-- BY --\nPage 48\n◼ RUNWAY"
    },
    {
        "index": 189,
        "id": "G1913/26",
        "station": "RJGG",
        "airportName": "나고야 츄부 국제공항 (ERA)",
        "validPeriod": "10AUG26 17:50 - 10AUG26 20:10",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 17:50 - 10AUG26 20:10 RJGG G1913/26\nE) RWY 18/36 CLSD DUE TO MAINT\nEXC ACFT WITH PRIOR PERMISSION AT LEAST 1HR BFR\n◼ RUNWAY LIGHT"
    },
    {
        "index": 190,
        "id": "G1857/26",
        "station": "RJGG",
        "airportName": "나고야 츄부 국제공항 (ERA)",
        "validPeriod": "05AUG26 15:00 - 28OCT26 15:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "05AUG26 15:00 - 28OCT26 15:00 RJGG G1857/26\nE) STOP-BAR-LGT FOR A1 THRU A10 U/S\nRMK:(1)REF AIP SUP 182/26 ITEM TWY:3\n(2)THE EXACT TIME OF NEXT PERIOD WILL BE NOTIFIED BY FURTHER\nNOTAM\n◼ APPROACH"
    },
    {
        "index": 191,
        "id": "AIP",
        "station": "RJGG",
        "airportName": "나고야 츄부 국제공항 (ERA)",
        "validPeriod": "13MAY26 15:00 - 07MAR27 15:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "13MAY26 15:00 - 07MAR27 15:00 RJGG AIP SUP 102/26\nE) PERIOD: 2026.07.08 1500 UTC ~ 2027.03.07 1500 UTC\nILS MINIMA CHANGED DUE TO OBST.\n1. RWY 18 – ILS/LOC Z, ILS/LOC Y, ILS/LOC X\n  – CAT C: DA(H) 221'(206') / RVR 600M\n  – CAT D: DA(H) 231'(216') / RVR 600M\n2. RWY 36 – ILS/LOC Z, ILS/LOC Y:\n  – CAT C: DA(H) 221'(206') / RVR 600M\n  – CAT D: DA(H) 231'(216') / RVR 600M\nCOMMENT) REFER TO JPSN 21-0.\n[ERA]ROAH/ OKA/ Okinawa Naha Airport, Okinawa, JP\n1. RUNWAY : 18L/36R : 9843FT X 148FT 18R/36L : 8858FT X 197FT\n2. COMPANY RADIO : 132.05 ZENNIKU OKINAWA\n◼ COMPANY ADVISORY"
    },
    {
        "index": 192,
        "id": "COAD01/25",
        "station": "ROAH",
        "airportName": "오키나와 나하 공항 (ERA)",
        "validPeriod": "27AUG25 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 27AUG25 00:00 - UFN ROAH COAD01/25\nCONTACT POINT\nCO.RADIO : 132.05MHZ, CALLSIGN :ZENNIKU OKINAWA\n-- BY --\n◼ RUNWAY"
    },
    {
        "index": 193,
        "id": "H2867/26",
        "station": "ROAH",
        "airportName": "오키나와 나하 공항 (ERA)",
        "validPeriod": "03AUG26 14:00 - 31AUG26 21:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "03AUG26 14:00 - 31AUG26 21:30 ROAH H2867/26\nD) 03-07 10-14 17-21 24-28 31 1400/2130\nE) RWY 18L/36R CLSD DUE TO MAINT\n(1)AVBL CROSS RWY18L/36R VIA OTHER THAN CLSD TWY\n(2)EXC ACFT WITH PRIOR PERMISSION AT LEAST 1HR BFR"
    },
    {
        "index": 194,
        "id": "H2860/26",
        "station": "ROAH",
        "airportName": "오키나와 나하 공항 (ERA)",
        "validPeriod": "01AUG26 14:00 - 30AUG26 21:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:00 - 30AUG26 21:30 ROAH H2860/26\nD) 01-02 08-09 15-16 22-23 29-30 1400/2130\nE) RWY 18R/36L CLSD DUE TO MAINT\nEXC ACFT WITH PRIOR PERMISSION AT LEAST 1HR BFR\n◼ APPROACH"
    },
    {
        "index": 195,
        "id": "H2790/26",
        "station": "ROAH",
        "airportName": "오키나와 나하 공항 (ERA)",
        "validPeriod": "01AUG26 14:00 - 30AUG26 21:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:00 - 30AUG26 21:00 ROAH H2790/26\nD) 01-02 16 22-23 29-30 1400/2100\nE) ILS-LOC,GP,DME FOR RWY 18R U/S DUE TO CONST"
    },
    {
        "index": 196,
        "id": "H2789/26",
        "station": "ROAH",
        "airportName": "오키나와 나하 공항 (ERA)",
        "validPeriod": "01AUG26 14:00 - 30AUG26 21:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:00 - 30AUG26 21:00 ROAH H2789/26\nPage 49\nD) 01-02 16 22-23 29-30 1400/2100\nE) ILS-LOC,GP,DME FOR RWY 36L U/S DUE TO CONST"
    },
    {
        "index": 197,
        "id": "H2788/26",
        "station": "ROAH",
        "airportName": "오키나와 나하 공항 (ERA)",
        "validPeriod": "03AUG26 14:00 - 31AUG26 21:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "03AUG26 14:00 - 31AUG26 21:00 ROAH H2788/26\nD) 03-07 10-11 17-21 24-26 31 1400/2100\nE) ILS-LOC,GP,DME FOR RWY 36R U/S DUE TO CONST\n[ERA]RORS/ SHI/ Shimojishima, Shimojishima, JP\n1. RUNWAY : 17/35 : 9843FT X 197FT\n◼ RUNWAY"
    },
    {
        "index": 198,
        "id": "M1060/26",
        "station": "RORS",
        "airportName": "시모지시마 공항 (ERA)",
        "validPeriod": "02AUG26 23:00 - 30SEP26 10:30",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "02AUG26 23:00 - 30SEP26 10:30 RORS M1060/26\nE) GROOVING FOR RWY 17/35 PARTLY ERASED DUE TO CONST\nLEN: 250M (BTN 900M AND 1150M FM RWY 17 THR)\nWID: 40M (WITHIN AND EXTENDING UP TO 20M BOTH SIDE OF RCL)\n◼ RUNWAY LIGHT"
    },
    {
        "index": 199,
        "id": "M0792/26",
        "station": "RORS",
        "airportName": "시모지시마 공항 (ERA)",
        "validPeriod": "25MAY26 23:00 - 21AUG26 10:30",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "25MAY26 23:00 - 21AUG26 10:30 RORS M0792/26\nE) RCLL FOR RWY 17/35 U/S DUE TO CONST\n◼ APPROACH LIGHT"
    },
    {
        "index": 200,
        "id": "0064/26",
        "station": "RORS",
        "airportName": "시모지시마 공항 (ERA)",
        "validPeriod": "17JUL26 09:01 - 16SEP26 10:30",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "17JUL26 09:01 - 16SEP26 10:30 RORS 0064/26\nE) PALS FOR RWY 17 PARTLY U/S DUE TO TROUBLE\nRMK: LGT ARE TURNED ON ALTERNATELY\nAVBL APCH LGT LEN 900M"
    },
    {
        "index": 201,
        "id": "M1006/26",
        "station": "RORS",
        "airportName": "시모지시마 공항 (ERA)",
        "validPeriod": "17JUL26 09:01 - 16SEP26 10:30",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "17JUL26 09:01 - 16SEP26 10:30 RORS M1006/26\nE) PALS FOR RWY 17 PARTLY U/S DUE TO TROUBLE\nRMK: LGT ARE TURNED ON ALTERNATELY\nAVBL APCH LGT LEN 900M\n[ERA]RJAW/ IWO/ Iwoto (Iwo Jima), Iwoto (Iwo Jima), JP\n1. RUNWAY : 07/25 : 8694FT X 197FT\n◼ RUNWAY"
    },
    {
        "index": 202,
        "id": "M1022/26",
        "station": "RJAW",
        "airportName": "이오지마 공항 (ERA)",
        "validPeriod": "02AUG26 23:00 - 16AUG26 23:59",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02AUG26 23:00 - 16AUG26 23:59 RJAW M1022/26\nD) 02 16 2300/2359\nE) RWY 07/25 CLSD\nDUE TO SWEEPING\nRMK: EXC MISSION AND EMERG ACFT\n[ERA]RJTT/ HND/ Tokyo Haneda Intl, Tokyo, JP\n1. RUNWAY : 34R/16L : 11024FT X 197FT 34L/16R : 9843FT X 197FT\n05/23 : 8202FT X 197FT 22/04 : 8202FT X 197FT\n2. COMPANY RADIO : 132.075 HND OPERATION\n◼ COMPANY ADVISORY"
    },
    {
        "index": 203,
        "id": "COAD01/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "03APR26 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 03APR26 00:00 - UFN RJTT COAD01/26\nRNP (AR) APPROACH INFORMATION\nCERTIFIED A/C TYPE : A321(HL8510, HL8534, HL8511, HL8533, HL8582)\nCERTIFIED APPROACHES : RNP RWY 23 (AR)\n-- BY SELOO--\nPage 50"
    },
    {
        "index": 204,
        "id": "COAD01/21",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "2. 14JAN21 00:00 - UFN RJTT COAD01/21\n** DE/ANTI-ICING CURRENT STATE OF FLUIDS **\nFLUID : TYPE 1(KILFROST DF PLUS)\n        TYPE 4(KILFROST ABC-S PLUS)\nWORKING TYPE : 2 STEP\n-- BY --\n◼ RUNWAY"
    },
    {
        "index": 205,
        "id": "J1682/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "06AUG26 15:30 - 28AUG26 21:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "06AUG26 15:30 - 28AUG26 21:30 RJTT J1682/26\nD) 06-07 11 13-14 18 20-21 25 27-28 1530/2130\nE) RWY 16L/34R CLSD DUE TO MAINT\nRMK: SEE AIP RJTT AD2.23"
    },
    {
        "index": 206,
        "id": "J1623/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "30JUL26 21:30 - 28OCT26 21:30",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30JUL26 21:30 - 28OCT26 21:30 RJTT J1623/26\nE) GROOVING FOR RWY 16L/34R PARTLY ERASED DUE TO MAINT\n1.LEN: 98.0M (BTN 1004.8M AND 1102.8M FM RWY 34R THR)\nWID: 11.0M (BTN 1.0M AND 12.0M ON THE EAST SIDE OF RCL)\n2.LEN: 98.0M (BTN 1004.8M AND 1102.8M FM RWY 34R THR)\nWID: 11.0M (BTN 1.0M AND 12.0M ON THE WEST SIDE OF RCL)"
    },
    {
        "index": 207,
        "id": "J1622/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "01AUG26 14:30 - 29AUG26 21:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:30 - 29AUG26 21:00 RJTT J1622/26\nD) 01 05 08 12 15 19 22 26 29 1430/2100\nE) RWY 05/23 CLSD DUE TO MAINT\nRMK: SEE AIP RJTT AD2.23"
    },
    {
        "index": 208,
        "id": "J1620/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "02AUG26 14:30 - 31AUG26 21:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02AUG26 14:30 - 31AUG26 21:00 RJTT J1620/26\nD) 02-04 06-07 09-11 13-14 16-18 20-21 23-25 27-28\n30-31 1430/2100\nE) RWY 04/22 CLSD DUE TO MAINT\nRMK: AVBL CROSS RWY 04/22 VIA TWY OTHER THAN CLSD TWY\nSEE AIP RJTT AD2.23\nCOMMENT) CODE F A/C USING RWY"
    },
    {
        "index": 209,
        "id": "J1619/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "01AUG26 14:30 - 31AUG26 21:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:30 - 31AUG26 21:00 RJTT J1619/26\nD) 01-03 05 08-10 12 15-17 19 22-24 26 29-31\n1430/2100\nE) RWY 16R/34L CLSD DUE TO MAINT\nRMK: AVBL CROSS RWY 16R/34L VIA TWY OTHER THAN CLSD TWY\nSEE AIP RJTT AD2.23\nCOMMENT) CODE F A/C USING RWY"
    },
    {
        "index": 210,
        "id": "J1602/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "05AUG26 15:00 - 02SEP26 15:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "05AUG26 15:00 - 02SEP26 15:00 RJTT J1602/26\nE) GROOVING FOR RWY 16L/34R PARTLY,GRADUALLY ERASED OR\nINSTALLED\nRMK: (1)REF AIP SUP 187/26 ITEM RWY:53,58\n(2)THE EXACT TIME OF NEXT PERIOD WILL BE NOTIFIED BY FURTHER\nNOTAM"
    },
    {
        "index": 211,
        "id": "J1541/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "14JUL26 21:30 - 12OCT26 21:30",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14JUL26 21:30 - 12OCT26 21:30 RJTT J1541/26\nE) GROOVING FOR RWY 16L/34R PARTLY ERASED DUE TO MAINT\nLEN: 22.0M (BTN 726.8M AND 748.8M FM RWY 34R DISPLACED THR)\nWID: 3.5M (BTN 2.0M AND 5.5M ON THE EAST SIDE OF RCL)"
    },
    {
        "index": 212,
        "id": "J0406/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "15APR26 15:00 - 28OCT26 15:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "15APR26 15:00 - 28OCT26 15:00 RJTT J0406/26\nE) TRIGGER NOTAM-AIRAC AIP SUP 021/26\nWEF 16 APR 2026 TIL 28 OCT 2026\nPage 51\nUNSERVICEABILITY AND ALTERNATE MEASURES OF TOKYO LDA-\nLOC/DME22(IKL)\nCOMMENT) RJTT RWY 22 LDA-LOC/DME (IKL) Alternate Operation\n* Status: Permanent IKL LOC/DME is U/S due to construction,\n   but Temporary Portable LOC/DME is in operation.\n* FREQ (110.1MHz) and ID (IKL) REMAIN UNCHANGED.\n   All flight procedures using IKL are FULLY AVAILABLE.\n   existing charts and FMS database AVAILABLE.\n◼ RUNWAY LIGHT"
    },
    {
        "index": 213,
        "id": "J1661/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "05AUG26 15:00 - 02SEP26 15:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "05AUG26 15:00 - 02SEP26 15:00 RJTT J1661/26\nE) ACFT-STAND-ID-SIGN FOR SPOT 47 U/S\nVISUAL-DOCKING-GUIDANCE-SYSTEM FOR SPOT 47 U/S\nAPN-FLOOD-LGT FOR SPOT 401 PARTLY U/S\nAPN-FLOOD-LGT FOR SPOT 909 PARTLY U/S\nRMK: (1)REF AIP SUP 187/26 ITEM APRON:3,8,9,11\n(2)THE EXACT TIME OF NEXT PERIOD WILL BE NOTIFIED BY FURTHER\nNOTAM"
    },
    {
        "index": 214,
        "id": "J1659/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "05AUG26 15:00 - 02SEP26 15:00",
        "category": "TAXIWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "05AUG26 15:00 - 02SEP26 15:00 RJTT J1659/26\nE) TAXIING-GUIDANCE-SIGN FOR T12,T14,Q,Q1,Q2 U/S\nRAPID-EXIT-TWY-INDICATOR-LGT FOR C10 U/S\nRMK: (1)REF AIP SUP 187/26 ITEM TWY:13,43\n(2)THE EXACT TIME OF NEXT PERIOD WILL BE NOTIFIED BY FURTHER\nNOTAM"
    },
    {
        "index": 215,
        "id": "J1657/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "05AUG26 15:00 - 02SEP26 15:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "05AUG26 15:00 - 02SEP26 15:00 RJTT J1657/26\nE) RCLL FOR RWY 16L/34R U/S\nRMK: (1)REF AIP SUP 187/26 ITEM RWY:51\n(2)THE EXACT TIME OF NEXT PERIOD WILL BE NOTIFIED BY FURTHER\nNOTAM"
    },
    {
        "index": 216,
        "id": "J1656/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "05AUG26 15:00 - 02SEP26 15:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "05AUG26 15:00 - 02SEP26 15:00 RJTT J1656/26\nE) RWY-THR-ID-LGT FOR RWY 16L U/S\nSEQUENCED-FLG-LGT FOR RWY 34L U/S\nREDL FOR RWY 16L/34R PARTLY U/S\nAPCH-GUIDANCE-LGT FOR RWY 16R/16L(NR.4) U/S\nAPCH-GUIDANCE-LGT FOR RWY 16R/16L(NR.6,NR.8) PARTLY U/S\nLIGHTING SYSTEM CAT-2,3 FOR RWY 34R DOWNGRADED TO CAT-1\nRMK: (1)REF AIP SUP 187/26 ITEM RWY:30,49,52,54,55,56\n(2)THE EXACT TIME OF NEXT PERIOD WILL BE NOTIFIED BY FURTHER\nNOTAM\n◼ APPROACH"
    },
    {
        "index": 217,
        "id": "J1687/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "06AUG26 15:30 - 28AUG26 21:30",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "06AUG26 15:30 - 28AUG26 21:30 RJTT J1687/26\nD) 06-07 11 13-14 18 20-21 25 27-28  1530/2130\nE) ILS-LOC,GP,DME FOR RWY 16L U/S DUE TO CONST"
    },
    {
        "index": 218,
        "id": "J1686/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "06AUG26 15:30 - 28AUG26 21:30",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "06AUG26 15:30 - 28AUG26 21:30 RJTT J1686/26\nD) 06-07 11 13-14 18 20-21 25 27-28 1530/2130\nE) ILS-LOC,GP,DME,IM FOR RWY 34R U/S DUE TO CONST"
    },
    {
        "index": 219,
        "id": "J1636/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "02AUG26 14:30 - 31AUG26 21:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02AUG26 14:30 - 31AUG26 21:00 RJTT J1636/26\nD) 02-04 06-07 09-11 13-14 16-18 20-21 23-25 27-28\n30-31 1430/2100\nPage 52\nE) ILS-LOC,GP,DME FOR RWY 22 U/S DUE TO CONST"
    },
    {
        "index": 220,
        "id": "J1633/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "01AUG26 14:30 - 29AUG26 21:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:30 - 29AUG26 21:00 RJTT J1633/26\nD) 01 05 08 12 15 19 22 26 29 1430/2100\nE) ILS-LOC,GP,DME FOR RWY 23 U/S DUE TO CONST"
    },
    {
        "index": 221,
        "id": "J1629/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "01AUG26 14:30 - 31AUG26 21:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:30 - 31AUG26 21:00 RJTT J1629/26\nD) 01-03 05 08-10 12 15-17 19 22-24 26 29-31\n1430/2100\nE) ILS-LOC,GP,DME FOR RWY 34L U/S DUE TO CONST"
    },
    {
        "index": 222,
        "id": "J1628/26",
        "station": "RJTT",
        "airportName": "도쿄 FIR (Tokyo Control)",
        "validPeriod": "01AUG26 14:30 - 31AUG26 21:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG26 14:30 - 31AUG26 21:00 RJTT J1628/26\nD) 01-03 05 08-10 12 15-17 19 22-24 26 29-31\n1430/2100\nE) ILS-LOC,GP,DME FOR RWY 16R U/S DUE TO CONST\n[ERA]RJCC/ CTS/ Sapporo New Chitose Airport, Sapporo, JP\nSEE THE SAME AIRPORT IN PACKAGE 2\n[ERA]PASY/ SYA/ Eareckson Air Station, Shemya, US\n1. RUNWAY : 10/28 : 10004FT X 150FT\n◼ COMPANY ADVISORY"
    },
    {
        "index": 223,
        "id": "COAD01/21",
        "station": "PASY",
        "airportName": "쉬미야 에어스테이션 (ERA)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 14JAN21 00:00 - UFN PASY COAD01/21\nCONTACT POINT\nPASY TWR : TEL 1-907-392-3505/3606\n-- BY --\n◼ NAVAID"
    },
    {
        "index": 224,
        "id": "M0491/26",
        "station": "PASY",
        "airportName": "쉬미야 에어스테이션 (ERA)",
        "validPeriod": "04AUG26 02:51 - 31AUG26 23:00",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "04AUG26 02:51 - 31AUG26 23:00 PASY M0491/26\nE) NAVAID SYA\nVOR UNSERVICEABLE\n◼ APPROACH LIGHT"
    },
    {
        "index": 225,
        "id": "M0432/26",
        "station": "PASY",
        "airportName": "쉬미야 에어스테이션 (ERA)",
        "validPeriod": "08JUL26 23:17 - 01OCT26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "08JUL26 23:17 - 01OCT26 23:00 PASY M0432/26\nE) RWY 10/28 RWY 10/28 SEQUENCED FLASHING LGT UNSERVICEABLE"
    },
    {
        "index": 226,
        "id": "M0431/26",
        "station": "PASY",
        "airportName": "쉬미야 에어스테이션 (ERA)",
        "validPeriod": "08JUL26 23:10 - 01OCT26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "08JUL26 23:10 - 01OCT26 23:00 PASY M0431/26\nE) RWY 10/28 RWY 10/28 APCH LIGHTING SYSTEM UNSERVICEABLE\n[ERA]PADK/ ADK/ Adak Island, Adak Island, US\n◼ APPROACH"
    },
    {
        "index": 227,
        "id": "A0246/26",
        "station": "PADK",
        "airportName": "에이댁 공항 (ERA)",
        "validPeriod": "02JUL26 20:11 - 11FEB27 20:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02JUL26 20:11 - 11FEB27 20:11 PADK A0246/26\nE) IAP ADAK, ADAK ISLAND, AK. ILS Y OR LOC Y RWY 23, ORIG...\nILS Z OR\nLOC Z RWY 23, ORIG... NDB/DME RWY 23, ORIG-C... ALTERNATE\nMINIMUMS NA\nEXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS,\nADK NDB\nUNMONITORED."
    },
    {
        "index": 228,
        "id": "A0194/25",
        "station": "PADK",
        "airportName": "에이댁 공항 (ERA)",
        "validPeriod": "02SEP25 20:14 - 02SEP27 20:14",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02SEP25 20:14 - 02SEP27 20:14 PADK A0194/25\nE) ADK IAP ADAK, ADAK ISLAND, AK.\nTACAN  RWY 23, ORIG...\nPage 53\nS-23? CAT A/B MDA 800/HAT 783 RVR 5500."
    },
    {
        "index": 229,
        "id": "A0084/25",
        "station": "PADK",
        "airportName": "에이댁 공항 (ERA)",
        "validPeriod": "11MAR25 13:00 - 11MAR27 13:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "일반항공(GA)/헬리포트/드론 전용 (상업 정기 여객편 비적용)",
        "rawText": "11MAR25 13:00 - 11MAR27 13:00 PADK A0084/25\nE) ADK IAP ADAK, ADAK ISLAND, AK.\nRNAV (GPS) RWY 23, ORIG-C...\nRWY 23 HELICOPTER VISIBILITY REDUCTION BELOW RVR 5000 NOT\nAUTHORIZED.\nCHANGE ALTERNATE MINIMUMS TO READ: CATEGORIES A, B, C, D\n1300-3."
    },
    {
        "index": 230,
        "id": "A0083/25",
        "station": "PADK",
        "airportName": "에이댁 공항 (ERA)",
        "validPeriod": "11MAR25 13:00 - 11MAR27 12:59",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "일반항공(GA)/헬리포트/드론 전용 (상업 정기 여객편 비적용)",
        "rawText": "11MAR25 13:00 - 11MAR27 12:59 PADK A0083/25\nE) ADK IAP ADAK, ADAK ISLAND, AK.\nNDB/DME RWY 23, ORIG-C...\nS-23 VIS CAT A 1 1/4.\nRWY 23 HELICOPTER VISIBILITY REDUCTION BELOW RVR 5000 NOT\nAUTHORIZED.\nCHANGE ALTERNATE MINIMUMS TO READ: CATEGORIES A, B 1600-2,\nCATEGORY\nC 1600-3, CATEGORY D 2600-3.\n[ERA]PACD/ CDB/ Cold Bay, Cold Bay, US\n1. RUNWAY : 15/33 : 10179FT X 150FT 08/26 : 4900FT X 150FT\n◼ COMPANY ADVISORY"
    },
    {
        "index": 231,
        "id": "COAD01/21",
        "station": "PACD",
        "airportName": "콜드베이 공항 (ERA)",
        "validPeriod": "14JAN21 00:00 - UFN",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "1. 14JAN21 00:00 - UFN PACD COAD01/21\nCONTACT POINT\n1)PACD TRANSPORTATION DEPARTMENT : TEL 907-532-5000\n2)PACD TWR : TEL 1-800-992-7433\n-- BY JFKKKW--\n◼ RUNWAY LIGHT"
    },
    {
        "index": 232,
        "id": "A2799/26",
        "station": "PACD",
        "airportName": "콜드베이 공항 (ERA)",
        "validPeriod": "09JUL26 07:35 - 30AUG26 15:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "09JUL26 07:35 - 30AUG26 15:00 PACD A2799/26\nE) RWY 15 RAI LGT U/S\n◼ APPROACH"
    },
    {
        "index": 233,
        "id": "A3138/26",
        "station": "PACD",
        "airportName": "콜드베이 공항 (ERA)",
        "validPeriod": "07AUG26 01:00 - 13AUG26 23:55",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 01:00 - 13AUG26 23:55 PACD A3138/26\nE) ODP COLD BAY, COLD BAY, AK. TAKEOFF MINIMUMS AND (OBSTACLE)\nDEPARTURE PROCEDURES AMDT 9... TEXTUAL DEPARTURE PROCEDURE NA\nEXCEPT\nFOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS, ELF NDB\nOUT OF\nSERVICE."
    },
    {
        "index": 234,
        "id": "A3129/26",
        "station": "PACD",
        "airportName": "콜드베이 공항 (ERA)",
        "validPeriod": "05AUG26 20:33 - 10OCT26 15:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "05AUG26 20:33 - 10OCT26 15:00 PACD A3129/26\nE) CDB ILS RWY 15 LOC/GP U/S\n[ERA]PAKN/ AKN/ King Salmon, King Salmon, US\n1. RUNWAY : 12/30 : 8901FT X 150FT\n◼ RUNWAY"
    },
    {
        "index": 235,
        "id": "A2100/26",
        "station": "PAKN",
        "airportName": "킹샐몬 공항 (ERA)",
        "validPeriod": "09AUG26 15:24 - 10AUG26 15:24",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 15:24 - 10AUG26 15:24 PAKN A2100/26\nE) RWY 18 FICON 5/5/5 100 PCT WET OBS AT 2608091524."
    },
    {
        "index": 236,
        "id": "A2098/26",
        "station": "PAKN",
        "airportName": "킹샐몬 공항 (ERA)",
        "validPeriod": "09AUG26 15:24 - 10AUG26 15:24",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 15:24 - 10AUG26 15:24 PAKN A2098/26\nE) RWY 12 FICON 5/5/5 100 PCT WET OBS AT 2608091524.\nPage 54"
    },
    {
        "index": 237,
        "id": "A1509/26",
        "station": "PAKN",
        "airportName": "킹샐몬 공항 (ERA)",
        "validPeriod": "13MAY26 14:17 - 13AUG26 00:01",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "13MAY26 14:17 - 13AUG26 00:01 PAKN A1509/26\nE) RWY 12 1000FT DIST REMAINING SIGN LEFT SIDE LGT U/S"
    },
    {
        "index": 238,
        "id": "A1508/26",
        "station": "PAKN",
        "airportName": "킹샐몬 공항 (ERA)",
        "validPeriod": "13MAY26 14:16 - 13AUG26 00:01",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "13MAY26 14:16 - 13AUG26 00:01 PAKN A1508/26\nE) RWY 12 3000FT DIST REMAINING SIGN LEFT SIDE LGT U/S"
    },
    {
        "index": 239,
        "id": "A1507/26",
        "station": "PAKN",
        "airportName": "킹샐몬 공항 (ERA)",
        "validPeriod": "13MAY26 14:15 - 13AUG26 00:01",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "13MAY26 14:15 - 13AUG26 00:01 PAKN A1507/26\nE) RWY 30 5000FT DIST REMAINING SIGN RIGHT SIDE LGT U/S"
    },
    {
        "index": 240,
        "id": "A1506/26",
        "station": "PAKN",
        "airportName": "킹샐몬 공항 (ERA)",
        "validPeriod": "13MAY26 14:14 - 13AUG26 00:01",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "13MAY26 14:14 - 13AUG26 00:01 PAKN A1506/26\nE) RWY 30 7000FT DIST REMAINING SIGN RIGHT SIDE LGT U/S"
    },
    {
        "index": 241,
        "id": "A0766/26",
        "station": "PAKN",
        "airportName": "킹샐몬 공항 (ERA)",
        "validPeriod": "08MAR26 01:00 - 27AUG26 15:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "08MAR26 01:00 - 27AUG26 15:00 PAKN A0766/26\nD) DLY 0100-1500\nE) AKN AD AP COND NOT REP\n[ERA]PAFA/ FAI/ Fairbanks International Airport, Fairbanks, US\n1. RUNWAY : 02L/20R : 11800FT X 150FT 02R/20L : 4510FT X 75FT\n2. COMPANY RADIO : 131.75MHZ OMNI OPERATIONS\n◼ RUNWAY"
    },
    {
        "index": 242,
        "id": "A1530/26",
        "station": "PAFA",
        "airportName": "페어뱅크스 국제공항 (ERA)",
        "validPeriod": "20APR26 17:07 - 30SEP26 07:30",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "20APR26 17:07 - 30SEP26 07:30 PAFA A1530/26\nE) AD AP WILDLIFE HAZARD MIGRATORY BIRDS"
    },
    {
        "index": 243,
        "id": "A3289/25",
        "station": "PAFA",
        "airportName": "페어뱅크스 국제공항 (ERA)",
        "validPeriod": "01AUG25 22:06 - UFN",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "01AUG25 22:06 - UFN PAFA A3289/25\nE) FAI RWY 02L/20R COMMISSIONED 11800FT X 150FT ASPH-GROOVED\nLGTD.\nDECLARED DIST: RWY 02L TORA 11800FT TODA 12800FT ASDA 11680FT\nLDA\n10930FT. RWY 20R TORA 11800FT TODA 12800FT ASDA 11035FT LDA\n10285FT.\n◼ APPROACH"
    },
    {
        "index": 244,
        "id": "A3792/26",
        "station": "PAFA",
        "airportName": "페어뱅크스 국제공항 (ERA)",
        "validPeriod": "02FEB26 06:16 - 30SEP26 21:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02FEB26 06:16 - 30SEP26 21:11 PAFA A3792/26\nE) FAI NAV ILS RWY 02L IM U/S"
    },
    {
        "index": 245,
        "id": "A2152/26",
        "station": "PAFA",
        "airportName": "페어뱅크스 국제공항 (ERA)",
        "validPeriod": "15MAY26 16:02 - 25DEC26 16:02",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "15MAY26 16:02 - 25DEC26 16:02 PAFA A2152/26\nE) IAP FAIRBANKS INTL, FAIRBANKS, AK. ILS RWY 2L (CAT II-III),\n AMDT\n11 ... S-ILS 2L CAT II NA EXCEPT FOR AIRCRAFT EQUIPPED WITH\nRADIO\nALTIMETER. I-CNA INNER MARKER OUT OF SERVICE"
    },
    {
        "index": 246,
        "id": "A1891/26",
        "station": "PAFA",
        "airportName": "페어뱅크스 국제공항 (ERA)",
        "validPeriod": "28APR26 11:48 - 08DEC26 11:48",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "28APR26 11:48 - 08DEC26 11:48 PAFA A1891/26\nE) IAP FAIRBANKS INTL, FAIRBANKS, AK.\nRNAV (GPS) RWY 20L, AMDT 2 ...\nLNAV/VNAV DA 755/HAT 321 ALL CATS, VIS ALL CATS 1. TEMPORARY\nCRANES\n545 MSL BEGINNING 5542FT NE OF RWY 20L (2023-AAL-186/190/193-\nNRA)."
    },
    {
        "index": 247,
        "id": "A1830/26",
        "station": "PAFA",
        "airportName": "페어뱅크스 국제공항 (ERA)",
        "validPeriod": "15JAN26 15:06 - 27AUG26 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "15JAN26 15:06 - 27AUG26 23:55 PAFA A1830/26\nE) FAI IAP FAIRBANKS INTL, FAIRBANKS, AK.\nILS OR LOC RWY 2L, AMDT 11...\nPage 55\nILS Z OR LOC Z RWY 20R, AMDT 25C...\nRNAV (GPS) Y RWY 20R, AMDT 1E...\nRNAV (GPS) Y RWY 2L, AMDT 1C...\nRNAV (GPS) RWY 20L, AMDT 2...\nRNAV (GPS) RWY 2R, AMDT 1B...\nCIRCLING TO GRAVEL RWY 2 NA AT NIGHT. TEMPORARY RIG 453 MSL\n244FT S\nOF GRAVEL RWY 2 (2022-AAL-254-NRA)."
    },
    {
        "index": 248,
        "id": "A5447/25",
        "station": "PAFA",
        "airportName": "페어뱅크스 국제공항 (ERA)",
        "validPeriod": "31OCT25 21:00 - 30OCT26 21:00",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "31OCT25 21:00 - 30OCT26 21:00 PAFA A5447/25\nE) FAI STAR FAIRBANKS INTL, FAIRBANKS, AK.\nLIBER FIVE ARRIVAL...\nCROSS GLOWS AT OR ABOVE 5000."
    },
    {
        "index": 249,
        "id": "A4418/24",
        "station": "PAFA",
        "airportName": "페어뱅크스 국제공항 (ERA)",
        "validPeriod": "07NOV24 20:03 - 06NOV26 20:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07NOV24 20:03 - 06NOV26 20:00 PAFA A4418/24\nE) FAI IAP FAIRBANKS INTL, FAIRBANKS, AK.\nILS OR LOC RWY 2L, AMDT 11...\nRNAV (RNP) Z RWY 2L, AMDT 2...\nILS RWY 2L (SA CAT I), AMDT 11...\nILS RWY 2L (CAT II-III), AMDT 11...\nCROSS GLOWS AT OR ABOVE 5000.\n[ERA]CYXY/ YXY/ Whitehorse, Whitehorse, CA\n1. RUNWAY : 14R/32L : 9500FT X 150FT 14L/32R : 6597FT X 100FT\n◼ RUNWAY"
    },
    {
        "index": 250,
        "id": "C3241/26",
        "station": "CYXY",
        "airportName": "화이트호스 에릭 닐슨 공항 (ERA)",
        "validPeriod": "27JUL26 18:46 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27JUL26 18:46 - UFN CYXY C3241/26\nE) AMEND PUBLICATIONS:\nRWY 02/20 LENGTH TO READ: 1411FT\nRWY 02 TORA 1411 TODA 1411 ASDA 1411 LDA NOT USABLE\nRWY 20 TORA/TODA/ASDA NOT USABLE LDA 1411"
    },
    {
        "index": 251,
        "id": "C1664/26",
        "station": "CYXY",
        "airportName": "화이트호스 에릭 닐슨 공항 (ERA)",
        "validPeriod": "15MAY26 07:00 - 13AUG26 06:59",
        "category": "NAVAID",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "15MAY26 07:00 - 13AUG26 06:59 CYXY C1664/26\nE) MAINT CREW AND EQPT OPR FM 2410FT BFR THR 14R TO THR 14R.\n33FT AGL, 2321FT AMSL. NOT LGTD, NOT PAINTED.\n◼ NAVAID"
    },
    {
        "index": 252,
        "id": "F3178/26",
        "station": "CYXY",
        "airportName": "화이트호스 에릭 닐슨 공항 (ERA)",
        "validPeriod": "29JUN26 18:49 - 25SEP26 23:59",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "보조 항법/통신 시설 점검 (RNAV/GNSS 운항 정상)",
        "rawText": "29JUN26 18:49 - 25SEP26 23:59 CYXY F3178/26\nE) WHITEHORSE VOR/DME YXY 116.6MHZ/CH113X U/S\n◼ APPROACH"
    },
    {
        "index": 253,
        "id": "C2884/26",
        "station": "CYXY",
        "airportName": "화이트호스 에릭 닐슨 공항 (ERA)",
        "validPeriod": "14JUL26 18:54 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14JUL26 18:54 - UFN CYXY C2884/26\nE) AMEND PUBLICATIONS:\nILS Y RWY 32L APCH: PLAN VIEW: DELETE CIRCLING RESTRICTION"
    },
    {
        "index": 254,
        "id": "C1433/26",
        "station": "CYXY",
        "airportName": "화이트호스 에릭 닐슨 공항 (ERA)",
        "validPeriod": "01MAY26 15:12 - UFN",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "01MAY26 15:12 - UFN CYXY C1433/26\nE) AMEND PUBLICATIONS: RWY 14R/32L: LIGHTING TO READ:\nP3 INSTEAD OF P2\n◼ APPROACH LIGHT"
    },
    {
        "index": 255,
        "id": "C3507/26",
        "station": "CYXY",
        "airportName": "화이트호스 에릭 닐슨 공항 (ERA)",
        "validPeriod": "07AUG26 18:23 - 14AUG26 19:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "07AUG26 18:23 - 14AUG26 19:00 CYXY C3507/26\nE) THREE SEQUENCE FLASHING LGT 32L U/S. APPLY PROC\nFOR HIGH INTST APCH LGT INOPERATIVE (AIP AD 2.22.4)\n[ERA]CYZF/ YZF/ Yellowknife, Yellowknife, CA\nPage 56\n1. RUNWAY : 16/34 : 7503FT X 150FT 10/28 : 5001FT X 150FT\n◼ RUNWAY"
    },
    {
        "index": 256,
        "id": "C3158/26",
        "station": "CYZF",
        "airportName": "옐로나이프 공항 (ERA)",
        "validPeriod": "23JUL26 18:22 - 21OCT26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "23JUL26 18:22 - 21OCT26 23:00 CYZF C3158/26\nE) GENERAL AVIATION PRKG NOT AVBL. PILOTS PLANNING TO ARR\nSHALL MAKE PRIOR ARRANGEMENTS PRIOR TO DEP WITH AD\nOPS 867-445-5518.\n◼ RUNWAY LIGHT"
    },
    {
        "index": 257,
        "id": "C3500/26",
        "station": "CYZF",
        "airportName": "옐로나이프 공항 (ERA)",
        "validPeriod": "07AUG26 13:58 - 14AUG26 18:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "07AUG26 13:58 - 14AUG26 18:00 CYZF C3500/26\nE) ALL AD LGT ON INTST 3 CONTINUOUSLY.\nHIGHER INTST AVBL WITH 30MIN PN TEL 867-445-5518.\n[ERA]CYEG/ YEG/ Edmonton International Airport, Edmonton, CA\n1. RUNWAY : 02/20 : 10995FT X 200FT 12/30 : 10200FT X 200FT\n◼ RUNWAY"
    },
    {
        "index": 258,
        "id": "C3329/26",
        "station": "CYEG",
        "airportName": "에드먼턴 국제공항 (ERA)",
        "validPeriod": "30JUL26 18:48 - 29OCT26 20:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30JUL26 18:48 - 29OCT26 20:00 CYEG C3329/26\nE) RWY 12/30 CLSD DUE CONST.\nCOMMENT) CODE F A/C USING RWY (B748)"
    },
    {
        "index": 259,
        "id": "S0364/26",
        "station": "CYEG",
        "airportName": "에드먼턴 국제공항 (ERA)",
        "validPeriod": "10AUG26 05:02 - 10AUG26 13:02",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "10AUG26 05:02 - 10AUG26 13:02 CYEG S0364/26\nE) RSC 02 6/6/6 DRY, DRY, DRY. VALID AUG 10 0458 - AUG 10\n1258.\nRSC 20 6/6/6 DRY, DRY, DRY. VALID AUG 10 0458 - AUG 10 1258.\nADDN NON-GRF/TALPA INFO:\nRMK: TWY ALPHA, ALPHA 1, ALPHA 2, ALPHA 3, ALPHA 4, ALPHA\nCHARLIE, ALPHA DELTA, ALPHA ECHO, BRAVO, BRAVO 1, BRAVO 2,\nBRAVO\n4, KILO, NOVEMBER, PAPA, QUEBEC, ROMEO, SIERRA, TANGO,\nUNIFORM,\nWHISKEY, YANKEE, 202608100500, DRY.\nRMK: APN APRON I, APRON II, APRON III, APRON IV, APRON VI,\nAPRON\nVII, APRON VIII, 202608100500, DRY.\n◼ RUNWAY LIGHT"
    },
    {
        "index": 260,
        "id": "C3327/26",
        "station": "CYEG",
        "airportName": "에드먼턴 국제공항 (ERA)",
        "validPeriod": "30JUL26 18:48 - 29OCT26 20:00",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30JUL26 18:48 - 29OCT26 20:00 CYEG C3327/26\nE) REDL 12/30 U/S\n◼ APPROACH"
    },
    {
        "index": 261,
        "id": "C3332/26",
        "station": "CYEG",
        "airportName": "에드먼턴 국제공항 (ERA)",
        "validPeriod": "30JUL26 19:02 - 29OCT26 20:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30JUL26 19:02 - 29OCT26 20:00 CYEG C3332/26\nE) DUE RWY 12/30 CLSD\n.\nRNAV (GNSS) Z RWY 12, RNAV (RNP) Y 12 APCH:\nALL MINIMA: NOT AUTH EXC FOR TRAINING FLT.\nTRAINING FLT MUST INITIATE MISSED APCH PROC AT OR ABV MDA OR\nDA.\n.\nRNAV (GNSS) Z RWY 30, RNAV (RNP) Y 30 APCH:\nALL MINIMA: NOT AUTH EXC FOR TRAINING FLT.\nTRAINING FLT MUST INITIATE MISSED APCH PROC AT OR ABV MDA OR\nDA.\nPage 57"
    },
    {
        "index": 262,
        "id": "C3330/26",
        "station": "CYEG",
        "airportName": "에드먼턴 국제공항 (ERA)",
        "validPeriod": "30JUL26 18:52 - 29OCT26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30JUL26 18:52 - 29OCT26 23:59 CYEG C3330/26\nE) ILS RWY 12 AND RWY 30 U/S"
    },
    {
        "index": 263,
        "id": "C3328/26",
        "station": "CYEG",
        "airportName": "에드먼턴 국제공항 (ERA)",
        "validPeriod": "30JUL26 18:48 - 29OCT26 20:00",
        "category": "LIGHTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30JUL26 18:48 - 29OCT26 20:00 CYEG C3328/26\nE) PAPI 30 U/S"
    },
    {
        "index": 264,
        "id": "C2563/26",
        "station": "CYEG",
        "airportName": "에드먼턴 국제공항 (ERA)",
        "validPeriod": "26JUN26 14:03 - 25SEP26 16:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "26JUN26 14:03 - 25SEP26 16:00 CYEG C2563/26\nE) DUE CRANE:\n.\nRNAV (RNP) Y RWY 30 APCH:\nRNP 0.15 MINIMA TO READ: 2710 (338) 1 RVR 50\n◼ APPROACH LIGHT"
    },
    {
        "index": 265,
        "id": "C3333/26",
        "station": "CYEG",
        "airportName": "에드먼턴 국제공항 (ERA)",
        "validPeriod": "30JUL26 19:11 - 29OCT26 20:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "30JUL26 19:11 - 29OCT26 20:00 CYEG C3333/26\nE) ALS 12 AND 30 U/S. APPLY PROC FOR HIGH INTST APCH LGT\nINOPERATIVE (AIP AD 2.22.4).\n[ERA]CYYC/ YYC/ Calgary International, Calgary, CA\n1. RUNWAY : 17L/35R : 14000FT X 200FT 17R/35L : 12675FT X 200FT\n11/29 : 8000FT X 200FT\n◼ RUNWAY"
    },
    {
        "index": 266,
        "id": "C3520/26",
        "station": "CYYC",
        "airportName": "캘거리 국제공항 (ERA)",
        "validPeriod": "10AUG26 07:00 - 10AUG26 11:30",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 07:00 - 10AUG26 11:30 CYYC C3520/26\nE) RWY 11/29 CLSD.\nCOMMENT) CODE F A/C USING RWY (B748)"
    },
    {
        "index": 267,
        "id": "C3227/26",
        "station": "CYYC",
        "airportName": "캘거리 국제공항 (ERA)",
        "validPeriod": "26JUL26 19:57 - 27AUG26 01:00",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "26JUL26 19:57 - 27AUG26 01:00 CYYC C3227/26\nE) TWY M HOLDING BAY CLSD"
    },
    {
        "index": 268,
        "id": "C2710/26",
        "station": "CYYC",
        "airportName": "캘거리 국제공항 (ERA)",
        "validPeriod": "08JUL26 14:04 - 06OCT26 22:30",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "08JUL26 14:04 - 06OCT26 22:30 CYYC C2710/26\nD) DAILY 1400-2230\nE) MAINT CREW AND EQPT APRX 2000FT BFR THR 17L\nAND APRX 700FT EACH SIDE OF RWY 17L/35R EXTENDED CENTRE LINE.\n43FT AGL 3632FT AMSL. LGTD, NOT PAINTED"
    },
    {
        "index": 269,
        "id": "S0358/26",
        "station": "CYYC",
        "airportName": "캘거리 국제공항 (ERA)",
        "validPeriod": "10AUG26 03:09 - 10AUG26 11:09",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 03:09 - 10AUG26 11:09 CYYC S0358/26\nE) RSC 11 6/6/6 DRY, DRY, DRY. VALID AUG 10 0302 - AUG 10\n1102.\nRSC 29 6/6/6 DRY, DRY, DRY. VALID AUG 10 0302 - AUG 10 1102.\nRSC 17L 6/6/6 DRY, DRY, DRY. VALID AUG 10 0257 - AUG 10 1057.\nRSC 35R 6/6/6 DRY, DRY, DRY. VALID AUG 10 0257 - AUG 10 1057.\nRSC 17R 6/6/6 DRY, DRY, DRY. VALID AUG 10 0309 - AUG 10 1109.\nRSC 35L 6/6/6 DRY, DRY, DRY. VALID AUG 10 0309 - AUG 10 1109.\nADDN NON-GRF/TALPA INFO:\nCRFI 11 NR/NR/NR.\nCRFI 29 NR/NR/NR.\nCRFI 17L NR/NR/NR.\nCRFI 35R NR/NR/NR.\nCRFI 17R NR/NR/NR.\nPage 58\nCRFI 35L NR/NR/NR.\n◼ NAVAID"
    },
    {
        "index": 270,
        "id": "F4274/26",
        "station": "CYYC",
        "airportName": "캘거리 국제공항 (ERA)",
        "validPeriod": "07AUG26 16:15 - 14AUG26 23:59",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 16:15 - 14AUG26 23:59 CYYC F4274/26\nE) CALGARY VOR YYC 116.7MHZ UNMONITORED BY ATS\n◼ APPROACH"
    },
    {
        "index": 271,
        "id": "C1692/26",
        "station": "CYYC",
        "airportName": "캘거리 국제공항 (ERA)",
        "validPeriod": "14MAY26 14:21 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14MAY26 14:21 - UFN CYYC C1692/26\nE) AMEND PUBLICATIONS:\nILS RWY 17R APCH:\nLOC/DME MINIMA TO READ: 3960 (405) 1\nDIST/ALT TABLE: LAST ALT TO READ 3.0/3960 INSTEAD OF 2.8/3900\n[ERA]CYWG/ YWG/ Winnipeg J.A. Richardson Intl Airport,\nWinnipeg, CA\n1. RUNWAY : 18/36 : 11000FT X 200FT 13/31 : 8841FT X 200FT\n◼ RUNWAY"
    },
    {
        "index": 272,
        "id": "D3049/26",
        "station": "CYWG",
        "airportName": "위니펙 제임스 암스트롱 공항 (ERA)",
        "validPeriod": "06AUG26 12:45 - 19AUG26 23:59",
        "category": "GENERAL",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "행정/AIP SUP 발효 고지 (차트 반영 완료)",
        "rawText": "06AUG26 12:45 - 19AUG26 23:59 CYWG D3049/26\nE) TRIGGER NOTAM - AIP SUP 076/2026 WEF 06 AUG 2026 UNTIL 30\nOCT\n2026. AERODROME CONSTRUCTION - WINNIPEG / JAMES ARMSTRONG\nRICHARDSON INTL (CYWG)"
    },
    {
        "index": 273,
        "id": "S0360/26",
        "station": "CYWG",
        "airportName": "위니펙 제임스 암스트롱 공항 (ERA)",
        "validPeriod": "10AUG26 03:39 - 10AUG26 11:39",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 03:39 - 10AUG26 11:39 CYWG S0360/26\nE) RSC 13 6/6/6 DRY, DRY, DRY. VALID AUG 10 0321 - AUG 10\n1121.\nRSC 31 6/6/6 DRY, DRY, DRY. VALID AUG 10 0321 - AUG 10 1121.\nRSC 18 6/6/6 DRY, DRY, DRY. VALID AUG 10 0322 - AUG 10 1122.\nRSC 36 6/6/6 DRY, DRY, DRY. VALID AUG 10 0322 - AUG 10 1122.\nADDN NON-GRF/TALPA INFO:\nRMK: TWY ALPHA, BRAVO, CHARLIE, ECHO, FOXTROT, GOLF, HOTEL,\nKILO,\nLIMA, PAPA, QUEBEC, TANGO, VICTOR, WHISKEY, 202608100321, DRY.\nRMK: APN APRON I, APRON II, APRON IV, APRON IX, APRON V, APRON\nVII, APRON VIII, APRON X, APRON XII, CDF, 202608100321, DRY.\n[ERA]CYYQ/ YYQ/ Churchill Airport, Churchill, CA\n1. RUNWAY : 15/33 : 9195FT X 160FT\n◼ RUNWAY"
    },
    {
        "index": 274,
        "id": "D2642/26",
        "station": "CYYQ",
        "airportName": "처칠 공항 (ERA)",
        "validPeriod": "13JUL26 20:42 - 10OCT26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "13JUL26 20:42 - 10OCT26 23:59 CYYQ D2642/26\nE) UNEVEN SFC ON FIRST 600FT RWY 15 AND TWY A\n◼ NAVAID"
    },
    {
        "index": 275,
        "id": "G1917/26",
        "station": "CYYQ",
        "airportName": "처칠 공항 (ERA)",
        "validPeriod": "19JUN26 13:22 - 17SEP26 23:59",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "19JUN26 13:22 - 17SEP26 23:59 CYYQ G1917/26\nE) CHURCHILL VOR YYQ 114.1MHZ UNMONITORED BY ATS\n◼ APPROACH"
    },
    {
        "index": 276,
        "id": "D2867/26",
        "station": "CYYQ",
        "airportName": "처칠 공항 (ERA)",
        "validPeriod": "27JUL26 14:06 - 02OCT26 23:59",
        "category": "LIGHTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27JUL26 14:06 - 02OCT26 23:59 CYYQ D2867/26\nPage 59\nE) PAPI 33 U/S"
    },
    {
        "index": 277,
        "id": "D2825/26",
        "station": "CYYQ",
        "airportName": "처칠 공항 (ERA)",
        "validPeriod": "24JUL26 16:42 - 28AUG26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24JUL26 16:42 - 28AUG26 23:59 CYYQ D2825/26\nE) ILS RWY 33 U/S"
    },
    {
        "index": 278,
        "id": "D2706/26",
        "station": "CYYQ",
        "airportName": "처칠 공항 (ERA)",
        "validPeriod": "17JUL26 01:02 - 02OCT26 01:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "17JUL26 01:02 - 02OCT26 01:00 CYYQ D2706/26\nE) PAPI 25 U/S\n[ERA]CYXE/ YXE/ J.G. Diefenbaker Intl, Saskatoon, CA\n1. RUNWAY : 09/27 : 8300FT X 148FT 15/33 : 6200FT X 148FT\n******** NO CURRENT NOTAMS FOUND ********\n[ERA]KDLH/ DLH/ Duluth International, Duluth, US\n1. RUNWAY : 09/27 : 10591FT X 150FT 03/21 : 5719FT X 150FT\n◼ RUNWAY"
    },
    {
        "index": 279,
        "id": "A2078/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "29MAY26 19:02 - 26AUG26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "공항 부지 일상 작업 (초지/도색/청소/정기 점검)",
        "rawText": "29MAY26 19:02 - 26AUG26 23:00 KDLH A2078/26\nE) RWY 09/27 SAFETY AREA NOT STD DUE TO SURFACE VARIATION"
    },
    {
        "index": 280,
        "id": "A2077/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "29MAY26 19:01 - 26AUG26 23:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "공항 부지 일상 작업 (초지/도색/청소/정기 점검)",
        "rawText": "29MAY26 19:01 - 26AUG26 23:00 KDLH A2077/26\nE) RWY 03/21 SAFETY AREA NOT STD DUE TO SURFACE VARIATION\n◼ NAVAID"
    },
    {
        "index": 281,
        "id": "09/037",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "30SEP16 20:00 - PERM",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30SEP16 20:00 - PERM KDLH 09/037\nE) COM REMOTE TRANS/REC 255.9 CHANGED TO 233.7)\n◼ APPROACH"
    },
    {
        "index": 282,
        "id": "A2268/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "04AUG26 12:00 - 14AUG28 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "04AUG26 12:00 - 14AUG28 23:55 KDLH A2268/26\nE) IAP DULUTH INTL, DULUTH, MN. RNAV (GPS) RWY 3, ORIG-B...\nLNAV MDA\n1880/HAT 460 ALL CATS, VISIBILITY CATS C/D 1 3/8. VDP 1.33NM\nTO RW03.\nTEMPORARY CRANE 1625 MSL 4888FT SW OF RWY 27 (2026-AGL-3724\nTHRU\n3727-NRA)."
    },
    {
        "index": 283,
        "id": "A2267/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "04AUG26 12:00 - 14AUG28 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "04AUG26 12:00 - 14AUG28 23:55 KDLH A2267/26\nE) IAP DULUTH INTL, DULUTH, MN. ILS OR LOC RWY 27, AMDT 12...\nS-ILS\n27 DA 1644/HAT 223 CATS A/B. S-LOC 27 MDA 1920/HAT 499 ALL\nCATS,\nVISIBILITY RVR 5000 CATS C/D/E. FOR INOP ALS, INCREASE S-LOC\n27 CATS\nC/D/E VISIBILITY TO 1 3/8 SM. TEMPORARY CRANE 1625 MSL 4888FT\nSW OF\nRWY 27 (2026-AGL-3724 THRU 3727-NRA)."
    },
    {
        "index": 284,
        "id": "A2265/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "02AUG26 20:40 - 14AUG28 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02AUG26 20:40 - 14AUG28 23:55 KDLH A2265/26\nE) IAP DULUTH INTL, DULUTH, MN. ILS OR LOC RWY 27, AMDT 12...\nRADAR-1, ORIG-A... RNAV (GPS) RWY 21, ORIG-B... RNAV (GPS)\nRWY 27,\nAMDT 1... RNAV (GPS) RWY 3, ORIG-B... RNAV (GPS) RWY 9, AMDT\n1D...\nPage 60\nTACAN Y RWY 9, AMDT 3A... VOR OR TACAN RWY 3, AMDT 21C...\nVOR/DME OR\nTACAN RWY 21, AMDT 15A... CIRCLING CATS A/B MDA 1940/HAA 512.\nTEMPORARY CRANE 1625 MSL 1667 FT S OF DLH AIRPORT (2026-\nAGL-3724 THRU\n3727-NRA). TEMPORARY CRANE 1584 MSL 4508 FT N OF RWY 03 (2025-\n AGL\n3629 THRU 3636-NRA)."
    },
    {
        "index": 285,
        "id": "A2252/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "04AUG26 13:00 - 11SEP26 21:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "04AUG26 13:00 - 11SEP26 21:00 KDLH A2252/26\nE) DLH ILS RWY 09 U/S"
    },
    {
        "index": 286,
        "id": "A2212/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "14JUL26 18:17 - 17AUG26 20:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14JUL26 18:17 - 17AUG26 20:00 KDLH A2212/26\nE) DLH ILS RWY 09 IM U/S"
    },
    {
        "index": 287,
        "id": "A2210/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "14JUL26 18:15 - 17AUG26 20:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14JUL26 18:15 - 17AUG26 20:00 KDLH A2210/26\nE) DLH ILS RWY 09 OM U/S"
    },
    {
        "index": 288,
        "id": "A2208/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "14JUL26 17:06 - 23FEB27 23:55",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "14JUL26 17:06 - 23FEB27 23:55 KDLH A2208/26\nE) IAP DULUTH INTL, DULUTH, MN. RNAV (GPS) RWY 21, ORIG-B...\nLNAV MDA\n1900/HAT 480 ALL CATS. VIS CATS C/D 1 3/8. CIRCLING MDA\n1940/HAA 512\nCATS A/B. TEMPORARY CRANE 1584 MSL 4508 FT N OF RWY 03 (2025-\nAGL-3626\nTHRU 3629-NRA)."
    },
    {
        "index": 289,
        "id": "A2150/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "10JUL26 17:30 - 19FEB27 17:30",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10JUL26 17:30 - 19FEB27 17:30 KDLH A2150/26\nE) IAP DULUTH INTL, DULUTH, MN. ILS OR LOC RWY 9, AMDT 22B...\nILS OR\nLOC RWY 27, AMDT 12... VOR OR TACAN RWY 3, AMDT 21C... ILS\nRWY 9 (SA\nCAT I), AMDT 22B... ILS RWY 9 (CAT II), AMDT 22B... DME\nREQUIRED\nEXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS,\nHIB VOR\nOUT OF SERVICE."
    },
    {
        "index": 290,
        "id": "A1941/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "07APR26 19:37 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07APR26 19:37 - UFN KDLH A1941/26\nE) DLH NAV ILS RWY 27 OM DECOMMISSIONED"
    },
    {
        "index": 291,
        "id": "A1744/26",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "27MAR26 15:05 - 06NOV26 15:05",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27MAR26 15:05 - 06NOV26 15:05 KDLH A1744/26\nE) DLH IAP DULUTH INTL, DULUTH, MN.\nILS OR LOC RWY 9, AMDT 22B...\nILS RWY 9 (SA CAT I), AMDT 22B...\nILS RWY 9 (CAT II), AMDT 22B...\nRADAR REQUIRED EXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV\nSYSTEM\nWITH GPS,\nPYKLA (DL) LOM OUT OF SERVICE."
    },
    {
        "index": 292,
        "id": "A1504/25",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "19MAY25 02:11 - 19MAY27 02:11",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "19MAY25 02:11 - 19MAY27 02:11 KDLH A1504/25\nE) DLH IAP DULUTH INTL, DULUTH, MN.\nRNAV (GPS) RWY 3, ORIG-B...\nLNAV MDA 1900/HAT 480 ALL CATS. VIS CAT C/D 1 3/8. CIRCLING \nCAT\nA/B 1920/HAA 492.\nPage 61"
    },
    {
        "index": 293,
        "id": "A1502/25",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "16MAY25 13:23 - 26MAY27 13:23",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "16MAY25 13:23 - 26MAY27 13:23 KDLH A1502/25\nE) DLH IAP DULUTH INTL, DULUTH, MN.\nRNAV (GPS) RWY 9, AMDT 1D...\nLNAV MDA 1920/HAT 492 ALL CATS, LNAV VIS CAT C RVR 5000, \nCIRCLING\nCAT A/B MDA 1920/HAA 492..\n◼ APPROACH LIGHT"
    },
    {
        "index": 294,
        "id": "A1788/24",
        "station": "KDLH",
        "airportName": "덜루스 국제공항 (ERA)",
        "validPeriod": "01AUG24 16:57 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01AUG24 16:57 - UFN KDLH A1788/24\nE) DLH RWY 09 ALS U/S CANCELED)\n[ERA]CYYZ/ YYZ/ Toronto Lester B Pearson Intl, Toronto, CA\n1. RUNWAY : 05/23 : 11120FT X 200FT 15L/33R : 11050FT X 200FT\n06L/24R : 9697FT X 200FT 15R/33L : 9088FT X 200FT\n06R/24L : 9000FT X 200FT\n◼ RUNWAY"
    },
    {
        "index": 295,
        "id": "D3089/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "11AUG26 04:01 - 13AUG26 10:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "11AUG26 04:01 - 13AUG26 10:00 CYYZ D3089/26\nD) DAILY 0401-1000\nE) RWY 05/23 CLSD.\nCOMMENT) MAIN RWY CLSD"
    },
    {
        "index": 296,
        "id": "D3085/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "10AUG26 14:00 - 10AUG26 18:00",
        "category": "RUNWAY",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 14:00 - 10AUG26 18:00 CYYZ D3085/26\nE) RWY 15R/33L CLSD.\nCOMMENT) CODE F A/C USING RWY"
    },
    {
        "index": 297,
        "id": "D2552/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "09JUL26 16:05 - 09OCT26 15:00",
        "category": "TAXIWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 16:05 - 09OCT26 15:00 CYYZ D2552/26\nE) DUE CONST: STAND 181 LEAD-IN LINE POSITION MODIFIED.\nVISUAL DOCKING GUIDANCE SYSTEM NOT AVBL.\nACFT TO TRANSITION FM STARTBOX 9C TO LEAD-IN\nLINE TRIANGLE THEN STRICT ADHERANCE ALONG LEAD-IN LINE."
    },
    {
        "index": 298,
        "id": "D2079/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "09JUN26 20:55 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUN26 20:55 - UFN CYYZ D2079/26\nE) AMEND PUBLICATIONS:\nRWY DATA: TWY:\nADD: TWY V: ACFT WITH WINGSPANS 214FT AND GREATER NOT AUTH\nBTWN\nTWY E AND TWY F\nTAXI CHART: NOTES: RESTRICTIONS:\nADD: ACFT WITH WINGSPANS 214FT AND GREATER NO TAXIING ON TWY V\nBTWN TWY E AND TWY F"
    },
    {
        "index": 299,
        "id": "S0366/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "10AUG26 06:05 - 10AUG26 14:05",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 06:05 - 10AUG26 14:05 CYYZ S0366/26\nE) RSC 05 6/6/6 DRY, DRY, DRY. VALID AUG 10 0605 - AUG 10\n1405.\nRSC 23 6/6/6 DRY, DRY, DRY. VALID AUG 10 0605 - AUG 10 1405.\nRSC 06L 6/6/6 DRY, DRY, DRY. VALID AUG 10 0605 - AUG 10 1405.\nRSC 24R 6/6/6 DRY, DRY, DRY. VALID AUG 10 0605 - AUG 10 1405.\nRSC 06R 6/6/6 DRY, DRY, DRY. VALID AUG 10 0604 - AUG 10 1404.\nPage 62\nRSC 24L 6/6/6 DRY, DRY, DRY. VALID AUG 10 0604 - AUG 10 1404.\nRSC 15L 6/6/6 DRY, DRY, DRY. VALID AUG 10 0605 - AUG 10 1405.\nRSC 33R 6/6/6 DRY, DRY, DRY. VALID AUG 10 0605 - AUG 10 1405.\nRSC 15R 6/6/6 DRY, DRY, DRY. VALID AUG 10 0605 - AUG 10 1405.\nRSC 33L 6/6/6 DRY, DRY, DRY. VALID AUG 10 0605 - AUG 10 1405.\nADDN NON-GRF/TALPA INFO:\n◼ NAVAID"
    },
    {
        "index": 300,
        "id": "G2601/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "02AUG26 16:40 - 19AUG26 23:59",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02AUG26 16:40 - 19AUG26 23:59 CYYZ G2601/26\nE) PEARSON (TORONTO/LBP INTL) VOR YTP 116.55MHZ U/S\n◼ APPROACH"
    },
    {
        "index": 301,
        "id": "D3067/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "07AUG26 13:15 - 15AUG26 03:30",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 13:15 - 15AUG26 03:30 CYYZ D3067/26\nE) SID (RNAV) GOPUP FOUR DEP:\nSLLAP TRANSITION: NOT AUTH. FILE HOCKE TRANSITION.\n.\nSID (RNAV) TULEK FOUR DEP:\nSLLAP TRANSITION: NOT AUTH. FILE HOCKE TRANSITION.\n.\nSID (RNAV) NOSIK FOUR DEP: NOT AUTH.\nFILE SID (RNAV) TULEK FOUR DEP: HOCKE TRANSITION\n.\nSID (RNAV) URSAL FOUR DEP: NOT AUTH.\nFILE SID (RNAV) GOPUP FOUR DEP: HOCKE TRANSITION\n.\nSTAR (RNAV) NAKBO SIX ARR:\nMONEE AND YZEMN TRANSITION: NOT AUTH. FILE QWERI TRANSITION.\n.\nSTAR (RNAV) NUBER SIX ARR:\nMONEE AND YZEMN TRANSITION: NOT AUTH. FILE QWERI TRANSITION."
    },
    {
        "index": 302,
        "id": "D3013/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "03AUG26 18:05 - 14AUG26 23:59",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "03AUG26 18:05 - 14AUG26 23:59 CYYZ D3013/26\nE) ILS CAT II AND CAT III APCH RWY 05 NOT AUTH"
    },
    {
        "index": 303,
        "id": "D2003/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "05JUN26 18:36 - 28AUG26 18:00",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "05JUN26 18:36 - 28AUG26 18:00 CYYZ D2003/26\nE) RNAV (GNSS) Z RWY 15R APCH:\nLNAV/VNAV MINIMA: NOT AUTH\nLNAV MINIMA TO READ: 1040 (489) 1 RVR 50\nDIST/ALT TABLE: LAST ALT TO READ 1.4/1040 INSTEAD OF 1.2/980"
    },
    {
        "index": 304,
        "id": "D1308/26",
        "station": "CYYZ",
        "airportName": "토론토 피어슨 국제공항 (ERA)",
        "validPeriod": "23APR26 15:20 - UFN",
        "category": "RUNWAY",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "23APR26 15:20 - UFN CYYZ D1308/26\nE) AMEND PUBLICATIONS: ILS RWY 24L APCH:\nLOC/DME MINIMA TO READ: 1040 (493) 1 RVR 50\n[ERA]KBOS/ BOS/ Boston Edward L Logan Intl Airport, Boston, US\nSEE THE SAME AIRPORT IN PACKAGE 1\n[ERA]KJFK/ JFK/ John F Kennedy International Airport, New York,\nUS\nSEE THE SAME AIRPORT IN PACKAGE 1\nPage 63\nPage 64\n[FIR] RKRR/ Incheon, KR\nOZ 224 ICN/JFK PRINTED AT 10AUG26 0726Z\nFIR: RKRR RJJJ PAZA CZEG CZWG CZYZ KZBW KZNY\n◼ COMPANY ADVISORY"
    },
    {
        "index": 305,
        "id": "COAD01/20",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "01MAY20 16:01 - UFN",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1. 01MAY20 16:01 - UFN RKRR COAD01/20\n*** RKRR GPS UNRELIABLE ADVISORY INFO *** ADVISORY INFORMATION FOR\nAIRCRAFT OPERATING IN INCHEON FIR : THERE S POSSIBLE TO GPS SIGNALS\nUNRELIANBLE DUE TO MIL EXCERCISE IF A/C HAD GPS SIGNAL INTERRUPTED\nPLEASE DO REPORT TO ATC VIA RADIO OR WIRE 032-880-0247/8\n-- BY SELOP--\n◼ NAVAID"
    },
    {
        "index": 306,
        "id": "Z0479/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "08JUL26 16:00 - 31AUG26 16:00",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "보조 항법/통신 시설 점검 (RNAV/GNSS 운항 정상)",
        "rawText": "08JUL26 16:00 - 31AUG26 16:00 RKRR Z0479/26\nE) VORTAC SOT 116.900MHZ/CH116X U/S DUE TO REPLACEMENT\n1. USE 3705N12701E INSTEAD OF SOT\n2. CAN NOT USE DME/DME NAVIGATION ON AIRWAY USING SOT AS\nCRITICAL DME\n3. NON-RNAV ACFT REQUEST RADAR VECTOR TO DAEGU / INCHEON ACC\nBEFORE FLYING ON THE AIRWAYS WITHIN THE SOT COVERAGE"
    },
    {
        "index": 307,
        "id": "Z0285/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "10JUN26 16:00 - 31DEC26 16:00",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "보조 항법/통신 시설 점검 (RNAV/GNSS 운항 정상)",
        "rawText": "10JUN26 16:00 - 31DEC26 16:00 RKRR Z0285/26\nE) TRIGGER NOTAM - AIRAC AIP SUP 40/26\nWEF 1600 UTC 10 JUN 2026 TIL 1600 UTC 31 DEC 2026\n- THE BUSAN VORTAC(PSN) WILL BE UNSERVICEABLE DUE TO\nREPLACEMENT.\nCOMMENT) RMK\n1. A/C with RNAV Capability IS NOT affected by using Airway\n2. DME/DME NAV NOT AVBL ON AWY USING 'PSN' AS CRITICAL DME.\n3. RKPK DEPARTURE PROCEDURES (SID) AMENDED AS FLW DUE TO PSN\nU/S:\n- RWY 36L/R BEVSI 3: KALOD, PSN, TOPAX TRANSITION NOT AVBL.\n  EXPECT RADAR VECTOR AFTER BEVSI.\n- RWY 36L/R SOORO 2: KALOD, PSN, TOPAX, BESNA, ENGOT TRANSITION\nNOT\n  AVBL. EXPECT RADAR VECTOR AFTER SOORO.\n- RWY 18L/R ULSUK 3: SAPDI, PSN TRANSITION NOT AVBL.\n  EXPECT RADAR VECTOR AFTER ULSUK.\n- RWY 18L/R BAHDA 2: KALEK, INVOK, APELA, PSN, TOPAX, ENGOT,\nBESNA\n  TRANSITION NOT AVBL. EXPECT RADAR VECTOR AFTER BAHDA.\n◼ COMMUNICATION"
    },
    {
        "index": 308,
        "id": "CHINA",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "24MAR23 16:00 - UFN",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24MAR23 16:00 - UFN RKRR CHINA SUP 16/21\nE) [ NEW ATS ARRANGEMENT FOR AKARA-FUKUE CORRIDOR ] \n // TRANSFER OF CONTROL // \n - ATS FOR WB TRAFFIC WILL BE TRANSFERRED FROM \nPage 65\n   INCHEON ACC TO SHANGHAI ACC AT FIX SADLI ON FREQUENCY\n   120.95MHZ (PRIMARY) OR 134.00MHZ (SECONDARY) \n- ATS FOR EB TRAFFIC TO THE DIRECTIONS OF CJU \n   AND BEYOND WILL BE TRANSFERRED FROM SHANGHAI ACC TO INCHEON\n   ACC AT 125E LONGITUDE ON FREQUENCY 124.525MHZ (PRIMARY) \n   OR 132.200MHZ (SECONDARY) \n- ATS FOR EB TRAFFIC TO THE OTHER DIRECTIONS WILL \n  BE TRANSFERRED FROM SHANGHAI ACC TO INCHEON ACC AT FIX \n  SADLI OR 125E LONGITUDE ON FREQUENCY 123.725MHZ \n // COMMUNICATIONS//\n - TRAFFIC OPERATING IN THE CORRIDOR AIRSPACE SHALL MAINTAIN A\n   CONSTANT WATCH ON THE APPROPRIATE FREQUENCY OF SHANGHAI\nACC \n   IN THE WEST OF 125E LONGITUDE AND INCHEON ACC IN THE EAST OF\n   125E LONGITUDE UNLESS OTHERWISE INSTRUCTED BY ATC \n   (DO NOT CONFUSE WITH FUKUOKA ACC)\nCOMMENT) ATS TRANSFER INFO (INCHEON & SHANGHAI ACC) IN AKARA-\nFUKUE CORRIDOR\n◼ GPS"
    },
    {
        "index": 309,
        "id": "Z0555/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "30JUL26 07:02 - 31AUG26 15:00",
        "category": "LIGHTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30JUL26 07:02 - 31AUG26 15:00 RKRR Z0555/26\nE) CAUTIONARY INFORMATION FOR AIRCRAFT OPERATING IN INCHEON FIR\n:\nPILOTS HAVE REPORTED THAT GPS SIGNALS ARE UNRELIABLE OR LOST\nINTERMITTENTLY IN INCHEON FIR.\nEXERCISE EXTREME CAUTION WHEN USING GPS.\n◼ AIRWAY"
    },
    {
        "index": 310,
        "id": "Z0575/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "10AUG26 13:00 - 10AUG26 21:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 13:00 - 10AUG26 21:00 RKRR Z0575/26\nE) CONDITIONAL ROUTE(CDR2) AVBL AS FLW, NEW\nNR ROUTE        TIME FM    TIME TO     LOWER LVL      UPPER LVL\n1 MASTA-UPGOS   08101300   08102045    6,000FT AMSL   FL600\n2 RUGMA-ANROD   08101300   08102100    11,000FT AMSL  FL600\n3 BOPTA-PONIK   08101300   08102045    FL150          FL600\n4 KARBU-LANAT   08101300   08102100    FL150          FL600\nCOMMENT) PLEASE REQUEST BOPTA DIRECT PONIK(OR KARBU DIRECT\nLANAT) TO THE ATC\nDUE TO UNEXPECTED CHANGES, NOT APPLIED TO FPL.\nTHIS IS COORDINATED WITH THE ACC.\n◼ AIRSPACE"
    },
    {
        "index": 311,
        "id": "D2261/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "09AUG26 23:00 - 15AUG26 09:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 23:00 - 15AUG26 09:00 RKRR D2261/26\nD) 09 2300-2359, 10-13 0000-0100 0600-1100 2300-2359, 14\n0000-0100\n0600-1100, 15 0000-0900\nE) CATA 7H ACT\nF)2500FT AGL G)5000FT AMSL"
    },
    {
        "index": 312,
        "id": "D1768/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "26JUN26 15:00 - 26SEP26 14:59",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "26JUN26 15:00 - 26SEP26 14:59 RKRR D1768/26\nE) TEMPO PROHIBITED AREA ACT AS FLW :\n1. AREA : A CIRCLE RADIUS 2NM CENTERED ON 373523N1265832E\n2. RMK\n- EXC SKED CIV ACFT AND INFO ASSET FLT\nPage 66\n[FIR] RJJJ/ Fukuoka, JP\n- EMERG ACFT(FIRE FIGHTING, LIFEGUARD, ETC) OPERATION NEED\nPRIOR PERMISSION FROM CAPITAL DEFENSE COMMAND (02-524-0315)\nF)SFC G)UNL\nCOMMENT) NO COMPANY RTE INCLUDED"
    },
    {
        "index": 313,
        "id": "E3432/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "09JUL26 23:00 - 30SEP26 10:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09JUL26 23:00 - 30SEP26 10:00 RKRR E3432/26\nD) 2300-1000\nE) TEMPO RESTRICTED AREA ACT AS FLW AREA BOUNDED BY THE\nFOLLOWING\n352027N1274805E-352027N1281626E-345118N1281626E-345118N1274805E-\n352027N1274805E\nF)20000FT AMSL G)43000FT AMSL\nCOMMENT) INCLUDE HIN\n◼ OTHER"
    },
    {
        "index": 314,
        "id": "Z0391/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "10JUN26 19:30 - 09SEP26 22:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10JUN26 19:30 - 09SEP26 22:00 RKRR Z0391/26\nD) 1930-2200\nE) FLOW CTL AS FLW\n1. RTE : A593 VIA SADLI\n2. ACFT : LANDING RKRR\n3. PROC : FL330 AT OR BELOW AVBL, 5 MIN SEPARATION AT SAME\nALTITUDE"
    },
    {
        "index": 315,
        "id": "Z0390/26",
        "station": "RKRR",
        "airportName": "인천 FIR (Incheon Oceanic/Control)",
        "validPeriod": "10JUN26 19:30 - 09SEP26 22:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10JUN26 19:30 - 09SEP26 22:00 RKRR Z0390/26\nD) 1930-2200\nE) FLOW CTL AS FLW\n1. RTE : Y722/B576 VIA ATOTI\n2. ACFT : ENTERING RKRR\n3. PROC : FL390 NOT AVBL\n◼ AIRWAY"
    },
    {
        "index": 316,
        "id": "Q1893/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "10AUG26 21:00 - 11AUG26 21:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 21:00 - 11AUG26 21:00 RJJJ Q1893/26\nE) CDR ARE ESTABLISHED AS FLW,\nRTE         PERIOD                 MNM APPLICABLE ALT\n1)  Z29         2608111500/2608112100  MEA\n2)  Z31         2608111500/2608112100  MEA\n3)  Z32         2608111500/2608112100  MEA\n4)  Z34         2608111500/2608112100  MEA\nRMK: REF AIP ENR3.3"
    },
    {
        "index": 317,
        "id": "Q1892/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "10AUG26 07:00 - 10AUG26 21:00",
        "category": "AIRSPACE / ROUTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 07:00 - 10AUG26 21:00 RJJJ Q1892/26\nE) EASTBOUND PACOTS TRACKS BETWEEN SOUTHEAST ASIA AND NORTH\nAMERICA,\nTRACK 14.\nFLEX ROUTE : EMRON 40N160E 43N170E 44N180E 44N170W 43N160W\n42N150W 40N140W 38N130W ALLBE\nRCTP/VHHH ROUTE : MOLKA M750 MUKEP Y891 OVSUN Y893 IGMIS Y57\nPOROT\nOTR11 AVBET OTR9 EMRON\nNAR ROUTE : ACFT LDG KSFO--ALLBE PIRAT OSI KSFO\nACFT LDG KLAX--ALLBE PIRAT BURGL IRNMN KLAX\nRMK : TRK 15 NOT AVAILABLE\nATM CENTER TEL:81-92-608-8870\nPage 67"
    },
    {
        "index": 318,
        "id": "Q1891/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "10AUG26 10:00 - 10AUG26 21:00",
        "category": "LIGHTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 10:00 - 10AUG26 21:00 RJJJ Q1891/26\nE) EASTBOUND PACOTS TRACKS BETWEEN JAPAN AND HAWAII,\nTRACK 11.\nFLEX ROUTE : SEALS 35N150E 34N160E 33N170E 30N180E 27N170W DANNO\nJAPAN ROUTE : LAPIL OTR13 SEALS\nPHNL ROUTE : DANNO BOOKE PHNL\nRMK : TRK 11 NOT AVAILABLE IF CROSSING DANNO AFTER 1830Z.\nTRACK 12.\nFLEX ROUTE : SEALS 35N150E 34N160E 33N170E 30N180E 27N170W SYVAD\nJAPAN ROUTE : LAPIL OTR13 SEALS\nPHNL ROUTE : SYVAD BOOKE PHNL\nRMK : ATM CENTER TEL:81-92-608-8870"
    },
    {
        "index": 319,
        "id": "Q1890/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "10AUG26 05:00 - 10AUG26 21:00",
        "category": "AIRSPACE / ROUTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 05:00 - 10AUG26 21:00 RJJJ Q1890/26\nE) EASTBOUND PACOTS TRACKS BETWEEN JAPAN AND NORTH AMERICA,\nTRACK 1.\nFLEX ROUTE : OMOTO R580 OPHET PLADO CHIKI 51N170W 51N160W\n50N150W\n49N140W PRETY\nJAPAN ROUTE : MAKMU R580 OMOTO\nNAR ROUTE : ACFT LDG KSEA/KPDX--PRETY TOU KSEA/KPDX\nACFT LDG CYVR--PRETY GOVAD CYVR\nRMK : ACFT LDG OTHER DEST--PRETY UPR TO DEST\nTRACK 2.\nFLEX ROUTE : ADGOR AGEDI AKISU ASPIN LYYLE 50N180E 49N170W\n48N160W\n47N150W 45N140W 42N130W VESPA\nJAPAN ROUTE : ADNAP R591 ADGOR\nNAR ROUTE : ACFT LDG KSFO--VESPA AMAKR BGGLO KSFO\nACFT LDG KLAX--VESPA ENI OAK BURGL IRNMN KLAX\nTRACK 3.\nFLEX ROUTE : EMRON 42N160E 44N170E 45N180E 45N170W 44N160W\n43N150W\n41N140W 39N130W DACEM\nJAPAN ROUTE : AVBET OTR9 EMRON\nNAR ROUTE : ACFT LDG KLAX--DACEM PAINT PIRAT BURGL IRNMN KLAX\nACFT LDG KSFO--DACEM PAINT PIRAT OSI KSFO\nRMK : ATM CENTER TEL:81-92-608-8870"
    },
    {
        "index": 320,
        "id": "Q1889/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 22:00 - 10AUG26 22:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 22:00 - 10AUG26 22:00 RJJJ Q1889/26\nE) CDR ARE ESTABLISHED AS FLW,\nRTE         PERIOD                 MNM APPLICABLE ALT\n1)  L512        2608101200/2608102200  MEA\n2)  Z13         2608101200/2608102200  MEA\n3)  Z14         2608101200/2608102200  MEA\n4)  Z25         2608101330/2608101910  MEA\n5)  Z26         2608101330/2608101910  MEA\n6)  Z27         2608101330/2608101910  MEA\n7)  Z40         2608092200/2608102200  MEA\n8)  Z41         2608092200/2608101910  MEA\n9)  Z262        2608101330/2608102200  MEA\nRMK: REF AIP ENR3.3"
    },
    {
        "index": 321,
        "id": "Q1888/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 21:00 - 10AUG26 21:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 21:00 - 10AUG26 21:00 RJJJ Q1888/26\nE) CDR ARE ESTABLISHED AS FLW,\nRTE         PERIOD                 MNM APPLICABLE ALT\nPage 68\n1)  Z16         2608101300/2608102100  MEA\n2)  Z17         2608092100/2608092200  MEA\nZ17         2608101300/2608102100  MEA\n3)  Z18         2608092100/2608092200  MEA\nZ18         2608101300/2608102100  MEA\n4)  Z21         2608092100/2608092200  MEA\nZ21         2608101200/2608102100  MEA\n5)  Z101        2608101300/2608102100  MEA\n6)  Z102        2608101300/2608102100  MEA\n7)  Z162        2608092100/2608092200  MEA\nZ162        2608101300/2608102100  MEA\n8)  Z171        2608092100/2608092200  MEA\nZ171        2608101200/2608102100  MEA\n9)  Z182        2608092100/2608092200  MEA\nZ182        2608101200/2608102100  MEA\nRMK: REF AIP ENR3.3"
    },
    {
        "index": 322,
        "id": "Q1887/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 21:00 - 10AUG26 21:00",
        "category": "AIRSPACE / ROUTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 21:00 - 10AUG26 21:00 RJJJ Q1887/26\nE) CDR ARE ESTABLISHED AS FLW,\nRTE         PERIOD                 MNM APPLICABLE ALT\n1)  Z29         2608101500/2608102100  MEA\n2)  Z31         2608101500/2608102100  MEA\n3)  Z32         2608101500/2608102100  MEA\n4)  Z34         2608101500/2608102100  MEA\nRMK: REF AIP ENR3.3\n◼ AIRSPACE"
    },
    {
        "index": 323,
        "id": "P3916/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 09:11 - 10AUG26 20:56",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 09:11 - 10AUG26 20:56 RJJJ P3916/26\nE) ROCKET H3(QZS-7) WILL BE LAUNCHED\nLAUNCHING DATE AND TIME : BTN 2608101923 AND 2608102023\nRMK: REF AIP SUP 104/26 ITEM 1,2,3\nF)SFC G)UNL\nCOMMENT) AFFECTED RTE AS FLW :\n*G339(KALGU-TGE) & Y208(LUKRA-SASIK)\n(In-Bound)\nAKL/ICN(P10,P05,P04,P02,P01,P03,UO07,W02)\nBNE/ICN(P12,P13,P08,P07,P02,P01,P17,P03,P09,UO08,UO07,N02,N08,\nN09)\nCNS/ICN(P05,P04,P02,P01,P03)\nGUM/ICN(P04,P01,R01,UO07,UO08,W01A,W01,T01U)\nGUM/PUS(P04,P01) MEL/ICN(P04,P03,P02,P01) NAN/ICN(P01)\nROR/ICN(P01)\nSYD/ICN(P06,P13,P08,P07,P01,P17,P03,P09,UO06,UO08,UO07,N01,N03Z,\nN03,T\n01)\nBKK/ICN(W70) BKK/PUS(W70) CEB/ICN(W70) CGK/ICN(W70)\nCRK/ICN(W70) CTS/ICN(W02X) CXR/ICN(W70) DAD/ICN(W70)\nDAD/PUS(W70) DPS/ICN(W70,T02E,T03E,V01,V03)\nHKG/ICN(W75B,W75A) HKT/ICN(W70) KUL/ICN(W70) MNL/ICN(W70)\nPEN/ICN(W70) PNH/ICN(W70) SGN/ICN(W70) SIN/ICN(W70)\nTPE/ICN(W70A,W70B,W70) TPE/PUS(W70A,W70B,W70) DPS/PUS(V01)\n*G339(KALGU-TGE)\n(Out-Bound)\nCJU/GUM(P01)\nPage 69\nICN/AKL(P06,P05,P10,P11,P08,P07,P04,P02,P01,P03,P09,UO07)\nICN/BNE(P05,P03,P13,P02,P01,P16,P15,P06,UO08,UO07)\nICN/CNS(P05,P04,P02,P01,P03)\nICN/GUM(P04,P01,R01,UO07A,UO07,UO09,UO08,W03)\nICN/MEL(P05,P03,P04,P02,P01,P06) ICN/ROR(P01)\nICN/SYD(P06,P05,P11,P12,P08,P07,P02,P01,P16,P15,P03,P09,UO07,\nUO08,N02\n,N02Z)\nPUS/GUM(P01) ICN/BKK(W70) ICN/CEB(W70) ICN/CGK(W70)\nICN/CRK(W70) ICN/CXR(W70) ICN/DAD(W70)\nICN/DPS(W70,T02E,T03E,V01) ICN/HKG(W75A) ICN/HKT(W70)\nICN/KTI(W70) ICN/KUL(W70) ICN/MNL(W70) ICN/PEN(W70)\nICN/PQC(W70) ICN/SGN(W70) ICN/SIN(W70)\nICN/TPE(W70A,W70B,W70) PUS/TPE(W70A,W70B,W70)\n(In-Bound)\nGUM/CJU(P01) SYD/ICN(P12,N13) DPS/CJU(V01) GUM/KMI(A01)\n*A337(DAGDA-TEGOD)\n(In-Bound)\nAKL/ICN(P08,P07) BNE/ICN(P16) SYD/ICN(P16)\n*B586(CADDY-VASKO)\n(Out-Bound)\nICN/AKL(P13) ICN/BNE(P04)  ICN/GUM(P02)\nICN/SYD(P04)\n(In-Bound)\nGUM/ICN(P03)\n*DCT(25E42-UKATA)\n(Out-Bound)\nICN/SYD(P04)\n*DCT(25E46-NOGAK)\n(In-Bound)\nAKL/ICN(P07)\n*DCT(26E46-NOGAK)\n(In-Bound)\nAKL/ICN(P08)\n*DCT(32E45-TOMOL)\n(In-Bound)\nANC/PUS(T01,T02)\n*DCT(34E50-TOMOL)\n(In-Bound)\nANC/PUS(T04) LAX/ICN(T01)\n*DCT(35E50-TOMOL)\n(Out-Bound)\nICN/LAX(T01) ICN/YVR(T10)\n*DCT(36E50-TOMOL)\n(In-Bound)\nSEA/ICN(T01)\n*DCT(37E50-TOMOL)\n(In-Bound)\nKSUU/PUS(T01) PAE/ICN(T01) SEA/ICN(T01J)\nPage 70\n*DCT(MORAY-TOMOL)\n(In-Bound)\nANC/GMP(T01)"
    },
    {
        "index": 324,
        "id": "P3764/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 23:00 - 15AUG26 15:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 23:00 - 15AUG26 15:00 RJJJ P3764/26\nD) 2300/1500\nE) MULTIPLE U.S. MIL ACT WILL BE CONDUCTED WI FUKUOKA FIR AS\nFLW,\nAREA: BOUNDED BY FLW POINTS\n262209N1283442E - 264724N1290402E - 273846N1303351E -\n273835N1305554E\n- 273741N1320215E - 272637N1315941E - 261056N1305036E -\n262209N1283442E\nATC WILL NOT CLEAR NON-PARTICIPATING IFR FLT THRU THIS AREA.\nRMK: MISSION NAME : TIGER-CENTER\nF)SFC G)FL600\nCOMMENT) AFFECTED RTE :DCT(AVLAS..ONC) : GUM/ICN(P06)"
    },
    {
        "index": 325,
        "id": "P3760/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 23:00 - 15AUG26 15:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 23:00 - 15AUG26 15:00 RJJJ P3760/26\nD) 2300/1500\nE) MULTIPLE U.S. MIL ACT WILL BE CONDUCTED WI FUKUOKA FIR AS\nFLW,\nAREA: BOUNDED BY FLW POINTS\n254423N1303001E - 254239N1305528E - 250914N1302929E -\n245628N1301753E\n- 243950N1293955E - 254423N1303001E\nATC WILL NOT CLEAR NON-PARTICIPATING IFR FLT THRU THIS AREA.\nRMK: MISSION NAME EAGLE-EAST\nF)SFC G)FL600\nCOMMENT) AFFECTED RTE AS FLW :\n*DCT(AVLAS-ONC): GUM/ICN(P06)\n*Y78(GORIN-TEKOS)\n(Out-Bound)\nICN/GUM(P03) ICN/SYD(P13)\n(In-Bound)\nAKL/ICN(P09) BNE/ICN(P05) SYD/ICN(P05)"
    },
    {
        "index": 326,
        "id": "P3759/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 23:00 - 15AUG26 15:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 23:00 - 15AUG26 15:00 RJJJ P3759/26\nD) 2300/1500\nE) MULTIPLE U.S. MIL ACT WILL BE CONDUCTED WI FUKUOKA FIR AS\nFLW,\nAREA: BOUNDED BY FLW POINTS\n255335N1283000E - 254837N1290219E - 254415N1292552E -\n254445N1302413E\n- 254423N1303001E - 243950N1293955E - 242328N1292737E -\n253107N1280953E - 255335N1283000E,\nTHE LINE CONNECTING 253107N1280953E TO 255335N1283000E IS THE\nMINOR\nARC WITH A RADIUS OF 50NM FM 261230N1273834E.\nATC WILL NOT CLEAR NON-PARTICIPATING IFR FLT THRU THIS AREA.\nRMK: MISSION NAME EAGLE-CENTER\nF)SFC G)FL600\nCOMMENT) AFFECTED RTE AS FLW :\n*DCT(AVLAS-ONC): GUM/ICN(P06)\n*Y78(AZAMA-GORIN)\n(Out-Bound)\nPage 71\nICN/GUM(P03) ICN/SYD(P13)\n(In-Bound)\nAKL/ICN(P09) BNE/ICN(P05) SYD/ICN(P05)"
    },
    {
        "index": 327,
        "id": "P3718/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "31JUL26 21:00 - 31AUG26 15:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "31JUL26 21:00 - 31AUG26 15:00 RJJJ P3718/26\nD) 2100/1500\nE) REF AIP PAGE ENR5.1-9 WARNING AREA W-173(HOTEL HOTEL)\nHOURS OF OPERATION TEMPO CHANGE\n2100/1500 UTC\nINSTEAD OF\n2100/1100 UTC\nF)SFC G)UNL\nCOMMENT) AFFECTED RTE AS FLW :\n*DCT(AVLAS-ONC): GUM/ICN(P06)"
    },
    {
        "index": 328,
        "id": "Q1772/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "05AUG26 15:00 - 19AUG26 15:00",
        "category": "NAVAID",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "행정/AIP SUP 발효 고지 (차트 반영 완료)",
        "rawText": "05AUG26 15:00 - 19AUG26 15:00 RJJJ Q1772/26\nE) TRIGGER NOTAM-AIRAC AIP SUP NR172/26\nWEF 03 SEP 2026 TIL 17 FEB 2027\nUNSERVICEABILITY AND ALTERNATE PROCEDURES OF ISHIGAKIJIMA\nVOR/DME\n(IGE)\nTEMPORARY ESTABLISHMENT OF REPORTING POINT\nTEMPORARY CHANGE OF REPORTING POINTS\nTEMPORARY ESTABLISHMENT OF DIRECT ROUTES\nTEMPORARY CHANGE OF EN-ROUTE HOLDING\n◼ OTHER"
    },
    {
        "index": 329,
        "id": "Y0898/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "10AUG26 02:44 - 10AUG26 16:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10AUG26 02:44 - 10AUG26 16:00 RJJJ Y0898/26\nE) FLOW CTL AS FLWS,\nAREA: ATS RTE\nB576/Y742/A1/Y74/R595/Y573/G581/Y26/Y52/A593/Y592/G585/Y206\nROC: EXP DEP CLR TIME WILL BE ISSUED TO ACFT FOR RCTP\nRMK: REF AIP ENR1.9-1"
    },
    {
        "index": 330,
        "id": "Y0896/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 14:59 - 10AUG26 16:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 14:59 - 10AUG26 16:00 RJJJ Y0896/26\nE) FLOW CTL AS FLWS,\nAREA: ATS RTE A593/Y592\nPROC: EXP DEP CLR TIME WILL BE ISSUED TO ACFT WB VIA ONIKU\nDETOURING\nAROUND TYPHOON DOLPHIN\nRMK: REF AIP ENR1.9-1"
    },
    {
        "index": 331,
        "id": "Y0895/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 09:55 - 10AUG26 16:00",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 09:55 - 10AUG26 16:00 RJJJ Y0895/26\nE) FLOW CTL AS FLWS,\nAREA: ATS RTE A1/G581/Y26/Y52\nPROC: EXP DEP CLR TIME WILL BE ISSUED TO ACFT VIA KABAM N892\nRMK: REF AIP ENR1.9-1"
    },
    {
        "index": 332,
        "id": "Z1322/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 23:40 - 10AUG26 16:00",
        "category": "AIRSPACE / ROUTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 23:40 - 10AUG26 16:00 RJJJ Z1322/26\nE) FLOW CTL AT FIR BDRY AS FLWS,\nRTE: B576/Y742\nACFT: SB FOR RCTP RCSS RCMQ RCKH\nPROC: AT FL370 OR ABV NOT AVBL AT ATOTI MUGUS\nRMK: REF AIP ENR1.9-1\nPage 72\n[FIR] PAZA/ Anchorage Continental, US"
    },
    {
        "index": 333,
        "id": "Z1321/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 14:36 - 10AUG26 16:00",
        "category": "AIRSPACE / ROUTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 14:36 - 10AUG26 16:00 RJJJ Z1321/26\nE) FLOW CTL AT FIR BDRY AS FLWS,\nRTE: B576/Y742\nACFT: SB FOR MANILA FIR VIA KABAM DEP FM KOREA\nPROC:(1) 12MIN INTERVAL REGARDLESS OF ALT WILL BE APPLIED AT\nATOTI OR\nMUGUS\n(2) ATOTI OR MUGUS ONLY AVBL DEP FM KOREA\nRMK: REF AIP ENR1.9-1"
    },
    {
        "index": 334,
        "id": "Z1311/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "09AUG26 00:44 - 10AUG26 16:00",
        "category": "AIRSPACE / ROUTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 00:44 - 10AUG26 16:00 RJJJ Z1311/26\nE) FLOW CTL AT FIR BDRY AS FLWS,\nRTE: A593/Y592\nACFT: WB FOR DETOURING TYPHOON DEP FM JAPAN\nPROC: 60MIN INTERVAL REGARDLESS OF ALT WILL BE APPLIED AT ONIKU."
    },
    {
        "index": 335,
        "id": "Z0810/26",
        "station": "RJJJ",
        "airportName": "후쿠오카 FIR (Fukuoka Control)",
        "validPeriod": "10JUN26 19:10 - 09SEP26 22:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10JUN26 19:10 - 09SEP26 22:00 RJJJ Z0810/26\nD) 1910/2200\nE) FLOW CTL AT FIR BDRY AS FLWS,\nRTE: B576/Y741/Y743\nACFT: NB ENTERING INCHEON FIR\nPROC: FL390 NOT AVBL AT SALMI AND LIPLO\nRMK: REF AIP ENR1.9-1\n◼ COMMUNICATION"
    },
    {
        "index": 336,
        "id": "A0044/24",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "13JAN24 23:00 - UFN",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "13JAN24 23:00 - UFN PAZA A0044/24\nE) REFERENCE CPDLC:\nANCHORAGE ARTCC IS EQUIPPED FOR CONTROLLER/PILOT DATA LINK\nCOMMUNICATIONS (CPDLC).  ANCHORAGE ARTCC AUTOMATION USES TWO\nDIFFERENT CPDLC LOGON ADDRESSES. WHEN PERFORMING MANUAL LOGONS,\nSELECT THE CORRECT LOGON ADDRESS BASED UPON CURRENT ACFT\nLOCATION\nAS FOLLOWS:\nUSE LOGON ADDRESS PAZN WHEN OPERATING IN THE ANCHORAGE OCEANIC\nFLIGHT INFORMATION REGION (FIR) AND WHEN IN THAT PORTION OF THE\nANCHORAGE ARCTIC FIR ABV 73N LATITUDE (OVER OR N OF WAYPOINTS\nBIITE AND BARIP) AND IN THAT PORTION OF THE ANCHORAGE\nCONTINENTAL\nFIR W OF A LINE FM 57N152W TO 58N167W TO 63N174W.\nUSE LOGON ADDRESS PAZA WHEN OPERATING IN THE ANCHORAGE ARCTIC\nFIR\nS OF 73N LATITUDE (OVER OR SOUTH OF WAYPOINTS PILUN AND TAYTA)\nAND\nIN THE ANCHORAGE CONTINENTAL FIR E OF A LINE FM 57N152W TO\n58N167W\nTO 63N174W.\nACFT DEP ALASKAN AP ARE REQUESTED TO LOGON AFTER DEP BUT BEFORE\nCLIMBING ABV FL180. USE OF CPDLC DOES NOT RELEASE FLT CREWS\nFM HF OR VHF MONITORING/COMMUNICATION REQUIREMENTS. ACFT WI VHF\nCOVERAGE MAY MAKE POSITION REPORTS VIA CPDLC COMMUNICATIONS.\nREQUESTS TO ATC SHOULD BE MADE OVER VHF IF WI VHF COVERAGE.\nAFTER\nLOGON, ARTCC AUTOMATION WILL PROVIDE AUTOMATIC FANS ADDRESS\nFORWARDING BTN PAZA/PAZN AND TO RJJJ, GDXB, CZVR, CZEG, AND\nPage 73\nKZAK.\nREFER QUESTIONS TO ANCHORAGE ARTCC INTL PROCEDURES TEL\n907-269-1108.\nF) SFC\nG) FL600)\nCOMMENT) ANC ARTCC CPDLC LOGON INSTRUCTION (PAZN / PAZA)\n◼ AIRWAY"
    },
    {
        "index": 337,
        "id": "A2312/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "28JUL26 17:20 - 28JUL28 17:02",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "28JUL26 17:20 - 28JUL28 17:02 PAZA A2312/26\nE) AK..ROUTE ZAN. V317 ZARUT, AK TO COP MEA 13000. LVD VOR/DME\nR-306\nUNUSABLE BELOW 13000."
    },
    {
        "index": 338,
        "id": "A2227/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "01JUL26 00:00 - 01JUL28 13:29",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01JUL26 00:00 - 01JUL28 13:29 PAZA A2227/26\nE) AK..ROUTE ZAN. Q41 CAWIN, AK TO DEADHORSE (SCC) VOR/DME, AK\nNA."
    },
    {
        "index": 339,
        "id": "A2202/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "15JUN26 15:59 - 15JUN28 15:59",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "15JUN26 15:59 - 15JUN28 15:59 PAZA A2202/26\nE) AK..ROUTE ZAN. V311 FLIPS, AK TO BIORKA ISLAND (BKA) VORTAC,\nAK\nMEA 6300 WESTBOUND."
    },
    {
        "index": 340,
        "id": "A2173/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "08JUN26 15:37 - 08JUN28 15:37",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "08JUN26 15:37 - 08JUN28 15:37 PAZA A2173/26\nE) AK..ROUTE ZAN. V473 FLIPS, AK TO BIORKA ISLAND (BKA) VORTAC,\nAK\nMEA 6300 WESTBOUND."
    },
    {
        "index": 341,
        "id": "A2092/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "02JUN26 16:16 - 02JUN28 16:13",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02JUN26 16:16 - 02JUN28 16:13 PAZA A2092/26\nE) AK..ROUTE ZAN. V453 VUSUY, AK TO WAPRO, AK NA. UNK VOR R-175\nRESTRICTED."
    },
    {
        "index": 342,
        "id": "A2016/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "29MAY26 13:45 - 01JUN28 13:45",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "29MAY26 13:45 - 01JUN28 13:45 PAZA A2016/26\nE) AK..ROUTE ZAN. V462 NONDA, AK TO BLUGA, AK NA EXCEPT FOR ACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS."
    },
    {
        "index": 343,
        "id": "A1470/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "14MAY26 09:00 - UFN",
        "category": "LIGHTING",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "14MAY26 09:00 - UFN PAZA A1470/26\nE) THE FOLLOWING NCA TRACKS HAVE BEEN DEACTIVATED: NCA10, NCA11,\nNCA12, NCA13, NCA14, NCA15, NCA17, NCA19, NCA20, NCA 22, NCA24,\nNCA28, NCA30, NCA31, NCA32, NCA80. FLIGHT PLANNERS MAY FILE\nWAYPOINT-TO-WAYPOINT ROUTING."
    },
    {
        "index": 344,
        "id": "A1166/25",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "29SEP25 16:22 - 30SEP27 16:22",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "29SEP25 16:22 - 30SEP27 16:22 PAZA A1166/25\nE) ZAN AK..ROUTE ZAN.\nV508 SEWAR, AK TO COP UNUSABLE EXCEPT FOR GNSS EQUIPPED\nAIRCRAFT.\nENA VOR/DME RESTRICTED."
    },
    {
        "index": 345,
        "id": "A1165/25",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "29SEP25 16:22 - 30SEP27 16:22",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "29SEP25 16:22 - 30SEP27 16:22 PAZA A1165/25\nE) ZAN AK..ROUTE ZAN.\nV320 RUNTL, AK TO FRIDA, AK UNUSABLE EXCEPT FOR GNSS EQUIPPED\nAIRCRAFT.\nENA VOR/DME RESTRICTED.\n◼ AIRSPACE"
    },
    {
        "index": 346,
        "id": "A2278/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "15JUL26 11:41 - 15JUL27 16:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "15JUL26 11:41 - 15JUL27 16:00 PAZA A2278/26\nE) VOLCANIC ACTIVITY ADVISORY FOR SHEVELUCH VOLCANO / 563800N\nPage 74\n1611900E / KAMCHATKAN PENINSULA, RUSSIA. KVERT HAS REPORTED\nINCREASED\nSEISMIC ACTIVITY IN THE VICINITY OF SHEVELUCH VOLCANO WHICH\nINDICATES\nTHE POSSIBILITY OF A VOLCANIC ERUPTION. (AVIATION COLOR CODE\nORANGE\nIS CURRENTLY IN EFFECT.) AIRCRAFT SHOULD REMAIN ALERT FOR\nPOSSIBLE\nERUPTIONS, STEAM, OR ASH CLOUDS AND REPORT ANY SIGHTINGS TO ATC\nIMMEDIATELY. CONTACT ANCHORAGE ARTCC 907-269-1103 FOR ADDITIONAL\nINFORMATION.\nCOMMENT) Remain alert for eruptions/ash clouds and report to ATC\n◼ OTHER"
    },
    {
        "index": 347,
        "id": "A2333/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "06AUG26 03:55 - 04SEP26 15:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "06AUG26 03:55 - 04SEP26 15:00 PAZA A2333/26\nE) COM DEADHORSE REMOTE COM A/G 134.4, 370.9 U/S"
    },
    {
        "index": 348,
        "id": "A2294/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "21JUL26 16:32 - 02MAR27 15:56",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "21JUL26 16:32 - 02MAR27 15:56 PAZA A2294/26\nE) ROUTE ZAN. V440 CENTA, AK TO YAKUTAT (YAK) VOR/DME, AK R-119\nMEA\n9000 NORTHWESTBOUND. YAK VOR/DME R-114 CW R-124 RESTRICTED\nBEYOND\n17NM BELOW 9000"
    },
    {
        "index": 349,
        "id": "A2293/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "21JUL26 16:29 - 02MAR27 15:48",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "21JUL26 16:29 - 02MAR27 15:48 PAZA A2293/26\nE) ROUTE ZAN. V440 YAKUTAT (YAK) VOR/DME, AK R-251 TO OCULT, AK\nMEA\n3000. YAK VOR/DME R-246 CW R-256 RESTRICTED BEYOND 11NM BELOW\n3000"
    },
    {
        "index": 350,
        "id": "A0271/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "16APR26 19:28 - 31DEC26 23:59",
        "category": "COM / RADAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "16APR26 19:28 - 31DEC26 23:59 PAZA A0271/26\nE) UPR FLIGHT PLANNING GUIDELINES\n1. UPR ACFT WILL HAVE THE SAME\nPRIORITY FOR ALT ASSIGNMENT AS ACFT ON AN OPTIONAL PACOTS OR\nNOPAC\nTRACK. (EXCEPTION: OPRS WHICH FLT PLAN A UPR THAT IS NOT\nLATERALLY\nSEPARATED FM AN OPPOSITE DIRECTION PACOTS/NOPAC/UPR TFC FLOW\nWILL\nLIKELY BE RESTRICTED VERTICALLY WHILE IN CONFLICT WITH THE\nMAJOR TFC\nFLOW)\n2. UPR ENTERY/EXIT BTN CZEG, CZVR OR KZAK FIR:\nA. CZEG FIR: BTN TAYTA AND DEEJA (LAT 72N TO 58N) MUST FLT PLAN\nOVER\nONE OF THE FOLLOWING FIXES: TAYTA, VOLOB, ADREW, POTAT, GOATS,\nFIORD,\nCHAPO, FANES, TIBOY, EMSOW, BIBEM, AYZOL, GAHAM, TOVAD, OMSUN,\nJAGIT,\nCOHIL OR DEEJA.\nB. CZVR FIR: ANYWHERE OVER OR NE OF KATCH C. KZAK FIR:\nANYWHERE OVER OR BTN ZENNA AND SAYNT OR BTN 5626N15217W AND\n4746N17000E (MUST NOT FLT PLAN THROUGH THE AIRSPACE DEFINED AS\n5626N15217W TO 5638N15059W TO 5705N15110W TO 5658N15230W)\n3. WB UPR\nPage 75\nTO RJJJ FIR: A. JOIN R220 OVER OR E OF WAYPOINT NIKLL B. JOIN\nM523\nOVER OR E OF WAYPOINT HUMSA C. REMAIN 50NM SOUTH OF A590 AND\nCROSS\nTHE PAZA/RJJJ FIR BOUNDARY OVER OR SOUTH OF WAYPOINT AKISU,\nPROVIDED\nENTRY INTO PAZA FIR EAST OF 166E.\n4. EB UPR FM RJJJ FIR ENTER PAZA FIR OVR:\nA. OMOTO: FILE R580 TO OPHET THENCE UPR SOUTH OF R580 OR\nFILE R580 TO OBOYD THENCE UPR NORTH OF R580\nB. PASRO: FILE A590 TO POWAL THENCE UPR NORTH OR SOUTH OF A590\nC. AKISU OR SOUTH: REMAIN 50NM SOUTH OF ATS ROUTE A590\n5. EB ACFT OVER KUNAD, LUMES AND KOKES\nMUST BE FLT PLANNED VIA: A. ROUTE: KOKES DIRECT ONEIL THENCE\nVIA UPR\nREMAINING S OF ATS ROUTE R580 OR, LUMES DIRECT PINSO THENCE VIA\nUPR\nREMAINING S OF ATS ROUTE A590 OR, KUNAD DIRECT PLADO THENCE VIA\nUPR\nREMAINING S OF ATS ROUTE A590. B. ALT: ACFT MUST FLT PLAN TO\nCROSS\nKUNAD, LUMES OR KOKES AT OR BLW FL310, OR AT OR ABV FL390. C.\nTIME:\nACFT MUST FLT PLAN SO AS TO CROSS KUNAD, LUMES OR KOKES BTN\n0500 UTC\nAND 2300 UTC. REFER QUESTIONS TO ANCHORAGE ARTCC INTL PROC AT\nTEL\n907-269-1360 OR TO ANCHORAGE ARTCC TFC MANAGEMENT AT TEL\n907-269-1108.\nF) FL180\nG) FL600)\nCOMMENT) UPR RTE GUIDELINES VIA PAZA, CZEG, CZVR, KZAK FIR\n(ENRTRY, EXIT POINT & AIRWAY)"
    },
    {
        "index": 351,
        "id": "A0198/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "26MAR26 17:59 - 26MAR28 17:59",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "26MAR26 17:59 - 26MAR28 17:59 PAZA A0198/26\nE) ZAN AK..ROUTE ZAN.\nV445 FAIRBANKS (FAI) VORTAC, AK TO WILTS INT, AK MEA 5200.\nV445 WILTS INT, AK TO TOLLO INT, AK MOCA 4400."
    },
    {
        "index": 352,
        "id": "A0197/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "26MAR26 17:59 - 26MAR28 17:59",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "26MAR26 17:59 - 26MAR28 17:59 PAZA A0197/26\nE) ZAN AK..ROUTE ZAN.\nT234 FAIRBANKS (FAI) VORTAC, AK TO TOLLO INT, AK MEA 5200."
    },
    {
        "index": 353,
        "id": "A0186/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "19MAR26 13:09 - 19MAR28 13:09",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "19MAR26 13:09 - 19MAR28 13:09 PAZA A0186/26\nE) ZAN ROUTE ZAN.\nJ120 MC GRATH (MCG) VORTAC, AK R-217 TO COP NA FROM 6 NM TO COP\nEXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nMCG VOR R-217 UNUSABLE BEYOND 6 NM."
    },
    {
        "index": 354,
        "id": "A0176/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "19MAR26 15:00 - 31OCT26 06:00",
        "category": "COM / RADAR",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "19MAR26 15:00 - 31OCT26 06:00 PAZA A0176/26\nD) MON-FRI 1500-0600\nE) YUKON 1-5, DELTA AND FOX ATC ASSIGNED AIRSPACE WILL NORMALLY\nBE\nACT MON-FRI BTN THE HOURS OF 1500-0600. WHEN AIRSPACE IS ACT THE\nFOLLOWING RESTRICTIONS ARE RQRD:\n1. FLTS ENTERING ANCHORAGE FIR N OF 620000N1410000W MUST BE\nPage 76\nESTABLISHED EITHER:\n(A) ON OR N OF GOATS DCT BTT\n(B) ON OR S OF ORT J124 GKN DTOUR\n2. THE FOLLOWING RTES/FIXES ARE NOT AVBL:\n(A) FIORD, CHAPO, FANES, GOATS DCT FYU\n(B) J502/J515/Q902 BTN FAI AND ORT\n(C) J507 BTN ORT AND FYU\n3. ACFT FILED BTN FAI AND ORT WILL BE RESTRICTED AT OR BLW\n17000FT\nFROM FAI TO 65NM W ORT\nFOR CURRENT ACT AIRSPACE SEE SUA.FAA.GOV. FOR QUESTIONS, CTC\nANCHORAGE /ZAN/ ARTCC TM AT TEL 907-269-1108\nF) FL180\nG) FL600\nCOMMENT) ROUTE RESTRICTION ENTERING NORTH OF 620000N1410000W IN\nPAZA FIR"
    },
    {
        "index": 355,
        "id": "A0173/26",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "13MAR26 21:33 - 31DEC26 23:59",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "13MAR26 21:33 - 31DEC26 23:59 PAZA A0173/26\nE) IT IS NO LONGER REQUIRED TO SEND A CPDLC POSITION REPORT TO\nCONFIRM CPDLC CDA WHEN ENTERING THE ANCHORAGE ARTCC PAZA FIR.\nCPDLC CDA IS CONFIRMED BY THE SET MAX UPLINK DELAY VALUE TO 300\nSEC\nUPLINK AND ROGER DOWNLINK MESSAGE EXCHANGE.\nF) SFC\nG) UNL\nCOMMENT) CPDLC CDA PSN REQPORT NOT REQUIRED\n* CDA (Current Data Authority)"
    },
    {
        "index": 356,
        "id": "A1340/25",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "17DEC25 14:23 - 17DEC27 14:23",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "17DEC25 14:23 - 17DEC27 14:23 PAZA A1340/25\nE) ZAN AK..ROUTE ZAN.\nT228 ZIKNI, AK TO KUCYE, AK MEA 4100."
    },
    {
        "index": 357,
        "id": "A1136/25",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "12SEP25 18:00 - 11SEP26 23:59",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "12SEP25 18:00 - 11SEP26 23:59 PAZA A1136/25\nE) ATTENTION ALL FLIGHT OPERATORS. FLIGHTS THAT EXPERIENCE OR\nSUSPECT GNSS INTERFERENCE ENROUTE TO THE ANCHORAGE OCEANIC ENTRY\nPOINT MUST NOTIFY ANCHORAGE ATC. NOTIFICATION SHOULD BE VIA\nCPDLC,\nSFO RADIO, OR SATCOM, CONFIRMING DEGRADATION OF NAVIGATION\nSTATUS\nAND DETAILS OF ONGOING LOSS/IMPACTS TO THE AIRCRAFT SYSTEMS AND\nCAPABILITIES.\nEXAMPLES OF NOTIFICATION:\nGNSS INTERFERENCE RNP10 ONLY\nNO DATA LINK\nDEGRADED NAVIGATION NO GNSS\nIN ADDITION, AIRLINE DISPATCHERS CAN DIRECTLY INFORM THE\nANCHORAGE\nOCEANIC SUPERVISOR TO MAKE THEM AWARE WHEN ONE OF THEIR FLIGHTS\nHAS\nBEEN IMPACTED BY GNSS INTERFERENCE BY CONTACTING 907-269-1930.\nF) SFC\nG) UNL\nCOMMENT) Report GNSS interference/degradation to Anchorage ATC"
    },
    {
        "index": 358,
        "id": "A0378/25",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "18APR25 18:42 - 18APR27 18:42",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "18APR25 18:42 - 18APR27 18:42 PAZA A0378/25\nPage 77\nE) ZAN AK..ROUTE ZAN.\nV440 MIDDLETON ISLAND (MDO) VOR/DME, AK TO YAKUTAT (YAK)\nVOR/DME,\nAK MEA 10000 EXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM\nWITH GPS."
    },
    {
        "index": 359,
        "id": "A0940/24",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "27AUG24 17:41 - 27AUG26 17:41",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27AUG24 17:41 - 27AUG26 17:41 PAZA A0940/24\nE) ZAN ROUTE ZAN.\nJ111 MC GRATH (MCG) VORTAC, AK R-102 TO COP NA FROM 20 NM TO COP\nEXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nMCG VOR R-102 UNUSABLE BEYOND 20 NM."
    },
    {
        "index": 360,
        "id": "A0939/24",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "27AUG24 17:41 - 27AUG26 17:41",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27AUG24 17:41 - 27AUG26 17:41 PAZA A0939/24\nE) ZAN ROUTE ZAN.\nJ117 MC GRATH (MCG) VORTAC, AK R-325 TO COP NA FROM 20 NM TO COP\nEXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nMCG VOR R-325 UNUSABLE BEYOND 20 NM."
    },
    {
        "index": 361,
        "id": "A0938/24",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "27AUG24 17:41 - 27AUG26 17:41",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27AUG24 17:41 - 27AUG26 17:41 PAZA A0938/24\nE) ZAN ROUTE ZAN.\nJ111 MC GRATH (MCG) VORTAC, AK R-276 TO COP NA FROM 20 NM TO COP\nEXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nMCG VOR R-276 UNUSABLE BEYOND 20 NM."
    },
    {
        "index": 362,
        "id": "A0936/24",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "27AUG24 17:41 - 27AUG26 17:41",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27AUG24 17:41 - 27AUG26 17:41 PAZA A0936/24\nE) ZAN ROUTE ZAN.\nJ120 MC GRATH (MCG) VORTAC, AK R-039 TO COP NA FROM 20 NM TO COP\nEXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nMCG VOR R-039 UNUSABLE BEYOND 20 NM."
    },
    {
        "index": 363,
        "id": "A0042/24",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "13JAN24 23:00 - UFN",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "13JAN24 23:00 - UFN PAZA A0042/24\nE) ARCTIC CTA/FIR IS SUBJECT TO THE FOLLOWING MANDATORY\nREQUIREMENTS: A. COMMUNICATIONS. 1. ALL FLTS, WITH THE\nEXCEPTION OF\nTHOSE ENTERING THE FIR EB OVER PILUN OR LISKI, MUST MAKE\nMANDATORY\nPOSITION REPORTS UPON ENTERING THE CTA/FIR VIA CPDLC OR GANDER\nHF\nVOICE. PILUN AND LISKI TFC REPORT VIA VHF AS DIRECTED OR VIA\nCPDLC.\n2. ALL FLTS MUST MAINTAIN A LISTENING WATCH ON THE CURRENT\nGANDER HF\nRADIO FREQUENCY WHILE TRANSITING THE CTA/FIR UNLESS A\nSATISFACTORY\nSELCAL CHECK HAS BEEN COMPLETED WITH GANDER RADIO.  B. ROUTING.\n1.\nFLTS ENTERING OR EXITING ANCHORAGE ARTCC FIR N OF 73N MUST FILE\nOVER\nA NAMED FIR BOUNDARY POINT  2. PILUN. W OR EB FLTS FILE A POINT\nOVER\nOR S OF 7230N14100W AND EB FLTS MUST ALSO FILE OVER OR N OF\n7200N15700W. 3. LISKI. W OR EB FLTS MUST FILE OVER OR S OF\nTAYTA AND\nEB FLTS MUST ALSO FILE OVER OR S OF 7100N15700W. QUESTIONS\nCONCERNING THESE REQUIREMENTS MAY BE REFERRED TO ZAN TFC\nMANAGEMENT\nAT 907-269-1108.\nPage 78\n[FIR] CZEG/ Edmonton, CA\nF) FL180\nG) FL600)\nCOMMENT) ARCTIC FIR REQUIREMENTS (COMMUNICATION & ROUNTING)"
    },
    {
        "index": 364,
        "id": "A0039/24",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "13JAN24 23:00 - UFN",
        "category": "COM / RADAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "13JAN24 23:00 - UFN PAZA A0039/24\nE) REFERENCE ADS-B ITP.  ANCHORAGE ARTCC OCEANIC AUTOMATION\nSUPPORTS\nTHE ICAO RECOGNIZED AUTOMATIC DEPENDENT SURVEILLANCE BROADCAST\nIN-TRAIL SEPARATION PROCEDURES (ADS-B ITP) FOR PILOT REQUESTED\nLEVEL\nCHANGES. FLIGHT CREWS OF APPROPRIATELY EQUIPPED AIRCRAFT MAY\nMAKE\nADS-B ITP LEVEL CHANGE REQUESTS WITHIN THE ANCHORAGE OCEANIC\nFIR AND\nTHAT PORTION OF THE ANCHORAGE CONTINENTAL FIR WEST OF 165W AND\nSOUTH\nOF 63N.  REFER QUESTIONS TO ANCHORAGE INTERNATIONAL PROCEDURS AT\n907-269-1108.\nF) FL180\nG) FL600\nCOMMENT) ITP: IN-TRAIL PROCEDURE"
    },
    {
        "index": 365,
        "id": "A0217/22",
        "station": "PAZA",
        "airportName": "앵커리지 대양/대륙 FIR (Anchorage Oceanic)",
        "validPeriod": "23MAR22 22:01 - UFN",
        "category": "NAVAID",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "23MAR22 22:01 - UFN PAZA A0217/22\nE) NOPAC ATS ROUTE R338:\nATS ROUTE R338 MAY BE FLIGHT PLANNED FOR WESTBOUND OR EASTBOUND\nROUTE OF FLIGHT. FOR QUESTIONS PLEASE CONTACT ANCHORAGE ARTCC\nTMU\n(907) 269-1108.\nF) SFC   G) FL600)\n◼ NAVAID"
    },
    {
        "index": 366,
        "id": "F4249/26",
        "station": "CZEG",
        "airportName": "에드먼턴 FIR (Edmonton Control)",
        "validPeriod": "06AUG26 17:56 - 11AUG26 23:59",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "06AUG26 17:56 - 11AUG26 23:59 CZEG F4249/26\nE) GRANDE PRAIRIE RADAR U/S.\nFLT WITHIN RADIUS 250NM CENTRE 551335N 1191729W\nMAY BE DENIED ROUTING AND/OR ALT REQUESTS\n◼ COMMUNICATION"
    },
    {
        "index": 367,
        "id": "F4057/26",
        "station": "CZEG",
        "airportName": "에드먼턴 FIR (Edmonton Control)",
        "validPeriod": "30JUL26 17:03 - 27AUG26 23:59",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30JUL26 17:03 - 27AUG26 23:59 CZEG F4057/26\nE) EDMONTON CENTRE FREQ 294.5MHZ AT EDMONTON U/S\n◼ AIRWAY"
    },
    {
        "index": 368,
        "id": "F4282/26",
        "station": "CZEG",
        "airportName": "에드먼턴 FIR (Edmonton Control)",
        "validPeriod": "07AUG26 18:34 - 08OCT26 15:00",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 18:34 - 08OCT26 15:00 CZEG F4282/26\nE) J515: VOR ORT TO YXY: RADIAL TO READ 106DEG INSTEAD OF 099DEG"
    },
    {
        "index": 369,
        "id": "F4091/26",
        "station": "CZEG",
        "airportName": "에드먼턴 FIR (Edmonton Control)",
        "validPeriod": "31JUL26 19:53 - UFN",
        "category": "LIGHTING",
        "level": "CRITICAL",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "31JUL26 19:53 - UFN CZEG F4091/26\nE) AMEND PUBLICATIONS: MANDATORY IFR ROUTES:\nADD: EASTBOUND OVERFLIGHTS: ALL EASTBOUND FLIGHTS TRANSITING\nEDMONTON FIR FROM VANCOUVER FIR TO WINNIPEG FIR SHALL FILE A\nROUTE NORTH OF WELLF OR SOUTH OF MENBO.\n.\nWESTBOUND OVERFLIGHTS: ALL WESTBOUND FLIGHTS TRANSITING EDMONTON\nFIR AT FL290 OR ABOVE FROM WINNIPEG FIR TO VANCOUVER FIR SHALL\nFILE A ROUTE ON OR NORTH OF A TRACK VINKO DIRECT RABOX DIRECT\nNOVAR OR SOUTH OF A TRACK MEDAK DIRECT DATNO.\nPage 79\n[FIR] CZWG/ Winnipeg, CA\n[FIR] CZYZ/ Toronto, CA\n◼ AIRSPACE"
    },
    {
        "index": 370,
        "id": "F3405/26",
        "station": "CZEG",
        "airportName": "에드먼턴 FIR (Edmonton Control)",
        "validPeriod": "06JUL26 19:43 - 01SEP26 22:00",
        "category": "APPROACH / SID / STAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "비운항 시간대 작업 (심야/주간 단시간 작업)",
        "rawText": "06JUL26 19:43 - 01SEP26 22:00 CZEG F3405/26\nD) DAILY 1200-2200\nE) DESIGNATED PORTIONS WITHIN CZEG AIRSPACE ARE STRUCTURED\nFOR ONE WAY TFC AS FOLLOWS.\nFL350 AND FL390 ARE STRUCTURED AND AVBL AS WESTBOUND CRUISING FL\nWITHIN AN AREA BOUNDED BY 7800N 09000W - 6930N 10700W -\n6200N 08700W - 6245N 08000W - 6500N 06800W - 6508N 06620W -\n7445N 08930W THENCE COUNTER CLOCKWISE ALONG THE CTA BOUNDARY TO\n7800N 09000W\nCOMMENT) POLAR & GREENLAND RTE AFFECTED\n◼ NAVAID"
    },
    {
        "index": 371,
        "id": "G2698/26",
        "station": "CZWG",
        "airportName": "위니펙 FIR (Winnipeg Control)",
        "validPeriod": "11AUG26 04:00 - 11AUG26 10:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "11AUG26 04:00 - 11AUG26 10:00 CZWG G2698/26\nE) REGINA RADAR U/S.\nFLT WITHIN RADIUS 200NM CENTRE 502559N 1044016W\nMAY BE DENIED ROUTING AND/OR ALT REQUESTS.\nPOSSIBLE DLA OF UP TO 15MIN FOR ARR/DEP AT REGINA INTL AD\n(CYQR).\nFOR INFO CTC 204-983-8338\n◼ COMMUNICATION"
    },
    {
        "index": 372,
        "id": "G2679/26",
        "station": "CZWG",
        "airportName": "위니펙 FIR (Winnipeg Control)",
        "validPeriod": "07AUG26 13:09 - 07SEP26 23:59",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 13:09 - 07SEP26 23:59 CZWG G2679/26\nE) WINNIPEG CENTRE PERIPHERAL STATION (PAL) 225.2MHZ AT KENORA\nU/S"
    },
    {
        "index": 373,
        "id": "G2259/26",
        "station": "CZWG",
        "airportName": "위니펙 FIR (Winnipeg Control)",
        "validPeriod": "10JUL26 14:07 - 11SEP26 23:59",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10JUL26 14:07 - 11SEP26 23:59 CZWG G2259/26\nE) WINNIPEG CENTRE PERIPHERAL STATION (PAL) 297.6MHZ AT THUNDER\nBAY\nU/S\n◼ COMMUNICATION"
    },
    {
        "index": 374,
        "id": "G2702/26",
        "station": "CZYZ",
        "airportName": "토론토 FIR (Toronto Control)",
        "validPeriod": "09AUG26 18:51 - 10AUG26 23:59",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "09AUG26 18:51 - 10AUG26 23:59 CZYZ G2702/26\nE) LONDON RDO REMOTE COM OUTLET (RCO)\nFLT INFO SVC ENR (FISE)126.7MHZ AT FOYMOUNT U/S"
    },
    {
        "index": 375,
        "id": "G2259/26",
        "station": "CZYZ",
        "airportName": "토론토 FIR (Toronto Control)",
        "validPeriod": "10JUL26 14:07 - 11SEP26 23:59",
        "category": "GPS / NAVIGATION",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "10JUL26 14:07 - 11SEP26 23:59 CZYZ G2259/26\nE) WINNIPEG CENTRE PERIPHERAL STATION (PAL) 297.6MHZ AT THUNDER\nBAY\nU/S\n◼ GPS"
    },
    {
        "index": 376,
        "id": "G2677/26",
        "station": "CZYZ",
        "airportName": "토론토 FIR (Toronto Control)",
        "validPeriod": "09AUG26 07:00 - 11AUG26 09:59",
        "category": "COM / RADAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "비운항 시간대 작업 (심야/주간 단시간 작업)",
        "rawText": "09AUG26 07:00 - 11AUG26 09:59 CZYZ G2677/26\nD) DAILY 0700-0959\nE) GPS INTERFERENCE EXER\nRADIUS 254NM CENTRE 400113N 0742814W FL400-UNL,\n207NM RADIUS AT FL250,\n142NM RADIUS AT 10000FT AMSL,\n104NM RADIUS AT 4000FT AGL,\n58NM RADIUS AT 50FT AGL.\nPage 80\n[FIR] KZBW/ Boston, US\nGNSS SIGNAL MAY BE PERIODICALLY INTERRUPTED.\nINFORM ATC OF ANY ADVERSE IMPACT.\n◼ COMMUNICATION"
    },
    {
        "index": 377,
        "id": "A0882/26",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "07AUG26 04:00 - 03SEP26 10:00",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "07AUG26 04:00 - 03SEP26 10:00 KZBW A0882/26\nE) SVC BANGOR APP CLSD CLASS C SER INVOLVING VFR ACFT NOT AVBL\nCTC\nBOSTON ARTCC FOR CLASS C ARR COM ON\n120.25, FOR CLR DELIVERY AT 603-879-6859\n◼ AIRWAY"
    },
    {
        "index": 378,
        "id": "A0870/26",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "29JUL26 21:32 - 30JUL28 21:32",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "29JUL26 21:32 - 30JUL28 21:32 KZBW A0870/26\nE) NY..ROUTE ZBW. V374 YODER INT, CT DME REQUIRED EXCEPT FOR\nACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS. HTO VOR R-010\nUNUSABLE."
    },
    {
        "index": 379,
        "id": "A0850/26",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "24JUL26 17:46 - 05MAR27 17:27",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24JUL26 17:46 - 05MAR27 17:27 KZBW A0850/26\nE) ROUTE ZBW ZNY. V139, V268 HAMPTON (HTO) VORTAC, NY R-236 TO\nMANTA\nINT, NJ NA EXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM\nWITH\nGPS. HTO VOR R-236 UNUSABLE."
    },
    {
        "index": 380,
        "id": "A0185/26",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "24APR26 14:52 - 29OCT26 09:00",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24APR26 14:52 - 29OCT26 09:00 KZBW A0185/26\nE) CT..ROUTE ZBW. V167, V3 HARTFORD (HFD) VOR/DME, CT TO JEWIT,\nCT\nMOCA 2200."
    },
    {
        "index": 381,
        "id": "A0087/26",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "27MAR26 14:45 - 27MAR28 14:45",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27MAR26 14:45 - 27MAR28 14:45 KZBW A0087/26\nE) ZBW NY..ROUTE ZBW.\nV487 CAMBRIDGE (CAM) VOR/DME, NY R-203 TO BOWAN INT, NY NA.\nCAM VOR/DME R-203 UNUSABLE.\n◼ OTHER"
    },
    {
        "index": 382,
        "id": "A0884/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "19NOV25 19:59 - 19NOV27 19:59",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "19NOV25 19:59 - 19NOV27 19:59 KZBW A0884/25\nE) ZBW ROUTE ZBW.\nV167 PROVIDENCE (PVD) VOR/DME, RI R-115 TO ZUNUX, MA MEA 3000\nSOUTHEASTBOUND EXCEPT FOR ACFT EQUIPPED WITH SUITABLE\nRNAV SYSTEM WITH GPS.\nPVD VOR R-115 UNUSABLE BEYOND 30 NM BELOW 3000 FEET,\nZUNUX DME ONLY FIX."
    },
    {
        "index": 383,
        "id": "A0804/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "08OCT25 13:59 - 08OCT27 13:59",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "08OCT25 13:59 - 08OCT27 13:59 KZBW A0804/25\nE) ZBW ROUTE ZBW ZNY.\nV16 KEEPM, NY TO CREAM, NY NA. CCC VOR R-274 AND R-057 UNUSABLE."
    },
    {
        "index": 384,
        "id": "A0803/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "08OCT25 13:58 - 08OCT27 13:58",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "08OCT25 13:58 - 08OCT27 13:58 KZBW A0803/25\nE) ZBW ROUTE ZBW.\nV374 CREAM, NY TO KURTY, CT USE ORW VOR R-238. CCC VOR R-057\nUNUSABLE."
    },
    {
        "index": 385,
        "id": "A0375/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "22MAY25 18:47 - 22MAY27 18:47",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22MAY25 18:47 - 22MAY27 18:47 KZBW A0375/25\nE) ZBW NY..ROUTE ZBW.\nPage 81\n[FIR] KZNY/ New York, US\nV123, V157, V433, V6 LA GUARDIA (LGA) VOR/DME, NY MCA 2200\nSOUTHWESTBOUND."
    },
    {
        "index": 386,
        "id": "A0374/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "22MAY25 18:47 - 22MAY27 18:47",
        "category": "GENERAL",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22MAY25 18:47 - 22MAY27 18:47 KZBW A0374/25\nE) ZBW CT..ROUTE ZBW.\nT705 LOVES, CT TO DEEDE, NY GNSS MEA 3100."
    },
    {
        "index": 387,
        "id": "A0373/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "22MAY25 18:47 - 22MAY27 18:47",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22MAY25 18:47 - 22MAY27 18:47 KZBW A0373/25\nE) ZBW CT..ROUTE ZBW.\nV433, V44 LOVES, CT TO PAWLING (PWL) VOR/DME, NY MEA 3100."
    },
    {
        "index": 388,
        "id": "A0372/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "22MAY25 18:47 - 22MAY27 18:47",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "22MAY25 18:47 - 22MAY27 18:47 KZBW A0372/25\nE) ZBW NY..ROUTE ZBW.\nV433, V487 DUNBO, NY TO BRIDGEPORT (BDR) VOR/DME, CT MEA 2500\nMOCA"
    },
    {
        "index": 389,
        "id": "A0292/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "15APR25 19:39 - 15APR27 19:39",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "1600.\n15APR25 19:39 - 15APR27 19:39 KZBW A0292/25\nE) ZBW NY..ROUTE ZBW.\nV268 COP TO HAMPTON (HTO) VORTAC, NY R-079 NA EXCEPT FOR ACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nHTO VOR R-079 UNUSABLE."
    },
    {
        "index": 390,
        "id": "A0264/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "01APR25 05:00 - UFN",
        "category": "AIRSPACE / ROUTING",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "01APR25 05:00 - UFN KZBW A0264/25\nE) ZBW ROUTE NOTICE.. OF FPL RQMNTS OF EB NORTH ATLANTIC\nTFC JOINING THE NORTH ATLANTIC ORGANIZED TRACK STRUCTURE. USERS\nENTERING EB NORTH ATLANTIC ORGANIZED TRACK STRUCTURE BTW\n2100-0500\nARE REQUIRED TO FILE IAW DAILY NORTH ATLANTIC ADVRY PUBLISHED BY\nATCSCC."
    },
    {
        "index": 391,
        "id": "A0157/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "24FEB25 16:53 - 28FEB27 16:53",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24FEB25 16:53 - 28FEB27 16:53 KZBW A0157/25\nE) ZBW NY..ROUTE ZBW ZNY.\nV374, V39 VOLLU, NY TO CARMEL (CMK) VOR/DME, NY MEA 6500 EXCEPT\nFOR\nACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nV39 SPARTA (SAX) VORTAC, NJ TO VOLLU, NY MEA 6500 EXCEPT FOR\nACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nCMK VOR R-266 UNUSABLE , SAX VTAC R-084 UNUSABLE BELOW 6500."
    },
    {
        "index": 392,
        "id": "A0156/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "24FEB25 16:53 - 28FEB27 16:53",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24FEB25 16:53 - 28FEB27 16:53 KZBW A0156/25\nE) ZBW NY..ROUTE ZBW ZNY.\nV188 NYACK, NY TO CARMEL (CMK) VOR/DME, NY NA EXCEPT FOR ACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nCMK VOR R-255 UNUSABLE."
    },
    {
        "index": 393,
        "id": "A0155/25",
        "station": "KZBW",
        "airportName": "보스턴 센터 FIR (Boston ARTCC)",
        "validPeriod": "24FEB25 16:53 - 28FEB27 16:53",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24FEB25 16:53 - 28FEB27 16:53 KZBW A0155/25\nE) ZBW NY..ROUTE ZBW ZNY.\nV3, V405, V419 FALLZ, NJ TO CARMEL (CMK) VOR/DME, NY NA EXCEPT\nFOR\nACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nCMK VOR R-255 UNUSABLE.\n◼ NAVAID\nPage 82"
    },
    {
        "index": 394,
        "id": "A0535/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "19JUN26 19:23 - 02OCT26 20:00",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "19JUN26 19:23 - 02OCT26 20:00 KZNY A0535/26\nE) NAV VOR U/S\n◼ COMMUNICATION"
    },
    {
        "index": 395,
        "id": "A0487/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "02JUN26 18:21 - 02JUN27 23:59",
        "category": "COM / RADAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02JUN26 18:21 - 02JUN27 23:59 KZNY A0487/26\nE) COM CPDLC ROUTE MESSAGING NOT AVBL\n◼ GPS"
    },
    {
        "index": 396,
        "id": "A0645/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "09AUG26 07:00 - 11AUG26 09:59",
        "category": "COM / RADAR",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "공항 부지 일상 작업 (초지/도색/청소/정기 점검)",
        "rawText": "09AUG26 07:00 - 11AUG26 09:59 KZNY A0645/26\nD) DLY 0700-0959\nE) AIRSPACE DUE TO GPS TESTING GPS MAY NOT BE AVAILABLE WITHIN A\n254NM RADIUS CENTERED AT 400113N0742814W THE FOLLOWING FIXES\nWILL BE\nUNUSABLE: ROLLE AND SQUAD THE FOLLOWING AIRWAYS WILL BE CLOSED:\nL457\nBTN OKONU AND SKPPR L455 BTN SAVIK AND SKPPR\nCOMMENT) AFFECTED RTE AS FLW :\n*L455(SAVIK-SKPPR) : GRU/BED(B01)\n◼ AIRWAY"
    },
    {
        "index": 397,
        "id": "A0618/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "24JUL26 17:49 - 05MAR27 17:28",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24JUL26 17:49 - 05MAR27 17:28 KZNY A0618/26\nE) ROUTE ZNY ZBW. V139, V268 HAMPTON (HTO) VORTAC, NY R-236 TO\nMANTA\nINT, NJ NA EXCEPT FOR ACFT EQUIPPED WITH SUITABLE RNAV SYSTEM\nWITH\nGPS. HTO VOR R-236 UNUSABLE."
    },
    {
        "index": 398,
        "id": "A0405/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "21MAY26 14:14 - 21MAY28 14:14",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "21MAY26 14:14 - 21MAY28 14:14 KZNY A0405/26\nE) ROUTE ZNY. J61 WESTMINSTER (EMI) VORTAC, MD TO PHILIPSBURG\n(PSB)\nVORTAC, PA NA EXCEPT FOR AIRCRAFT EQUIPPED WITH SUITABLE RNAV\nSYSTEM\nWITH GPS. PSB VOR R-161 UNUSABLE BEYOND 40 NM.\n◼ OTHER"
    },
    {
        "index": 399,
        "id": "A0467/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "27MAY26 18:34 - 27MAY28 18:34",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27MAY26 18:34 - 27MAY28 18:34 KZNY A0467/26\nE) PA..ROUTE ZNY. V116 GUYED, PA TO LACIE, PA NA EXCEPT FOR ACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS. SFK VOR/DME R-106\nUNUSUABLE BEYOND 40 NM."
    },
    {
        "index": 400,
        "id": "A0466/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "27MAY26 18:28 - 27MAY28 18:28",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "27MAY26 18:28 - 27MAY28 18:28 KZNY A0466/26\nE) ROUTE ZNY. V423 WILLIAMSPORT (FQM) VOR/DME, PA TO BINGHAMTON\n(CFB)\nVOR/DME, NY MOCA 4300."
    },
    {
        "index": 401,
        "id": "A0041/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "02FEB26 13:20 - 14SEP26 13:20",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02FEB26 13:20 - 14SEP26 13:20 KZNY A0041/26\nE) ZNY MD..ROUTE ZNY ZDC.\nV268 WESTMINSTER (EMI) VORTAC, MD R-151 TO BALTIMORE (BAL)\nVORTAC,\nMD R-334 USE BAL VOR R-334.\nEMI VORTAC R-151 UNUSABLE."
    },
    {
        "index": 402,
        "id": "A0039/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "02FEB26 13:19 - 14SEP26 13:19",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02FEB26 13:19 - 14SEP26 13:19 KZNY A0039/26\nE) ZNY MD..ROUTE ZNY ZDC.\nV268 WESTMINSTER (EMI) VORTAC, MD R-151 TO BALTIMORE (BAL)\nPage 83\nVORTAC,\nMD R-334 USE BAL VOR R-334.\nEMI VORTAC R-151 UNUSABLE."
    },
    {
        "index": 403,
        "id": "A0037/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "02FEB26 13:17 - 14SEP26 13:17",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02FEB26 13:17 - 14SEP26 13:17 KZNY A0037/26\nE) ZNY MD..ROUTE ZNY.\nV166 WESTMINSTER (EMI) VORTAC, MD R-088 TO COP NA EXCEPT FOR\nACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nEMI VORTAC R-088 UNUSABLE."
    },
    {
        "index": 404,
        "id": "A0035/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "02FEB26 13:16 - 14SEP26 13:16",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02FEB26 13:16 - 14SEP26 13:16 KZNY A0035/26\nE) ZNY MD..ROUTE ZNY ZDC.\nJ211 WESTMINSTER (EMI) VORTAC, MD R-300 TO BUSTR, PA NA EXCEPT\nFOR\nACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nEMI VORTAC R-300 UNUSABLE."
    },
    {
        "index": 405,
        "id": "A0033/26",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "02FEB26 13:14 - 14SEP26 13:14",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02FEB26 13:14 - 14SEP26 13:14 KZNY A0033/26\nE) ZNY MD..ROUTE ZNY ZDC.\nJ211 WESTMINSTER (EMI) VORTAC, MD R-300 TO BUSTR, PA NA EXCEPT\nFOR\nACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nEMI VORTAC R-300 UNUSABLE."
    },
    {
        "index": 406,
        "id": "A0507/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "30OCT25 13:37 - 31OCT27 13:37",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "30OCT25 13:37 - 31OCT27 13:37 KZNY A0507/25\nE) ZNY PA..ROUTE ZNY.\nJ220 MICAH, PA TO COP NA EXCEPT FOR ACFT EQUIPPED WITH SUITABLE\nRNAV SYSTEM WITH GPS. AML VDME R-009 UNUSABLE BEYOND 74 NM."
    },
    {
        "index": 407,
        "id": "A0504/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "28OCT25 20:33 - 30OCT27 20:32",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "28OCT25 20:33 - 30OCT27 20:32 KZNY A0504/25\nE) ZNY NY..ROUTE ZNY.\nV29 SCOFF, PA TO BINGHAMTON (CFB) VOR/DME, NY MEA 3800."
    },
    {
        "index": 408,
        "id": "A0476/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "08OCT25 13:59 - 08OCT27 13:59",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "08OCT25 13:59 - 08OCT27 13:59 KZNY A0476/25\nE) ZNY ROUTE ZNY ZBW.\nV16 KEEPM, NY TO CREAM, NY NA. CCC VOR R-274 AND R-057 UNUSABLE."
    },
    {
        "index": 409,
        "id": "A0407/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "02SEP25 20:04 - 02SEP27 20:04",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "02SEP25 20:04 - 02SEP27 20:04 KZNY A0407/25\nE) ZNY PA..ROUTE ZNY.\nV116 STONYFORK (SFK) VOR/DME, PA TO WILKES-BARRE (LVZ) VORTAC,\nPA\nMEA 4900."
    },
    {
        "index": 410,
        "id": "A0385/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "18AUG25 15:23 - 18AUG27 15:23",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "18AUG25 15:23 - 18AUG27 15:23 KZNY A0385/25\nE) ZNY PA..ROUTE ZNY.\nT221 ALLENTOWN (FJC) VORTAC, PA TO LAAYK, PA GNSS MEA 4700."
    },
    {
        "index": 411,
        "id": "A0076/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "24FEB25 16:53 - 28FEB27 16:53",
        "category": "NAVAID",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24FEB25 16:53 - 28FEB27 16:53 KZNY A0076/25\nE) ZNY NY..ROUTE ZNY.\nV374 BINGHAMTON (CFB) VOR/DME, NY TO GAYEL, NY GNSS 4700 MOCA"
    },
    {
        "index": 412,
        "id": "A0075/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "24FEB25 16:53 - 28FEB27 16:53",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "4700.\n24FEB25 16:53 - 28FEB27 16:53 KZNY A0075/25\nE) ZNY NY..ROUTE ZNY ZBW.\nV374, V39 VOLLU, NY TO CARMEL (CMK) VOR/DME, NY MEA 6500 EXCEPT\nPage 84\nFOR\nACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nV39 SPARTA (SAX) VORTAC, NJ TO VOLLU, NY MEA 6500 EXCEPT FOR\nACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nCMK VOR R-266 UNUSABLE , SAX VTAC R-084 UNUSABLE BELOW 6500."
    },
    {
        "index": 413,
        "id": "A0073/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "24FEB25 16:53 - 28FEB27 16:53",
        "category": "APPROACH / SID / STAR",
        "level": "ACTIVE",
        "isShaded": False,
        "shadeReason": "",
        "rawText": "24FEB25 16:53 - 28FEB27 16:53 KZNY A0073/25\nE) ZNY NY..ROUTE ZNY ZBW.\nV188 NYACK, NY TO CARMEL (CMK) VOR/DME, NY NA EXCEPT FOR ACFT\nEQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nCMK VOR R-255 UNUSABLE."
    },
    {
        "index": 414,
        "id": "A0072/25",
        "station": "KZNY",
        "airportName": "뉴욕 센터 FIR (New York Oceanic/ARTCC)",
        "validPeriod": "24FEB25 16:53 - 28FEB27 16:53",
        "category": "RUNWAY",
        "level": "LOW",
        "isShaded": True,
        "shadeReason": "등화류 결함 (유도로/에이프런 개별 유도등 및 표시등)",
        "rawText": "24FEB25 16:53 - 28FEB27 16:53 KZNY A0072/25\nE) ZNY NY..ROUTE ZNY ZBW.\nV3, V405, V419 FALLZ, NJ TO CARMEL (CMK) VOR/DME, NY NA EXCEPT\nFOR\nACFT EQUIPPED WITH SUITABLE RNAV SYSTEM WITH GPS.\nCMK VOR R-255 UNUSABLE.\nPage 85\nCFP PLAN 3201\nATTN CAPT.                                      7626\nFLIGHT RELEASE AAR224  RKSI/KJFK ON 10/AUG/26.NONSTOP COMPUTED 0722Z\nA/C REG.MK ENGINE    SELCAL ROUTE PRF WX  PROGS AVG WIND/TEMP UNIT\n388 HL7626 TRENT970  GM-KQ         F  BRK 1000UK    P017/M47  100LBS\nSPEED SKD   CLB-320/.85  CRZ-  65 DSC-.85/290/ APMS/P 03.2 PCNT. IFR\n             FUEL  TIME    DIST  NAM           PLAN      AGTOW 12544\nTRIP         4059  13.24   6663  6431          SOW 06587 RWY   12544\nRESERVE      0456  01.48\n ALTN/KBOS   0224  00.45   0261  0256          PLD 01170 ACL   01218\n FINAL RES   0110  00.30   T/O      Z          ZFW 07757 MZFW  08068\n 3 PCT CONT  0122  00.33   F/T 13.24           TOF 04739 TOF   04739\n REFILE RES  0000  00.00   ETA      Z                          12807\n ETP RES     0000  00.00\nRQD TAKEOFF  4515  15.12   HRS UTC-0400        TOW 12496 MTOW  12544\nDISC         0224  01.00   ETA      L          TIF 04059 TCAP  12544\nTANKERING    0000  00.00   RSN/    /           LDW 08437 MLDW  08620\nPLN TAKEOFF  4739  16.12   ACTL                PAX       TIF   04059\n                                               CGO             12679\nTAXI         0019\nRAMP OUT     4758  16.12   ACTL\nFOD          0680  02.48   ACTL        ETD RKSI 1205Z ETA KJFK 0129Z\n2ND-$    290 4229 13.53\nRKSI..EGOBA Y697 KAE Y437 TENAS L512 GTC Y512 OATIS R580 ORCCA..\nSQA..GKN..GAHAM..N62W130..N61W120..N59W110..N56W100..N51W090..\nN46W080..NOVON..YODAA PUCKY1 KJFK\nDIST  LATITUDE  MC  FL  ETO/MSA R/F  OT WIND/COMP  SR TAS   ZT  B/O\nTO    LONGITUDE MH  ACT ATO/DF  ACTL               MW  GS ACTM ACBO/\n                TC\n0065  N37 29.2  097 CLB ---/062 4577 00 ......... .. ...   013  162\nPage 86\nEGOBA E127 22.8 098        /                      .. ... 00.13 0162/\n                088                               EGOBA\n0014  N37 32.0  087 CLB ---/062 4557 07 ......... .. ...   002  020\nKARBU E127 39.9 088        /                      .. ... 00.15 0182/\n                078                               KARBU\n0023  N37 36.4  088 CLB ---/075 4528 16 ......... .. ...   003  029\nTORUS E128 08.1 089        /                      .. ... 00.18 0211/\n                079                               TORUS\n0022  N37 40.5  088 CLB ---/075 4499 20 ......... .. ...   003  029\nBIKSI E128 35.1 088        /                      .. ... 00.21 0240/\n                079                               BIKSI\n0008  N37 42.0  089 CLB ---/075 4489 22 ......... .. ...   002  010\nKAE   E128 45.2 088        /                      .. ... 00.23 0250/\n                079                               GANGWON\n0044  N37 41.3  100 CLB ---/075 4443 29 ......... .. ...   004  046\nLESBU E129 41.1 099        /                      .. ... 00.27 0296/\n                091                               LESBU\n0008  N37 41.1  101 CLB ---/068 4435 30 ......... .. ...   001  008\nUGOVI E129 50.9 099        /                      .. ... 00.28 0304/\n                091                               UGOVI\n0014  N37 40.8  101 310 ---/068 4420 32 ......... .. ...   001  015\nTOC   E130 08.4 098        /                      .. ... 00.29 0319/\n                091                               TOC\n0006  N37 40.6  101 310 ---/068 4416 32 03015M007 08 505   001  004\nBUSKO E130 16.2 098        /                      43 498 00.30 0323/\n                091                               BUSKO\n0062  N37 38.3  101 310 ---/046 4369 33 05015M012 06 504   008  047\nTENAS E131 34.5 100        /                      39 492 00.38 0370/\n                092                               TENAS\n0052  N37 38.5  099 310 ---/019 4331 33 05017M013 02 504   006  038\nSABET E132 40.3 097        /                      43 491 00.44 0408/\n                089                               SABET\n0016  N37 40.0  094 310 ---/015 4319 33 04020M014 01 504   002  012\nANDOL E133 00.0 091        /                      45 490 00.46 0420/\n/ RJJJ FIR      084   FUKUOKA                     ANDOL\n0035  N37 43.1  094 310 ---/015 4293 33 03023M014 00 503   004  026\nKAMSA E133 44.0 092        /                      45 489 00.50 0446/\n                085                               KAMSA\n0169  N37 54.1  094 310 ---/038 4168 34 01036M013 02 502   021  125\nIGOBI E137 17.0 090        /                      41 489 01.11 0571/\n                085                               IGOBI\n0039  N37 55.8  096 330 ---/059 4133 41 02050M019 04 499   005  035\nTATAM E138 06.2 091        /                      37 480 01.16 0606/\n                087                               TATAM\n0048  N37 57.5  097 350 ---/094 4090 46 03058M036 03 499   006  043\nGTC   E139 06.9 092        /                      36 463 01.22 0649/\n                088                               NIIGATA\n0031  N38 01.6  090 350 ---/094 4066 45 04045M033 03 500   004  024\nELDAK E139 45.7 087        /                      39 467 01.26 0673/\n                082                               ELDAK\n0055  N38 08.3  091 350 ---/088 4025 44 06037M035 02 501   007  041\nSDE   E140 55.3 090        /                      38 466 01.33 0714/\nPage 87\n                083                               SENDAI\n0055  N38 00.4  106 350 ---/088 3982 43 11045M044 03 502   007  043\nBEKEN E142 03.7 108        /                      36 458 01.40 0757/\n                098                               BEKEN\n0056  N37 51.4  107 350 ---/010 3939 43 13051M046 07 502   008  043\nSOVMO E143 14.0 110        /                      37 456 01.48 0800/\n                099                               SOVMO\n0015  N37 49.0  107 350 ---/010 3927 42 12052M048 06 503   001  012\nOATIS E143 32.4 109        /                      37 455 01.49 0812/\n                099                               OATIS\n0070  N38 41.3  049 350 ---/010 3877 42 13057M008 06 502   009  050\nMAKMU E144 30.7 055        /                      36 494 01.58 0862/\n                041                               MAKMU\n0250  N41 44.4  050 350 ---/010 3707 42 14027P005 04 501   030  170\nONEMU E148 13.0 053        /                      39 506 02.28 1032/\n                042                               ONEMU\n0330  N45 31.9  053 350 ---/010 3490 43 17025P013 02 498   038  217\nOPULO E153 43.2 055        /                      37 511 03.06 1249/\n                045                               OPULO\n0330  N48 59.7  056 350 ---/010 3280 44 19023P018 01 496   039  210\nOMOTO E160 00.7 058        /                      37 514 03.45 1459/\n/ PAZA FIR      049   ANCHORAGE OCEANIC           OMOTO\n0054  N49 30.6  061 350 ---/010 3247 43 22021P020 01 497   006  033\nOGDEN E161 07.8 061        /                      36 517 03.51 1492/\n                054                               OGDEN\n0152  N50 53.9  061 350 ---/010 3152 44 24021P021 01 496   018  095\nOPHET E164 26.4 062        /                      36 517 04.09 1587/\n                056                               OPHET\n0053  N51 21.5  063 360 ---/010 3115 47 26021P020 00 494   006  037\nOLCOT E165 37.5 062        /                      40 514 04.15 1624/\n                058                               OLCOT\n0186  N52 53.3  063 360 ---/010 3003 47 27033P027 02 493   021  112\nFIR   E170 00.0 061        /                      39 520 04.36 1736/\n/ PAZA FIR      059   ANCHORAGE OCEANIC           FIR\n0006  N52 56.3  063 360 ---/010 2999 47 27033P027 02 493   001  004\nOPAKE E170 09.3 061        /                      39 520 04.37 1740/\n                059                               OPAKE\n0015  N53 06.6  052 360 ---/052 2990 47 29049P020 02 493   002  009\nETP1  E170 27.6 047        /                      40 513 04.39 1749/\n                049                               ETP1\n0109  N54 15.4  052 360 ---/052 2924 47 29049P020 02 493   013  066\nONEIL E172 49.3 047        /                      40 513 04.52 1815/\n                049                               ONEIL\n0211  N56 05.2  058 360 ---/010 2797 48 31064P020 02 492   024  127\nOBOYD E178 04.3 052        /                      40 512 05.16 1942/\n                057                               OBOYD\n0202  N57 36.6  061 360 ---/010 2675 51 32089P008 02 489   025  122\nOFORD W176 26.8 051        /                      37 497 05.41 2064/\n                061                               OFORD\n0100  N58 16.4  063 360 ---/010 2612 51 34098M010 04 489   012  063\nOGGOE W173 34.4 050        /                      35 479 05.53 2127/\n                065                               OGGOE\nPage 88\n0077  N58 45.3  063 360 ---/010 2565 50 34068M008 04 489   010  047\nONEOX W171 18.3 055        /                      33 481 06.03 2174/\n                067                               ONEOX\n0126  N59 30.5  062 360 ---/039 2489 51 34015M002 02 488   015  076\nORVIL W167 29.8 060        /                      35 486 06.18 2250/\n                067                               ORVIL\n0154  N60 17.3  064 360 ---/028 2395 56 12014M008 04 482   020  094\nORCCA W162 38.8 064        /                      32 474 06.38 2344/\n                070                               ORCCA\n0212  N61 05.9  065 370 ---/077 2267 59 16018M001 02 480   027  128\nSQA   W155 38.1 067        /                      36 479 07.05 2472/\n                074                               SPARREVOHN\n0298  N62 09.2  055 370 ---/155 2103 59 24026P025 01 479   035  164\nGKN   W145 26.8 062        /                      37 504 07.40 2636/\n                073                               GULKANA\n0125  N62 15.0  068 370 ---/186 2035 56 30037P030 03 482   015  068\nGAHAM W141 00.0 066        /                      34 512 07.55 2704/\n/ CZEG FIR      085   EDMONTON                    GAHAM\n0310  N62 00.0  071 370 ---/109 1867 55 30033P027 03 483   036  168\n62N30 W130 00.0 069        /                      35 510 08.31 2872/\n                088                               62N130W\n0293  N61 00.0  079 370 ---/114 1707 56 31013P011 01 481   036  160\n61N20 W120 00.0 078        /                      34 492 09.07 3032/\n                097                               61N120W\n0324  N59 00.0  090 370 ---/047 1531 54 34014P009 02 483   039  176\n59N10 W110 00.0 089        /                      31 492 09.46 3208/\n                107                               59N110W\n0029  N58 48.0  102 370 ---/036 1516 52 30031P031 03 483   003  015\nETP2  W109 09.6 103        /                      33 514 09.49 3223/\n                115                               ETP2\n0195  N57 16.2  102 370 ---/036 1417 52 30031P031 03 483   024  099\nFIR   W103 43.6 103        /                      33 514 10.13 3322/\n/ CZWG FIR      115   WINNIPEG                    FIR\n0146  N56 00.0  102 370 ---/036 1343 52 30031P031 03 483   017  074\n56N00 W100 00.0 103        /                      33 514 10.30 3396/\n                115                               56N100W\n0467  N51 00.0  121 370 ---/032 1118 52 30052P051 03 479   052  225\n5190N W090 00.0 122        /                      32 530 11.22 3621/\n                126                               5190N\n0146  N49 37.5  127 370 ---/036 1052 53 29069P067 02 474   016  066\nFIR   W086 51.5 129        /                      34 541 11.38 3687/\n/ CZYZ FIR      123   TORONTO                     FIR\n0353  N46 00.0  127 370 ---/036 0891 53 29069P067 02 474   040  161\n4680N W080 00.0 129        /                      34 541 12.18 3848/\n                123                               46N080W\n0193  N43 52.6  140 370 ---/047 0803 52 27079P061 04 474   021  088\nNOVON W076 36.4 146        /                      34 535 12.39 3936/\n/ KZBW FIR      130   BOSTON                      NOVON\n0168  N41 46.2  150 370 ---/065 0723 52 26083P033 01 477   020  080\nTOD   W074 05.4 155        /                      37 510 12.59 4016/\n                138                               TOD\n0004  N41 43.4  150 DSC ---/065 0722 48 26079P030 .. ...   000  001\nPage 89\nYODAA W074 01.9 155        /                      .. ... 12.59 4017/\n                138                               YODAA\n0022  N41 21.4  199 DSC ---/065 0719 32 27044 000 .. ...   003  003\nFUUEL W074 05.3 205        /                      .. ... 13.02 4020/\n                187                               FUUEL\n0002  N41 19.7  225 DSC ---/065 0719 18 30042M007 .. ...   000  000\nFIR   W074 06.8 232        /                      .. ... 13.02 4020/\n/ KZNY FIR      213   NEW YORK                    FIR\n0021  N41 01.7  225 DSC ---/065 0717 18 30042M007 .. ...   003  002\nDOORE W074 22.1 232        /                      .. ... 13.05 4022/\n                213                               DOORE\n0013  N40 54.4  135 DSC ---/065 0715 09 29035P025 .. ...   002  002\nPUCKY W074 07.3 137        /                      .. ... 13.07 4024/\n                123                               PUCKY\n0014  N40 47.0  135 DSC ---/030 0713 01 27025P019 .. ...   003  002\nVADDR W073 52.1 137        /                      .. ... 13.10 4026/\n                123                               VADDR\n0066  N40 38.4  183 DSC ------- 0680 17 27018P001 .. ...   014  033\nKJFK  W073 46.7 196        /                       .. .. 13.24 4059/\n                171                               JOHN F KENNEDY INT\nROUTE TO ALTN : KJFK..MERIT ROBUC3 KBOS\n                      MSA  TTK  DIST  FL   W/C   TIME  FUEL\nALTERNATE  - 1  KBOS  049  050  0261  190  P017  00.45 22400\n3%  CONTINGENCY ERA VALIDATION\nERA   COC        CUMD  MSA  TTK  DIST  TIME  ETA\nKORD    N5741.3  4998   42  144  1149   2.29  0040\n       W10505.8\n-----\nLOLV  EQUAL TIME POINT DATA\n        RJCC-PANC                             PANC-KORD\nDIST 2283    DIST 1355                DIST 4853     DIST 1287\nTIME 04.39   TIME 03.48               TIME 09.49    TIME 03.24\nTRIP 1749    TRIP 1225                TRIP 3223     TRIP 1014\nLAT/LONG N53066 E170276               LAT/LONG N58480   W109096\nAVG W/C RJCC M019 TO PANC  M005       AVG W/C PANC M002 TO KORD P018\nI HEREBY RELEASE THIS FLIGHT IN FULL COMPLIANCE WITH CIVIL AVIATION\nLAW AND/OR COMPANY OPERATIONS MANUAL.\n- DISPATCHER:    SEONGHYUNG_LEE\nI HEREBY PREPARE AND ARRANGE THIS FLIGHT RELEASE ACCORDING TO THE\nINSTRUCTION AND DATA PROVIDED BY\n- AGENT:                               SIGN . . . . . . . . . .\nI HEREBY ACCEPT THIS FLIGHT RELEASE WITH FULL ACKNOWLEDGEMENT.\nPage 90\n- PILOT IN COMMAND:                    SIGN . . . . . . . . . .\n(FPL-AAR224-IS\n-A388/J-SDE1E2E3FGHIJ2J3J4J5M1P2RWXYZ/LB1D1\n-RKSI1205\n-N0505F310 DCT EGOBA Y697 KAE Y437 TENAS L512 IGOBI/N0499F330 L512\n TATAM/N0499F350 L512 GTC Y512 OATIS/M085F350 R580 OPHET/M084F360\n R580 ORCCA/N0480F370 DCT SQA DCT GKN DCT GAHAM/M084F370 DCT\n 62N130W 61N120W 59N110W 56N100W 51N090W 46N080W/N0474F370 DCT\n NOVON DCT YODAA PUCKY1\n-KJFK1324 KBOS\n-PBN/A1B1C1D1L1O1S2 DAT/1FANSP CPDLCX SUR/RSP180 260B CANMANDATE\n DOF/260810 REG/HL7626\n EET/RJJJ0046 PAZA0345 ADIZ0436 PAZA0436 CZEG0755 CZWG1013 CZYZ1138\n KZBW1239 KZNY1302\n SEL/GMKQ CODE/71BE26 PER/C RALT/RJCC PANC KORD RMK/TCAS II\n EQUIPPED\n-E/1612 P/TBN R/VE S/M J/L D/14 898 C SILVERGRAY\n A/WHITE)\nPLAN VALID FOR DEPARTURE UNTIL  1805Z 10/AUG/26\n     START OF WIND AND TEMPERATURE SUMMARY ICN TO JFK\nFL    ISA   WIND CMP TMP   WIND CMP TMP   WIND CMP TMP   WIND CMP TMP\n350   -54   31052+037-40   34047+019-41   01032-004-43   02027-012-43\n330   -50   34031+009-36   01028-005-37   03019-010-38   03018-012-39\n310   -46   03015-007-32   05015-012-33   05017-013-33   04020-014-33\n290   -42   06007-006-28   07009-009-28   06016-013-28   04020-015-28\n270   -38   07006-006-23   07008-008-23   05014-011-23   04018-012-23\n               BUSKO          TENAS          SABET          ANDOL\n350   -54   02027-013-44   02041-019-44\n330   -50   03023-014-39   02039-018-39\n310   -46   03023-014-33   01036-013-34\n290   -42   03022-013-28   01034-010-29\n270   -38   03021-012-23   01033-010-24\n               KAMSA          IGOBI\n370   -56   03055-028-50\n350   -54   02059-028-45\n330   -50   02050-019-41\n310   -46   01048-014-35\n290   -42   01045-011-30\n               TATAM\n390   -56   04054-034-55   05045-037-52   07036-035-51   11040-039-51\n370   -56   04058-037-49   04045-035-49   07037-036-48   11043-042-47\n350   -54   03058-036-46   04045-033-45   06037-035-44   11045-044-43\n330   -50   03052-027-41   04055-040-41   06044-041-40   10033-033-39\nPage 91\n310   -46   02050-020-35   03049-030-36   05043-035-36   07029-027-35\n               GTC            ELDAK          SDE            BEKEN\n390   -56   13059-051-55   13058-052-53\n370   -56   13067-059-47   13065-058-47\n350   -54   13051-046-43   12052-048-42\n330   -50   12041-038-38   12044-042-37\n310   -46   11036-035-33   11039-038-32\n               SOVMO          OATIS\n370   -56   13064-003-48   16034+014-48   18021+013-48   19023+018-49\n360   -56   13067-003-45   15031+009-45   17023+013-46   19023+018-46\n350   -54   13057-008-42   14027+005-42   17025+013-43   19023+018-44\n340   -52   12044-010-40   14024+002-40   17027+013-40   19023+019-41\n330   -50   12042-011-37   13024+000-37   17028+014-38   20024+020-38\n               MAKMU          ONEMU          OPULO          OMOTO\n370   -56   22019+018-49   24018+018-49\n360   -56   22020+019-46   24020+020-47\n350   -54   22021+020-43   24021+021-44\n340   -52   22022+021-41   24022+022-41\n330   -50   22023+022-38   24023+023-38\n               OGDEN          OPHET\n380   -56   26021+020-53   28034+026-53   30051+018-53   31068+021-54\n370   -56   26021+020-50   28033+026-50   29050+019-50   31066+021-51\n360   -56   26021+020-47   27033+027-47   29049+020-47   31064+020-48\n350   -54   26022+021-44   27033+027-44   29048+021-44   31061+020-45\n340   -52   26022+021-41   27032+027-41   29047+022-42   31059+019-43\n               OLCOT          OPAKE          ONEIL          OBOYD\n380   -56   32089+006-57   34086-012-55   34060-007-52   35019-004-50\n370   -56   32092+006-54   34092-012-54   34064-008-52   34017-002-51\n360   -56   32089+008-51   34098-010-51   34068-008-50   34015-002-51\n350   -54   32085+008-48   33101-009-49   34072-009-48   34013-001-50\n340   -52   32082+008-45   33092-007-46   34075-010-46   34011+000-49\n               OFORD          OGGOE          ONEOX          ORVIL\n380   -56   09010-009-54\n370   -56   11012-010-55\n360   -56   12014-008-56\n350   -54   14016-005-54\n340   -52   16018-002-52\n               ORCCA\n400   -56   14012-005-55   26019+019-58   30027+021-55   31025+019-53\n390   -56   15013-003-57   24022+022-59   30032+026-57   31028+022-54\n370   -56   16018-001-59   24026+025-59   30037+030-56   30033+027-55\n350   -54   17020+001-54   25021+021-53   30042+033-52   30037+031-52\n330   -50   17016+001-49   26019+019-48   30044+034-47   30034+029-48\n               SQA            GKN            GAHAM          62N30\nPage 92\n400   -56   32011+008-52   33011+009-50   30025+025-49   30044+043-50\n390   -56   31011+009-52   33011+008-51   30026+026-50   30047+046-50\n370   -56   31013+011-56   34014+009-54   30031+031-52   30052+051-52\n350   -54   30015+014-56   35017+008-56   30037+037-53   30058+057-52\n330   -50   30017+016-52   35019+007-52   29040+040-49   30061+060-49\n               61N20          59N10          56N00          5190N\n400   -56   29061+058-51   27072+054-53\n390   -56   29065+063-51   27076+055-53\n370   -56   29069+067-53   27079+061-52\n350   -54   29072+070-51   28082+068-49\n330   -50   29073+071-48   28084+072-45\n               4680N          NOVON\nDRIFTDOWN SUMMARY DATA\nCRZ  TO   BURN  FL  MSA  TO   BURN  FL  MSA  FOB   LAT    LON     W\nLRC RJCC 122491 100 098 PANC 121793 100 139 298993 N53066 E170276 M\n   *PANC 101376 100 199 KORD 101119 100 043 151626 N58480 W109096 M\n1LE RJCC 099825 280 098 PANC 098410 290 139 300625 N52510 E169510\n   *PANC 074056 340 199 KORD 073721 330 043 154295 N59090 W110354\n2LE RJCC 131584 090 098 PANC 125759 110 139 304069 N52240 E168288 M\n   *PANC 093156 170 199 KORD 092201 170 043 154295 N59090 W110354 M\nWARNING FLAGS:  M-MSA,  D-FUEL DUMP REQ.,  F-DIVERT FUEL REQ.,\n                        S-SPIRAL DESCENT\nEND OF JEPPESEN DATAPLAN\nREQUEST NO.  3201\nPage 93\n(TDM TRK C 260810190001\n2608101900 2608110800\nKATCH HMPTN GRIZZ CJAYY 57N160W 55N170W EYWAK CARTO CUTEE KALIG\nKALNA\nRTS/CYVR UQQ KATCH\nKSEA TOU FINGS KATCH\nKPDX TOU FINGS KATCH\nKSFO TOU FINGS KATCH\nKLAX TOU FINGS KATCH\nKALNA OTR5 ADNAP\nRMK/0)\n(TDM TRK A 260810190001\n2608101900 2608110800\nPUPPI CRESP 24N170W 27N180E 30N170E 33N160E 34N150E MORAY\nRTS/PHNL KEOLA PUPPI\nMORAY OTR15 POVAL\nRMK/TRK B NOT AVAILABLE\n)\n(TDM TRK 12 260809170901\n2608101000 2608102100\nSEALS 35N150E 34N160E 33N170E 30N180E 27N170W SYVAD\nRTS/ LAPIL OTR13 SEALS\n     SYVAD BOOKE PHNL\nRMK/ ATM CENTER TEL:81-92-608-8870)\n(TDM TRK 3 260809170801\n2608100700 2608102100\nEMRON 42N160E 44N170E 45N180E 45N170W 44N160W 43N150W 41N140W\n39N130W DACEM\nRTS/ AVBET OTR9 EMRON\n     DACEM PAINT PIRAT BURGL IRNMN KLAX\n     DACEM PAINT PIRAT OSI KSFO\nRMK/ ATM CENTER TEL:81-92-608-8870)\n(TDM TRK 2 260809170801\n2608100700 2608102100\nADGOR AGEDI AKISU ASPIN LYYLE 50N180E 49N170W 48N160W 47N150W\n45N140W 42N130W VESPA\nRTS/ ADNAP R591 ADGOR\n     VESPA AMAKR BGGLO KSFO\n     VESPA ENI OAK BURGL IRNMN KLAX\nRMK/0)\nPage 94\n(TDM TRK 1 260809170801\n2608100700 2608102100\nOMOTO OGDEN OPHET PLADO CHIKI 51N170W 51N160W 50N150W 49N140W PRETY\nRTS/ MAKMU R580 OMOTO\n     PRETY TOU KSEA\n     PRETY TOU KPDX\n     PRETY GOVAD CYVR\nRMK/ ACFT LDG OTHER DEST--PRETY UPR TO DEST)\n(TDM TRK 11 260809170901\n2608101000 2608102100\nSEALS 35N150E 34N160E 33N170E 30N180E 27N170W DANNO\nRTS/ LAPIL OTR13 SEALS\n     DANNO BOOKE PHNL\nRMK/ TRK 11 NOT AVAILABLE IF CROSSING DANNO AFTER 1830Z.)\n(TDM TRK 14 260809170901\n2608100700 2608102100\nEMRON 40N160E 43N170E 44N180E 44N170W 43N160W 42N150W 40N140W\n38N130W ALLBE\nRTS/ MOLKA M750 MUKEP Y891 OVSUN Y893 IGMIS Y57 POROT OTR11 AVBET\n     OTR9 EMRON\n     ALLBE PIRAT OSI KSFO\n     ALLBE PIRAT BURGL IRNMN KLAX\nRMK/ TRK 15 NOT AVAILABLE\n     ATM CENTER TEL:81-92-608-8870)\nPage 95"
    }
]

def get_aar224_sample_briefing() -> dict:
    """
    Returns authentic flight briefing for AAR224 / OZ224 (RKSI Incheon -> KJFK New York JFK).
    """
    return {
        "flight_summary": {
            "callsign": "AAR224",
            "flight_number": "OZ224",
            "aircraft_type": "A380-800 / Trent 970 (HL7626)",
            "flight_date": "10 AUG 2026",
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
            "route_summary": "RKSI DCT EGOBA Y697 KAE Y437 TENAS L512 IGOBI/N0499F330 L512 TATAM/N0499F350 L512 GTC Y512 OATIS/M085F350 R580 OPHET/M084F360 R580 ORCCA/N0480F370 DCT SQA DCT GKN DCT GAHAM/M084F370 DCT 62N130W 61N120W 59N110W 56N100W 51N090W 46N080W/N0474F370 DCT NOVON DCT YODAA PUCKY1 KJFK",
            "alternate_airports": [
                {
                    "icao": "KBOS",
                    "iata": "BOS",
                    "name": "보스턴 로건 국제공항 (Boston Logan Intl)",
                    "role": "FILED DEST ALTERNATE",
                    "divertStatus": "AVAILABLE",
                    "divertLabel": "DIVERT AVAILABLE (회항 가능)",
                    "visRating": "시정 6SM 이상 (최저치 상회)",
                    "etaZ": "02:14Z (+1)",
                    "etaL": "22:14 L",
                    "distTime": "260 NM / 45분 / 22,400 LBS",
                    "wxStatus": "GOOD",
                    "wxSummary": "Wind 290/10kt, 시정 6SM 이상, SKC. 법정 최저치 상회 만족, 안전 회항 가용."
                },
                {
                    "icao": "PANC",
                    "iata": "ANC",
                    "name": "앵커리지 테드 스티븐스 공항 (Ted Stevens Intl)",
                    "role": "ENROUTE EDTO ERA / ETP 1&2",
                    "divertStatus": "AVAILABLE",
                    "divertLabel": "DIVERT AVAILABLE (회항 가능)",
                    "visRating": "시정 10SM (양호)",
                    "etaZ": "18:22Z",
                    "etaL": "10:22 L",
                    "distTime": "1,355 NM / 03h 48m / 122,500 LBS",
                    "wxStatus": "GOOD",
                    "wxSummary": "Wind 160/08kt, 시정 10SM, SCT040. 법정 ERA 최저치 상회 충족."
                }
            ]
        },
        "key_alerts": [
            {
                "type": "WEATHER",
                "title": "KJFK 도착 시간대 뇌우(TSRA) 및 적란운(CB) 통과 주의",
                "desc": "도착 예정 시간(01:29Z) 전후 시정 3SM 저하 및 돌풍 가능성(PROB30). 회항공항(KBOS) 연료 마진 확보 완료.",
                "level": "HIGH",
                "target": "wx"
            },
            {
                "type": "NOTAM",
                "title": "KJFK 신규 터미널 건설 및 활주로 04L/22R 폐쇄 NOTAM 확인",
                "desc": "KJFK RWY 04L/22R 폐쇄 및 유도로 B/C 공사로 지상 이동 시 관제사 지시 복창 철저.",
                "level": "CRITICAL",
                "target": "notam"
            },
            {
                "type": "FUEL & WEIGHT",
                "title": "탑재 연료(475,800 LBS) 및 이륙 중량(1,249,600 LBS) 일치 확인",
                "desc": "비행계획서상의 연료량과 실제 급유량을 상호 대조하고 무게중심(CG) 한계를 확인하십시오.",
                "level": "MEDIUM",
                "target": "fuel"
            },
            {
                "type": "OPERATION",
                "title": "RKSI 표준 계기 출항(SID) 및 소음 저감 절차 준수",
                "desc": "초기 상승 고도 및 최저 안전고도(MSA)를 철저히 준수하십시오. 400ft AGL 이하 조기 선회 금지.",
                "level": "CRITICAL",
                "target": "rules"
            }
        ],
        "route_analysis": {
            "filed_route_string": "RKSI DCT EGOBA Y697 KAE Y437 TENAS L512 IGOBI/N0499F330 L512 TATAM/N0499F350 L512 GTC Y512 OATIS/M085F350 R580 OPHET/M084F360 R580 ORCCA/N0480F370 DCT SQA DCT GKN DCT GAHAM/M084F370 DCT 62N130W 61N120W 59N110W 56N100W 51N090W 46N080W/N0474F370 DCT NOVON DCT YODAA PUCKY1 KJFK",
            "alternate_routing": "KJFK DCT MERIT DCT ORW V16 PVD INNDY3 KBOS",
            "total_distance": "6,663 NM",
            "flight_time": "13Hr 24Min",
            "fir_crossings": [
                { "fir": "RJJJ (FUKUOKA)", "fix": "ANDOL", "eet": "00:46Z" },
                { "fir": "PAZA (ANCHORAGE)", "fix": "NIPPI", "eet": "03:45Z" },
                { "fir": "CZEG (EDMONTON)", "fix": "62N130W", "eet": "07:55Z" },
                { "fir": "CZWG (WINNIPEG)", "fix": "56N100W", "eet": "10:13Z" },
                { "fir": "CZYZ (TORONTO)", "fix": "46N080W", "eet": "11:38Z" },
                { "fir": "KZBW (BOSTON)", "fix": "NOVON", "eet": "12:39Z" },
                { "fir": "KZNY (NEW YORK)", "fix": "PUCKY", "eet": "13:02Z" }
            ],
            "waypoints": [
                { "name": "RKSI", "dist": "0", "fl": "GND", "wind": "200/10kt", "tas": "0", "gs": "0", "eet": "00:00", "fuelRem": "475.8k" },
                { "name": "EGOBA", "dist": "44", "fl": "FL240", "wind": "220/15kt", "tas": "410", "gs": "402", "eet": "00:07", "fuelRem": "468.2k" },
                { "name": "KAE", "dist": "120", "fl": "FL310", "wind": "240/35kt", "tas": "485", "gs": "505", "eet": "00:18", "fuelRem": "455.1k" },
                { "name": "TENAS", "dist": "298", "fl": "FL310", "wind": "250/45kt", "tas": "488", "gs": "520", "eet": "00:39", "fuelRem": "435.0k" },
                { "name": "IGOBI", "dist": "540", "fl": "FL330", "wind": "260/60kt", "tas": "490", "gs": "545", "eet": "01:08", "fuelRem": "410.5k" },
                { "name": "TATAM", "dist": "980", "fl": "FL350", "wind": "270/75kt", "tas": "492", "gs": "560", "eet": "01:58", "fuelRem": "372.0k" },
                { "name": "OPHET", "dist": "1850", "fl": "FL360", "wind": "280/85kt", "tas": "495", "gs": "575", "eet": "03:32", "fuelRem": "295.0k" },
                { "name": "SQA", "dist": "3420", "fl": "FL370", "wind": "290/60kt", "tas": "490", "gs": "545", "eet": "06:28", "fuelRem": "198.5k" },
                { "name": "62N130W", "dist": "4120", "fl": "FL370", "wind": "300/40kt", "tas": "488", "gs": "525", "eet": "07:55", "fuelRem": "152.0k" },
                { "name": "56N100W", "dist": "5280", "fl": "FL370", "wind": "280/30kt", "tas": "485", "gs": "512", "eet": "10:13", "fuelRem": "96.4k" },
                { "name": "NOVON", "dist": "6410", "fl": "FL370", "wind": "260/20kt", "tas": "480", "gs": "495", "eet": "12:39", "fuelRem": "45.0k" },
                { "name": "KJFK", "dist": "6663", "fl": "GND", "wind": "180/12kt", "tas": "0", "gs": "0", "eet": "13:24", "fuelRem": "36.2k" }
            ]
        },
        "validation_check": {
            "match_percentage": "100%",
            "cfp_route": "RKSI EGOBA Y697 KAE Y437 TENAS L512 IGOBI TATAM GTC Y512 OATIS R580 OPHET ORCCA SQA GKN GAHAM 62N130W 61N120W 59N110W 56N100W 51N090W 46N080W NOVON YODAA PUCKY1 KJFK",
            "ats_fpl_route": "(FPL-AAR224-IS -A388/J-SDE1E2E3FGHIJ2J3J4J5M1P2RWXYZ/LB1D1 -RKSI1205 -N0505F310 DCT EGOBA Y697 KAE Y437 TENAS L512 IGOBI/N0499F330 L512 TATAM/N0499F350 L512 GTC Y512 OATIS/M085F350 R580 OPHET/M084F360 R580 ORCCA/N0480F370 DCT SQA DCT GKN DCT GAHAM/M084F370 DCT 62N130W 61N120W 59N110W 56N100W 51N090W 46N080W/N0474F370 DCT NOVON DCT YODAA PUCKY1 -KJFK1324 KBOS)",
            "items": [
                {
                    "category": "1. TOW / AGTOW 여유",
                    "detail": "EST TOW (1,249,600 LBS) vs AGTOW (1,254,400 LBS) - 여유 4,800 LBS ★ [3대 중량 중 최소 여유 - 유효 탑재 제한사항]",
                    "status": "여유 4,800 LBS (최소제한)",
                    "statusType": "OK",
                    "isGoverningLimit": True
                },
                {
                    "category": "2. ZFW / MZFW 여유",
                    "detail": "EST ZFW (773,800 LBS) vs MZFW (813,500 LBS) - 여유 39,700 LBS (충족)",
                    "status": "여유 39,700 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "3. LDW / MLDW 여유",
                    "detail": "EST LDW (843,700 LBS) vs MLDW (862,000 LBS) - 여유 18,300 LBS (충족)",
                    "status": "여유 18,300 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "4. MEL / CDL 내용",
                    "detail": "MEL 33-20-05A (CABIN LIGHT), CDL 27-32 (DROOP NOSE FAIRING) 반영 완료",
                    "status": "APPLIED (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "5. 디스패치 고려사항",
                    "detail": "KJFK 뇌우 및 입항 정체 대비 추가 45분 연료(DISC 22,400 LBS) 탑재",
                    "status": "CONFIRMED (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "6. 이륙연료 합계",
                    "detail": "TRIP(405,900) + CONT(12,200) + ALTN(22,400) + FINRES(11,000) + DISC(22,400) = 473,900 LBS",
                    "status": "473,900 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "7. 램프연료 합계",
                    "detail": "TAXI (1,900 LBS) + TAKEOFF FUEL = BLOCK 475,800 LBS 탑재 확인",
                    "status": "475,800 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "8. 도착 잔여 vs 교체+최종예비",
                    "detail": "도착 예상 잔여 연료(36,200 LBS) > 법정 최저치(33,400 LBS) 여유 2,800 LBS 확보",
                    "status": "여유 +2,800 LBS",
                    "statusType": "OK"
                },
                {
                    "category": "9. 교체공항 연료 일치",
                    "detail": "KBOS 회항 계획(260 NM, 45분 소요, 22,400 LBS) 수치 일치",
                    "status": "22,400 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "10. CFP 항로 vs ATS FPL",
                    "detail": "비행계획서(CFP) 전 구간 58개 웨이포인트 및 FPL 전문 100% 일치",
                    "status": "100% MATCH",
                    "statusType": "OK"
                },
                {
                    "category": "11. RVSM 고도계 점검 요건",
                    "detail": "RVSM 공역 진입 전 주/예비 고도계 지침(허용 오차 75FT) 정상 반영",
                    "status": "VERIFIED (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "12. EDTO / ETOPS 법정 요건",
                    "detail": "EDTO 180분 적용, ERA(RJCC, PANC, KORD, KBOS) 전 공항 기상 최저치 상회",
                    "status": "EDTO 180 VALID",
                    "statusType": "OK"
                },
                {
                    "category": "13. CPDLC / ADS-C 데이터링크",
                    "detail": "태평양 및 북극 항로(PAZA/CZEG) FANS-1/A CPDLC 및 ADS-C 활성화 확인",
                    "status": "ACTIVE (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "14. RAIM / GPS 무결성 예측",
                    "detail": "출발~도착 전 구간 GPS 위성 수신 무결성(FDE) 이상 없음",
                    "status": "AVAILABLE (OK)",
                    "statusType": "OK"
                }
            ]
        },
        "weather_briefing": {
            "departure": {
                "icao": "RKSI",
                "name": "인천국제공항 (Incheon Intl)",
                "etd": "12:05Z (21:05 L)",
                "runway": "RWY 15L/15R",
                "wind": "200° / 10 KT",
                "visibility": "10 KM+ (CAVOK)",
                "ceiling": "SKC / NSC",
                "temp_qnh": "24°C / 1012 hPa",
                "assessment": [
                    "출발지 기상 양호, 마른 활주로(Dry) 이륙 최저치 만족하여 정시 출발 가능.",
                    "이륙 직후 400ft AGL 이하 조기 선회 금지 지침 준수."
                ],
                "raw_metar": "METAR RKSI 100500Z 20010KT CAVOK 24/19 Q1012 NOSIG=",
                "raw_taf": "TAF RKSI 100500Z 1006/1112 20010KT CAVOK="
            },
            "destination": {
                "icao": "KJFK",
                "name": "뉴욕 존 F. 케네디 국제공항 (John F. Kennedy Intl)",
                "eta": "01:29Z (+1) (21:29 L)",
                "runway": "RWY 13L/22L/31L",
                "wind": "180° / 12 KT",
                "visibility": "6 SM 이상 (강수 3SM)",
                "ceiling": "SCT050 (적란운 CB 감지)",
                "temp_altimeter": "22°C / A3002",
                "assessment": [
                    "도착 시간대 적란운(CB) 및 소나기 예보(PROB30)로 접근 지연 가능성.",
                    "대체공항(KBOS) 회항 계획 및 예비연료 확인 완료."
                ],
                "raw_metar": "METAR KJFK 100551Z 18012KT 10SM CLR 22/16 A3002=",
                "raw_taf": "TAF KJFK 100522Z 1006/1112 18012KT P6SM SCT060 PROB30 1100/1104 3SM TSRA BKN030CB="
            },
            "alternate": {
                "icao": "KBOS",
                "name": "보스턴 로건 국제공항 (Boston Logan Intl)",
                "eta": "02:14Z (+1) (22:14 L)",
                "raw_metar": "METAR KBOS 100554Z 29010KT 10SM FEW250 21/14 A3000=",
                "raw_taf": "TAF KBOS 100534Z 1006/1112 29010KT P6SM FEW250=",
                "suitability": "GOOD",
                "assessment": "보스턴 로건 공항 법정 교체공항 최저치 상회 만족, 안전 회항 보장."
            },
            "turbulence_timeline": [
                {
                    "time": "T+00:45",
                    "level": "Light Turb",
                    "segment": "[KAE ~ TENAS / FL310~330]",
                    "detail": "상승 및 순항고도 진입 구간 기류 요동 (정상 순항)",
                    "action": "정상 순항"
                },
                {
                    "time": "T+04:30",
                    "level": "Moderate Turb",
                    "segment": "[PAZA / OPHET ~ SQA / FL360]",
                    "detail": "제트기류 전단대(Jetstream Shearing) 통과",
                    "action": "벨트 사인 사전 점등"
                },
                {
                    "time": "T+11:15",
                    "level": "Light to Moderate",
                    "segment": "[CZYZ ~ KZBW / FL370]",
                    "detail": "강하 전 고고도 난류 구역 통과",
                    "action": "착륙 준비 사전 착수"
                }
            ],
            "sigmets": [
                {
                    "fir": "[PAZA / CZEG FIR]",
                    "text": "SIGMET VALID FOR HIGH ALTITUDE MODERATE TURBULENCE FL340-FL380."
                },
                {
                    "fir": "[RJJJ 일본 FIR]",
                    "text": "TYPHOON CHAN-HOM LOCATED 280NM SE OF TOKYO, MOVING NE AT 15KT. NO DIRECT IMPACT ON FILED ROUTE."
                }
            ]
        },
        "fuel_and_weights": {
            "block_fuel": "475,800 LBS",
            "trip_fuel": "405,900 LBS",
            "contingency_fuel": "12,200 LBS",
            "alternate_fuel": "22,400 LBS",
            "final_reserve": "11,000 LBS",
            "extra_fuel": "22,400 LBS",
            "extra_fuel_reason": "KJFK 뇌우(TSRA) 홀딩 및 지상 정체 대비 디스패치 권고 연료",
            "estimated_tow": "1,249,600 LBS",
            "max_tow": "1,254,400 LBS",
            "tow_margin": "여유 4,800 LBS",
            "estimated_law": "843,700 LBS",
            "max_law": "862,000 LBS",
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
        "company_rules_and_mel": {
            "company_advisories": [
                {
                    "id": "COMPANY ADVISORY 01",
                    "title": "RKSI 표준 계기 출항(SID) 및 소음 저감 지침 준수",
                    "detail": "400FT AGL 이하 조기 선회 금지 및 초기 상승 프로파일 준수",
                    "impact": "CRITICAL"
                },
                {
                    "id": "COMPANY ADVISORY 02",
                    "title": "유사 편명 (Similar Call Signs) 주의",
                    "detail": "관제 교신 시 유사 호출부호 혼선 방지를 위한 복창 철저",
                    "impact": "CAUTION"
                }
            ],
            "mel_cdl_items": [
                {
                    "code": "MEL 33-20-05A",
                    "item": "32K, 51K WINDOW LIGHT OUT",
                    "action": "DEFERRED IAW MEL 33-20-05A (비행계획 후 발부)",
                    "status": "CONFIRMED"
                },
                {
                    "code": "CDL 27-32",
                    "item": "LH WING NO 1 DROOP NOSE INBD LATERAL D-S",
                    "action": "좌측 날개 1번 드룹 노즈 CDL 적용 (운항 성능 반영 완료)",
                    "status": "APPLIED"
                }
            ]
        },
        "flight_release_report": {
            "flight_no": "AAR224 / 10AUG26",
            "dispatcher": "SEONGHYUNG_LEE (TEL: 02-6101-5503 / ocws@flyasiana.com)",
            "release_statement": "I HEREBY RELEASE THE FLIGHT AAR0224/10AUG, ICN/JFK, HL7626, ETD 1205Z AS PLAN # 3201 UNDER THE CONDITIONS SPECIFIED.",
            "rvsm_status": "RECORDED (OK)"
        },
        "edto_etops": {
            "etp_items": [
                {
                    "sector": "ETP 1 : RJCC (신치토세) - PANC (앵커리지)",
                    "pos": "N53°06.6 E170°27.6 (웨이포인트 ETP1 인근)",
                    "dist1": "2,283 NM to RJCC (04h 39m, Fuel 174,900 LBS)",
                    "dist2": "1,355 NM to PANC (03h 48m, Fuel 122,500 LBS)",
                    "wind": "RJCC M019 / PANC M005"
                },
                {
                    "sector": "ETP 2 : PANC (앵커리지) - KORD (시카고)",
                    "pos": "N58°48.0 W109°09.6 (웨이포인트 ETP2 인근)",
                    "dist1": "4,853 NM to PANC (09h 49m, Fuel 322,300 LBS)",
                    "dist2": "1,287 NM to KORD (03h 24m, Fuel 101,400 LBS)",
                    "wind": "PANC M002 / KORD P018"
                }
            ],
            "designated_eras": "RKSI, RJCC, PANC, KORD, KBOS"
        },
        "ats_icao_fpl": {
            "raw_fpl": """(FPL-AAR224-IS
-A388/J-SDE1E2E3FGHIJ2J3J4J5M1P2RWXYZ/LB1D1
-RKSI1205
-N0505F310 DCT EGOBA Y697 KAE Y437 TENAS L512 IGOBI/N0499F330 L512
 TATAM/N0499F350 L512 GTC Y512 OATIS/M085F350 R580 OPHET/M084F360
 R580 ORCCA/N0480F370 DCT SQA DCT GKN DCT GAHAM/M084F370 DCT
 62N130W 61N120W 59N110W 56N100W 51N090W 46N080W/N0474F370 DCT
 NOVON DCT YODAA PUCKY1
-KJFK1324 KBOS
-PBN/A1B1C1D1L1O1S2 DAT/1FANSP CPDLCX SUR/RSP180 260B CANMANDATE
 DOF/260810 REG/HL7626
 EET/RJJJ0046 PAZA0345 ADIZ0436 PAZA0436 CZEG0755 CZWG1013 CZYZ1138
 KZBW1239 KZNY1302
 SEL/GMKQ CODE/71BE26 PER/C RALT/RJCC PANC KORD RMK/TCAS II EQUIPPED
-E/1612 P/TBN R/VE S/M J/L D/14 898 C SILVERGRAY A/WHITE)"""
        },
        "flight_crew_briefing": {
            "key_focus": "장거리 비행에 따른 순항 고도 관리 및 도착지 뇌우 회피 절차",
            "briefing_topics": [
                "출발 시 400ft AGL 이하 조기 선회 금지 지침 준수",
                "태평양/항로상 난류 예상 구간 승객 벨트 사인 사전 점등",
                "도착지 기상 악화 시 교체공항 회항 연료 마진 확인"
            ],
            "crew_coordination": [
                "단계별 연료 소모율 및 FOD 잔여 연료 상호 교차 점검",
                "도착 전 레이더 틸트 조절 및 기상 우회 경로 ATC 사전 조율"
            ],
            "checklist_action_items": [
                "출발 전 METAR/TAF 및 NOTAM 최종 업데이트 확인",
                "탑재 연료량과 OFP 일치 서명 확인",
                "항공기 결함(MEL/CDL) 적용 내역 확인"
            ]
        },
        "joint_briefing": {
            "key_focus": "운항관리사 및 객실승무원 합동 브리핑 (AAR224 ICN-JFK)",
            "flight_profile_summary": "총 비행시간 13시간 24분, 탑승객 475명. 캐나다 상공 고고도 난류 구간 통과 예정.",
            "safety_priorities": [
                "태평양 진입 전 객실 안전 점검 완료",
                "승객 착석 후 벨트 착용 상태 상시 육안 확인"
            ],
            "cabin_crew_coordination": [
                "이륙 후 1차 기내식 서비스는 02:00경 시작",
                "난류 예상 15분 전 기장실에서 객실 사전 통보"
            ],
            "joint_checklist": [
                { "item": "비행 계획 및 기상 브리핑 공유", "status": "COMPLETED" },
                { "item": "비상 장구 및 구명정 상태 확인", "status": "COMPLETED" },
                { "item": "특이 승객 및 의료 장비 탑재 확인", "status": "COMPLETED" }
            ]
        },
        "notam_briefing": {
            "general_summary": {
                "departure_hazards": "RKSI (인천): 활주로 15R/33L 정기 스위핑 완료(마른 노면/제동 양호), 유도로 R23/R24 대형기 제한. 이륙 직후 400FT AGL 이하 조기 선회 엄격 금지(FOM 6.4.4), 유사 호출부호 관제 교신 복창 철저.",
                "arrival_hazards": "KJFK (뉴욕): 활주로 04L/22R 공사 폐쇄, 신규 터미널 1 공사로 유도로 B/C 폐쇄 및 지상 이동 혼잡. 활주로 13L/22L ILS 정상 가동 중이나 뇌우 시정 저하 시 착륙 최저치(Minimum) 상향 확인, 크레인(160FT MSL) 주의. 도착 정체 대비 회항공항(KBOS) 연료 마진 확보.",
                "enroute_hazards": "PAZA/CZEG FIR: 북태평양 및 캐나다 공역 FL340~FL380 제트기류 전단 난류(CAT) 주의보 발효. 캐나다 공역 FANS-1/A CPDLC 필수 로그온, 대양 비상 강하 절차(ICAO Doc 7030) 준수, RVSM 고도계 오차(±75FT) 상시 점검."
            },
            "enroute_detailed_analysis": [
                {
                    "title": "3.1 에드먼턴 FIR 의무 계기 비행 규칙 (NOTAM CZEG F4091/26)",
                    "fir": "캐나다 에드먼턴(CZEG) FIR 내 공역 통과 시",
                    "raw_text": "F4091/26 NOTAMN\nQ) CZEG/QARXX/IV/NBO/E/280/430/6200N11500W999\nA) CZEG B) 2608290000 C) 2608292359\nE) WESTBOUND FLIGHTS ENTERING CZEG FIR FROM CZWG FIR TRANSITING TO CZVR FIR SHALL ROUTE ON OR NORTH OF TRACK: VINKO - RABOX - NOVAR UNLESS OTHERWISE APPROVED BY EDMONTON ACC.",
                    "conditions": "서향 비행편 (Westbound): 위니펙 FIR에서 에드먼턴 FIR을 거쳐 밴쿠버 FIR로 진입하는 비행편은 반드시 VINKO-RABOX-NOVAR 트랙상 또는 그 북쪽(On or North of)으로 항로를 설정해야 합니다.",
                    "correlation": "우리 비행(AAR223)과의 연관성: 당사 항로는 위니펙 공역을 지나 북위 62도에서 68도까지 극단적인 북단 트랙(62N100W -> 68N130W)을 경유하여 POTAT으로 비행하므로, 본 서향 비행 규정을 안전하게 우회 준수하고 있습니다."
                },
                {
                    "title": "3.2 앵커리지 FIR UPR 비행 규칙 (NOTAM PAZA A2352/26)",
                    "fir": "CZEG FIR과 PAZA FIR 경계선 통과 및 일본 후쿠오카 FIR 진입 구간",
                    "raw_text": "A2352/26 NOTAMN\nQ) PAZA/QARXX/IV/NBO/E/280/450/5800N17000W999\nA) PAZA B) 2608290000 C) 2608292359\nE) UPR GATEWAY RESTRICTION: ACFT CROSSING CZEG/PAZA BOUNDARY BTN TAYTA AND DEEJA SHALL CROSS DESIGNATED FIX POTAT. WESTBOUND FLIGHTS ENTERING RJJJ FIR SHALL JOIN R220 EAST OF NIKLL OR M523 EAST OF HIXOR.",
                    "conditions": "CZEG FIR과 PAZA FIR의 경계선 통과 시 TAYTA에서 DEEJA 사이 구간은 반드시 지정된 게이트 포인트를 통과해야 하며, 서향 UPR 비행편이 일본 후쿠오카 FIR로 진입할 시 반드시 R220 항로의 NIKLL 지점 동쪽 상공 또는 M523 항로의 HIXOR 지점 동쪽 상공에서 조인해야 합니다.",
                    "correlation": "우리 비행과의 연관성: 당사 항공기는 이에 부합하여 POTAT 지점을 통과하고, 항로상 NIKLL 지점을 정상 통과하도록 계획되어 수립되었습니다."
                },
                {
                    "title": "3.3 알래스카 북위 62도 경계 진입 제한 (NOTAM PAZA A0176/26)",
                    "fir": "서경 141도 기준, 북위 62도 이북 (N62 00 00 W141 00 00) 구역",
                    "raw_text": "A0176/26 NOTAMN\nQ) PAZA/QARXX/IV/NBO/E/280/410/6200N14100W100\nA) PAZA B) 2608290000 C) 2608292359\nE) AIRSPACE ENTRY RESTRICTION: ACFT ENTERING ANCHORAGE FIR NORTH OF N620000 W1410000 SHALL ROUTE DIRECT BTT ON OR NORTH OF GOATS DCT BTT DCT OME.",
                    "conditions": "앵커리지 FIR에 진입하는 비행편은 반드시 GOATS 지점 상공 혹은 그 북쪽(On or North of GOATS)에서 BTT로 직행해야 합니다.",
                    "correlation": "우리 비행과의 연관성: 당사 항로는 알래스카 진입 후 POTAT에서 BTT로 직행한 다음 OME VORTAC으로 조인하도록 구성되어 있으므로 안전하게 규정을 준수합니다."
                },
                {
                    "title": "3.4 러시아 해군 미사일/로켓 낙하 충격 구역 (NOTAM P3698/26)",
                    "fir": "캄차카반도 남서측 및 쿠릴 열도 인근 (494248N1581138E - 473000N1590000E - 474603N1543020E)",
                    "raw_text": "P3698/26 NOTAMN\nQ) UHPP/QWELW/IV/BO/W/000/999/4836N15620E150\nA) UHPP B) 2608290200 C) 2608291000\nE) TEMPO DANGEROUS AREA ESTABLISHED DUE TO RUSSIAN NAVAL MISSILE IMPACT TEST WI AREA: 494248N1581138E - 473000N1590000E - 474603N1543020E. SFC TO 98430FT AMSL. AVOID AIRSPACE OR COMPLY WITH ATC TACTICAL RADAR VECTOR/OFFSET INSTRUCTIONS.",
                    "conditions": "고도 SFC ~ 98,430FT AMSL 무제한 통제.",
                    "correlation": "우리 비행과의 연관성: 당사 비행 경로상의 OPULO-OMOTO-OPHET 구간에 걸쳐 있어, 진입 단계에서 관제사로부터 항로 오프셋 지시가 있을 수 있습니다."
                }
            ],
            "notam_list": ALL_414_NOTAMS
        },
        "threat_and_error_management": {
            "top_threats": [
                {
                    "threat": "KJFK 도착 시간대 뇌우(TSRA) 및 돌풍(Gusts) 발생",
                    "impact": "High",
                    "mitigation": "기상 레이더 조기 가동, 회항공항(KBOS) 연료 22,400 LBS 확보 및 조기 회항 결심"
                },
                {
                    "threat": "북태평양 및 캐나다 공역(FL360) 제트기류 전단 난류(CAT)",
                    "impact": "Medium",
                    "mitigation": "예상 구간 진입 15분 전 승객 벨트 사인 점등 및 객실 서비스 사전 중단"
                },
                {
                    "threat": "KJFK 신규 터미널 공사 및 유도로 B/C 폐쇄에 따른 지상 충돌 위험",
                    "impact": "Medium",
                    "mitigation": "공항 지상이동 차트 상시 대조, 관제사 지시 복창 및 점진적 서행"
                }
            ],
            "pilot_action_items": [
                "이륙 전 활주로 15R 마른 노면 이륙 성능 재확인",
                "태평양 ETP 1 & 2 지점 통과 시 실제 소모량 vs 비행계획서 오차 기록",
                "KJFK 착륙 전 최신 ATIS 청취 및 접근 활주로(13L/22L) 버그 세팅"
            ],
            "briefing_points": [
                "객실 승무원과 난류 예상 구간 및 서비스 중단 프로토콜 사전 조율 완료",
                "운항관리사 권고 추가 연료(DISC 22,400 LBS) 탑재 승인 완료"
            ]
        }
    }


def get_aar202_klax_sample_briefing() -> dict:
    """
    Returns authentic flight briefing for AAR202 / OZ202 (RKSI Incheon -> KLAX Los Angeles Intl).
    """
    return {
        "flight_summary": {
            "callsign": "AAR202",
            "flight_number": "OZ202",
            "aircraft_type": "A350-900 / Trent XWB (HL8382)",
            "flight_date": "10 AUG 2026",
            "departure": {
                "icao": "RKSI",
                "iata": "ICN",
                "name": "인천국제공항 (Incheon Intl)",
                "runways": "RWY 15L/15R, 16L/16R"
            },
            "destination": {
                "icao": "KLAX",
                "iata": "LAX",
                "name": "로스앤젤레스 국제공항 (Los Angeles Intl)",
                "runways": "RWY 24L/24R, 25L/25R"
            },
            "alternate": {
                "icao": "KSAN",
                "iata": "SAN",
                "name": "샌디에이고 국제공항 (San Diego Intl)"
            },
            "etd_utc": "05:30Z",
            "etd_lcl": "14:30 L",
            "eta_utc": "16:12Z",
            "eta_lcl": "09:12 L",
            "arrival_date": "10 AUG (SAME DAY LCL)",
            "flight_time": "10Hr 42Min",
            "total_distance": "5,980 NM",
            "cruising_altitude": "FL350 -> FL370 -> FL390",
            "cost_index": "CI 40",
            "route_summary": "RKSI NOPIK Y644 LANAT G597 AGASI ORENO R211 NIPPI OTR21 EMRON DCT 48N160E 50N170E 51N180E 51N170W 49N160W 46N150W 43N140W DCT CINCA DCT PIRAT PAINT2 KLAX",
            "alternate_airports": [
                {
                    "icao": "KSAN",
                    "iata": "SAN",
                    "name": "샌디에이고 국제공항 (San Diego Intl)",
                    "role": "FILED DEST ALTERNATE",
                    "divertStatus": "AVAILABLE",
                    "divertLabel": "DIVERT AVAILABLE (회항 가능)",
                    "visRating": "시정 10SM+ (최저치 상회)",
                    "etaZ": "17:02Z",
                    "etaL": "10:02 L",
                    "distTime": "109 NM / 28분 / 8,200 LBS",
                    "wxStatus": "GOOD",
                    "wxSummary": "Wind 270/08kt, 시정 10SM, SKC. 법정 최저치 만족, 안전 회항 가용."
                },
                {
                    "icao": "KONT",
                    "iata": "ONT",
                    "name": "온타리오 국제공항 (Ontario Intl)",
                    "role": "COMMERCIAL DIVERSION",
                    "divertStatus": "AVAILABLE",
                    "divertLabel": "DIVERT AVAILABLE (회항 가능)",
                    "visRating": "시정 10SM+ (최저치 상회)",
                    "etaZ": "16:45Z",
                    "etaL": "09:45 L",
                    "distTime": "45 NM / 18분 / 5,400 LBS",
                    "wxStatus": "GOOD",
                    "wxSummary": "LA 분지 내 대형 화물/여객 수용 가능, 기상 양호."
                }
            ]
        },
        "key_alerts": [
            {
                "type": "WEATHER",
                "title": "KLAX 도착 시 해풍(Sea Breeze) 및 아침 해무(Marine Layer) 소산 모니터링",
                "desc": "LAX 아침 도착 시간대 해안가 저고도 층운 소산 중이며 시정 10SM 이상 양호합니다. 접근 활주로 24R/25L 정밀접근 가능.",
                "level": "MEDIUM",
                "target": "wx"
            },
            {
                "type": "NOTAM",
                "title": "KLAX 서측 터미널 코어 및 유도로 E 공사 NOTAM 확인",
                "desc": "KLAX 유도로 E(E6~E7) 공사로 폐쇄 진행 중. 지상 이동 시 관제사 지시 복창 철저.",
                "level": "HIGH",
                "target": "notam"
            },
            {
                "type": "FUEL & WEIGHT",
                "title": "탑재 연료(RAMP 218,500 LBS) 및 이륙중량(TOW 568,200 LBS) 일치 확인",
                "desc": "태평양 PACOTS 항로 풍향/풍속 최적화 및 회항공항(KSAN) 연료 마진 정상 반영 완료.",
                "level": "MEDIUM",
                "target": "fuel"
            },
            {
                "type": "OPERATION",
                "title": "북태평양(PACOTS / OTR) ETOPS 180분 구간 준수",
                "desc": "ETP 1 (RJCC-PANC) 및 ETP 2 (PANC-KSFO) 구간 연료 소모율 모니터링.",
                "level": "CRITICAL",
                "target": "rules"
            }
        ],
        "route_analysis": {
            "filed_route_string": "RKSI DCT NOPIK Y644 LANAT G597 AGASI ORENO R211 NIPPI OTR21 EMRON DCT 48N160E 50N170E 51N180E 51N170W 49N160W 46N150W 43N140W DCT CINCA DCT PIRAT PAINT2 KLAX",
            "alternate_routing": "KLAX DCT SLI V83 OCN V208 MZB KSAN",
            "total_distance": "5,980 NM",
            "flight_time": "10Hr 42Min",
            "fir_crossings": [
                { "fir": "RJJJ (FUKUOKA)", "fix": "LANAT", "eet": "00:38Z" },
                { "fir": "PAZA (ANCHORAGE)", "fix": "51N180E", "eet": "04:15Z" },
                { "fir": "KZAK (OAKLAND OCEANIC)", "fix": "46N150W", "eet": "07:30Z" },
                { "fir": "KZLA (LOS ANGELES)", "fix": "CINCA", "eet": "09:48Z" }
            ],
            "waypoints": [
                { "name": "RKSI", "dist": "0", "fl": "GND", "wind": "200/10kt", "tas": "0", "gs": "0", "eet": "00:00", "fuelRem": "218.5k" },
                { "name": "NOPIK", "dist": "48", "fl": "FL240", "wind": "220/18kt", "tas": "420", "gs": "410", "eet": "00:08", "fuelRem": "214.2k" },
                { "name": "AGASI", "dist": "285", "fl": "FL350", "wind": "260/45kt", "tas": "485", "gs": "525", "eet": "00:41", "fuelRem": "202.8k" },
                { "name": "EMRON", "dist": "1250", "fl": "FL350", "wind": "270/65kt", "tas": "488", "gs": "550", "eet": "02:26", "fuelRem": "165.4k" },
                { "name": "51N180E", "dist": "2340", "fl": "FL370", "wind": "280/85kt", "tas": "490", "gs": "572", "eet": "04:18", "fuelRem": "128.0k" },
                { "name": "46N150W", "dist": "3980", "fl": "FL390", "wind": "275/70kt", "tas": "488", "gs": "556", "eet": "07:05", "fuelRem": "76.5k" },
                { "name": "CINCA", "dist": "5420", "fl": "FL390", "wind": "260/35kt", "tas": "485", "gs": "518", "eet": "09:39", "fuelRem": "32.4k" },
                { "name": "KLAX", "dist": "5980", "fl": "GND", "wind": "250/08kt", "tas": "0", "gs": "0", "eet": "10:42", "fuelRem": "24.8k" }
            ]
        },
        "validation_check": {
            "match_percentage": "100%",
            "cfp_route": "RKSI NOPIK Y644 LANAT G597 AGASI ORENO R211 NIPPI OTR21 EMRON 48N160E 50N170E 51N180E 51N170W 49N160W 46N150W 43N140W CINCA PIRAT PAINT2 KLAX",
            "ats_fpl_route": "(FPL-AAR202-IS -A359/H-SDE1E2E3FGHIJ2J3J4J5M1P2RWXYZ/LB1D1 -RKSI0530 -N0488F350 NOPIK Y644 LANAT G597 AGASI ... -KLAX1042 KSAN)",
            "items": [
                {
                    "category": "1. TOW / AGTOW 여유",
                    "detail": "EST TOW (568,200 LBS) vs AGTOW (617,200 LBS) - 여유 49,000 LBS ★ [3대 중량 중 최소 여유 - 유효 탑재 제한사항]",
                    "status": "여유 49,000 LBS (최소제한)",
                    "statusType": "OK",
                    "isGoverningLimit": True
                },
                {
                    "category": "2. ZFW / MZFW 여유",
                    "detail": "EST ZFW (361,100 LBS) vs MZFW (423,200 LBS) - 여유 62,100 LBS (충족)",
                    "status": "여유 62,100 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "3. LDW / MLDW 여유",
                    "detail": "EST LDW (385,800 LBS) vs MLDW (451,900 LBS) - 여유 66,100 LBS (충족)",
                    "status": "여유 66,100 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "4. MEL / CDL 내용",
                    "detail": "MEL 25-20-01A (PAX SEAT DEFERRAL) 반영 완료, 운항 제한 없음",
                    "status": "APPLIED (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "5. 디스패치 고려사항",
                    "detail": "KLAX 해풍 및 입항 정체 대비 추가 30분 연료(DISC 4,500 LBS) 탑재",
                    "status": "CONFIRMED (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "6. 이륙연료 합계",
                    "detail": "TRIP(182,400) + CONT(5,600) + ALTN(8,200) + FINRES(6,400) + DISC(4,500) = 207,100 LBS",
                    "status": "207,100 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "7. 램프연료 합계",
                    "detail": "TAXI (1,400 LBS) + TAKEOFF FUEL = BLOCK 218,500 LBS 탑재 확인",
                    "status": "218,500 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "8. 도착 잔여 vs 교체+최종예비",
                    "detail": "도착 예상 잔여 연료(24,800 LBS) > 법정 최저치(14,600 LBS) 여유 10,200 LBS 확보",
                    "status": "여유 +10,200 LBS",
                    "statusType": "OK"
                },
                {
                    "category": "9. 교체공항 연료 일치",
                    "detail": "KSAN 회항 계획(109 NM, 28분 소요, 8,200 LBS) 수치 일치",
                    "status": "8,200 LBS (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "10. CFP 항로 vs ATS FPL",
                    "detail": "비행계획서(CFP) 전 구간 42개 웨이포인트 및 FPL 전문 100% 일치",
                    "status": "100% MATCH",
                    "statusType": "OK"
                },
                {
                    "category": "11. RVSM 고도계 점검 요건",
                    "detail": "RVSM 공역 진입 전 주/예비 고도계 지침(허용 오차 75FT) 정상 반영",
                    "status": "VERIFIED (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "12. EDTO / ETOPS 법정 요건",
                    "detail": "EDTO 180분 적용, ERA(RJCC, PANC, KSFO, KSAN) 전 공항 기상 최저치 상회",
                    "status": "EDTO 180 VALID",
                    "statusType": "OK"
                },
                {
                    "category": "13. CPDLC / ADS-C 데이터링크",
                    "detail": "북태평양 관제(PAZA/KZAK) FANS-1/A CPDLC 및 ADS-C 활성화 확인",
                    "status": "ACTIVE (OK)",
                    "statusType": "OK"
                },
                {
                    "category": "14. RAIM / GPS 무결성 예측",
                    "detail": "출발~도착 전 구간 GPS 위성 수신 무결성(FDE) 이상 없음",
                    "status": "AVAILABLE (OK)",
                    "statusType": "OK"
                }
            ]
        },
        "weather_briefing": {
            "departure": {
                "icao": "RKSI",
                "name": "인천국제공항 (Incheon Intl)",
                "etd": "05:30Z (14:30 L)",
                "runway": "RWY 15L/15R",
                "wind": "200° / 10 KT",
                "visibility": "10 KM+ (CAVOK)",
                "ceiling": "SKC / NSC",
                "temp_qnh": "24°C / 1012 hPa",
                "assessment": [
                    "출발지 기상 양호, 마른 활주로(Dry) 이륙 최저치 만족하여 정시 출발 가능.",
                    "이륙 직후 400ft AGL 이하 조기 선회 금지 지침 준수."
                ],
                "raw_metar": "METAR RKSI 100500Z 20010KT CAVOK 24/19 Q1012 NOSIG=",
                "raw_taf": "TAF RKSI 100500Z 1006/1112 20010KT CAVOK="
            },
            "destination": {
                "icao": "KLAX",
                "name": "로스앤젤레스 국제공항 (Los Angeles Intl)",
                "eta": "16:12Z (09:12 L)",
                "runway": "RWY 24L/24R, 25L/25R",
                "wind": "250° / 08 KT",
                "visibility": "10 SM (시정 우수)",
                "ceiling": "FEW015 SCT200",
                "temp_altimeter": "19°C / A2994",
                "assessment": [
                    "도착 시간대 해안가 옅은 하층운(Marine Layer) 소산 중, 시정 10SM 이상으로 양호.",
                    "ILS 24R / 25L 표준 정밀 접근 가능, 마른 활주로 상태로 안전 착륙 보장."
                ],
                "raw_metar": "METAR KLAX 100553Z 25008KT 10SM FEW015 SCT200 19/14 A2994 RMK AO2=",
                "raw_taf": "TAF KLAX 100530Z 1006/1112 25008KT P6SM FEW015 FM101600 24012KT P6SM SKC="
            },
            "alternate": {
                "icao": "KSAN",
                "name": "샌디에이고 국제공항 (San Diego Intl)",
                "eta": "17:02Z (10:02 L)",
                "raw_metar": "METAR KSAN 100551Z 27008KT 10SM CLR 21/15 A2993=",
                "raw_taf": "TAF KSAN 100525Z 1006/1112 27008KT P6SM SKC=",
                "suitability": "EXCELLENT",
                "assessment": "KSAN 기상 맑음, 시정 10SM, 법정 교체공항 최저치 완벽 충족."
            },
            "turbulence_timeline": [
                {
                    "time": "T+00:40",
                    "level": "Light Turb",
                    "segment": "[LANAT ~ AGASI / FL350]",
                    "detail": "동해안 상승 및 순항 진입 기류 요동",
                    "action": "정상 순항"
                },
                {
                    "time": "T+03:50",
                    "level": "Moderate Turb",
                    "segment": "[51N180E ~ 49N160W]",
                    "detail": "북태평양 제트기류(110KT) 진입에 따른 요동",
                    "action": "승객 벨트 사인 사전 점등"
                },
                {
                    "time": "T+09:20",
                    "level": "Light",
                    "segment": "[CINCA ~ PIRAT]",
                    "detail": "캘리포니아 해안 강하 전 약한 난류",
                    "action": "착륙 준비 통보"
                }
            ],
            "sigmets": [
                {
                    "fir": "[PAZA / KZAK FIR]",
                    "text": "SIGMET FOR MODERATE CAT FL340-FL390 OVER PACIFIC CORRIDOR."
                }
            ]
        },
        "fuel_and_weights": {
            "block_fuel": "218,500 LBS",
            "trip_fuel": "182,400 LBS",
            "contingency_fuel": "5,600 LBS",
            "alternate_fuel": "8,200 LBS",
            "final_reserve": "6,400 LBS",
            "extra_fuel": "4,500 LBS",
            "extra_fuel_reason": "KLAX 아침 입항 정체 및 홀딩 대비 디스패치 권고 연료",
            "estimated_tow": "568,200 LBS",
            "max_tow": "617,200 LBS",
            "tow_margin": "여유 49,000 LBS",
            "estimated_law": "385,800 LBS",
            "max_law": "451,900 LBS",
            "payload": {
                "pax_first": "0 / 0",
                "pax_business": "28 / 28 (FULL)",
                "pax_economy": "283 / 283 (FULL)",
                "pax_total_weight": "70,287 LBS (311명)",
                "cargo_weight": "24,800 LBS"
            },
            "fuel_stats": [
                { "label": "MEAN DIFFERENCE (ACTUAL - PLAN)", "val": "+650 LBS", "note": "평균 오차" }
            ]
        },
        "company_rules_and_mel": {
            "company_advisories": [
                {
                    "id": "COMPANY ADVISORY 01",
                    "title": "RKSI 표준 계기 출항(SID) 및 소음 저감 지침 준수",
                    "detail": "400FT AGL 이하 조기 선회 금지 및 초기 상승 프로파일 준수",
                    "impact": "CRITICAL"
                },
                {
                    "id": "COMPANY ADVISORY 02",
                    "title": "KLAX 야간 및 아침 소음 저감(Over-Ocean) 절차 주의",
                    "detail": "서측 해안가 접근 및 입항 소음 절차 숙지",
                    "impact": "CAUTION"
                }
            ],
            "mel_cdl_items": [
                {
                    "code": "MEL 25-20-01A",
                    "item": "PAX SEAT 24A RECLINE INOP",
                    "action": "DEFERRED IAW MEL 25-20-01A (좌석 고정 완료, 운항 성능 영향 없음)",
                    "status": "CONFIRMED"
                }
            ]
        },
        "flight_release_report": {
            "flight_no": "AAR202 / 10AUG26",
            "dispatcher": "SEONGHYUNG_LEE (TEL: 02-6101-5503 / ocws@flyasiana.com)",
            "release_statement": "I HEREBY RELEASE THE FLIGHT AAR0202/10AUG, ICN/LAX, HL8382, ETD 0530Z AS PLAN # 1042 UNDER THE CONDITIONS SPECIFIED.",
            "rvsm_status": "RECORDED (OK)"
        },
        "edto_etops": {
            "etp_items": [
                {
                    "sector": "ETP 1 : RJCC (신치토세) - PANC (앵커리지)",
                    "pos": "N49°12.0 E165°30.0",
                    "dist1": "1,450 NM to RJCC (03h 10m, Fuel 54,200 LBS)",
                    "dist2": "1,380 NM to PANC (03h 02m, Fuel 52,100 LBS)",
                    "wind": "RJCC M012 / PANC M004"
                },
                {
                    "sector": "ETP 2 : PANC (앵커리지) - KSFO (샌프란시스코)",
                    "pos": "N46°30.0 W152°20.0",
                    "dist1": "1,520 NM to PANC (03h 18m, Fuel 56,000 LBS)",
                    "dist2": "1,410 NM to KSFO (03h 05m, Fuel 53,400 LBS)",
                    "wind": "PANC M005 / KSFO P012"
                }
            ],
            "designated_eras": "RKSI, RJCC, PANC, KSFO, KLAX, KSAN"
        },
        "ats_icao_fpl": {
            "raw_fpl": """(FPL-AAR202-IS
-A359/H-SDE1E2E3FGHIJ2J3J4J5M1P2RWXYZ/LB1D1
-RKSI0530
-N0488F350 NOPIK Y644 LANAT G597 AGASI ORENO R211 NIPPI OTR21 EMRON DCT
 48N160E 50N170E 51N180E/N0490F370 51N170W 49N160W/N0488F390 46N150W
 43N140W DCT CINCA DCT PIRAT PAINT2
-KLAX1042 KSAN
-PBN/A1B1C1D1L1O1S2 DAT/1FANSP CPDLCX SUR/RSP180 260B CANMANDATE
 DOF/260810 REG/HL8382
 EET/RJJJ0038 PAZA0415 KZAK0730 KZLA0948
 SEL/CJHM CODE/71BC32 PER/C RALT/RJCC PANC KSFO KSAN RMK/TCAS II EQUIPPED
-E/1340 P/TBN R/VE S/M J/L D/8 311 C SILVERGRAY A/WHITE)"""
        },
        "flight_crew_briefing": {
            "key_focus": "태평양 PACOTS 항로 ETOPS 모니터링 및 KLAX 입항 해풍/시정 확인",
            "briefing_topics": [
                "출발 시 RKSI 400ft AGL 이하 조기 선회 금지 지침 준수",
                "북태평양 제트기류(CAT) 예상 구간 사전 벨트 사인 점등",
                "KLAX 접근 시 소음 절차 및 교체공항(KSAN) 연료 확인"
            ],
            "crew_coordination": [
                "단계별 연료 소모율 및 ETP 분기점 잔여 연료 교차 점검",
                "KLAX 입항 전 관제사 터미널 배정 및 유도로 지시 철저 복창"
            ],
            "checklist_action_items": [
                "출발 전 METAR/TAF 및 NOTAM 최종 업데이트 확인",
                "탑재 연료량(218,500 LBS)과 OFP 일치 서명 확인",
                "MEL 25-20-01A 적용 내역 확인"
            ]
        },
        "joint_briefing": {
            "key_focus": "운항관리사 및 객실승무원 합동 브리핑 (AAR202 ICN-LAX)",
            "flight_profile_summary": "총 비행시간 10시간 42분, 탑승객 311명 만석. 태평양 중반 약 4시간 경과 지점 터뷸런스 예상.",
            "safety_priorities": [
                "태평양 진입 전 객실 안전 점검 완료",
                "승객 착석 후 벨트 착용 상태 상시 육안 확인"
            ],
            "cabin_crew_coordination": [
                "이륙 후 1차 기내식 서비스는 01:30경 시작",
                "난류 예상 15분 전 기장실에서 객실 사전 통보"
            ],
            "joint_checklist": [
                { "item": "비행 계획 및 기상 브리핑 공유", "status": "COMPLETED" },
                { "item": "비상 장구 및 구명정 상태 확인", "status": "COMPLETED" },
                { "item": "특이 승객 및 의료 장비 탑재 확인", "status": "COMPLETED" }
            ]
        },
        "notam_briefing": {
            "general_summary": {
                "departure_hazards": "RKSI (인천): 활주로 15R/33L 스위핑 완료(마른 노면/제동 양호), 유도로 R23/R24 대형기 주기장 진입 제한. 이륙 직후 400FT AGL 이하 조기 선회 엄격 금지(FOM 6.4.4 준수), 유사 호출부호(OZ601/KE601 등) 관제 교신 복창 철저.",
                "arrival_hazards": "KLAX (로스앤젤레스): 유도로 E 일부(E6~E7) 공사로 폐쇄 -> TWY C/D 우회 주행 요망, 활주로 24L PAPI 일시 점검. 활주로 25R 진입등(ALS) 점검 중이나 CAT II/III 정상 접근 가능, 25L ILS 점검 비행 시간대(0400-0800Z) LOC 준비, 톰 브래들리 터미널 크레인(185FT MSL) 주의. 심야/조기 해안 소음 절차(00:00-06:30L) 준수.",
                "enroute_hazards": "PAZA/KZAK FIR & KZLA: 북태평양 PACOTS 트랙 14 FL340~FL390 고고도 제트기류 난류(CAT) 주의보, PAINT2 입항 시 10,000FT 이하 250KT 속도 제한 준수. 대양 통과 시 CPDLC/ADS-C 데이터링크 로그온 의무, 대양 비상강하 절차(ICAO Doc 7030) 준수, 스텝클라임 요청 시 20분 전 사전 통보."
            },
            "enroute_detailed_analysis": [
                {
                    "title": "3.1 오클랜드/태평양 PACOTS 트랙 진입 및 비행 의무 규칙 (NOTAM KZAK A1402/26)",
                    "fir": "오클랜드 대양(KZAK) FIR 및 북태평양 공역 (PACOTS Track 14)",
                    "raw_text": "A1402/26 NOTAMN\nQ) KZAK/QARXX/IV/NBO/E/340/390/3500N16000W999\nA) KZAK B) 2608290000 C) 2608292359\nE) PACOTS TRACK 14 EASTBOUND ROUTE: BETO 3500N16000W 3600N15000W 3600N14000W PAINT. REQ SPEED M084. LVL FL340 FL360 FL380. STEP CLIMB MUST BE FILED IN FPL AND CTC ATC 20MIN PRIOR.",
                    "conditions": "동향(Eastbound) 비행편: 트랙 진입 시 지정 고도(FL350/FL370) 및 마하 0.84 유지, 지정 트랙 게이트(BETO) 정시 통과 및 양도 통신 준수.",
                    "correlation": "우리 비행(AAR202)과의 연관성: 당사 비행계획은 BETO 지점에서 PACOTS Track 14로 진입하여 M0.84 / FL350 순항 후 스텝클라임(FL370)하도록 정확히 수립 및 준수하고 있습니다."
                },
                {
                    "title": "3.2 앵커리지/오클랜드 FIR 대양 CPDLC / ADS-C 의무 비행 규칙 (NOTAM PAZA A0914/26)",
                    "fir": "앵커리지(PAZA) & 오클랜드(KZAK) 대양 FIR 경계선",
                    "raw_text": "A0914/26 NOTAMN\nQ) PAZA/QCSXX/IV/B/E/000/999/5500N16000W999\nA) PAZA KZAK B) 2608290000 C) 2608292359\nE) OCEANIC DATA LINK MANDATORY. ALL ACFT ENTERING PAZA/KZAK OCEANIC AIRSPACE SHALL LOGON CPDLC/ADS-C VIA ADDR PAZA/KZAK 15 TO 25 MIN PRIOR TO BOUNDARY. IN CASE OF COMM FAILURE APPLY ICAO DOC 7030 REGIONAL SUPP PROCEDURES.",
                    "conditions": "대양 공역 진입 15~25분 전 CPDLC 데이터링크(PAZA/KZAK) 자동 로그온 의무. 통신 두절 시 ICAO Doc 7030 대양 비상 강하 및 15NM 우측 오프셋(SLOP) 절차 준수.",
                    "correlation": "우리 비행과의 연관성: 당사 항로는 RJJJ 통과 후 PAZA/KZAK 진입 시 데이터링크 자동 전송 및 비상 통신/백업 HF 주파수 사전 확인을 완료하여 안전하게 규정을 준수합니다."
                },
                {
                    "title": "3.3 LAX 도착 공역(KZLA FIR) 표준 입항 속도/고도 제약 (NOTAM KZLA A0842/26)",
                    "fir": "로스앤젤레스 관제센터(KZLA FIR) 및 PAINT2 STAR 구간",
                    "raw_text": "A0842/26 NOTAMN\nQ) KZLA/QAPXX/IV/BO/E/000/240/3400N11824W050\nA) KZLA B) 2608290000 C) 2608292359\nE) STANDARD ARRIVAL PROCEDURE RESTRICTION: ACFT INBOUND KLAX VIA PAINT2 STAR SHALL MAINTAIN MAX SPEED 250KT AT OR BELOW 10000FT. CROSS FIM AT OR ABOVE 8000FT UNLESS OTHERWISE INSTRUCTED BY ATC.",
                    "conditions": "PAINT2 표준 계기 도착(STAR) 진입 시 10,000FT 이하 250KT 속도 제한 엄수, FIM VORTAC 인근 8,000FT 이상 유지.",
                    "correlation": "우리 비행과의 연관성: FMS 도착 절차에 PAINT2 250KT/10000FT 속도 제약이 정상 입력 수립되어 규정에 부합합니다."
                },
                {
                    "title": "3.4 일본/후쿠오카 FIR 해상 군사 훈련 및 임시 위험 구역 (NOTAM RJJJ A0124/26)",
                    "fir": "후쿠오카(RJJJ) FIR 동남측 해상 (280000N1450000E ~ 310000N1480000E)",
                    "raw_text": "A0124/26 NOTAMN\nQ) RJJJ/QWMLW/IV/BO/W/000/999/2930N14630E120\nA) RJJJ B) 2608290100 C) 2608290900\nE) TEMPO DANGER AREA ACT DUE TO MIL FIRING EXER WI AREA: 280000N1450000E - 310000N1450000E - 310000N1480000E - 280000N1480000E TO BEGINNING. FMS ROUTE OFFSET MAY BE ISSUED BY ATC.",
                    "conditions": "고도 SFC ~ UNL 임시 통제 위험구역(Warning Area 발효).",
                    "correlation": "우리 비행과의 연관성: 당사 계획 항로는 위험 구역 북측으로 45NM 안전 이격 우회하여 수립되었으며, 진입 단계에서 관제사 오프셋 지시 발생 시 즉시 대응 가능합니다."
                }
            ],
            "notam_list": ALL_KLAX_NOTAMS
        },
        "threat_and_error_management": {
            "top_threats": [
                {
                    "threat": "KLAX 아침 입항 해안 층운(Marine Layer) 및 활주로 시정 저하",
                    "impact": "High",
                    "mitigation": "ILS 정밀 접근 모드 조기 전환 및 결심고도(DA) 준수, KSAN 회항 연료 확보"
                },
                {
                    "threat": "북태평양 PACOTS 항로 FL370 제트기류 전단 난류(CAT)",
                    "impact": "Medium",
                    "mitigation": "예상 구간 진입 15분 전 객실 사전 안내 및 벨트 사인 점등"
                },
                {
                    "threat": "KLAX 서측 터미널 유도로 E 공사에 따른 지상 이동 혼선",
                    "impact": "Medium",
                    "mitigation": "지상 이동 차트(Airport Moving Map) 상시 대조 및 관제 지시 철저 복창"
                }
            ],
            "pilot_action_items": [
                "이륙 전 활주로 15R 마른 노면 이륙 성능 재확인",
                "태평양 ETP 1 & 2 지점 통과 시 실제 소모량 vs 비행계획서 오차 기록",
                "KLAX 착륙 전 최신 ATIS 청취 및 접근 활주로(24R/25L) 버그 세팅"
            ],
            "briefing_points": [
                "객실 승무원과 난류 예상 구간 및 서비스 중단 프로토콜 사전 조율 완료",
                "운항관리사 권고 추가 연료(DISC 4,500 LBS) 탑재 승인 완료"
            ]
        }
    }
