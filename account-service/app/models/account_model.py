from datetime import datetime, date
from typing import Optional
from uuid import UUID
from sqlmodel import Relationship, Field
from app.models.base_model import EntityBaseModel
from uuid import uuid4


class Account(EntityBaseModel, table=True):
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
        data = super().as_json()
        data["auth_info"] = self._auth.as_json()

        if deep:
            data["devices_info"] = [device.as_json() for device in self._devices ]
            data["profiles_info"] = [profile.as_json() for profile in self._profiles]
        return data
    