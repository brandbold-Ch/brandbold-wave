from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class ProfileInfo(BaseModel):
    nickname: str
    avatar_file: Optional[str] = None
    