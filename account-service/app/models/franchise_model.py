from uuid import UUID, uuid4
from sqlmodel import Field, Relationship
from app.models.content_franchise_model import ContentFranchise
from app.models.base_model import EntityBaseModel


class Franchise(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    name: str
    description: str
    content: list["Content"] = Relationship(
        back_populates="franchises",
        link_model=ContentFranchise
    )
