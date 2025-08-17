from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, EmailStr


class UserInfo(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    

class AuthInfo(BaseModel):
    username: Optional[str] = None
    email: EmailStr
    password: str


class DeviceInfo(BaseModel):
    device_brand: str
    device_model: str
    ip_address: str


class CreateUserDto(BaseModel):
    user_info: UserInfo
    auth_info: AuthInfo
    device_info: DeviceInfo
    
    
class UpdateUserDto(UserInfo):
    last_login: Optional[datetime] = None
    last_used_at: Optional[datetime] = None
