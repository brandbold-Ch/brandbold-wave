from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from src.api.v1.models import Account
from src.utils.wrappers import ListWrapper
from src.api.v1.dtos import AccountInfoDto


class AbstractAccountImpl(ABC):
    """
    Abstract base class for account-related operations.
    Defines the interface for creating, retrieving, updating, and deleting accounts.
    """

    @abstractmethod
    def create_account(
        self,
        data: AccountInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Account:
        """
        Create a new account.
        Args:
            data (AccountInfo): The account information to create.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after creation. Defaults to True.
        Returns:
            Account: The created account instance.
        """

    @abstractmethod
    def get_accounts(
        self,
        session: Session
    ) -> ListWrapper:
        """
        Retrieve all accounts.
        Args:
            session (Session): The database session.
        Returns:
            ListWrapper: A wrapper containing all account instances.
        """

    @abstractmethod
    def get_account(
        self,
        account_id: UUID,
        session: Session
    ) -> Account:
        """
        Retrieve a specific account by its ID.
        Args:
            account_id (UUID): The account's unique identifier.
            session (Session): The database session.
        Returns:
            Account: The requested account instance.
        """

    @abstractmethod
    def delete_account(
        self,
        account_id: UUID,
        session: Session,
        auto_commit: bool = True
    ) -> Account:
        """
        Delete a specific account by its ID.
        Args:
            account_id (UUID): The account's unique identifier.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after deletion. Defaults to True.
        Returns:
            Account: The deleted account instance.
        """

    @abstractmethod
    def update_account(
        self,
        account_id: UUID,
        data: AccountInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Account:
        """
        Update a specific account by its ID.
        Args:
            account_id (UUID): The account's unique identifier.
            data (AccountInfo): The updated account information.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after update. Defaults to True.
        Returns:
            Account: The updated account instance.
        """
