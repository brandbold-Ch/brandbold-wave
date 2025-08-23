"""
Authentication model and status enumeration.
Defines the Auth model for user authentication and the Status enum for account status.
"""
from enum import Enum
from typing import Optional
from bcrypt import hashpw, gensalt
from sqlmodel import Field, Relationship
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import EmailStr
from app.models.base_model import EntityBaseModel


class Status(str, Enum):
    """
    Enumeration for authentication status values.
    """
    ACTIVE = "active"
    INACTIVE = "inactive"


class Auth(EntityBaseModel, table=True):
    """
    Authentication model for user credentials and status.
    Includes fields for username, email, password, status, and relationship to Account.
    """
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
        """
        Initialize the Auth model and hash the password if provided.
        Args:
            **kwargs: Keyword arguments for model fields.
        """
        super().__init__(**kwargs)
        if self.password:
            self.password = self.password_hash(self.password)

    @classmethod
    def password_hash(cls, password: str) -> str:
        """
        Hash a password using bcrypt.
        Args:
            password (str): The plain text password.
        Returns:
            str: The hashed password.
        """
        return hashpw(
            password.encode("utf-8"),
            gensalt(12)
        ).decode("utf-8")

    def hide_fields(self) -> set:
        """
        Return a set of fields to hide when serializing the model.
        Returns:
            set: The set of field names to hide.
        """
        return {"password"}
