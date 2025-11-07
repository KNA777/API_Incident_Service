from src.schemas.incidents import IncidentRequestAdd, IncidentUpdateStatus
from src.services.base import BaseService
from src.utils import IncidentStatus


class IncidentService(BaseService):

    async def create_incident(self, data, status, source):
        new_data = IncidentRequestAdd(**data.model_dump(), status=status, source=source)
        return await self.db.incident.create(data=new_data)

    async def get_incidents_by_status(self, status):
        return await self.db.incident.get_filtered(status=status)

    async def update_incident_status(self, data: IncidentUpdateStatus, incident_id):
        updated_incident = await self.db.incident.edit(data, id=incident_id)
        return updated_incident
