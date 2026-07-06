from enum import StrEnum
from typing import TypeAlias

from thermal_brain_core.value_objects import Energy, Percentage, Power, Temperature


class ObservationQuantity(StrEnum):
    TEMPERATURE = "temperature"
    POWER = "power"
    ENERGY = "energy"
    PERCENTAGE = "percentage"


ObservationValue: TypeAlias = Temperature | Power | Energy | Percentage


def quantity_for_value(value: ObservationValue) -> ObservationQuantity:
    if isinstance(value, Temperature):
        return ObservationQuantity.TEMPERATURE
    if isinstance(value, Power):
        return ObservationQuantity.POWER
    if isinstance(value, Energy):
        return ObservationQuantity.ENERGY
    if isinstance(value, Percentage):
        return ObservationQuantity.PERCENTAGE
    raise TypeError(f"Unsupported observation value type: {type(value)!r}")


def supported_units_for_quantity(quantity: ObservationQuantity) -> frozenset[str]:
    units = {
        ObservationQuantity.TEMPERATURE: frozenset({"°C"}),
        ObservationQuantity.POWER: frozenset({"kW"}),
        ObservationQuantity.ENERGY: frozenset({"kWh"}),
        ObservationQuantity.PERCENTAGE: frozenset({"%"}),
    }
    return units[quantity]
