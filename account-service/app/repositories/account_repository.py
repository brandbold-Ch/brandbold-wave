from app.models import Account
from app.repositories.base_repository import BaseRepository



class AccountRepository(BaseRepository):
    """
    Repository class for Account model.
    Inherits generic CRUD operations from BaseRepository.
    """

    def __init__(self) -> None:
        """
        Initialize the AccountRepository with the Account model.
        """
        super().__init__(Account)
