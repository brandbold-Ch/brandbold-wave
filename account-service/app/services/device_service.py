from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractDeviceImpl
from app.models import Device
from app.repositories.device_repository import DeviceRepository
from app.utils.wrappers import ListWrapper


class DeviceService(AbstractDeviceImpl):

    def __init__(
            self,
            repository: DeviceRepository = DeviceRepository()
    ) -> None:
        self.repository = repository

    def condition(
            self,
            user_id: UUID,
            device_id: UUID
    ) -> bool:
        return ((Device.user_id == user_id) &
                (Device.id == device_id))

    def create_device(
            self,
            user_id: UUID,
            data: dict,
            session: Session = None,
            auto_commit: bool = True
    ) -> Device:
        device = Device(**data, user_id=user_id)
        self.repository.create(device, session, auto_commit)
        return device

    def get_devices(
            self,
            user_id: UUID,
            session: Session
    ) -> ListWrapper:
        result = self.repository.get_many(
            Device.user_id == user_id,
            session
        )
        return result

    def get_device(
            self,
            user_id: UUID,
            device_id: UUID,
            session: Session
    ) -> Device:
        condition = self.condition(user_id, device_id)
        result = self.repository.get_one(condition, session)
        return result

    def delete_device(
            self,
            user_id: UUID,
            device_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> Device:
        condition = self.condition(user_id, device_id)
        result = self.repository.delete_one(
            condition,
            session,
            auto_commit
        )
        return result

    def update_device(
            self,
            user_id: UUID,
            device_id: UUID,
            data: dict,
            session: Session = None,
            auto_commit: bool = True
    ) -> Device:
        condition = self.condition(user_id, device_id)
        result = self.repository.update_one(
            condition,
            data,
            session,
            auto_commit
        )
        return result
