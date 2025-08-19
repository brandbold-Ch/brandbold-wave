from app.abstract import AbstractProfileImpl
from app.repositories.profile_repository import ProfileRepository
from app.models import Profile
from sqlmodel import Session
from app.utils.wrappers import ListWrapper
from uuid import UUID
from app.dtos import ProfileInfo
from app.utils.io_tools import auto_select_avatar


class ProfileService(AbstractProfileImpl):
    
    def __init__(
        self, 
        repository: ProfileRepository = ProfileRepository()
    ) -> None:
        self.repository = repository

    def condition(
            self,
            account_id: UUID,
            profile_id: UUID
    ) -> bool:
        return ((Profile.account_id == account_id) &
                (Profile.id == profile_id))
        
    def create_profile(
        self,
        account_id: UUID,
        data: ProfileInfo,
        session: Session,
        auto_commit: bool = True
    ) -> Profile:
        profile_data = data.model_dump(exclude={"avatar_file"})
        profile_data["account_id"] = account_id
        
        if data.avatar_file is None:
            profile_data["avatar_url"] = auto_select_avatar()
                    
        return self.repository.create(
            Profile(**profile_data), session, auto_commit
        )

    
    def get_profiles(
        self,
        account_id: UUID,
        session: Session
    ) -> ListWrapper:
        return self.repository.get_many(
            Profile.account_id == account_id,
            session
        )
    
    def get_profile(
        self,
        account_id: UUID,
        profile_id: UUID,
        session: Session
    ) -> Profile:
        condition = self.condition(account_id, profile_id)
        result = self.repository.get_one(condition, session)
        return result
    
    def delete_profile(
        self,
        account_id: UUID,
        profile_id: UUID,
        session: Session,
        auto_commit: bool = True
    ) -> Profile:
        condition = self.condition(account_id, profile_id)
        result = self.repository.delete_one(
            condition,
            session,
            auto_commit
        )
        return result
    
    def update_profile(
        self,
        account_id: UUID,
        profile_id: UUID,
        data: dict,
        session: Session,
        auto_commit: bool = True
    ) -> Profile:
        condition = self.condition(account_id, profile_id)
        result = self.repository.update_one(
            condition,
            data,
            session,
            auto_commit
        )
        return result
