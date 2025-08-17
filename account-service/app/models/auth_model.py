from enum import Enum
from typing import Optional
from bcrypt import hashpw, gensalt
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import EmailStr
from app.models.base_model import EntityBaseModel


class Roles(str, Enum):
    USER = "user"
    ADMIN = "admin"


class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Auth(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True, index=True)
    user_id: UUID = Field(foreign_key="user.id", nullable=False, ondelete="CASCADE")
    username: Optional[str] = Field(unique=True, index=True, default=None)
    email: EmailStr = Field(unique=True, index=True)
    password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    role: Roles = Roles.USER
    status: Status = Status.ACTIVE
    user: "User" = Relationship(back_populates="auth", sa_relationship_kwargs={'uselist': False})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.password:
            self.password = self.password_hash(self.password)

    @classmethod
    def password_hash(cls, password: str) -> str:
        return hashpw(
            password.encode("utf-8"),
            gensalt(12)
        ).decode("utf-8")

    def hide_fields(self) -> set:
        return {"password"}
