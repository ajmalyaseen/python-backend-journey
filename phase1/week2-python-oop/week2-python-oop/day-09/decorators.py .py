import time 
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        before=time.time()
        func(*args,**kwargs)
        after=time.time()
        excution_time=after-before
        print(f"{excution_time:.4f}")
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello {name}!")

say_hello(name="Ajmal")

print(say_hello.__name__)