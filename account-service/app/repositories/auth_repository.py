from app.models import Auth
from app.repositories.base_repository import BaseRepository


class AuthRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Auth)
