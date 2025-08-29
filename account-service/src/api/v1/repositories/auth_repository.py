from src.api.v1.models import Auth
from src.api.v1.repositories.base_repository import BaseRepository



class AuthRepository(BaseRepository):
    """
    Repository class for Auth model.
    Inherits generic CRUD operations from BaseRepository.
    """

    def __init__(self) -> None:
        """
        Initialize the AuthRepository with the Auth model.
        """
        super().__init__(Auth)
