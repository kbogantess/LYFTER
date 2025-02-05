from datetime import date

# Definición de la clase User
class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )


def require_adult(func):
    def wrapper(user, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("First parameter must be an object User type")
        if user.age < 18:
            raise ValueError("The user needs to be older")
        return func(user, *args, **kwargs)
    return wrapper

# Función decorada
@require_adult
def send_offer(user):
    print(f"Offer sent to user with {user.age} years old")

# Ejecución de pruebas
youngest_user = User(date(2010, 9, 15))  
oldest_user = User(date(1995, 2, 10)) 

# Caso exitoso
send_offer(oldest_user)  # 

# Caso con excepción
try:
    send_offer(youngest_user)  
except ValueError as e:
    print(e)  # Im
