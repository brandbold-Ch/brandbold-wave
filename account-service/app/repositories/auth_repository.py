from app.models import Auth
from app.repositories.base_repository import BaseRepository



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
