from enum import StrEnum
from typing import Iterable, Protocol

from pydantic import BaseModel, ConfigDict, Field

from thermal_brain_core.value_objects import Identifier

from .observation import Observation


class DataSourceType(StrEnum):
    SENSOR = "sensor"
    WEATHER = "weather"
    CALCULATED = "calculated"
    MANUAL = "manual"


class DataSource(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: Identifier = Field(default_factory=Identifier)
    name: str
    source_type: DataSourceType
    description: str | None = None


class DataSourceReader(Protocol):
    @property
    def source(self) -> DataSource:
        """Return metadata describing the data source."""

    def read_observations(self) -> Iterable[Observation]:
        """Return observations collected from the data source."""
