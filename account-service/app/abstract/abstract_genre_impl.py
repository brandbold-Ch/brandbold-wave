from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import Genre
from app.utils.wrappers import ListWrapper


class AbstractGenreImpl(ABC):

    @abstractmethod
    def create_genre(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Genre:
        pass

    @abstractmethod
    def get_genres(
            self,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_genre(
            self,
            genre_id: UUID,
            session: Session
    ) -> Genre:
        pass

    @abstractmethod
    def delete_genre(
            self,
            genre_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Genre:
        pass

    @abstractmethod
    def update_genre(
            self,
            genre_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Genre:
        pass
