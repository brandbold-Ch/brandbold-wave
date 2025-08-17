from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractGenreImpl
from app.models import Genre, Genres
from app.repositories.genre_repository import GenreRepository
from app.utils.wrappers import ListWrapper


class GenreService(AbstractGenreImpl):

    def __init__(
            self,
            repository: GenreRepository = GenreRepository()
    ) -> None:
        self.repository = repository

    def condition(self, genre_name) -> bool:
        return Genre.genre_name == Genres(genre_name.title())

    def create_genre(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Genre:
        genre = Genre(**data)
        self.repository.create(
            genre,
            session,
            auto_commit
        )
        return genre

    def update_genre(
            self,
            genre_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Genre:
        result = self.repository.update(
            genre_id,
            data,
            session,
            auto_commit
        )
        return result

    def get_genre(
            self,
            genre_id: UUID,
            session: Session
    ) -> Genre:
        result = self.repository.get(genre_id, session)
        return result

    def get_genres(
            self,
            session: Session
    ) -> ListWrapper:
        result = self.repository.select(session)
        return result

    def delete_genre(
            self,
            genre_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Genre:
        result = self.repository.delete(
            genre_id,
            session,
            auto_commit
        )
        return result

    def get_content_by_genre(
            self,
            genre_name: str,
            session: Session
    ) -> Genre:
        condition = self.condition(genre_name)
        result = self.repository.get_one(condition, session)
        return result

    def get_contents_by_genre(
            self,
            genre_name: str,
            session: Session
    ) -> Genre:
        condition = self.condition(genre_name)
        result = self.repository.get_many(condition, session)
        return result
