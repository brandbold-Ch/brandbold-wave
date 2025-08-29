"""
Service class for account operations.
Implements business logic for creating, retrieving, updating, and deleting accounts.
"""
from uuid import UUID
from sqlmodel import Session
from src.api.v1.interfaces import AbstractAccountImpl
from src.api.v1.models import Account
from src.api.v1.repositories.account_repository import AccountRepository
from src.utils.wrappers import ListWrapper
from src.api.v1.dtos import AccountInfoDto
from src.decorators import exception_handler


class AccountService(AbstractAccountImpl):
    """
    Service class for account-related operations.
    Provides methods to create, retrieve, update, and delete accounts using the repository pattern.
    """

    def __init__(
        self,
        user_repository: AccountRepository = AccountRepository()
    ) -> None:
        """
        Initialize the AccountService with a repository instance.
        Args:
            user_repository (AccountRepository, optional): The repository to use. Defaults to AccountRepository().
        """
        self.repository = user_repository
    
    @exception_handler
    def create_account(
        self,
        data: AccountInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Account:
        """
        Create a new account.
        Args:
            data (AccountInfoDto): The account information DTO.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after creation. Defaults to True.
        Returns:
            Account: The created account instance.
        """
        account_data = data.model_dump()
        return self.repository.create(
            Account(**account_data), session, auto_commit
        )

    @exception_handler
    def get_accounts(
        self,
        session: Session = None
    ) -> ListWrapper:
        """
        Retrieve all accounts.
        Args:
            session (Session, optional): The database session.
        Returns:
            ListWrapper: A wrapper containing all account instances.
        """
        return self.repository.select(session)

    @exception_handler
    def get_account(
        self,
        account_id: UUID,
        session: Session = None
    ) -> Account:
        """
        Retrieve a specific account by its ID.
        Args:
            account_id (UUID): The account's unique identifier.
            session (Session, optional): The database session.
        Returns:
            Account: The requested account instance.
        """
        return self.repository.get(account_id, session)

    @exception_handler
    def delete_account(
        self,
        account_id: UUID,
        session: Session,
        auto_commit: bool = True
    ) -> Account:
        """
        Delete an account by its ID.
        Args:
            account_id (UUID): The account's unique identifier.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after deletion. Defaults to True.
        Returns:
            Account: The deleted account instance.
        """
        return self.repository.delete(
            account_id, session, auto_commit
        )

    @exception_handler
    def update_account(
        self,
        account_id: UUID,
        data: AccountInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Account:
        """
        Update an account by its ID.
        Args:
            account_id (UUID): The account's unique identifier.
            data (AccountInfoDto): The updated account information DTO.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after update. Defaults to True.
        Returns:
            Account: The updated account instance.
        """
        account_data = data.model_dump()
        return self.repository.update(
            account_id, account_data, session, auto_commit
        )
