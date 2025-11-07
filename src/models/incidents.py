from datetime import datetime
from enum import StrEnum

from sqlalchemy import String, Enum, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.db_conf.config import BaseOrm


class IncidentORM(BaseOrm):
    __tablename__ = "incident"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(255))
    status: Mapped[str] = mapped_column(String(20), default="todo", nullable=False)
    source: Mapped[str] = mapped_column(String(20), default="operator", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False
    )
