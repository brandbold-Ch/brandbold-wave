from typing import Optional
from sqlmodel import Field
from app.models.base_model import EntityBaseModel
from sqlalchemy import Column, SMALLINT
from datetime import datetime
from uuid import UUID, uuid4


class Profile(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    account_id: UUID = Field(foreign_key="account.id", nullable=False, ondelete="CASCADE")
    nickname: str
    avatar_url: Optional[str] = None
    maturity_rating: int = Field(sa_column=Column(SMALLINT, nullable=True, default=0))
    autoplay_next_episode: bool = False
    skip_intro: bool = False
    skip_credits: bool = False
    language_code: Optional[int] = 0
    last_activity_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    is_admin: bool = True
    