from functools import wraps
from time import sleep

def retry(tries=3, delay=1.0, exceptions=(Exception, )):
    """ A retry function up to 'tries' times with a 'delay' 
    between attempts. 'exceptions' controls which errors
    trigger a retry.
    """
    if tries < 1:
        raise ValueError("tries must me greater than 1")
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < tries:
                        sleep(delay)
            raise last_exception
        return wrapper
    return decorator


if __name__ == "__main__":
    counter = {"n": 0}
    @retry(tries=3, delay=2.0, exceptions=(RuntimeError,))
    def flaky():
        counter["n"] += 1
        if counter["n"] < 3:
            print("failing...")
            raise RuntimeError("Temporary failure!")
        print("success!")
        return 42
    
    print(flaky())