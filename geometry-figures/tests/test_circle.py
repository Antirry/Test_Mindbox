import math
import pytest
from geometry.circle import Circle


def test_circle_area():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi)


def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)


