from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractSubscriptionPlanImpl
from app.models import SubscriptionPlan
from app.repositories.subscription_plan_repository import SubscriptionPlanRepository
from app.utils.wrappers import ListWrapper


class SubscriptionPlanService(AbstractSubscriptionPlanImpl):

    def __init__(
            self,
            repository: SubscriptionPlanRepository = SubscriptionPlanRepository()
    ) -> None:
        self.repository = repository

    def create_plan(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> SubscriptionPlan:
        plan = SubscriptionPlan(**data)
        self.repository.create(
            plan,
            session,
            auto_commit
        )
        return plan

    def get_plans(
            self,
            session: Session
    ) -> ListWrapper:
        result = self.repository.select(session)
        return result

    def get_plan(
            self,
            plan_id: UUID,
            session: Session
    ) -> SubscriptionPlan:
        result = self.repository.get(plan_id, session)
        return result

    def get_one_plan(
            self,
            value: str,
            session: Session
    ) -> SubscriptionPlan:
        result = self.repository.get_one(
            SubscriptionPlan.plan_name == value,
            session
        )
        return result

    def delete_plan(
            self,
            plan_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> SubscriptionPlan:
        result = self.repository.delete(
            plan_id,
            session,
            auto_commit
        )
        return result

    def update_plan(
            self,
            plan_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> SubscriptionPlan:
        result = self.repository.update(
            plan_id,
            data,
            session,
            auto_commit
        )
        return result
