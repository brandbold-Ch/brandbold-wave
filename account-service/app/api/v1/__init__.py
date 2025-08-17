from ...web.controllers.admin_controller import admin_bl
from .auth_controller import auth_bl
from .content_controller import content_bl
from .device_controller import device_bl
from .genre_controller import genre_bl
from .subscription_plan_controller import subscription_plan_bl
from .user_controller import user_bl
from .watch_history_controller import watch_bl

__all__ = [
    "admin_bl",
    "auth_bl",
    "content_bl",
    "device_bl",
    "genre_bl",
    "subscription_plan_bl",
    "user_bl",
    "watch_bl"
]
