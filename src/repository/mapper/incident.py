from src.models.incidents import IncidentORM
from src.repository.mapper.base import BaseMapper
from src.schemas.incidents import IncidentResponse


class IncidentMapper(BaseMapper):
    schema = IncidentResponse
    db_model = IncidentORM
