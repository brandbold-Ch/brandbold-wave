from uuid import uuid4
from uuid import UUID
from typing import Optional
from datetime import datetime, date
from sqlmodel import Relationship, Field
from src.api.v1.models.base_model import EntityBaseModel


class Account(EntityBaseModel, table=True):
    """
    Account model representing a user account in the system.
    Includes personal information, relationships to auth, devices, and profiles.
    """
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True, index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    subscription_plan_id: Optional[UUID] = None
    first_name: str
    last_name: str
    birth_date: date
    
    _auth: "Auth" = Relationship(
        back_populates="_account", 
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    _devices: list["Device"] = Relationship(
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    _profiles: list["Profile"] = Relationship(
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )
    
    def as_json(self, deep: bool = True) -> dict:
        """
        Convert the Account instance to a JSON-serializable dictionary.
        Args:
            deep (bool, optional): Whether to include related devices and profiles. Defaults to True.
        Returns:
            dict: The account data as a dictionary.
        """
        data = super().as_json()
        data["auth_info"] = self._auth.as_json()

        if deep:
            data["devices_info"] = [device.as_json() for device in self._devices]
            data["profiles_info"] = [profile.as_json() for profile in self._profiles]
        return data
    