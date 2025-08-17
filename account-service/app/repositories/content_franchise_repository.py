from app.models import ContentFranchise
from app.repositories.base_repository import BaseRepository


class ContentFranchiseRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(ContentFranchise)
