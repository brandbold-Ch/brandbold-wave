from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractDeviceImpl
from app.models import Device
from app.repositories.device_repository import DeviceRepository
from app.utils.wrappers import ListWrapper
from app.dtos import DeviceInfo


class DeviceService(AbstractDeviceImpl):

    def __init__(
            self,
            repository: DeviceRepository = DeviceRepository()
    ) -> None:
        self.repository = repository

    def condition(
            self,
            account_id: UUID,
            device_id: UUID
    ) -> bool:
        return ((Device.account_id == account_id) &
                (Device.id == device_id))

    def create_device(
            self,
            account_id: UUID,
            data: DeviceInfo,
            session: Session = None,
            auto_commit: bool = True
    ) -> Device:
        device_data = data.model_dump()
        device_data["account_id"] = account_id

        return self.repository.create(
            Device(**device_data), session, auto_commit
        )


    def get_devices(
            self,
            account_id: UUID,
            session: Session
    ) -> ListWrapper:
        return self.repository.get_many(
            Device.account_id == account_id,
            session
        )

    def get_device(
            self,
            account_id: UUID,
            device_id: UUID,
            session: Session
    ) -> Device:
        condition = self.condition(account_id, device_id)
        result = self.repository.get_one(condition, session)
        return result

    def delete_device(
            self,
            account_id: UUID,
            device_id: UUID,
            session: Session = None,
            auto_commit: bool = True
    ) -> Device:
        condition = self.condition(account_id, device_id)
        result = self.repository.delete_one(
            condition,
            session,
            auto_commit
        )
        return result

    def update_device(
            self,
            account_id: UUID,
            device_id: UUID,
            data: dict,
            session: Session = None,
            auto_commit: bool = True
    ) -> Device:
        condition = self.condition(account_id, device_id)
        result = self.repository.update_one(
            condition,
            data,
            session,
            auto_commit
        )
        return result
