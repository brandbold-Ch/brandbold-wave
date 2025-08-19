from app.models import Device
from app.repositories.base_repository import BaseRepository


class DeviceRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__(Device)
