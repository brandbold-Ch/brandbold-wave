from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractFranchiseImpl
from app.decorators.handlers import exception_handler
from app.models import Franchise
from app.repositories.franchise_repository import FranchiseRepository
from app.utils.wrappers import ListWrapper


class FranchiseService(AbstractFranchiseImpl):

    def __init__(
            self,
            repository: FranchiseRepository = FranchiseRepository()
    ) -> None:
        self.repository = repository

    @exception_handler
    def create_franchise(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Franchise:
        franchise = Franchise(**data)
        self.repository.create(
            franchise,
            session,
            auto_commit
        )
        return franchise

    def get_franchise(
            self,
            franchise_id: UUID,
            session: Session,
    ) -> Franchise:
        result = self.repository.get(franchise_id, session)
        return result

    @exception_handler
    def update_franchise(
            self,
            franchise_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Franchise:
        result = self.repository.update(
            franchise_id,
            data,
            session,
            auto_commit
        )
        return result

    @exception_handler
    def get_franchises(
            self,
            session: Session
    ) -> ListWrapper:
        result = self.repository.select(session)
        return result

    @exception_handler
    def delete_franchise(
            self,
            franchise_id: str,
            session: Session,
            auto_commit: bool = True
    ) -> Franchise:
        result = self.repository.delete(
            franchise_id,
            session,
            auto_commit
        )
        return result
