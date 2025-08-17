from typing import Self
from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, RedisDsn, Field, model_validator


class Settings(BaseSettings):
    spring_internal_url: str = Field(alias="SPRING_INTERNAL_URL")
    spring_local_url: str = Field(alias="SPRING_LOCAL_URL")
    spring_proxy_prefix: str = Field(alias="SPRING_PROXY_PREFIX")
    
    postgres_internal_url: PostgresDsn = Field(alias="POSTGRES_INTERNAL_URL")
    postgres_local_url: PostgresDsn = Field(alias="POSTGRES_LOCAL_URL")
    
    redis_internal_url: RedisDsn = Field(alias="REDIS_INTERNAL_URL")
    redis_local_url: RedisDsn = Field(alias="REDIS_LOCAL_URL")
    
    @model_validator(mode="after")
    def parse_urls(self) -> Self:
        self.postgres_internal_url = str(self.postgres_internal_url)
        self.postgres_local_url = str(self.postgres_local_url)  
        self.redis_internal_url = str(self.redis_internal_url)
        self.redis_local_url = str(self.redis_local_url)
        return self
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
