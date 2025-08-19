from sqlmodel import Session
from app.dtos import CreateAccountDto, ProfileInfo
from app.decorators.handlers import exception_handler
from app.models import Account
from app.services import (
    AccountService, 
    AuthService, 
    DeviceService, 
    ProfileService
)


class AccountOrchestrator:

    def __init__(self) -> None:
        self.account_service = AccountService()
        self.profile_service = ProfileService()
        self.auth_service = AuthService()
        self.device_service = DeviceService()

    @exception_handler
    def register_account(
            self,
            data: CreateAccountDto,
            session: Session
    ) -> Account:
        account = self.account_service.create_account(
            data.account_info, session, False
        )
        session.flush()
        
        profile_info = ProfileInfo(nickname=data.auth_info.username)

        self.device_service.create_device(
            account.id, data.device_info, session, False
        )
        self.auth_service.create_auth(
            account.id, data.auth_info, session, False
        )        
        self.profile_service.create_profile(
            account.id, profile_info, session, False
        )
        session.commit()    
        
        return self.account_service.get_account(account.id, session)
