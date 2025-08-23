from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import Profile
from app.utils.wrappers import ListWrapper
from app.dtos import ProfileInfoDto



class AbstractProfileImpl(ABC):
    """
    Abstract base class for profile-related operations.
    Defines the interface for creating, retrieving, updating, and deleting profiles.
    """

    @abstractmethod
    def create_profile(
        self,
        account_id: UUID,
        data: ProfileInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Profile:
        """
        Create a new profile for a given account.
        Args:
            account_id (UUID): The account's unique identifier.
            data (ProfileInfo): The profile information to create.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after creation. Defaults to True.
        Returns:
            Profile: The created profile instance.
        """

    @abstractmethod
    def get_profiles(
        self,
        account_id: UUID,
        session: Session
    ) -> ListWrapper:
        """
        Retrieve all profiles associated with a given account.
        Args:
            account_id (UUID): The account's unique identifier.
            session (Session): The database session.
        Returns:
            ListWrapper: A wrapper containing all profile instances for the account.
        """

    @abstractmethod
    def get_profile(
        self,
        account_id: UUID,
        profile_id: UUID,
        session: Session
    ) -> Profile:
        """
        Retrieve a specific profile by account and profile ID.
        Args:
            account_id (UUID): The account's unique identifier.
            profile_id (UUID): The profile's unique identifier.
            session (Session): The database session.
        Returns:
            Profile: The requested profile instance.
        """

    @abstractmethod
    def delete_profile(
        self,
        account_id: UUID,
        profile_id: UUID,
        session: Session,
        auto_commit: bool = True
    ) -> Profile:
        """
        Delete a specific profile by account and profile ID.
        Args:
            account_id (UUID): The account's unique identifier.
            profile_id (UUID): The profile's unique identifier.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after deletion. Defaults to True.
        Returns:
            Profile: The deleted profile instance.
        """

    @abstractmethod
    def update_profile(
        self,
        account_id: UUID,
        profile_id: UUID,
        data: ProfileInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Profile:
        """
        Update a specific profile by account and profile ID.
        Args:
            account_id (UUID): The account's unique identifier.
            profile_id (UUID): The profile's unique identifier.
            data (ProfileInfo): The updated profile information.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after update. Defaults to True.
        Returns:
            Profile: The updated profile instance.
        """
