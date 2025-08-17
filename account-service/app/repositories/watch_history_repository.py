from app.models import WatchHistory
from app.repositories.base_repository import BaseRepository


class WatchHistoryRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(WatchHistory)
        