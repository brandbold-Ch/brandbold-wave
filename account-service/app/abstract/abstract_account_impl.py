from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import Account
from app.utils.wrappers import ListWrapper
from app.dtos import AccountInfo


class AbstractAccountImpl(ABC):

    @abstractmethod
    def create_account(
            self,
            data: AccountInfo,
            session: Session,
            auto_commit: bool = True
    ) -> Account:
        pass

    @abstractmethod
    def get_accounts(
            self,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_account(
            self,
            account_id: UUID,
            session: Session
    ) -> Account:
        pass

    @abstractmethod
    def delete_account(
            self,
            account_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Account:
        pass

    @abstractmethod
    def update_account(
            self,
            account_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Account:
        pass
