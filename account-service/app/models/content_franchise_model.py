from typing import Optional
from uuid import UUID
from sqlmodel import SQLModel, Field


class ContentFranchise(SQLModel, table=True):
    __tablename__ = "content_franchise"

    content_id: Optional[UUID] = Field(foreign_key="content.id", primary_key=True, index=True, ondelete="CASCADE")
    franchise_id: Optional[UUID] = Field(foreign_key="franchise.id", primary_key=True, index=True, ondelete="CASCADE")
