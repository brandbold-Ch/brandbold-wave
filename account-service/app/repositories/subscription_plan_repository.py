from app.models import SubscriptionPlan
from app.repositories.base_repository import BaseRepository


class SubscriptionPlanRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(SubscriptionPlan)
