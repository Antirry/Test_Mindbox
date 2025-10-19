import math
import pytest
from geometry.triangle import Triangle

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)

def test_triangle_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()

def test_triangle_invalid():
    try:
        Triangle(1, 2, 10)
        assert False, "Ожидалось исключение"
    except ValueError:
        assert True
