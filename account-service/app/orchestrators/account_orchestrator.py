"""
Orchestrator for account-related operations.
Coordinates the creation and management of accounts and their related entities.
"""
from sqlmodel import Session
from app.dtos import CreateAccountDto, SecureProfileInfoDto
from app.decorators.handlers import exception_handler
from app.models import Account
from app.services import (
    AccountService, 
    AuthService, 
    DeviceService, 
    ProfileService
)


class AccountOrchestrator:
    """
    Orchestrates the creation and management of accounts, profiles, devices, and authentication.
    Uses service classes to perform coordinated operations involving multiple entities.
    """

    def __init__(self) -> None:
        """
        Initialize the AccountOrchestrator with all required service instances.
        """
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
        """
        Register a new account and all its related entities (profile, device, auth).
        Args:
            data (CreateAccountDto): The data required to create the account and related entities.
            session (Session): The database session to use for all operations.
        Returns:
            Account: The created and fully populated account instance.
        """
        account = self.account_service.create_account(
            data.account_info, session, False
        )
        session.flush()
        
        profile_info = SecureProfileInfoDto(
            nickname=data.auth_info.username, is_admin=True
        )

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
