from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractWatchHistoryImpl
from app.models import WatchHistory
from app.repositories.watch_history_repository import WatchHistoryRepository
from app.utils.wrappers import ListWrapper


class WatchHistoryService(AbstractWatchHistoryImpl):

    def __init__(
            self,
            repository: WatchHistoryRepository = WatchHistoryRepository()
    ) -> None:
        self.repository = repository

    def user_and_content_cond(
            self,
            user_id: UUID,
            content_id: UUID
    ) -> bool:
        return ((WatchHistory.user_id == user_id) &
                (WatchHistory.content_id == content_id))

    def user_and_watch_cond(
            self,
            user_id: UUID,
            watch_id: UUID
    ) -> bool:
        return ((WatchHistory.user_id == user_id) &
                (WatchHistory.id == watch_id))

    def create_watch_history(
            self,
            user_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> WatchHistory:
        watch_history = WatchHistory(**data, user_id=user_id)
        condition = self.user_and_content_cond(
            user_id,
            watch_history.content_id
        )
        result = self.repository.get_one(condition, session)

        if result:
            return result

        self.repository.create(
            watch_history,
            session,
            auto_commit
        )
        return watch_history

    def update_watch_history(
            self,
            user_id: UUID,
            watch_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> WatchHistory:
        condition = self.user_and_watch_cond(user_id, watch_id)
        result = self.repository.update_one(
            condition,
            data,
            session,
            auto_commit
        )
        return result

    def get_watch_histories(
            self,
            user_id: UUID,
            session: Session
    ) -> ListWrapper:
        result = self.repository.get_many(
            WatchHistory.user_id == user_id,
            session
        )
        return result

    def get_watch_history(
            self,
            user_id: UUID,
            watch_id: UUID,
            session: Session
    ) -> WatchHistory:
        condition = self.user_and_watch_cond(user_id, watch_id)
        result = self.repository.get_one(condition, session)
        return result

    def delete_watch_history(
            self,
            user_id: UUID,
            watch_id,
            session: Session,
            auto_commit: bool = True
    ) -> WatchHistory:
        condition = self.user_and_watch_cond(user_id, watch_id)
        result = self.repository.delete_one(
            condition,
            session,
            auto_commit
        )
        return result
