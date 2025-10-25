from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


@log
def add(a, b):
    """Adds two numbers."""
    return a + b


if __name__ == "__main__":
    print(add(5, 10))
    print(add.__name__)
    print(add.__doc__)