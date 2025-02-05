
def log_params_and_return(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} w args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} return: {result}")
        return result
    return wrapper

@log_params_and_return
def subtract(x, y):
    return x - y


subtract(10, 4)  


