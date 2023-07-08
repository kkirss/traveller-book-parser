import logging
from pathlib import Path

from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

from .log_level import LogLevel


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8')

    log_level: LogLevel = LogLevel.INFO

    books_path: Path = Field(
        description="Folder path where books are loaded from",
        default_factory=lambda: Path(".") / "data" / "books")
    book_descriptions_path: Path = Field(
        description="Folder path where book description files are loaded from",
        default_factory=lambda: Path(".") / "book_descriptions")


try:
    SETTINGS = Settings()
except ValidationError as e:
    print(e)
else:
    logging.basicConfig(level=SETTINGS.log_level.value)
