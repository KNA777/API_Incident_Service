from src.models.incidents import IncidentORM
from src.repository.base import BaseRepository
from src.repository.mapper.incident import IncidentMapper


class IncidentRepository(BaseRepository):

    model = IncidentORM
    mapper = IncidentMapper