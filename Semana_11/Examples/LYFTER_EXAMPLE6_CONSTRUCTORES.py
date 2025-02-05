class Person():
    def __init__(self, name):
        print (f"Ha nacido una persona llamada {name}")
        self.name = name
        self.age = 0

person_1 = Person("Kev")


print(person_1.name)
print(person_1.age)