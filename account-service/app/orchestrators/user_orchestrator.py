from sqlmodel import Session
from app.decorators.handlers import exception_handler
from app.models import User
from app.services import UserService, AuthService
from app.services.device_service import DeviceService
from app.dtos.user_dto import CreateUserDto

class UserOrchestrator:

    def __init__(self) -> None:
        self.user_service = UserService()
        self.auth_service = AuthService()
        self.device_service = DeviceService()

    @exception_handler
    def register_user(
            self,
            data: CreateUserDto,
            session: Session
    ) -> User:
        user = self.user_service.create_user(data.user_info, session, False)
        session.flush()

        self.auth_service.create_auth(data.auth_info, user.id, session, False)
        self.device_service.create_device(user.id, data.device_info, session, False)
        
        session.commit()
        return self.user_service.get_user(user.id, session)
