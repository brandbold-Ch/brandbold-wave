from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import Franchise
from app.utils.wrappers import ListWrapper


class AbstractFranchiseImpl(ABC):

    @abstractmethod
    def create_franchise(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Franchise:
        pass

    @abstractmethod
    def get_franchises(
            self,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_franchise(
            self,
            franchise_id: UUID,
            session: Session
    ) -> Franchise:
        pass

    @abstractmethod
    def delete_franchise(
            self,
            franchise_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Franchise:
        pass

    @abstractmethod
    def update_franchise(
            self,
            franchise_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Franchise:
        pass
