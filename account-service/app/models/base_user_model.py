from datetime import datetime, date
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import Field
from app.models.base_model import EntityBaseModel


class BaseUser(EntityBaseModel):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True, index=True)
    first_name: str
    last_name: str
    birth_date: date
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    last_login: Optional[datetime] = None
