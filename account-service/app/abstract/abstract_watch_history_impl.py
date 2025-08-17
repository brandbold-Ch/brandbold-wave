from uuid import UUID
from sqlmodel import Session
from abc import ABC, abstractmethod
from app.models import WatchHistory
from app.utils.wrappers import ListWrapper


class AbstractWatchHistoryImpl(ABC):

    @abstractmethod
    def create_watch_history(
            self,
            user_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> WatchHistory:
        pass

    @abstractmethod
    def update_watch_history(
            self,
            user_id: UUID,
            watch_id,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> WatchHistory:
        pass

    @abstractmethod
    def get_watch_histories(
            self,
            user_id: UUID,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_watch_history(
            self,
            user_id: UUID,
            watch_id: UUID,
            session: Session
    ) -> WatchHistory:
        pass

    @abstractmethod
    def delete_watch_history(
            self,
            user_id: UUID,
            watch_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> WatchHistory:
        pass
