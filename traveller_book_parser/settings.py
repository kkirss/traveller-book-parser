from enum import Enum
import logging
from pathlib import Path

import pandas
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_PATH = Path(__file__).parent.parent


class LogLevel(str, Enum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_PATH / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    log_level: LogLevel = LogLevel.INFO

    books_path: Path = Field(
        description="Folder path where books are loaded from",
        default_factory=lambda: PROJECT_PATH / "data" / "books",
    )
    book_descriptions_path: Path = Field(
        description="Folder path where book description files are loaded from",
        default_factory=lambda: PROJECT_PATH / "book_descriptions",
    )

    cache_path: Path = Field(
        description="Path for temporary files",
        default_factory=lambda: PROJECT_PATH / "data" / "cache",
    )

    pdf_to_html_executable: Path = Field(
        description="Path to pdftohml (version 4.x) executable",
        default_factory=lambda: Path("pdftohtml"),
    )


try:
    SETTINGS = Settings()
except ValidationError as e:
    print(e)
else:
    logging.basicConfig(level=SETTINGS.log_level.value)


def set_pandas_options():
    pandas.set_option("display.max_columns", None)
    pandas.set_option("display.expand_frame_repr", False)  # noqa: FBT003


_SETUP_HAS_RUN = False

if not _SETUP_HAS_RUN:
    set_pandas_options()
    _SETUP_HAS_RUN = True
