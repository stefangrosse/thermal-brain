from enum import StrEnum
from .base import Measurement

class PowerUnit(StrEnum):
    KW="kW"

class Power(Measurement):
    unit: PowerUnit = PowerUnit.KW
