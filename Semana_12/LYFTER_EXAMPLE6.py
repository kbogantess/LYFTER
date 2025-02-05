#Polimorfismo


class Vehiculo:
  is_on: bool
  ruedas: int

  def encender(self):
    self.is_on = True
    print("Vehiculo encendida")

  def apagar(self):
    self.is_on = False

class Computadora:
  is_on: bool

  def encender(self):
    self.operative_system = "Windows"
    self.is_on = True
    print("Computadora encendida")

  def apagar(self):
    self.is_on = False


###################################################


object_list = [
	Vehiculo(),
	Vehiculo(),
	Computadora(),
	Computadora(),
]

for object in object_list:
	object.encender()