from app.models import Franchise
from app.repositories.base_repository import BaseRepository


class FranchiseRepository(BaseRepository):

    def __init__(self):
        super().__init__(Franchise)
