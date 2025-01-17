
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)
from functools import lru_cache


class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    supabase_url: str = ""
    supabase_key: str = ""
    kmd_address: str = "http://localhost:4002"
    kmd_token: str = ""

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    print(f"BASE_URL: ", settings.base_url)
    return settings

# print("ENV_NAME: ", get_settings().env_name)
# print("BASE_URL: ", get_settings().base_url)
# print("DATABASE_URL: ", get_settings().database_url)
