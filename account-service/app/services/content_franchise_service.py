from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractContentFranchiseImpl
from app.models import ContentFranchise
from app.repositories.content_franchise_repository import ContentFranchiseRepository
from app.utils.wrappers import ListWrapper


class ContentFranchiseService(AbstractContentFranchiseImpl):

    def __init__(
            self,
            repository:
            ContentFranchiseRepository = ContentFranchiseRepository()
    ) -> None:
        self.repository = repository

    def create_franchise(
            self,
            franchise_id: UUID,
            content_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> ContentFranchise:
        franchise = ContentFranchise(
            franchise_id=franchise_id,
            content_id=content_id
        )
        self.repository.create(franchise, session, auto_commit)
        return franchise

    def get_franchises(
            self, 
            session: Session = None
    ) -> ListWrapper:
        pass

    def get_franchise(
            self,
            franchise_id: UUID,
            content_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> ContentFranchise:
        condition = ((ContentFranchise.id == franchise_id) &
                     (ContentFranchise.content_id == content_id))
        result = self.repository.get_one(condition, session)
        return result

    def delete_franchise(
            self,
            franchise_id: UUID,
            content_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> ContentFranchise:
        pass

    def update_franchise(
            self,
            franchise_id: UUID,
            content_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> ContentFranchise:
        pass
