from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractUserImpl
from app.models import User
from app.repositories.user_repository import UserRepository
from app.utils.wrappers import ListWrapper


class UserService(AbstractUserImpl):

    def __init__(
            self,
            user_repository: UserRepository = UserRepository()
    ) -> None:
        self.repository = user_repository

    def create_user(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> User:
        user = User(**data)
        self.repository.create(
            user,
            session,
            auto_commit
        )
        return user

    def get_users(
            self,
            session: Session = None
    ) -> ListWrapper:
        result = self.repository.select(session)
        return result

    def get_user(
            self,
            user_id: UUID,
            session: Session = None
    ) -> User:
        result = self.repository.get(user_id, session)
        return result

    def delete_user(
            self,
            user_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> User:
        result = self.repository.delete(
            user_id,
            session,
            auto_commit
        )
        return result

    def update_user(
            self,
            user_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> User:
        result = self.repository.update(
            user_id,
            data,
            session,
            auto_commit
        )
        return result
