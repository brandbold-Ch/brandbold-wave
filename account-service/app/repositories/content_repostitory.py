from app.models import Content
from app.repositories.base_repository import BaseRepository


class ContentRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Content)
