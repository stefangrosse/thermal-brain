from pydantic import BaseModel, ConfigDict, Field, model_validator

from thermal_brain_core.value_objects import Identifier

from .data_sources import DataSource
from .observation import Observation
from .quantities import ObservationQuantity, supported_units_for_quantity


class Sensor(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: Identifier = Field(default_factory=Identifier)
    source_id: Identifier
    external_id: str
    name: str
    quantity: ObservationQuantity
    unit: str
    zone_id: Identifier | None = None
    enabled: bool = True

    @model_validator(mode="after")
    def validate_supported_unit(self) -> "Sensor":
        supported_units = supported_units_for_quantity(self.quantity)
        if self.unit not in supported_units:
            raise ValueError(
                f"Unit {self.unit!r} is not supported for quantity {self.quantity!s}"
            )
        return self


class SensorRegistry:
    def __init__(self) -> None:
        self._sources: dict[str, DataSource] = {}
        self._sensors: dict[str, Sensor] = {}

    def register_data_source(self, source: DataSource) -> None:
        source_key = self._key(source.id)
        if source_key in self._sources:
            raise ValueError(f"Data source already registered: {source.id.value}")
        self._sources[source_key] = source

    def register_sensor(self, sensor: Sensor) -> None:
        source_key = self._key(sensor.source_id)
        if source_key not in self._sources:
            raise ValueError(f"Unknown data source: {sensor.source_id.value}")
        sensor_key = self._key(sensor.id)
        if sensor_key in self._sensors:
            raise ValueError(f"Sensor already registered: {sensor.id.value}")
        if self._has_external_sensor_id(sensor):
            raise ValueError(
                f"External sensor id already registered for source: {sensor.external_id}"
            )
        self._sensors[sensor_key] = sensor

    def get_data_source(self, source_id: Identifier) -> DataSource:
        return self._sources[self._key(source_id)]

    def get_sensor(self, sensor_id: Identifier) -> Sensor:
        return self._sensors[self._key(sensor_id)]

    def sensors_for_source(self, source_id: Identifier) -> tuple[Sensor, ...]:
        return tuple(
            sensor
            for sensor in self._sensors.values()
            if sensor.source_id == source_id
        )

    def validate_observation(self, observation: Observation) -> None:
        source = self.get_data_source(observation.source_id)
        sensor = self.get_sensor(observation.sensor_id)
        if sensor.source_id != source.id:
            raise ValueError("Observation source does not match registered sensor source")
        if sensor.quantity != observation.quantity:
            raise ValueError("Observation quantity does not match registered sensor")
        if sensor.unit != observation.unit:
            raise ValueError("Observation unit does not match registered sensor")
        if not sensor.enabled:
            raise ValueError("Observation sensor is disabled")

    def _has_external_sensor_id(self, sensor: Sensor) -> bool:
        return any(
            registered.source_id == sensor.source_id
            and registered.external_id == sensor.external_id
            for registered in self._sensors.values()
        )

    @staticmethod
    def _key(identifier: Identifier) -> str:
        return str(identifier.value)
