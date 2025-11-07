from typing import Annotated
from fastapi import Depends, Query

from src.db_conf.config import async_session
from src.db_conf.db_context_manager import DBManager


async def get_db():
    async with DBManager(session_factory=async_session) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]
