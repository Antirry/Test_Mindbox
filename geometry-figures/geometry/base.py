from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Абстрактный базовый класс для всех геометрических фигур.
    Каждая фигура должна реализовать метод area().
    """

    @abstractmethod
    def area(self) -> float:
        """
        Вычисляет площадь фигуры.
        Должен быть реализован в подклассах.
        """
        pass

