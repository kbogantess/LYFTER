class Car:
    wheelNumber = 4

    def CarHistory(self, miles, crashes):
        print (f"The car has {miles} miles and {crashes} crashes and {self.wheelNumber} wheels") #Este self es como decir my_car.wheel_number

my_car = Car()
my_car.CarHistory(1000, 4)