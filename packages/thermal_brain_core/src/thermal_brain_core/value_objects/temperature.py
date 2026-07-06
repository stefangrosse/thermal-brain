from enum import StrEnum
from .base import Measurement

class TemperatureUnit(StrEnum):
    CELSIUS="°C"

class Temperature(Measurement):
    unit: TemperatureUnit = TemperatureUnit.CELSIUS
