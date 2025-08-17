from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import Content
from app.utils.wrappers import ListWrapper


class AbstractContentImpl(ABC):

    @abstractmethod
    def create_content(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> dict:
        pass

    @abstractmethod
    def get_contents(
            self,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_content(
            self,
            content_id: UUID,
            session: Session
    ) -> Content:
        pass

    @abstractmethod
    def delete_content(
            self,
            content_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Content:
        pass

    @abstractmethod
    def update_content(
            self,
            content_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Content:
        pass
