from typing import Optional
from uuid import UUID
from sqlmodel import Relationship, Field
from app.models.base_user_model import BaseUser


class User(BaseUser, table=True):
    subscription_plan_id: Optional[UUID] = Field(foreign_key="subscription_plan.id",
                                                 nullable=True, default=None)
    auth: "Auth" = Relationship(back_populates="user",
                                sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    devices: list["Device"] = Relationship(
        sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    watch_histories: list["WatchHistory"] = Relationship(
        sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    subscription: "SubscriptionPlan" = Relationship()

    def as_json(self, deep: bool = True) -> dict:
        data = super().as_json()
        data["auth_data"] = self.auth.as_json()
        data["subscription_data"] = self.subscription.as_json() \
            if self.subscription_plan_id else None
        if deep:
            data["devices"] = [device.as_json() for device in self.devices]
        return data

    def hide_fields(self) -> set:
        return {"subscription_plan_id"}
