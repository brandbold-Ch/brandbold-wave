from datetime import time
from uuid import uuid4, UUID
from sqlmodel import Field
from app.models.base_model import EntityBaseModel


class Serie(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    name: str
    description: str
    thumbnail_url: str
    trailer_url: str
    release_date: time
    