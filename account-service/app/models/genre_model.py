from enum import Enum
from uuid import UUID, uuid4
from sqlmodel import Field, Relationship
from app.models.content_genre_model import ContentGenre
from app.models.base_model import EntityBaseModel


class Genres(str, Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    ANIMATION = "Animation"
    BIOGRAPHY = "Biography"
    COMEDY = "Comedy"
    CRIME = "Crime"
    DOCUMENTARY = "Documentary"
    DRAMA = "Drama"
    FAMILY = "Family"
    FANTASY = "Fantasy"
    HISTORY = "History"
    HORROR = "Horror"
    MUSIC = "Music"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    SCI_FI = "Science Fiction"
    SPORT = "Sport"
    THRILLER = "Thriller"
    WAR = "War"
    WESTERN = "Western"


class Genre(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    genre_name: Genres
    content: list["Content"] = Relationship(
        back_populates="genres",
        link_model=ContentGenre
    )
