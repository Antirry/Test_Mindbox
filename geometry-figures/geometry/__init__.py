"""
Geometry Library
================

Библиотека для вычисления площадей фигур:
- Круг (Circle)
- Треугольник (Triangle)

Пример использования:
---------------------
from geometry import Circle, Triangle

c = Circle(5)
print(c.area())

t = Triangle(3, 4, 5)
print(t.area(), t.is_right())
"""

from .circle import Circle
from .triangle import Triangle

__all__ = ["Circle", "Triangle"]
__version__ = "0.1.0"
