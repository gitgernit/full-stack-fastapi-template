import secrets

import pydantic
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    model_config = pydantic_settings.SettingsConfigDict(
        env_file='../.env',
        env_ignore_empty=True,
        extra='ignore',
    )

    JWT_SECRET_KEY: str = secrets.token_urlsafe(32)
    JWT_ALGORITHM: str = 'HS256'
    SAMPLE_PAYLOAD: dict[str, str] = pydantic.fields.Field(
        default={'foo': 'bar', 'john': 'doe'}, exclude=True
    )


config = Config()
