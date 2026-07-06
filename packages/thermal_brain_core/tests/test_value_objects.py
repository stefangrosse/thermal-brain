import pytest
from thermal_brain_core.value_objects import Temperature, Percentage

def test_temperature():
    t=Temperature(value=21.5)
    assert t.value==21.5

def test_percentage():
    assert Percentage(value=42).value==42

def test_percentage_invalid():
    with pytest.raises(ValueError):
        Percentage(value=120)
