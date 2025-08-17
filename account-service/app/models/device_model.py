from datetime import datetime
from uuid import uuid4, UUID
from sqlmodel import Field, Column
from typing_extensions import Optional
from sqlalchemy.dialects.postgresql import INET
from app.models.base_model import EntityBaseModel


class Device(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    user_id: UUID = Field(foreign_key="user.id", nullable=False, ondelete="CASCADE")
    device_brand: str
    device_model: str
    ip_address: str = Field(sa_column=Column(INET))
    last_used_at: Optional[datetime]
