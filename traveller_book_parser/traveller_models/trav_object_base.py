from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field

from .trav_object_types import TravObjectType


class TravObjectBase(BaseModel):
    """A traveller object with name."""

    type: TravObjectType

    name: str = Field(repr=True)
    image_path: Optional[Path] = None
