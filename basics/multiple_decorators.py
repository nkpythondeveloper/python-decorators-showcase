def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"

    return wrapper


@bold
@italic
def greet() -> str:
    return "Hello"


if __name__ == "__main__":
    print(greet())