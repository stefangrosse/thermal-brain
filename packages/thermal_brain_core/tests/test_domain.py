from thermal_brain_core.domain import Building, Zone

def test_building():
    b=Building(name="House",zones=[Zone(id="eg",name="Ground Floor")])
    assert b.name=="House"
    assert len(b.zones)==1
