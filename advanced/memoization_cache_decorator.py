from functools import wraps, lru_cache
import time

def memoize(func):
    """ Very small memoizing decorator for call-by-value use cases. """
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def slow_add(a, b):
    print("computing slow_add..")
    time.sleep(5)
    return a + b

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(slow_add(2, 3)) # first time will compute
    print(slow_add(2, 3)) # now will read the memonize cache, and get result from there

    print(fib(30))
    print(fib.cache_info())