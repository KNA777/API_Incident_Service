from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.exceptions import ObjectNotFoundException, ObjectNotFoundHTTPException
from src.schemas.incidents import IncidentRequest, IncidentUpdateStatus, IncidentResponse
from src.services.incident import IncidentService
from src.utils import IncidentStatus, Source

router = APIRouter(prefix="/incident", tags=["Incidents"])


@router.post("")
async def create_incident(db: DBDep,
                          data: IncidentRequest,
                          status: IncidentStatus,
                          source: Source,
                          ) -> IncidentResponse:
    return await IncidentService(db).create_incident(
        data=data, status=status, source=source)


@router.get("/{status}")
async def get_incidents_by_status_filter(
        db: DBDep,
        status: IncidentStatus) -> list:
    return await IncidentService(db).get_incidents_by_status(
        status=status)


@router.patch("/{incident_id}")
async def update_incident_status_by_id(
        db: DBDep,
        data: IncidentUpdateStatus,
        incident_id: int) -> IncidentResponse:
    try:
        return await IncidentService(db).update_incident_status(data, incident_id)
    except ObjectNotFoundException:
        raise ObjectNotFoundHTTPException
