from abc import ABC, abstractmethod
from uuid import UUID
from sqlmodel import Session
from src.api.v1.models import Device
from src.utils.wrappers import ListWrapper
from src.api.v1.dtos import DeviceInfoDto


class AbstractDeviceImpl(ABC):
    """
    Abstract base class for device-related operations.
    Defines the interface for creating, retrieving, updating, and deleting devices.
    """

    @abstractmethod
    def create_device(
        self,
        account_id: UUID,
        data: DeviceInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Device:
        """
        Create a new device for a given account.
        Args:
            account_id (UUID): The account's unique identifier.
            data (DeviceInfo): The device information to create.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after creation. Defaults to True.
        Returns:
            Device: The created device instance.
        """

    @abstractmethod
    def get_devices(
        self,
        account_id: UUID,
        session: Session
    ) -> ListWrapper:
        """
        Retrieve all devices associated with a given account.
        Args:
            account_id (UUID): The account's unique identifier.
            session (Session): The database session.
        Returns:
            ListWrapper: A wrapper containing all device instances for the account.
        """

    @abstractmethod
    def get_device(
        self,
        account_id: UUID,
        device_id: UUID,
        session: Session
    ) -> Device:
        """
        Retrieve a specific device by account and device ID.
        Args:
            account_id (UUID): The account's unique identifier.
            device_id (UUID): The device's unique identifier.
            session (Session): The database session.
        Returns:
            Device: The requested device instance.
        """

    @abstractmethod
    def delete_device(
        self,
        account_id: UUID,
        device_id: UUID,
        session: Session,
        auto_commit: bool = True
    ) -> Device:
        """
        Delete a specific device by account and device ID.
        Args:
            account_id (UUID): The account's unique identifier.
            device_id (UUID): The device's unique identifier.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after deletion. Defaults to True.
        Returns:
            Device: The deleted device instance.
        """

    @abstractmethod
    def update_device(
        self,
        account_id: UUID,
        device_id: UUID,
        data: DeviceInfoDto,
        session: Session,
        auto_commit: bool = True
    ) -> Device:
        """
        Update a specific device by account and device ID.
        Args:
            account_id (UUID): The account's unique identifier.
            device_id (UUID): The device's unique identifier.
            data (DeviceInfo): The updated device information.
            session (Session): The database session.
            auto_commit (bool, optional): Whether to commit after update. Defaults to True.
        Returns:
            Device: The updated device instance.
        """
