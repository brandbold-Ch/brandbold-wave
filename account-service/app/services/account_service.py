from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractAccountImpl
from app.models import Account
from app.repositories.account_repository import AccountRepository
from app.utils.wrappers import ListWrapper
from app.dtos import AccountInfo


class AccountService(AbstractAccountImpl):

    def __init__(
            self,
            user_repository: AccountRepository = AccountRepository()
    ) -> None:
        self.repository = user_repository

    def create_account(
            self,
            data: AccountInfo,
            session: Session,
            auto_commit: bool = True
    ) -> Account:
        account_data = data.model_dump()
        
        return self.repository.create(
            Account(**account_data), session, auto_commit
        )

    def get_accounts(
            self,
            session: Session = None
    ) -> ListWrapper:
        return self.repository.select(session)

    def get_account(
            self,
            account_id: UUID,
            session: Session = None
    ) -> Account:
        result = self.repository.get(account_id, session)
        return result

    def delete_account(
            self,
            account_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Account:
        result = self.repository.delete(
            account_id, session, auto_commit
        )
        return result

    def update_account(
            self,
            account_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Account:
        result = self.repository.update(
            account_id,
            data,
            session,
            auto_commit
        )
        return result
