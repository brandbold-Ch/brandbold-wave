from typing import Optional
from uuid import UUID
from datetime import date
from pydantic import BaseModel, EmailStr


class AccountInfoDto(BaseModel):
    """
    Data Transfer Object for account information.
    Contains personal details for an account.
    """
    first_name: str
    last_name: str
    birth_date: date
    subscription_plan_id: Optional[UUID] = None  


class AuthInfoDto(BaseModel):
    """
    Data Transfer Object for authentication information.
    Contains credentials for account authentication.
    """
    username: Optional[str] = None
    email: EmailStr
    password: str


class DeviceInfoDto(BaseModel):
    """
    Data Transfer Object for device information.
    Contains details about the user's device.
    """
    device_brand: str
    device_model: str
    ip_address: str


class CreateAccountDto(BaseModel):
    """
    Data Transfer Object for creating a new account.
    Includes account, authentication, and device information.
    """
    account_info: AccountInfoDto
    auth_info: AuthInfoDto
    device_info: DeviceInfoDto
    