from typing import Optional
from uuid import UUID
from sqlmodel import SQLModel, Field


class ContentGenre(SQLModel, table=True):
    __tablename__ = "content_genre"

    content_id: Optional[UUID] = Field(foreign_key="content.id", primary_key=True, index=True, ondelete="CASCADE")
    genre_id: Optional[UUID] = Field(foreign_key="genre.id", primary_key=True, index=True, ondelete="CASCADE")
