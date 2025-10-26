from functools import wraps
from time import perf_counter

class TimeIt:
    def __init__(self, label="timeit"):
        self.label = label

    def  __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                end = perf_counter()
                duration = (end - start) * 1000
                print(f"[{self.label}]: {func.__name__} took {duration: .2f} ms")
        return wrapper
    

@TimeIt("range_sum_timer")
def work(n):
    return sum(range(n))


if __name__ == "__main__":
    print(work(200_000))