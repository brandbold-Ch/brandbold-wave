from app.models import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(User)
