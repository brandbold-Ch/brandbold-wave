from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractContentImpl
from app.models import Content
from app.repositories.content_repostitory import ContentRepository
from app.utils.wrappers import ListWrapper


class ContentService(AbstractContentImpl):

    def __init__(
            self,
            repository: ContentRepository = ContentRepository()
    ) -> None:
        self.repository = repository

    def create_content(
            self,
            data: dict,
            session: Session = None,
            auto_commit: bool = True
    ) -> Content:
        content = Content(**data)
        self.repository.create(content, session, auto_commit)
        return content

    def update_content(
            self,
            content_id: UUID,
            data: dict,
            session: Session = None,
            auto_commit: bool = True
    ) -> Content:
        result = self.repository.update(
            content_id,
            data,
            session,
            auto_commit
        )
        return result

    def get_contents(
            self,
            session: Session = None
    ) -> ListWrapper:
        result = self.repository.select(session)
        return result

    def delete_content(
            self,
            content_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> Content:
        result = self.repository.delete(
            content_id,
            session,
            auto_commit
        )
        return result

    def get_content(
            self,
            content_id: UUID,
            session: Session = None
    ) -> Content:
        result = self.repository.get(content_id, session)
        return result
