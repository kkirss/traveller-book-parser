from enum import Enum
import logging
from pathlib import Path

import pandas
import pydantic
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from rich.logging import RichHandler

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
    log_parsed_entities: bool = Field(
        description="Whether to log parsed entities. Note: These are logged at DEBUG level.",
        default=False,
    )

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
    images_path: Path = Field(
        description="Path for image files",
        default_factory=lambda: PROJECT_PATH / "data" / "cache" / "images",
    )

    pdf_to_html_executable: Path = Field(
        description="Path to pdftohml (version 4.x) executable",
        default_factory=lambda: Path("pdftohtml"),
    )


def configure_logging():
    logging.basicConfig(
        level=LogLevel.NOTSET.value,
        format="%(message)s",
        handlers=[
            RichHandler(
                show_time=False,
                show_path=False,
                rich_tracebacks=True,
                tracebacks_suppress=[pydantic],
            )
        ],
    )


def configure_pandas_display():
    pandas.set_option("display.max_columns", None)
    pandas.set_option("display.expand_frame_repr", False)  # noqa: FBT003


def set_log_level(log_level: LogLevel):
    logging.root.setLevel(log_level.value)

    if log_level == LogLevel.DEBUG:
        # Skip pdfminer debug logging as it's too verbose
        logging.getLogger("pdfminer").setLevel(logging.INFO)
    else:
        raise ValueError()


configure_pandas_display()
configure_logging()

SETTINGS = Settings()

set_log_level(SETTINGS.log_level)
