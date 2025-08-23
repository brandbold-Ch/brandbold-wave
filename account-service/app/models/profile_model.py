"""
Profile model definition for user profiles.
Represents a user profile associated with an account, including preferences and metadata.
"""
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import Field
from app.models.base_model import EntityBaseModel
from sqlalchemy import Column, SMALLINT
from app.utils.settings import get_settings


class Profile(EntityBaseModel, table=True):
    """
    Profile model representing a user profile in the system.
    Fields:
        id (UUID): Unique identifier for the profile.
        account_id (UUID): Foreign key to the associated account.
        nickname (str): Profile's display name.
        avatar_url (Optional[str]): URL to the profile's avatar image.
        maturity_rating (int): Maturity rating for content restrictions.
        autoplay_next_episode (bool): Whether to autoplay the next episode.
        skip_intro (bool): Whether to skip intros automatically.
        skip_credits (bool): Whether to skip credits automatically.
        language_code (Optional[int]): Preferred language code.
        last_activity_at (Optional[datetime]): Last activity timestamp.
        created_at (datetime): Profile creation timestamp.
        is_admin (bool): Whether the profile has admin privileges.
    """
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
    is_admin: bool = False
    
    def as_json(self, deep = True):
        data = super().as_json(deep)
        data["avatar_url"] = get_settings().avatars_url + self.avatar_url
        return data
    