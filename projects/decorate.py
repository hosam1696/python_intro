"""
Decorators:
modify or enhance functions without changing their defintion
in python a decorator is a callable object
and return a callable
"""


def decorate1(w):
    def wrap(*args, **kwargs):
        x = w(*args, **kwargs)
        return ascii(x)
    return wrap



@decorate1
def func1():
    return 'Hosam يحب Menna'


print(func1())