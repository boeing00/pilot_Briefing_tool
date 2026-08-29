import { NextRequest, NextResponse } from 'next/server';
import { askFlightAssistant } from '@/lib/gemini';
import { FlightBriefingData } from '@/types/flight';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { briefingContext, question, history, apiKey } = body as {
      briefingContext: FlightBriefingData;
      question: string;
      history?: Array<{ role: 'user' | 'model'; text: string }>;
      apiKey?: string;
    };

    if (!briefingContext || !question) {
      return NextResponse.json(
        { success: false, error: '비행 브리핑 데이터와 질문 내용이 필요합니다.' },
        { status: 400 }
      );
    }

    const answer = await askFlightAssistant(briefingContext, question, history || [], apiKey);

    return NextResponse.json({ success: true, answer });
  } catch (error: any) {
    console.error('Chat Assistant Error:', error);
    return NextResponse.json(
      { success: false, error: error.message || '답변 생성 중 오류가 발생했습니다.' },
      { status: 500 }
    );
  }
}
