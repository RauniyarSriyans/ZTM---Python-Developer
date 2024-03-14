# printing upto n^th fibonacci number using generator 
# doesn't store any previous data or list of fib numbers 

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)