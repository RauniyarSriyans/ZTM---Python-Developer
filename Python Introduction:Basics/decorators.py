# A higher order function is a function that either takes a function as an argument or
# returns a function. Examples are map, reduce, filter, zip because each of these take a function as argument


# this is a decorator we created
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')
    return wrap_func

@my_decorator
def hello(greeting):
    print(greeting)

@my_decorator
def bye(greeting):
    print(greeting)

hello('hi')
bye('bye')

# ----------------------------------------------------------------------

# Performance Decorator 
from time import time 

def perf_decorator(func):
    def wrap_func(*args, **kwargs):
        time1 = time()
        result = func(*args, **kwargs)
        time2 = time()
        print(f'It took {time2 - time1} ms')
        return result
    return wrap_func

@perf_decorator
def long_time():
    for i in range(100000000):
        i*5

long_time()


# ----------------------------------------------------------------------------------------------------------------------
# let's say we have an autheticating decorator or login decorator. 
# a user can access certain function only if they are autheticated or logged in. Pretty powerful, right?


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrap(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")
    
    return wrap

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)