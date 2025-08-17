from app.models import Genre
from app.repositories.base_repository import BaseRepository


class GenreRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Genre)
