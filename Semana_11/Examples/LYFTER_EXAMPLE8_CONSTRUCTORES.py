class Car:
    def __init__(self, brand, line, model, color):
        self.brand = brand
        self.line = line
        self.model = model
        self.color = color


my_audi = Car("Audi", "A4", 2023, "Red")
my_bmw = Car("BMW", "X5", 2021, "Green")
my_ferrari = Car("Ferrari", "Enzo", 1999, "Blue")

print(my_audi.brand, my_audi.line, my_audi.model, my_audi.color)
