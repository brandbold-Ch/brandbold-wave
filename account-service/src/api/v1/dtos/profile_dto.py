"""
Data Transfer Objects (DTOs) for user profile data.
Defines classes for transferring profile-related information between application layers.
"""
from typing import Optional
from pydantic import BaseModel


class ProfileInfoDto(BaseModel):
    """
    Data Transfer Object for user profile information.
    Fields:
        nickname (str): The profile's display name.
        avatar_file (Optional[str]): Path or identifier for the profile's avatar image.
        maturity_rating (Optional[int]): Maturity rating for content restrictions. Default is 0.
        autoplay_next_episode (Optional[bool]): Whether to autoplay the next episode. Default is False.
        skip_intro (Optional[bool]): Whether to skip intros automatically. Default is False.
        skip_credits (Optional[bool]): Whether to skip credits automatically. Default is False.
    """
    nickname: str
    avatar_file: Optional[str] = None
    maturity_rating: Optional[int] = 0
    autoplay_next_episode: Optional[bool] = False
    skip_intro: Optional[bool] = False
    skip_credits: Optional[bool] = False


class SecureProfileInfoDto(ProfileInfoDto):
    """
    Data Transfer Object for secure user profile information, extending ProfileInfoDto.
    Adds:
        is_admin (bool): Indicates if the profile has administrative privileges.
    """
    is_admin: bool
    