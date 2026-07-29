from pathlib import Path
import shutil
from app.ai.summarizer import AISummarizer
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.services.timeline_service import TimelineService
from app.database.database import get_db
from app.services.log_service import LogService
from app.services.threat_detector import ThreatDetector
from app.parser.log_parser import LogParser
from app.mitre.mapper import MitreMapper
from app.ai.llm_service import LLMService
import json
from app.schemas.upload_response import UploadResponse
router = APIRouter(
    prefix="/api/v1/logs",
    tags=["Logs"]
)

UPLOAD_FOLDER = Path("uploads")


@router.get("/")
def health():
    return {
        "message": "Logs API is working"
    }


@router.post(
    "/upload",
    response_model=UploadResponse
)
def upload_log(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Create uploads folder if it doesn't exist
    UPLOAD_FOLDER.mkdir(exist_ok=True)

    # File destination
    file_path = UPLOAD_FOLDER / file.filename

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get file size
    file_size = file_path.stat().st_size

    # Save metadata to database
    log = LogService.create_log(
        db=db,
        filename=file.filename,
        filepath=str(file_path),
        file_size=file_size,
    )

    # Parse uploaded log
    parsed_events = LogParser.parse_log(str(file_path))

    # Add MITRE ATT&CK mapping
    for event in parsed_events:
        mitre = MitreMapper.map_event(
            event["event_type"]
        )
        event["mitre"] = mitre

    # Detect threats
    threats = ThreatDetector.detect_threats(parsed_events)
    timeline = TimelineService.build(parsed_events)
    # Generate AI summary
    ai_summary = AISummarizer.summarize(
        parsed_events,
        threats
    )
    llm = LLMService()

    incident_data = json.dumps(
    {
        "parsed_events": parsed_events,
        "timeline": timeline,
        "threats": threats
    },
    indent=2,
    default=str
)

    ai_report = llm.analyze_incident(incident_data)
    # Return response
    return {
        "log": {
            "id": log.id,
            "filename": log.filename,
            "filepath": log.filepath,
            "file_size": log.file_size,
            "status": log.status,
            "uploaded_at": log.uploaded_at,
        },
        "parsed_events": parsed_events,
        "timeline": timeline,
        "threats": threats,
        "ai_summary": ai_summary,
        "ai_report": ai_report
    }