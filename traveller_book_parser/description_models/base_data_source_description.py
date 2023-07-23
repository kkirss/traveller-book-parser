from pydantic import BaseModel, Field


class BaseDataSourceDescription(BaseModel):
    """Description of a source of data (e.g. a table).

    See [Tabula website](https://tabula.technology/).
    """

    type: str = Field(repr=True)
