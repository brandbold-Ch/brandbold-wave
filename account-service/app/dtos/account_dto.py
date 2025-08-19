from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, EmailStr
from uuid import UUID


class AccountInfo(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    subscription_plan_id: Optional[UUID] = None
    

class AuthInfo(BaseModel):
    username: Optional[str] = None
    email: EmailStr
    password: str


class DeviceInfo(BaseModel):
    device_brand: str
    device_model: str
    ip_address: str


class CreateAccountDto(BaseModel):
    account_info: AccountInfo
    auth_info: AuthInfo
    device_info: DeviceInfo
    
    
class UpdateAccountDto(AccountInfo):
    ...
    