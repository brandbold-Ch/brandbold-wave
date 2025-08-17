from enum import Enum
from uuid import UUID, uuid4
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY, NUMERIC
from sqlmodel import Field
from app.models.base_model import EntityBaseModel


class Plans(str, Enum):
    FREE = "free"
    BASIC = "basic"
    SUPER = "super"
    MEGA = "mega"
    PRO = "pro"


class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    STRIPE = "stripe"
    APPLE_PAY = "apple_pay"
    GOOGLE_PAY = "google_pay"
    CRYPTO = "crypto"
    BANK_TRANSFER = "bank_transfer"


class SubscriptionPlan(EntityBaseModel, table=True):
    __tablename__ = "subscription_plan"

    id: UUID = Field(default_factory=lambda: uuid4(), primary_key=True)
    plan_name: Plans
    payment_methods: list[PaymentMethod] = Field(sa_column=Column(ARRAY(String)))
    price: float = Field(sa_column=Column(NUMERIC(10, 2)))
