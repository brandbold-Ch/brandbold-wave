from enum import Enum
from typing import Optional
from bcrypt import hashpw, gensalt
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import EmailStr
from app.models.base_model import EntityBaseModel


class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Auth(EntityBaseModel, table=True):
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True, index=True)
    account_id: UUID = Field(foreign_key="account.id", nullable=False, ondelete="CASCADE")
    username: Optional[str] = Field(unique=True, index=True, default=None)
    email: EmailStr = Field(unique=True, index=True)
    password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    status: Status = Status.ACTIVE
    
    _account: "Account" = Relationship(
        back_populates="_auth", 
        sa_relationship_kwargs={'uselist': False}
    )

    def __init__(self, **kwargs) -> None:
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
