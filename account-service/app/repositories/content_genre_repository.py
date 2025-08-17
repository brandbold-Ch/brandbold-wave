from app.models import ContentGenre
from app.repositories.base_repository import BaseRepository


class ContentGenreRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(ContentGenre)
