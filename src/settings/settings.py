import logging

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

from .log_level import LogLevel


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8')

    log_level: LogLevel = LogLevel.INFO


try:
    SETTINGS = Settings()
except ValidationError as e:
    print(e)
else:
    logging.basicConfig(level=SETTINGS.log_level.value)
