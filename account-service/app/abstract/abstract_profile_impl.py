from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import Profile
from app.utils.wrappers import ListWrapper
from app.dtos import ProfileInfo


class AbstractProfileImpl(ABC):

    @abstractmethod
    def create_profile(
            self,
            account_id: UUID,
            data: ProfileInfo,
            session: Session,
            auto_commit: bool = True
    ) -> Profile:
        pass

    @abstractmethod
    def get_profiles(
            self,
            account_id: UUID,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_profile(
            self,
            account_id: UUID,
            profile_id: UUID,
            session: Session
    ) -> Profile:
        pass

    @abstractmethod
    def delete_profile(
            self,
            account_id: UUID,
            profile_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Profile:
        pass

    @abstractmethod
    def update_profile(
            self,
            account_id: UUID,
            profile_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Profile:
        pass
