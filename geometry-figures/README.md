# Geometry Library

Библиотека для вычисления площадей фигур.

## Возможности
- Площадь круга по радиусу
- Площадь треугольника по трём сторонам
- Проверка, является ли треугольник прямоугольным
- Полиморфизм: вычисление площади без знания типа фигуры

## Установка
```bash
git clone https://github.com/Antirry/Test_Mindbox.git
cd Test_Mindbox
cd geometry-figures
pip install -e .[dev]
pytest -s
python run/file.py
```

## Пример использования
```py
# file.py
from geometry import Circle, Triangle

c = Circle(5)
print("Circle area:", c.area())

t = Triangle(3, 4, 5)
print("Triangle area:", t.area())
print("Is right triangle?", t.is_right())
```
