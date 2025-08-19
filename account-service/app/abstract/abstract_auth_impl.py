from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import Auth
from app.utils.wrappers import ListWrapper
from app.dtos import AuthInfo


class AbstractAuthImpl(ABC):

    @abstractmethod
    def create_auth(
            self,
            account_id: UUID,
            data: AuthInfo,
            session: Session,
            auto_commit: bool = True
    ) -> Auth:
        pass

    @abstractmethod
    def get_auths(
            self,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_auth(
            self,
            username: str,
            password: str,
            session: Session
    ) -> Auth:
        pass

    @abstractmethod
    def delete_auth(
            self,
            auth_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Auth:
        pass

    @abstractmethod
    def update_auth(
            self,
            auth_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Auth:
        pass
