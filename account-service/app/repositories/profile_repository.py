from app.models import Profile
from app.repositories.base_repository import BaseRepository


class ProfileRepository(BaseRepository):
    """
    Repository class for Profile model.
    Inherits generic CRUD operations from BaseRepository.
    """

    def __init__(self):
        """
        Initialize the ProfileRepository with the Profile model.
        """
        super().__init__(Profile)
