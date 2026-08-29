import React, { useState } from 'react';
import { Code2, Search, Copy, Check } from 'lucide-react';

export default function RawDocViewerCard({ rawText }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [copied, setCopied] = useState(false);

  const sampleRawText = rawText || `CFP PLAN 3201
ATTN CAPT. 7626
FLIGHT RELEASE AAR224 RKSI/KJFK ON 10/AUG/26.NONSTOP COMPUTED 0722Z
A/C REG.MK ENGINE SELCAL ROUTE PRF WX PROGS AVG WIND/TEMP UNIT
388 HL7626 TRENT970 GM-KQ F BRK 1000UK P017/M47 100LBS
SPEED SKD CLB-320/.85 CRZ- 65 DSC-.85/290/ APMS/P 03.2 PCNT. IFR
 FUEL TIME DIST NAM PLAN AGTOW 12544
TRIP 4059 13.24 6663 6431 SOW 06587 RWY 12544
RESERVE 0456 01.48
 ALTN/KBOS 0224 00.45 0261 0256 PLD 01170 ACL 01218
 FINAL RES 0110 00.30 T/O Z ZFW 07757 MZFW 08068
 3 PCT CONT 0122 00.33 F/T 13.24 TOF 04739 TOF 04739
RQD TAKEOFF 4515 15.12 HRS UTC-0400 TOW 12496 MTOW 12544
DISC 0224 01.00 ETA L TIF 04059 TCAP 12544
TANKERING 0000 00.00 RSN/ / LDW 08437 MLDW 08620
PLN TAKEOFF 4739 16.12 ACTL PAX TIF 04059
TAXI 0019
RAMP OUT 4758 16.12 ACTL
FOD 0680 02.48 ACTL ETD RKSI 1205Z ETA KJFK 0129Z
2ND-$ 290 4229 13.53
RKSI..EGOBA Y697 KAE Y437 TENAS L512 GTC Y512 OATIS R580 ORCCA..
SQA..GKN..GAHAM..N62W130..N61W120..N59W110..N56W100..N51W090..
N46W080..NOVON..YODAA PUCKY1 KJFK`;

  const handleCopy = () => {
    navigator.clipboard.writeText(sampleRawText);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div id="section-raw" className="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-lg space-y-5">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-4 border-b border-slate-800">
        <div className="flex items-center gap-3.5">
          <div className="p-2.5 bg-slate-800 border border-slate-700 rounded-xl text-amber-300 shadow-sm">
            <Code2 className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-xl sm:text-2xl font-bold text-white uppercase tracking-wide">
              RAW FLIGHT RELEASE & OFP DOCUMENT
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">비행계획서 및 디스패치 원문 텍스트 뷰어</p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <div className="relative">
            <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-2.5" />
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="OFP 원문 검색 (예: FUEL)"
              className="bg-slate-950 border border-slate-700 rounded-lg pl-8 pr-3 py-1.5 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-amber-400 w-full sm:w-48 min-w-0 font-mono"
            />
          </div>
          <button
            onClick={handleCopy}
            className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-950 hover:bg-slate-800 text-slate-200 text-xs font-bold rounded-lg border border-slate-700 transition shrink-0"
          >
            {copied ? <Check className="w-3.5 h-3.5 text-slate-300" /> : <Copy className="w-3.5 h-3.5 text-slate-400" />}
            <span>{copied ? '복사 완료' : '전체 복사'}</span>
          </button>
        </div>
      </div>

      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-300 leading-relaxed max-h-96 overflow-y-auto select-all">
        <pre className="whitespace-pre-wrap">{sampleRawText}</pre>
      </div>
    </div>
  );
}
