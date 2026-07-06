from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from thermal_brain_core.value_objects import Identifier


from .quantities import ObservationQuantity, ObservationValue, quantity_for_value


class Observation(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: Identifier = Field(default_factory=Identifier)
    timestamp: datetime
    sensor_id: Identifier
    source_id: Identifier
    quantity: ObservationQuantity
    value: ObservationValue

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp_is_timezone_aware(cls, timestamp: datetime) -> datetime:
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise ValueError("Observation timestamp must be timezone-aware")
        return timestamp

    @model_validator(mode="after")
    def validate_value_matches_quantity(self) -> "Observation":
        actual_quantity = quantity_for_value(self.value)
        if actual_quantity != self.quantity:
            raise ValueError(
                f"Observation quantity {self.quantity!s} does not match value type "
                f"{actual_quantity!s}"
            )
        return self

    @property
    def unit(self) -> str:
        return str(self.value.unit.value)
