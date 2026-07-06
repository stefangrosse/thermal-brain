from thermal_brain_core.domain.zone import Zone
from thermal_brain_core.value_objects import Identifier, Temperature

def test_zone():
    z=Zone(id=Identifier(),name="Living",target_temperature=Temperature(value=22))
    assert z.target_temperature.value==22
