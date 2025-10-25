def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello again!")


if __name__ == "__main__":
    say_hello()
