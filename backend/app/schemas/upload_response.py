from datetime import datetime
from typing import List, Optional
from app.schemas.ai_report import AIReport
from pydantic import BaseModel


class LogResponse(BaseModel):
    id: int
    filename: str
    filepath: str
    file_size: int
    status: str
    uploaded_at: datetime


class ParsedEventResponse(BaseModel):
    raw_log: str
    event_type: str
    severity: str
    ip_address: Optional[str] = None
    mitre: Optional[dict] = None


class TimelineResponse(BaseModel):
    step: int
    event: str
    severity: str
    ip: Optional[str] = None


class ThreatResponse(BaseModel):
    type: str
    severity: str
    ip: str
    attempts: int


class AISummaryResponse(BaseModel):
    summary: str
    severity: str
    recommendations: List[str]


class UploadResponse(BaseModel):
    log: LogResponse
    parsed_events: List[ParsedEventResponse]
    timeline: List[TimelineResponse]
    threats: List[ThreatResponse]
    ai_summary: AISummaryResponse
    ai_report: AIReport