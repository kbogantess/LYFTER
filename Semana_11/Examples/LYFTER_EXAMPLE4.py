class Car:
    wheelNumber = 0
    gas_type = "Diesel"

    def CarHistory(self, miles, crashes):
        print (f"The car has {miles} miles and {crashes} crashes and {self.wheelNumber} wheels") #Este self es como decir my_car.wheel_number
    
    def upgrade_engine(self):
        if self.gas_type == "Diesel":
            print("Cambiando Diesel por Super")
            self.gas_type = "Super"
            
        else:
            print("El carro ya tiene Super")

"""my_car = Car()
my_car.wheelNumber = 4

my_truck = Car()
my_truck.wheelNumber =6

my_bigger_truck = Car()
my_bigger_truck.wheelNumber = 8


my_car.CarHistory(1000, 4)
my_truck.CarHistory(2000, 2)
my_bigger_truck.CarHistory(500, 1)"""

print("Primer carro")
my_car_1 = Car()
print(my_car_1.gas_type)

my_car_1.upgrade_engine()

print("Auto al mejorarse: ")
print(my_car_1.gas_type)