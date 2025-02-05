class HandToHandCombat:

    def __init__(self, name):
        self.name = name

    def fight(self):
        print(f"{self.name} está luchando cuerpo a cuerpo")


class Flight:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} está volando")


class Superhero(HandToHandCombat, Flight):
    def __init__(self, name):
        HandToHandCombat.__init__(self, name)
        Flight.__init__(self, name)

    def use_powers(self):
        print(f"{self.name} está usando sus poderes")
        self.fight()  
        self.fly()   


iron_man = Superhero("Iron Man")


iron_man.use_powers()
