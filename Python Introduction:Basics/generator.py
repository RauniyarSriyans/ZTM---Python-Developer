# generators are iterable
# every generator is an iterable but all iterable are not generators 

def generator_function(num):
    for i in range(num):
        # yield pauses the function and comes back again when we want to proceed further
        yield i

g = generator_function(100)

print(next(g))
print(next(g))
print(next(g))

# so, generators doesn't store the entire list here but only the most recent yielded value. 
# function is paused until next is called on the generator function again.
# if the range exceeds when next is called, a StopIteration error is called. 
# the difference is rather than having a list of, let's say, 10 numbers compared to a generator 
# the time it takes to run a function is almost twice or comparably more. 
# example: for i in range(100) --> which is a generator vs for i in list(range(100))