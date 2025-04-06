from abc import ABC, abstractmethod
import math


class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass


class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Circle(Element):
    def __init__(self, radius: float):
        self.radius = radius

    def accept(self, visitor: Visitor):
        visitor.visit_circle(self)


class Rectangle(Element):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def accept(self, visitor: Visitor):
        visitor.visit_rectangle(self)


class AreaCalculator(Visitor):
    def visit_circle(self, circle: Circle):
        area = math.pi * circle.radius ** 2
        print(f"Circle Area: {area}")

    def visit_rectangle(self, rectangle: Rectangle):
        area = rectangle.width * rectangle.height
        print(f"Rectangle Area: {area}")


class PerimeterCalculator(Visitor):
    def visit_circle(self, circle: Circle):
        perimeter = 2 * math.pi * circle.radius
        print(f"Circle Perimeter: {perimeter}")

    def visit_rectangle(self, rectangle: Rectangle):
        perimeter = 2 * (rectangle.width + rectangle.height)
        print(f"Rectangle Perimeter: {perimeter}")


circle = Circle(5)
rectangle = Rectangle(4, 6)
area_visitor = AreaCalculator()
perimeter_visitor = PerimeterCalculator()
circle.accept(area_visitor)
rectangle.accept(area_visitor)
circle.accept(perimeter_visitor)
rectangle.accept(perimeter_visitor)
