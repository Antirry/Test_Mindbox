from geometry import Circle, Triangle

if __name__ == "__main__":
    c = Circle(5)
    print("Circle area:", c.area())

    t = Triangle(3, 4, 5)
    print("Triangle area:", t.area())
    print("Is right triangle?", t.is_right())
