# polymorphism_demo.py
import math

class Shape:
    """Base class for shapes."""
    def area(self):
        """Raises an error if not overridden in a derived class."""
        raise NotImplementedError("The area() method must be overridden by subclasses.")

class Rectangle(Shape):
    """Derived class for a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Derived class for a circle."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return math.pi * (self.radius ** 2)
