"""
Device model definition for user devices.
Represents a device associated with a user account, including brand, model, IP, and last usage.
"""
from datetime import datetime
from uuid import uuid4, UUID
from sqlmodel import Field, Column
from typing_extensions import Optional
from sqlalchemy.dialects.postgresql import INET
from app.models.base_model import EntityBaseModel


class Device(EntityBaseModel, table=True):
    """
    Device model representing a user's device in the system.
    Fields:
        id (UUID): Unique identifier for the device.
        account_id (UUID): Foreign key to the associated account.
        device_brand (str): Brand of the device.
        device_model (str): Model of the device.
        ip_address (str): IP address of the device.
        last_used_at (Optional[datetime]): Last time the device was used.
    """
    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    account_id: UUID = Field(foreign_key="account.id", nullable=False, ondelete="CASCADE")
    device_brand: str
    device_model: str
    ip_address: str = Field(sa_column=Column(INET))
    last_used_at: Optional[datetime]
