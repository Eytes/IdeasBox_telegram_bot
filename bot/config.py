import os

from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


class MongoSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MONGO_", case_sensitive=False)

    username: str = os.getenv("MONGO_USERNAME")
    password: SecretStr = os.getenv("MONGO_PASSWORD")
    host: str = os.getenv("MONGO_HOST")
    port: int = os.getenv("MONGO_PORT")
    database_name: str = os.getenv("MONGO_DATABASE_NAME")
    url: str = ""

    @model_validator(mode="after")
    def create_url(self) -> Self:
        self.url = f"mongodb://{self.username}:{self.password.get_secret_value()}@{self.host}:{self.port}"
        return self


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr
    # для конфиденциальных данных, например, токена бота
    token: SecretStr = os.getenv("TOKEN")
    mongodb: MongoSettings = MongoSettings()


# При импорте файла сразу создастся
# и провалидируется объект конфига,
# который можно далее импортировать из разных мест
settings = Settings()  # type: ignore[call-arg]
