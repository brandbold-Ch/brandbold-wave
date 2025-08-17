from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import SubscriptionPlan
from app.utils.wrappers import ListWrapper


class AbstractSubscriptionPlanImpl(ABC):

    @abstractmethod
    def create_plan(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> SubscriptionPlan:
        pass

    @abstractmethod
    def get_plans(
            self,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_plan(
            self,
            plan_id: UUID,
            session: Session
    ) -> SubscriptionPlan:
        pass

    @abstractmethod
    def delete_plan(
            self,
            plan_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> SubscriptionPlan:
        pass

    @abstractmethod
    def update_plan(
            self,
            plan_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> SubscriptionPlan:
        pass
