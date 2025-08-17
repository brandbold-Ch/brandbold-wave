from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractContentGenreImpl
from app.models import ContentGenre
from app.repositories.content_genre_repository import ContentGenreRepository
from app.utils.wrappers import ListWrapper


class ContentGenreService(AbstractContentGenreImpl):

    def __init__(
            self,
            service: ContentGenreRepository = ContentGenreRepository()
    ) -> None:
        self.service = service

    def create_genre(
            self,
            genre_id: UUID,
            content_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> ContentGenre:
        genre = ContentGenre(
            genre_id=genre_id,
            content_id=content_id
        )
        self.service.create(genre, session, auto_commit)
        return genre

    def get_genres(
            self,
            session: Session = None
    ) -> ListWrapper:
        pass

    def get_genre(
            self,
            genre_id: UUID,
            content_id: UUID,
            session: Session = None
    ) -> ContentGenre:
        condition = ((ContentGenre.id == genre_id) &
                     (ContentGenre.content_id == content_id))
        result = self.service.get_one(condition, session)
        return result

    def delete_genre(
            self,
            genre_id: UUID,
            content_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> ContentGenre:
        pass

    def update_genre(
            self,
            genre_id: UUID,
            content_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> ContentGenre:
        pass
