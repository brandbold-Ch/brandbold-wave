from app.models import Profile
from app.repositories.base_repository import BaseRepository


class ProfileRepository(BaseRepository):

    def __init__(self):
        super().__init__(Profile)
