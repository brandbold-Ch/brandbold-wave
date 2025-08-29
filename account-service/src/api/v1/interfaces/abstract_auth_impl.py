from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from src.api.v1.models import Auth
from src.utils.wrappers import ListWrapper
from src.api.v1.dtos import AuthInfoDto


class AbstractAuthImpl(ABC):
    """
    Abstract base class for authentication-related operations.
    Defines the interface for creating, retrieving, updating, and deleting authentication records.
    """

    @abstractmethod
    def create_auth(
        self,
        account_id: UUID,
        data: AuthInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Auth:
        """
        Create a new authentication record for a given account.
        Args:
            account_id (UUID): The account's unique identifier.
            data (AuthInfo): The authentication information to create.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after creation. Defaults to True.
        Returns:
            Auth: The created authentication instance.
        """

    @abstractmethod
    def get_auths(
        self,
        session: Session
    ) -> ListWrapper:
        """
        Retrieve all authentication records.
        Args:
            session (Session): The database session.
        Returns:
            ListWrapper: A wrapper containing all authentication instances.
        """

    @abstractmethod
    def get_auth(
        self,
        username: str,
        password: str,
        session: Session
    ) -> Auth:
        """
        Retrieve an authentication record by username and password.
        Args:
            username (str): The username.
            password (str): The password.
            session (Session): The database session.
        Returns:
            Auth: The requested authentication instance.
        """

    @abstractmethod
    def delete_auth(
        self,
        auth_id: UUID,
        session: Session,
        auto_commit: bool = True
    ) -> Auth:
        """
        Delete a specific authentication record by its ID.
        Args:
            auth_id (UUID): The authentication record's unique identifier.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after deletion. Defaults to True.
        Returns:
            Auth: The deleted authentication instance.
        """

    @abstractmethod
    def update_auth(
        self,
        auth_id: UUID,
        data: dict,
        session: Session,
        auto_commit: bool = True
    ) -> Auth:
        """
        Update a specific authentication record by its ID.
        Args:
            auth_id (UUID): The authentication record's unique identifier.
            data (dict): The updated authentication information.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after update. Defaults to True.
        Returns:
            Auth: The updated authentication instance.
        """
