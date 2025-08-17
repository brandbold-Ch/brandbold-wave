from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from app.models import Device
from app.utils.wrappers import ListWrapper


class AbstractDeviceImpl(ABC):

    @abstractmethod
    def create_device(
            self,
            user_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Device:
        pass

    @abstractmethod
    def get_devices(
            self,
            user_id: UUID,
            session: Session
    ) -> ListWrapper:
        pass

    @abstractmethod
    def get_device(
            self,
            user_id: UUID,
            device_id: UUID,
            session: Session
    ) -> Device:
        pass

    @abstractmethod
    def delete_device(
            self,
            user_id: UUID,
            device_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Device:
        pass

    @abstractmethod
    def update_device(
            self,
            user_id: UUID,
            device_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Device:
        pass
