from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='s3_proxy_')
    access_key: str
    secret_key: str


config = Settings()
