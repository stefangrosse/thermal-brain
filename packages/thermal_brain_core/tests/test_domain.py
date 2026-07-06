from thermal_brain_core.domain import Building

def test_building():
    b=Building(id="house",name="My House",construction_year=1954)
    assert b.id=="house"
    assert b.construction_year==1954
