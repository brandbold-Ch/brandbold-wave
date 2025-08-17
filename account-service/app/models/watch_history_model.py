from datetime import datetime
from uuid import uuid4, UUID
from sqlalchemy import Column, DOUBLE_PRECISION
from sqlmodel import Field
from typing import Optional
from app.models.base_model import EntityBaseModel


class WatchHistory(EntityBaseModel, table=True):
    __tablename__ = "watch_history"

    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    user_id: UUID = Field(foreign_key="user.id", nullable=False)
    content_id: UUID = Field(foreign_key="content.id", nullable=False, ondelete="CASCADE")
    watched_at: datetime = Field(default_factory=lambda: datetime.now())
    last_position: Optional[float] = Field(sa_column=Column(DOUBLE_PRECISION), default=None)
