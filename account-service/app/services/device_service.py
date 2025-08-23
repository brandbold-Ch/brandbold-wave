"""
Service class for device operations.
Implements business logic for creating, retrieving, updating, and deleting devices.
"""
from uuid import UUID
from sqlmodel import Session
from app.abstract import AbstractDeviceImpl
from app.models import Device
from app.repositories.device_repository import DeviceRepository
from app.utils.wrappers import ListWrapper
from app.dtos import DeviceInfoDto
from app.decorators import exception_handler



class DeviceService(AbstractDeviceImpl):
    """
    Service class for device-related operations.
    Provides methods to create, retrieve, update, and delete devices using the repository pattern.
    """

    def __init__(
        self,
        repository: DeviceRepository = DeviceRepository()
    ) -> None:
        """
        Initialize the DeviceService with a repository instance.
        Args:
            repository (DeviceRepository, optional): The repository to use. Defaults to DeviceRepository().
        """
        self.repository = repository

    def condition(
        self,
        account_id: UUID,
        device_id: UUID
    ) -> bool:
        """
        Build a condition to filter devices by account and device ID.
        Args:
            account_id (UUID): The account's unique identifier.
            device_id (UUID): The device's unique identifier.
        Returns:
            bool: The condition to use in queries.
        """
        return ((Device.account_id == account_id) &
                (Device.id == device_id))

    @exception_handler
    def create_device(
        self,
        account_id: UUID,
        data: DeviceInfoDto,
        session: Session = None,
        auto_commit: bool = True
    ) -> Device:
        """
        Create a new device for an account.
        Args:
            account_id (UUID): The account's unique identifier.
            data (DeviceInfoDto): The device information DTO.
            session (Session, optional): The database session.
            auto_commit (bool, optional): Whether to commit after creation. Defaults to True.
        Returns:
            Device: The created device instance.
        """
        device_data = data.model_dump()
        device_data["account_id"] = account_id
        return self.repository.create(
            Device(**device_data), session, auto_commit
        )

    @exception_handler
    def get_devices(
        self,
        account_id: UUID,
        session: Session
    ) -> ListWrapper:
        """
        Retrieve all devices for a given account.
        Args:
            account_id (UUID): The account's unique identifier.
            session (Session): The database session.
        Returns:
            ListWrapper: A wrapper containing all device instances for the account.
        """
        return self.repository.get_many(
            Device.account_id == account_id, session
        )

    @exception_handler
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
        condition = self.condition(account_id, device_id)
        return self.repository.get_one(condition, session)

    @exception_handler
    def delete_device(
        self,
        account_id: UUID,
        device_id: UUID,
        session: Session = None,
        auto_commit: bool = True
    ) -> Device:
        """
        Delete a specific device by account and device ID.
        Args:
            account_id (UUID): The account's unique identifier.
            device_id (UUID): The device's unique identifier.
            session (Session, optional): The database session.
            auto_commit (bool, optional): Whether to commit after deletion. Defaults to True.
        Returns:
            Device: The deleted device instance.
        """

    @exception_handler
    def update_device(
        self,
        account_id: UUID,
        device_id: UUID,
        data: dict,
        session: Session = None,
        auto_commit: bool = True
    ) -> Device:
        """
        Update a specific device by account and device ID.
        Args:
            account_id (UUID): The account's unique identifier.
            device_id (UUID): The device's unique identifier.
            data (dict): The updated device information.
            session (Session, optional): The database session.
            auto_commit (bool, optional): Whether to commit after update. Defaults to True.
        Returns:
            Device: The updated device instance.
        """
