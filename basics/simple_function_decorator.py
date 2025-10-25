def simple_decorator(func):
    def wrapper():
        print("1. Before the function runs")
        func()
        print("2. After the function runs")

    return wrapper


@simple_decorator
def greet():
    print("Hello, Python Decorators!")


if __name__ == "__main__":
    greet()
