from pydantic import BaseModel


class LoginDto(BaseModel):
    """
    Data Transfer Object for user login.
    Contains username and password fields for authentication.
    """
    username: str
    password: str
