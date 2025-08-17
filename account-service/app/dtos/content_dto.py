from typing import Optional 
from pydantic import BaseModel, Field
from datetime import date


class CreateContentDto(BaseModel):
    title: str
    description: str
    release_date: date
    duration: str
    thumbnail_file: str = Field(alias="thumbnailFile")
    content_file: str = Field(alias="contentFile")
    trailer_file: str = Field(alias="trailerFile")
    genres: Optional[list] = []
    franchises: Optional[list] = []
    
    def flat_info(self) -> dict:
        return self.model_dump(exclude={"genres", "franchises"})
        