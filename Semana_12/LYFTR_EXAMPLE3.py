#Clases abstractas


from abc import ABC, abstractmethod


class Animal(ABC):
	def breath(self):
		pass

	def born(self):
		pass

	def reproduce(self):
		# Todas las especies de animales deben reproducirse para sobrevivir
		# Pero lo pueden hacer de distintas maneras
		pass

class AsexualAnimal(Animal):
	def reproduce(self):
		print("Reproducing in an asexual manner")

class SexualAnimal(Animal):
	def reproduce(self, mate):
		print(f"Reproducing in a sexual manner with {mate}")

class OtherAnimal(Animal):
	pass


asexual_animal = AsexualAnimal()
asexual_animal.reproduce() # -> Reproducing in an asexual manner 

sexual_animal_a = SexualAnimal()
sexual_animal_b = SexualAnimal()
#sexual_animal.reproduce(sexual_animal_b) # -> Reproducing in a sexual manner with sexual_animal_b

animal = Animal() # va a fallar porque Animal es una clase abstracta
other_animal = OtherAnimal() # va a fallar porque no se sobre-escribió el método reproduce