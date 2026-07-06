from enum import StrEnum
from .base import Measurement

class EnergyUnit(StrEnum):
    KWH="kWh"

class Energy(Measurement):
    unit: EnergyUnit = EnergyUnit.KWH
