from functools import wraps

def prefix(msg):
    """ Decorator factory that prints a prefix before the function call. """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{msg}: calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefix("INFO")
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print(multiply(3, 4))