from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import ContentFranchise
from app.utils.wrappers import ListWrapper


class AbstractContentFranchiseImpl(ABC):

    @abstractmethod
    def create_franchise(
            self,
            franchise_id: UUID,
            content_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContentFranchise:
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
            content_id: UUID,
            session: Session
    ) -> ContentFranchise:
        pass

    @abstractmethod
    def delete_franchise(
            self,
            franchise_id: UUID,
            content_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContentFranchise:
        pass

    @abstractmethod
    def update_franchise(
            self,
            franchise_id: UUID,
            content_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContentFranchise:
        pass
