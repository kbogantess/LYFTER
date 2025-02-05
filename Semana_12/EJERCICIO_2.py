from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass


#each one requires area and perimeter


#CLASS CIRCLE
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return (2*self.radius*math.pi)
    
    def calculate_area(self):
        return (math.pi*self.radius*self.radius)

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return (4*self.side)
    
    def calculate_area(self):
        return (self.side*self.side)



class Rectangle(Shape):

    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return (2*self.width + 2*self.height)
    
    def calculate_area(self):
        return (self.width * self.height)



print ("Circle values ")
print()
radius = float(input("Enter circle radius: "))
circle = Circle(radius)
print(f"Perímetro del círculo: {circle.calculate_perimeter():.2f}")
print(f"Área del círculo: {circle.calculate_area():.2f}")
print()
print ("Square values: ")
print()
side = float(input("Enter square side lenght: "))
square = Square(side)
print(f"Perímetro del cuadrado: {square.calculate_perimeter()}")
print(f"Área del cuadrado: {square.calculate_area()}")
print()
print("Enter rectangle values")
width = float(input("Enter rectangle width: "))
height = float(input("Enter rectangle height: "))
rectangle = Rectangle(width, height)
print(f"Perímetro del rectángulo: {rectangle.calculate_perimeter()}")
print(f"Área del rectángulo: {rectangle.calculate_area()}")
