"""2. Cree una clase de `Bus` con:
    1. Un atributo de `max_passengers`.
    2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
    3. Un método para bajar pasajeros uno por uno (en cualquier orden)."""

class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, current_passengers):
        self.max_passengers = 20
        self.passengers = []

        if current_passengers > self.max_passengers:
            print("The bus is full")
            current_passengers = self.max_passengers
        else:
            print(f"You can add {self.max_passengers - current_passengers} more passengers")

        for i in range(current_passengers):
            self.passengers.append(Person(f"Passenger {i+1}"))

    def add_passenger(self):
        if len(self.passengers) < self.max_passengers:
            new_passenger = Person(f"Passenger {len(self.passengers) + 1}")
            self.passengers.append(new_passenger)
            print(f"{new_passenger.name} added. There are now {len(self.passengers)} passengers on the bus")
        else:
            print("The bus is full. No more passengers allowed")

    def take_out_passenger(self):
        if self.passengers:
            removed_person = self.passengers.pop()
            print(f"{removed_person.name} removed. There are now {len(self.passengers)} passengers on the bus.")
        else:
            print("The bus is empty. No passengers to remove")

    def menu(self):
        while True:
            menu = int(input("""

Select a menu option:

(1) --> Add passenger
(2) --> Remove passenger
(3) --> Exit program
"""))
            if menu == 1:
                self.add_passenger()
            elif menu == 2:
                self.take_out_passenger()
            elif menu == 3:
                print("Ending actions")
                break
            else:
                print("Invalid option. Please try again")

#####################################################################################

current_passengers = int(input("Enter the current number of passengers (maximum 20): "))

bus = Bus(current_passengers)
bus.menu()
