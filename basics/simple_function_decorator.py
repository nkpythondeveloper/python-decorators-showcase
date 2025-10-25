def simple_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")

    return wrapper


@simple_decorator
def greet():
    print("Hello, Python Decorators!")


if __name__ == "__main__":
    greet()
