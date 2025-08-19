from re import match
from uuid import UUID
import bcrypt
from sqlmodel import Session
from app.abstract import AbstractAuthImpl
from app.models import Auth
from app.exceptions.exceptions import NotFoundException, PasswordMismatchException
from app.repositories.auth_repository import AuthRepository
from app.utils.wrappers import ListWrapper
from app.dtos import AuthInfo


class AuthService(AbstractAuthImpl):

    def __init__(
            self,
            repository: AuthRepository = AuthRepository()
    ) -> None:
        self.repository = repository

    def get_auth_by_id(
            self,
            auth_id: UUID,
            session: Session
    ) -> Auth:
        result = self.repository.get_one(
            Auth.id == auth_id,
            session
        )
        if not result:
            raise NotFoundException("Auth ID not found")
        return result

    def get_auth_by_username(
            self,
            username: str,
            session: Session
    ) -> Auth:
        result = self.repository.get_one(
            Auth.username == username,
            session
        )
        if not result:
            raise NotFoundException("Username not found")
        return result

    def get_auth_by_email(
            self,
            email: str,
            session: Session
    ) -> Auth:
        result = self.repository.get_one(
            Auth.email == email,
            session
        )
        if not result:
            raise NotFoundException("Email not found")
        return result

    def get_auth(
            self,
            username: str,
            password: str,
            session: Session
    ) -> Auth:
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

    def create_auth(
            self,
            account_id: UUID,
            data: AuthInfo,
            session: Session = None,
            auto_commit: bool = True
    ) -> Auth:
        auth_data = data.model_dump()
        auth_data["account_id"] = account_id
        
        return self.repository.create(
            Auth(**auth_data), session, auto_commit
        )


    def update_auth(
            self,
            auth_id: UUID,
            data: dict,
            session: Session = None,
            auto_commit: bool = True
    ) -> Auth:
        result = self.repository.update(
            auth_id,
            data,
            session,
            auto_commit
        )
        return result

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
