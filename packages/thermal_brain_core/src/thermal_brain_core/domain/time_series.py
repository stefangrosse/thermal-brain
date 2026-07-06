from datetime import datetime
from typing import Iterable, Iterator

from thermal_brain_core.value_objects import Identifier

from .observation import Observation


class ObservationTimeSeries:
    def __init__(self, observations: Iterable[Observation] = ()) -> None:
        self._observations = tuple(sorted(observations, key=lambda item: item.timestamp))

    def __iter__(self) -> Iterator[Observation]:
        return iter(self._observations)

    def __len__(self) -> int:
        return len(self._observations)

    def append(self, observation: Observation) -> "ObservationTimeSeries":
        return ObservationTimeSeries((*self._observations, observation))

    def latest(self, sensor_id: Identifier | None = None) -> Observation | None:
        observations = self._observations
        if sensor_id is not None:
            observations = tuple(
                observation
                for observation in observations
                if observation.sensor_id == sensor_id
            )
        if not observations:
            return None
        return observations[-1]

    def between(self, start: datetime, end: datetime) -> "ObservationTimeSeries":
        return ObservationTimeSeries(
            observation
            for observation in self._observations
            if start <= observation.timestamp <= end
        )

    def for_sensor(self, sensor_id: Identifier) -> "ObservationTimeSeries":
        return ObservationTimeSeries(
            observation
            for observation in self._observations
            if observation.sensor_id == sensor_id
        )

    def to_tuple(self) -> tuple[Observation, ...]:
        return self._observations
