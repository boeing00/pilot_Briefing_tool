import os
import logging
from typing import Dict, Any, Optional
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from services.pdf_parser import extract_text_from_pdf_bytes
from services.gemini_briefing import generate_flight_briefing, chat_with_flight_docs, get_mock_briefing_data
from services.sample_data import get_aar202_klax_sample_briefing

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("pilot-briefing-api")

app = FastAPI(
    title="Pilot Briefing AI API",
    description="Aviation Flight Document (OFP/METAR/NOTAM) PDF Ingestion & Pilot Briefing Engine",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str
    briefing_context: Dict[str, Any]
    raw_text: Optional[str] = ""
    api_key: Optional[str] = None

@app.get("/api/health")
async def health_check():
    has_api_key = bool(os.environ.get("GEMINI_API_KEY"))
    return {
        "status": "online",
        "service": "Pilot Briefing API",
        "gemini_configured": has_api_key
    }

@app.get("/api/briefing/sample")
async def get_sample_briefing(flight: Optional[str] = "KJFK"):
    """
    Returns a sample structured flight briefing for development and preview.
    Supports ?flight=KLAX (AAR202) and ?flight=KJFK (AAR224).
    """
    if flight and flight.upper() in ["KLAX", "LAX", "AAR202", "OZ202"]:
        sample_data = get_aar202_klax_sample_briefing()
        filename = "AAR202_RKSI_KLAX_A350_RELEASE_PACKAGE.pdf"
    else:
        sample_data = get_mock_briefing_data()
        filename = "AAR224_RKSI_KJFK_A380_RELEASE_PACKAGE.pdf"

    return {
        "success": True,
        "briefing": sample_data,
        "document_meta": {
            "page_count": 88 if "KLAX" in filename else 95,
            "filename": filename,
            "is_sample": True
        }
    }

@app.post("/api/briefing/upload")
async def upload_flight_pdf(
    file: UploadFile = File(...),
    api_key: Optional[str] = Form(None)
):
    """
    Accepts an uploaded PDF (Flight Plan, NOTAMs, Weather Pack) and returns a structured pilot briefing.
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
        
    try:
        pdf_bytes = await file.read()
        if len(pdf_bytes) == 0:
            raise HTTPException(status_code=400, detail="Uploaded file is empty.")
            
        parsed_doc = extract_text_from_pdf_bytes(pdf_bytes)
        
        briefing_data = generate_flight_briefing(
            pdf_text=parsed_doc["full_text"],
            api_key=api_key,
            filename=file.filename
        )
        
        return {
            "success": True,
            "briefing": briefing_data,
            "document_meta": {
                "filename": file.filename,
                "page_count": parsed_doc["page_count"],
                "raw_snippet": parsed_doc["full_text"][:2000],
                "raw_text": parsed_doc["full_text"],
                "is_sample": False
            }
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing PDF: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to process flight document: {str(e)}")

@app.post("/api/briefing/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Pilot cockpit Q&A endpoint over the uploaded flight documents.
    """
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")
        
    answer = chat_with_flight_docs(
        question=request.question,
        briefing_context=request.briefing_context,
        raw_text=request.raw_text or "",
        api_key=request.api_key
    )
    
    return {
        "success": True,
        "question": request.question,
        "answer": answer
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
