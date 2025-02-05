
def ensure_numbers(func):
    def wrapper(*args, **kwargs):
        
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise TypeError("All parameters should be numbers")
        
        if not all(isinstance(value, (int, float)) for value in kwargs.values()):
            raise TypeError("All parameters should be numbers")
        return func(*args, **kwargs)
    return wrapper

@ensure_numbers
def dividir(a, b):
    if b == 0:
        raise ValueError("Cant use 0")
    return a / b


try:
    print(dividir(10, 2))  

except Exception as e:
    print(f"Error: {e}")
