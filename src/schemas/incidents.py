from datetime import datetime

from pydantic import BaseModel

from src.utils import IncidentStatus


class IncidentRequest(BaseModel):
    description: str


class IncidentResponse(IncidentRequest):
    id: int
    description: str
    status: str
    source: str
    created_at: datetime


class IncidentRequestAdd(BaseModel):
    description: str
    status: str
    source: str


class IncidentUpdateStatus(BaseModel):
    status: IncidentStatus
