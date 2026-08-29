import { NextRequest, NextResponse } from 'next/server';
import { analyzeFlightDocument } from '@/lib/gemini';

export const maxDuration = 60; // Allow sufficient time for large PDF analysis

export async function POST(request: NextRequest) {
  try {
    const contentType = request.headers.get('content-type') || '';

    let fileBase64 = '';
    let mimeType = 'application/pdf';
    let fileName = 'flight_document.pdf';
    let customApiKey: string | undefined;

    if (contentType.includes('multipart/form-data')) {
      const formData = await request.formData();
      const file = formData.get('file') as File | null;
      customApiKey = (formData.get('apiKey') as string) || undefined;

      if (!file) {
        return NextResponse.json({ success: false, error: 'PDF 파일이 업로드되지 않았습니다.' }, { status: 400 });
      }

      fileName = file.name;
      mimeType = file.type || 'application/pdf';
      const arrayBuffer = await file.arrayBuffer();
      const buffer = Buffer.from(arrayBuffer);
      fileBase64 = buffer.toString('base64');
    } else if (contentType.includes('application/json')) {
      const body = await request.json();
      fileBase64 = body.fileBase64;
      mimeType = body.mimeType || 'application/pdf';
      fileName = body.fileName || 'flight_document.pdf';
      customApiKey = body.apiKey;

      if (!fileBase64) {
        return NextResponse.json({ success: false, error: '파일 데이터(fileBase64)가 필요합니다.' }, { status: 400 });
      }
    } else {
      return NextResponse.json({ success: false, error: '지원되지 않는 Content-Type입니다.' }, { status: 400 });
    }

    const briefingData = await analyzeFlightDocument(fileBase64, mimeType, fileName, customApiKey);

    return NextResponse.json({ success: true, data: briefingData });
  } catch (error: any) {
    console.error('Flight Analysis Error:', error);
    return NextResponse.json(
      {
        success: false,
        error: error.message || '문서 분석 중 오류가 발생했습니다. 파일 형식이나 API 키를 확인해 주세요.',
      },
      { status: 500 }
    );
  }
}
