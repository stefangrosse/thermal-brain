from pydantic import BaseModel, Field
from thermal_brain_core.value_objects import Identifier
from .zone import Zone

class Building(BaseModel):
    id: Identifier = Field(default_factory=Identifier)
    name: str
    construction_year: int | None = None
    zones: list[Zone] = Field(default_factory=list)
