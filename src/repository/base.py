from src.exceptions import ObjectNotFoundException
from src.repository.mapper.base import BaseMapper
from pydantic import BaseModel
from sqlalchemy import insert, update, select
from sqlalchemy.exc import NoResultFound

class BaseRepository:
    model = None
    mapper: BaseMapper = None

    def __init__(self, session):
        self.session = session

    async def get_filtered(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        data = await self.session.execute(query)
        return [self.mapper.map_to_domain_entity(model) for model in data.scalars().all()]

    async def create(self, data: BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return self.mapper.map_to_domain_entity(result.scalars().one())

    async def edit(self, data: BaseModel, **filter_by):
        stmt = (update(self.model)
                .filter_by(**filter_by)
                .values(**data.model_dump())).returning(self.model)
        result = await self.session.execute(stmt)
        try:
            data = result.scalars().one()
        except NoResultFound:
            raise ObjectNotFoundException
        await self.session.commit()

        return self.mapper.map_to_domain_entity(data)
