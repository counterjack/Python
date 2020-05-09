#!/usr/bin/python3
import abc


class Shape:
    def __init__(self, *args, **kwargs):
        print (f"An object of {self.__class__.__name__} class is created")

    @abc.abstractmethod
    def draw(self):
        pass


class Triangle(Shape):

    def draw(self):
        print ("Im called")
        pass


class Square(Shape):

    def draw(self):
        print("Im called")
        pass


class ShapeFactory:

    def __init__(self):
        self.shapes = {}

    def register(self, shape_name:str, shape_class: Shape):
        self.shapes[shape_name] = shape_class

    def get_shape(self, shape_name):
        if shape_name in self.shapes:
            return self.shapes[shape_name]()
        raise Exception("Invalid Shape")


shape_factory = ShapeFactory()

shape_factory.register(**{"shape_name": "Square", "shape_class": Square})
shape_factory.register(**{"shape_name": "Triangle", "shape_class": Triangle})

square = shape_factory.get_shape("Square")
triangle = shape_factory.get_shape("Triangle")
# hexagonal = shape_factory.get_shape("Hexagonal")

square.draw()

