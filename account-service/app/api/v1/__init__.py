from ...web.controllers.admin_controller import admin_bl
from .auth_controller import auth_bl
from .device_controller import device_bl
from .account_controller import account_bl
from .profile_controller import profile_bl

__all__ = [
    "admin_bl",
    "auth_bl",
    "device_bl",
    "account_bl",
    "profile_bl"
]
