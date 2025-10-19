# Geometry Library

Библиотека для вычисления площадей фигур.

## Возможности
- Площадь круга по радиусу
- Площадь треугольника по трём сторонам
- Проверка, является ли треугольник прямоугольным
- Полиморфизм: вычисление площади без знания типа фигуры

## Установка
```bash
git clone https://github.com/Antirry/Test_Geometry_Mindbox.git
cd geometry-figures
pip install -e .[dev]
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

## Расположение папок проекта

```py
geometry-figures/
│
├── geometry/
│   ├── __init__.py
│   ├── base.py          # Абстрактный класс Figure
│   ├── circle.py        # Класс Circle
│   ├── triangle.py      # Класс Triangle
│
├── tests/
│   ├── test_circle.py
│   ├── test_triangle.py
│
├── setup.py             # Для установки как пакета
└── README.md
```