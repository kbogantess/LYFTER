""""

class Auto:
    def __init__(self,marca):
        self.__marca = marca #Privado

    def __acelerar(self):
        print("acelerando...")

"""

class Auto:
    
    def __init__(self, marca, modelo, año):

        self.__marca = marca
        self.__modelo = modelo
        self.año = año

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def __acelerar(self):
        print("Acelerando...")

#######################################################

mi_auto = Auto("Citroen", "C4", 2016)

mi_auto._Auto__acelerar() #(_NOMBRE DE CLASE)

print(mi_auto.año)
#print(mi_auto.__marca) #ERROR

print(f"La marca del carro es {mi_auto.get_marca()}")

mi_auto.set_marca("Audi")

print(f"La marca del carro es {mi_auto.get_marca()}")

