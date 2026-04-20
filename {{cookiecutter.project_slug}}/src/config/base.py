from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # -- AWS Configuration --
    AWS_REGION: str = "us-east-1"
    AWS_ACCESS_KEY_ID: str = "fake_access_key"
    AWS_SECRET_ACCESS_KEY: str = "fake_secret_key"
    AWS_ENVIRONMENT: str = "local"
    DYNAMO_TABLE_NAME: str = "my_table"
    ENDPOINT_URL: str | None = None

    # -- App Configuration --
    LOG_LEVEL: str | None = "INFO"

    model_config = SettingsConfigDict(env_file="./.env")


config = Config()
