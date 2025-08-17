from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import ContentGenre
from app.utils.wrappers import ListWrapper


class AbstractContentGenreImpl(ABC):

    @abstractmethod
    def create_genre(
            self,
            genre_id: UUID,
            content_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContentGenre:
        pass

    @abstractmethod
    def get_genres(
            self,
            session: Session,
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_genre(
            self,
            genre_id: UUID,
            content_id: UUID,
            session: Session
    ) -> ContentGenre:
        pass

    @abstractmethod
    def delete_genre(
            self,
            genre_id: UUID,
            content_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContentGenre:
        pass

    @abstractmethod
    def update_genre(
            self,
            genre_id: UUID,
            content_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContentGenre:
        pass
