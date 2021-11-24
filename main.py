"""Shapes."""

from math import pi
import os
import sys
import yaml


class Circle:
    def __init__(self, radius, fill="red", stroke="black", at=(0,0)):
        self._radius = radius
        self._fill = fill
        self._stroke = stroke
        self._at = at

    def __str__(self):
        return f"Instance of {self.__class__.__qualname__}"

    def calculate_area(self):
        return pi * self._radius ** 2

    @property
    def radius(self):
        return self._radius

    def to_yaml(self):
        yaml_structure = (
            "circle:\n"
            "    at: !!python/tuple\n"
            f"        - {self._at[0]}\n"
            f"        - {self._at[1]}\n"
            f"    fill: {self._fill}\n"
            f"    radius: {self._radius}\n"
            f"    stroke: {self._stroke}\n"
            )
        return yaml_structure

    @classmethod
    def from_yaml(cls, string):
        circle_dict = yaml.load(string, Loader=yaml.Loader)["circle"]
        obj = cls(**circle_dict)
        return obj



class Quadrilateral:
    def __init__(self, width, height, stroke="black", fill="white"):
        self._width = width
        self._height = height
        self._stroke = stroke
        self._fill = fill

    def __str__(self):
        return f"Quadrilateral of width {self._width} and height {self._height}"

    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2*self._width + 2*self._height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self.calculate_area()

    @property
    def perimeter(self):
        return self.calculate_perimeter()


class Canvas:
    def __init__(self, width, height, bkgd_color="white"):
        self._width = width
        self._height = height
        self._bkgd_color = bkgd_color

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def bkgd_color(self):
        return self._bkgd_color


class Text:
    def __init__(self, text, color="black", size=20, font="Arial"):
        self._text = text
        self._color = color
        self._size = size
        self._font = font

    @property
    def text(self):
        return self._text

    @property
    def color(self):
        return self._color

    @property
    def size(self):
        return self._size

    @property
    def font(self):
        return self._font


def main():
    circle = Circle(5.0, fill="orange", stroke="red")
    yaml_circle = circle.to_yaml()
    loaded_circle = Circle.from_yaml(yaml_circle)
    print(loaded_circle)
    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
