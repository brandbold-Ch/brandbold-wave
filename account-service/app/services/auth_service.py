"""
Service class for authentication operations.
Implements business logic for creating, retrieving, updating, and deleting authentication records.
"""
from re import match
from uuid import UUID
import bcrypt
from sqlmodel import Session
from app.abstract import AbstractAuthImpl
from app.models import Auth
from app.exceptions.exceptions import NotFoundException, PasswordMismatchException
from app.repositories.auth_repository import AuthRepository
from app.utils.wrappers import ListWrapper
from app.dtos import AuthInfoDto
from app.decorators import exception_handler



class AuthService(AbstractAuthImpl):
    """
    Service class for authentication-related operations.
    Provides methods to create, retrieve, update, and delete authentication records using the repository pattern.
    """

    def __init__(
        self,
        repository: AuthRepository = AuthRepository()
    ) -> None:
        """
        Initialize the AuthService with a repository instance.
        Args:
            repository (AuthRepository, optional): The repository to use. Defaults to AuthRepository().
        """
        self.repository = repository

    @exception_handler
    def get_auth_by_id(
        self,
        auth_id: UUID,
        session: Session
    ) -> Auth:
        """
        Retrieve an authentication record by its ID.
        Args:
            auth_id (UUID): The authentication record's unique identifier.
            session (Session): The database session.
        Returns:
            Auth: The requested authentication instance.
        Raises:
            NotFoundException: If the authentication record is not found.
        """
        result = self.repository.get_one(
            Auth.id == auth_id,
            session
        )
        if not result:
            raise NotFoundException("Auth ID not found")
        return result

    @exception_handler
    def get_auth_by_username(
        self,
        username: str,
        session: Session
    ) -> Auth:
        """
        Retrieve an authentication record by username.
        Args:
            username (str): The username.
            session (Session): The database session.
        Returns:
            Auth: The requested authentication instance.
        Raises:
            NotFoundException: If the authentication record is not found.
        """
        result = self.repository.get_one(
            Auth.username == username,
            session
        )
        if not result:
            raise NotFoundException("Username not found")
        return result
    
    @exception_handler
    def get_auth_by_email(
        self,
        email: str,
        session: Session
    ) -> Auth:
        """
        Retrieve an authentication record by email.
        Args:
            email (str): The email address.
            session (Session): The database session.
        Returns:
            Auth: The requested authentication instance.
        Raises:
            NotFoundException: If the authentication record is not found.
        """
        result = self.repository.get_one(
            Auth.email == email,
            session
        )
        if not result:
            raise NotFoundException("Email not found")
        return result

    @exception_handler
    def get_auth(
        self,
        username: str,
        password: str,
        session: Session
    ) -> Auth:
        """
        Authenticate a user by username/email and password.
        Args:
            username (str): The username or email address.
            password (str): The plain text password.
            session (Session): The database session.
        Returns:
            Auth: The authenticated user instance.
        Raises:
            NotFoundException: If the user is not found.
            PasswordMismatchException: If the password is incorrect.
        """
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if match(regex, username):
            auth = self.get_auth_by_email(username, session)
        else:
            auth = self.get_auth_by_username(username, session)
        if not bcrypt.checkpw(
            password.encode("utf-8"),
            auth.password.encode("utf-8")
        ):
            raise PasswordMismatchException("Incorrect Password")
        return auth

    @exception_handler
    def create_auth(
        self,
        account_id: UUID,
        data: AuthInfoDto,
        session: Session = None,
        auto_commit: bool = True
    ) -> Auth:
        """
        Create a new authentication record for an account.
        Args:
            account_id (UUID): The account's unique identifier.
            data (AuthInfoDto): The authentication information DTO.
            session (Session, optional): The database session.
            auto_commit (bool, optional): Whether to commit after creation. Defaults to True.
        Returns:
            Auth: The created authentication instance.
        """
        auth_data = data.model_dump()
        auth_data["account_id"] = account_id
        return self.repository.create(
            Auth(**auth_data), session, auto_commit
        )

    @exception_handler
    def update_auth(
        self,
        auth_id: UUID,
        data: dict,
        session: Session = None,
        auto_commit: bool = True
    ) -> Auth:
        """
        Update an authentication record by its ID.
        Args:
            auth_id (UUID): The authentication record's unique identifier.
            data (dict): The updated authentication information.
            session (Session, optional): The database session.
            auto_commit (bool, optional): Whether to commit after update. Defaults to True.
        Returns:
            Auth: The updated authentication instance.
        """
        return self.repository.update(
            auth_id, data, session, auto_commit
        )

    def get_auths(
        self,
        session: Session
    ) -> ListWrapper:
        pass

    def delete_auth(
        self,
        auth_id: UUID,
        session: Session = None,
        auto_commit: bool = True
    ) -> Auth:
        pass
