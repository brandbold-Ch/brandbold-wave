from app.models import Account
from app.repositories.base_repository import BaseRepository


class AccountRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Account)
