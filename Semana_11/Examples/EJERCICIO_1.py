"""1. Cree una clase de `Circle` con:
    1. Un atributo de `radius` (radio).
    2. Un método de `get_area` que retorne su área."""


import math

class Circle:
    pass

    def __init__ (self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)
    
circle_radius = Circle(5)

print(f"El radio del circulo es de {circle_radius.radius} y el área es {circle_radius.get_area()}")





"""class Person():
    def __init__(self, name):
        print (f"Ha nacido una persona llamada {name}")
        self.name = name
        self.age = 0

person_1 = Person("Kev")


print(person_1.name)
print(person_1.age)"""



