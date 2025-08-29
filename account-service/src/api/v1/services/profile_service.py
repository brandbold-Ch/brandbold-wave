"""
This module provides the ProfileService class, which implements business logic for managing user profiles.
It includes methods for creating, retrieving, updating, and deleting profiles, as well as handling avatar selection.
"""
from uuid import UUID
from sqlmodel import Session
from src.api.v1.interfaces import AbstractProfileImpl
from src.utils.wrappers import ListWrapper
from src.api.v1.repositories.profile_repository import ProfileRepository
from src.api.v1.models import Profile
from src.api.v1.dtos import ProfileInfoDto
from src.utils.io_tools import auto_select_avatar
from src.decorators import exception_handler


class ProfileService(AbstractProfileImpl):
    """
    Service class for managing user profiles. Implements business logic for profile operations
    such as creation, retrieval, update, and deletion, using a ProfileRepository.
    """

    def __init__(
        self,
        repository: ProfileRepository = ProfileRepository()
    ) -> None:
        """
        Initialize the ProfileService with a ProfileRepository instance.

        Args:
            repository (ProfileRepository): The repository to use for profile data access.
        """
        self.repository = repository

    def condition(
        self,
        account_id: UUID,
        profile_id: UUID
    ) -> bool:
        """
        Build a SQLModel condition for filtering by account and profile ID.

        Args:
            account_id (UUID): The account's unique identifier.
            profile_id (UUID): The profile's unique identifier.

        Returns:
            bool: SQLModel filter condition.
        """
        return ((Profile.account_id == account_id) &
                (Profile.id == profile_id))

    @exception_handler
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
            data (ProfileInfoDto): Profile data transfer object.
            session (Session): SQLModel session for database operations.
            auto_commit (bool, optional): Whether to commit after creation. Defaults to True.

        Returns:
            Profile: The created Profile instance.
        """
        profile_data = data.model_dump(exclude={"avatar_file"})
        profile_data["account_id"] = account_id

        if data.avatar_file is None:
            profile_data["avatar_url"] = auto_select_avatar()

        return self.repository.create(
            Profile(**profile_data), session, auto_commit
        )

    @exception_handler
    def get_profiles(
        self,
        account_id: UUID,
        session: Session
    ) -> ListWrapper:
        """
        Retrieve all profiles associated with a given account.

        Args:
            account_id (UUID): The account's unique identifier.
            session (Session): SQLModel session for database operations.

        Returns:
            ListWrapper: A wrapper containing the list of Profile instances.
        """
        return self.repository.get_many(
            Profile.account_id == account_id, session
        )

    @exception_handler
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
            session (Session): SQLModel session for database operations.

        Returns:
            Profile: The requested Profile instance.
        """
        condition = self.condition(account_id, profile_id)
        return self.repository.get_one(condition, session)

    @exception_handler
    def delete_profile(
        self,
        account_id: UUID,
        profile_id: UUID,
        session: Session,
        auto_commit: bool = True
    ) -> Profile:
        """
        Delete a profile by account and profile ID.

        Args:
            account_id (UUID): The account's unique identifier.
            profile_id (UUID): The profile's unique identifier.
            session (Session): SQLModel session for database operations.
            auto_commit (bool, optional): Whether to commit after deletion. Defaults to True.

        Returns:
            Profile: The deleted Profile instance.
        """
        condition = self.condition(account_id, profile_id)
        return self.repository.delete_one(
            condition, session, auto_commit
        )

    @exception_handler
    def update_profile(
        self,
        account_id: UUID,
        profile_id: UUID,
        data: ProfileInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Profile:
        """
        Update a profile's information by account and profile ID.

        Args:
            account_id (UUID): The account's unique identifier.
            profile_id (UUID): The profile's unique identifier.
            data (ProfileInfoDto): Profile data transfer object with updated fields.
            session (Session): SQLModel session for database operations.
            auto_commit (bool, optional): Whether to commit after update. Defaults to True.

        Returns:
            Profile: The updated Profile instance.
        """
        profile_data = data.model_dump()
        condition = self.condition(account_id, profile_id)
        return self.repository.update_one(
            condition, profile_data, session, auto_commit
        )
