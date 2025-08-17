from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import User
from app.utils.wrappers import ListWrapper


class AbstractUserImpl(ABC):

    @abstractmethod
    def create_user(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> User:
        pass

    @abstractmethod
    def get_users(
            self,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_user(
            self,
            user_id: UUID,
            session: Session
    ) -> User:
        pass

    @abstractmethod
    def delete_user(
            self,
            user_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> User:
        pass

    @abstractmethod
    def update_user(
            self,
            user_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> User:
        pass
