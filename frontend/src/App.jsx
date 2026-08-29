import React, { useState, useEffect, useRef } from 'react';
import { MessageSquare, AlertTriangle, Sparkles } from 'lucide-react';
import { useBriefing } from './hooks/useBriefing';

import Navbar from './components/Navbar';
import PdfUploader from './components/PdfUploader';
import EfbSidebar from './components/EfbSidebar';
import PilotChatModal from './components/PilotChatModal';
import ApiKeyModal from './components/ApiKeyModal';

// Dedicated EFB Page Components
import FlightCrewBriefPage from './pages/FlightCrewBriefPage';
import JointBriefPage from './pages/JointBriefPage';
import CheckPage from './pages/CheckPage';
import RoutePage from './pages/RoutePage';
import FuelPage from './pages/FuelPage';
import WxPage from './pages/WxPage';
import NotamPage from './pages/NotamPage';
import RulesPage from './pages/RulesPage';
import ReportPage from './pages/ReportPage';
import EdtoPage from './pages/EdtoPage';
import FplPage from './pages/FplPage';
import RawPage from './pages/RawPage';

export default function App() {
  const {
    briefing,
    docMeta,
    loading,
    error,
    apiKey,
    setApiKey,
    hasApiKey,
    handleFileUpload,
  } = useBriefing();

  const [activeTab, setActiveTab] = useState('flight_crew');
  const errorRef = useRef(null);

  // Bring a failure into view. The alert renders at the top of the page and the
  // pilot may well have scrolled away during a two-minute analysis.
  useEffect(() => {
    if (error) errorRef.current?.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }, [error]);

  const [isChatOpen, setIsChatOpen] = useState(false);
  const [isApiKeyOpen, setIsApiKeyOpen] = useState(false);

  const renderActivePage = () => {
    if (!briefing) return null;

    switch (activeTab) {
      case 'flight_crew':
        return <FlightCrewBriefPage briefing={briefing} onNavigate={(tab) => setActiveTab(tab)} />;
      case 'joint_brief':
        return <JointBriefPage briefing={briefing} />;
      case 'check':
        return <CheckPage briefing={briefing} />;
      case 'route':
        return <RoutePage briefing={briefing} />;
      case 'fuel':
        return <FuelPage briefing={briefing} />;
      case 'wx':
        return <WxPage briefing={briefing} />;
      case 'notam':
      case 'wnotam':
        return <NotamPage briefing={briefing} isSample={docMeta?.is_sample !== false} />;
      case 'rules':
        return <RulesPage briefing={briefing} />;
      case 'report':
        return <ReportPage briefing={briefing} />;
      case 'edto':
        return <EdtoPage briefing={briefing} />;
      case 'fpl':
        return <FplPage briefing={briefing} />;
      case 'raw':
        return <RawPage docMeta={docMeta} />;
      default:
        return <FlightCrewBriefPage briefing={briefing} onNavigate={(tab) => setActiveTab(tab)} />;
    }
  };

  return (
    <div className="min-h-screen text-slate-100 flex flex-col selection:bg-amber-600 selection:text-white">
      {/* Top Header Navbar */}
      <Navbar
        hasApiKey={hasApiKey}
        onOpenApiKey={() => setIsApiKeyOpen(true)}
      />

      {/* Main EFB Layout with Left Sidebar */}
      <div className="flex-1 flex relative pl-16">
        {/* Left EFB Bookmark Sidebar */}
        <EfbSidebar
          activeTab={activeTab}
          onSelectTab={setActiveTab}
          onOpenAiChat={() => setIsChatOpen(true)}
        />

        {/* Main Center Content View */}
        <main className="flex-1 max-w-[1400px] w-full mx-auto p-4 sm:p-7 pb-28 sm:pb-28 space-y-7">
          {/* Error Alert */}
          {error && (
            <div ref={errorRef} className="bg-rose-950/80 border border-rose-800 text-rose-200 px-4 py-3 rounded-xl flex items-start gap-3 text-sm shadow-lg">
              <AlertTriangle className="w-5 h-5 text-rose-400 shrink-0" />
              <span>{error}</span>
            </div>
          )}

          {/* API Key Warning Alert */}
          {briefing?._api_warning && (
            <div className="bg-amber-950/80 border border-amber-600 text-amber-200 px-4 py-3 rounded-xl flex items-center justify-between gap-3 text-sm shadow-lg">
              <div className="flex items-center gap-3">
                <AlertTriangle className="w-5 h-5 text-amber-400 shrink-0" />
                <span>
                  입력된 Gemini API Key가 유효하지 않아 <strong>로컬 PDF 파서 모드</strong>로 문서를 분석했습니다. 정밀 AI 분석을 원하시면 우측 상단에서 올바른 API 키를 다시 입력해 주세요.
                </span>
              </div>
              <button
                onClick={() => setIsApiKeyOpen(true)}
                className="px-3 py-1 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs rounded-lg shrink-0 transition"
              >
                API Key 재입력
              </button>
            </div>
          )}

          {/* Upload Zone */}
          <section>
            <PdfUploader
              onFileUpload={handleFileUpload}
              loading={loading}
              docMeta={docMeta}
            />
          </section>

          {/* Global AI Processing Overlay */}
          {loading && (
            <div className="fixed inset-0 z-50 bg-slate-950/85 backdrop-blur-md flex flex-col items-center justify-center p-6 text-center space-y-5 font-mono animate-fade-in">
              <div className="w-16 h-16 border-4 border-amber-400 border-t-transparent rounded-full animate-spin shadow-[0_0_25px_rgba(245,158,11,0.4)]"></div>
              <div className="space-y-2">
                <h3 className="text-xl sm:text-2xl font-bold text-white uppercase tracking-wider">
                  GEMINI 2.5 FLASH AI 비행 문서 분석 중...
                </h3>
                <p className="text-sm text-amber-300 font-bold">
                  OFP 비행계획서, WX 기상 예보, NOTAM 전문 데이터를 실시간 파싱 및 브리핑 생성 중입니다.
                </p>
                <p className="text-xs text-slate-400">
                  (문서 분량에 따라 1~3분 걸릴 수 있습니다. 완료 시 대시보드가 자동으로 갱신됩니다.)
                </p>
              </div>
            </div>
          )}

          {/* Active EFB Page Content */}
          {loading && !briefing ? (
            <div className="bg-slate-900/40 border border-slate-800 rounded-2xl p-12 text-center flex flex-col items-center justify-center gap-3">
              <div className="w-8 h-8 border-2 border-amber-400 border-t-transparent rounded-full animate-spin"></div>
              <p className="text-sm font-semibold text-slate-300">운항 브리핑 데이터를 불러오고 있습니다...</p>
            </div>
          ) : briefing ? (
            <div className="pb-12">
              {renderActivePage()}
            </div>
          ) : (
            <div className="bg-slate-900/50 border border-slate-800/80 rounded-2xl p-8 sm:p-12 text-center max-w-2xl mx-auto my-8 space-y-4">
              <div className="w-16 h-16 bg-amber-600/10 text-slate-300 border border-amber-500/20 rounded-2xl flex items-center justify-center mx-auto">
                <Sparkles className="w-8 h-8" />
              </div>
              <h2 className="text-xl font-bold text-slate-100">
                운항 비행계획서(OFP) 및 기상/NOTAM PDF를 업로드하세요
              </h2>
              <p className="text-xs text-slate-400 leading-relaxed">
                조종사에게 필요한 출발지/목적지 기상, 항로상 난류, 활주로 폐쇄 노탐, 필요 연료 및 대체공항, 3대 안전 위협 요소를 AI가 즉시 추출하여 대시보드로 제공합니다.
              </p>
            </div>
          )}
        </main>
      </div>

      {/* Floating Cockpit Q&A Chat Button */}
      {briefing && (
        <button
          onClick={() => setIsChatOpen(true)}
          className="fixed bottom-6 right-6 z-30 flex items-center gap-2.5 px-4 py-3 bg-gradient-to-r from-amber-600 to-amber-600 hover:from-amber-500 hover:to-amber-500 text-white rounded-full shadow-lg transition-all transform hover:scale-105 active:scale-95 text-xs font-bold"
        >
          <MessageSquare className="w-4 h-4" />
          <span>조종사 AI 질의응답 (Q&A)</span>
        </button>
      )}

      {/* Modals */}
      <PilotChatModal
        isOpen={isChatOpen}
        onClose={() => setIsChatOpen(false)}
        briefing={briefing}
        apiKey={apiKey}
        onOpenApiKey={() => setIsApiKeyOpen(true)}
      />

      <ApiKeyModal
        isOpen={isApiKeyOpen}
        onClose={() => setIsApiKeyOpen(false)}
        apiKey={apiKey}
        onSaveKey={setApiKey}
      />
    </div>
  );
}
