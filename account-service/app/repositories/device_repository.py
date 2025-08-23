from app.models import Device
from app.repositories.base_repository import BaseRepository



class DeviceRepository(BaseRepository):
    """
    Repository class for Device model.
    Inherits generic CRUD operations from BaseRepository.
    """

    def __init__(self) -> None:
        """
        Initialize the DeviceRepository with the Device model.
        """
        super().__init__(Device)
