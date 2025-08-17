from app.models import Auth
from app.repositories.base_repository import BaseRepository


class AuthRepository(BaseRepository):

    def __init__(self):
        super().__init__(Auth)
