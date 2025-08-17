from datetime import datetime, date
from uuid import uuid4, UUID
from sqlmodel import Field, Relationship
from typing import Optional
from app.models.content_genre_model import ContentGenre
from app.models.content_franchise_model import ContentFranchise
from app.models.base_model import EntityBaseModel
from app.utils.builders import build_spring_url


class Content(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True, index=True)
    title: str
    description: str
    release_date: date
    duration: str
    thumbnail_file: str = Field(alias="thumbnailFile")
    content_file: str = Field(alias="contentFile")
    trailer_file: Optional[str] = Field(alias="trailerFile")
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: Optional[datetime] = None

    episode_number: Optional[int] = None
    season_id: Optional[UUID] = Field(default=None, foreign_key="season.id")

    genres: list["Genre"] = Relationship(
        back_populates="content",
        link_model=ContentGenre
    )
    franchises: list["Franchise"] = Relationship(
        back_populates="content",
        link_model=ContentFranchise
    )
    watch_history: "WatchHistory" = Relationship(
        sa_relationship_kwargs={
            "passive_deletes": True
        }
    )

    def fromkeys(self, **kwargs) -> None:
        self.updated_at = datetime.now()
        super().fromkeys(**kwargs)

    def as_json(self, deep: bool = True) -> dict:
        data = super().as_json(deep)
        data["franchises"] = [franchise.as_json() for franchise in self.franchises]
        data["genres"] = [genre.as_json() for genre in self.genres]
        data["thumbnail_url"] = build_spring_url("thumbnails", self.thumbnail_file)
        data["content_url"] = build_spring_url("streaming", self.content_file, "?source=movie")
        data["trailer_url"] = build_spring_url("streaming", self.trailer_file, "?source=trailer")
        return data

    class Config:
        allow_population_by_alias = True
