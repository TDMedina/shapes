"""Shapes."""

from math import pi
import os


class Circle:
    def __init__(self, radius, fill="red", stroke="black"):
        self._radius = radius
        self._fill = fill
        self._stroke = stroke

    def calculate_area(self):
        return pi * self._radius ** 2


def main():
    circle = Circle(5.0, fill="orange", stroke="red")
    print(f"area = {circle.calculate_area()}")

    circle2 = Circle(8.0)
    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
