from datetime import time
from uuid import uuid4, UUID
from sqlmodel import Field
from app.models.base_model import EntityBaseModel


class Season(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    serie_id: UUID = Field(foreign_key="serie.id", nullable=False)
    number_of_season: int
    release_date: time
