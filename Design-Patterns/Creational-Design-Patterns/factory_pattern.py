#!/usr/bin/python3
import abc
import enum
# Example 1


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


# Example 2


class VehicleEnum(enum.Enum):
    TWO_WHEELER = "Two Wheeler"
    FOUR_WHEELER = "Four Wheeler"


class Vehicle(abc.ABC):
    tyres = None

    def __init__(self, *args, **kwargs):
        pass

    def get_tyres(self):
        return self.tyres


class TwoWheeler(Vehicle):
    tyres = 2


class FourWheeler(Vehicle):
    tyres = 4


class VehicleFactory:
    _vehicles = {
        VehicleEnum.TWO_WHEELER.value: TwoWheeler,
        VehicleEnum.FOUR_WHEELER.value: FourWheeler
    }

    def __init__(self) -> None:
        pass

    def register(self, vehicle: Vehicle):
        pass

    @staticmethod
    def get_vehicle(vehicle_type: str):
        return VehicleFactory._vehicles[vehicle_type]()


four_wheeler = VehicleFactory.get_vehicle(VehicleEnum.FOUR_WHEELER.value)

print (four_wheeler.get_tyres())


