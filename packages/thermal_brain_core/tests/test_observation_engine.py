from datetime import UTC, datetime, timedelta

import pytest

from thermal_brain_core.domain import (
    DataSource,
    DataSourceType,
    Observation,
    ObservationQuantity,
    ObservationTimeSeries,
    Sensor,
    SensorRegistry,
)
from thermal_brain_core.value_objects import Energy, Identifier, Power, Temperature


def test_observation_uses_value_object_and_exposes_unit() -> None:
    source_id = Identifier()
    sensor_id = Identifier()

    observation = Observation(
        timestamp=datetime(2026, 1, 1, 12, 0, tzinfo=UTC),
        sensor_id=sensor_id,
        source_id=source_id,
        quantity=ObservationQuantity.TEMPERATURE,
        value=Temperature(value=21.5),
    )

    assert observation.unit == "°C"


def test_observation_rejects_naive_timestamp() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        Observation(
            timestamp=datetime(2026, 1, 1, 12, 0),
            sensor_id=Identifier(),
            source_id=Identifier(),
            quantity=ObservationQuantity.POWER,
            value=Power(value=4.2),
        )


def test_observation_rejects_quantity_mismatch() -> None:
    with pytest.raises(ValueError, match="does not match value type"):
        Observation(
            timestamp=datetime(2026, 1, 1, 12, 0, tzinfo=UTC),
            sensor_id=Identifier(),
            source_id=Identifier(),
            quantity=ObservationQuantity.ENERGY,
            value=Power(value=4.2),
        )


def test_sensor_registry_validates_observation_against_registered_sensor() -> None:
    registry = SensorRegistry()
    source = DataSource(name="Home Assistant", source_type=DataSourceType.SENSOR)
    sensor = Sensor(
        source_id=source.id,
        external_id="sensor.living_room_temperature",
        name="Living room temperature",
        quantity=ObservationQuantity.TEMPERATURE,
        unit="°C",
    )
    observation = Observation(
        timestamp=datetime(2026, 1, 1, 12, 0, tzinfo=UTC),
        sensor_id=sensor.id,
        source_id=source.id,
        quantity=ObservationQuantity.TEMPERATURE,
        value=Temperature(value=20.8),
    )

    registry.register_data_source(source)
    registry.register_sensor(sensor)

    registry.validate_observation(observation)


def test_sensor_registry_rejects_unknown_source() -> None:
    registry = SensorRegistry()
    sensor = Sensor(
        source_id=Identifier(),
        external_id="sensor.boiler_power",
        name="Boiler power",
        quantity=ObservationQuantity.POWER,
        unit="kW",
    )

    with pytest.raises(ValueError, match="Unknown data source"):
        registry.register_sensor(sensor)


def test_sensor_unit_must_match_quantity() -> None:
    with pytest.raises(ValueError, match="not supported"):
        Sensor(
            source_id=Identifier(),
            external_id="sensor.energy",
            name="Energy",
            quantity=ObservationQuantity.ENERGY,
            unit="kW",
        )


def test_time_series_orders_and_filters_observations() -> None:
    source_id = Identifier()
    temperature_sensor_id = Identifier()
    energy_sensor_id = Identifier()
    now = datetime(2026, 1, 1, 12, 0, tzinfo=UTC)
    later = now + timedelta(hours=1)
    earlier = now - timedelta(hours=1)
    temperature_observation = Observation(
        timestamp=now,
        sensor_id=temperature_sensor_id,
        source_id=source_id,
        quantity=ObservationQuantity.TEMPERATURE,
        value=Temperature(value=20.0),
    )
    energy_observation = Observation(
        timestamp=later,
        sensor_id=energy_sensor_id,
        source_id=source_id,
        quantity=ObservationQuantity.ENERGY,
        value=Energy(value=12.0),
    )
    earlier_temperature_observation = Observation(
        timestamp=earlier,
        sensor_id=temperature_sensor_id,
        source_id=source_id,
        quantity=ObservationQuantity.TEMPERATURE,
        value=Temperature(value=19.5),
    )

    series = ObservationTimeSeries(
        [temperature_observation, energy_observation, earlier_temperature_observation]
    )

    assert series.latest() == energy_observation
    assert series.latest(temperature_sensor_id) == temperature_observation
    assert series.for_sensor(temperature_sensor_id).to_tuple() == (
        earlier_temperature_observation,
        temperature_observation,
    )
    assert series.between(now, later).to_tuple() == (
        temperature_observation,
        energy_observation,
    )


def test_time_series_descriptive_statistics() -> None:
    source_id = Identifier()
    sensor_id = Identifier()
    observations = [
        Observation(
            timestamp=datetime(2026, 1, 1, 10, 0, tzinfo=UTC),
            sensor_id=sensor_id,
            source_id=source_id,
            quantity=ObservationQuantity.TEMPERATURE,
            value=Temperature(value=18.0),
        ),
        Observation(
            timestamp=datetime(2026, 1, 1, 11, 0, tzinfo=UTC),
            sensor_id=sensor_id,
            source_id=source_id,
            quantity=ObservationQuantity.TEMPERATURE,
            value=Temperature(value=20.0),
        ),
        Observation(
            timestamp=datetime(2026, 1, 1, 12, 0, tzinfo=UTC),
            sensor_id=sensor_id,
            source_id=source_id,
            quantity=ObservationQuantity.TEMPERATURE,
            value=Temperature(value=22.0),
        ),
    ]

    statistics = ObservationTimeSeries(observations).descriptive_statistics()

    assert statistics.count == 3
    assert statistics.minimum == 18.0
    assert statistics.maximum == 22.0
    assert statistics.mean == 20.0
    assert statistics.median == 20.0
    assert statistics.variance == 8 / 3
    assert statistics.standard_deviation == pytest.approx((8 / 3) ** 0.5)


def test_time_series_descriptive_statistics_for_empty_series() -> None:
    statistics = ObservationTimeSeries().descriptive_statistics()

    assert statistics.count == 0
    assert statistics.minimum is None
    assert statistics.maximum is None
    assert statistics.mean is None
    assert statistics.median is None
    assert statistics.variance is None
    assert statistics.standard_deviation is None
