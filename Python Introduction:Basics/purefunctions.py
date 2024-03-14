# map, filter, zip, reduce

my_list = [1,2,3]
your_list = [1,2,3,4,5]

def multiply_by2(item):
    return item * 2 

def check_odd(item):
    return item % 2 != 0

# here, map takes in an action function and a list of arguments in which the action is performed one after other
# we can have the function above take in a list and return a list but this makes it much neater
print(list(map(multiply_by2, my_list)))

# here, filter also takes in a function that checks on an item and filters out required items from an iterable
print(list(filter(check_odd, your_list)))

# here, zip takes in a number of iterables and returns a tuple of values at same index
# the no of return is equal to the lowest index in the iterables sent 
# Let's say one list has usernames, second list has passwords, third list has age, and so on
# zip can be a great way to combine it all and have one tuple per user returned 
print(list(zip(my_list, your_list)))


# Using lambda expressions now:
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: (item%2 != 0), your_list)))


# to use reduce, we need to import it first 
from functools import reduce
# using lambda here again 
print(reduce(lambda acc, item: acc+item, my_list))

# normally, you will do as follows
def accumulator(acc, item):
    print(acc, item)
    return acc + item

# reduce reduces the given list to a single value using the accumulator function
# here, the third parameter is the acc value to initialize the accumulator
print(reduce(accumulator, my_list, 0))


# lambda to give squares 
print(list(map(lambda item: item**2, my_list)))

# use lambda expression to sort this list based off of second item in the tuple 
list_3 = [(0,2), (4,3), (9,9), (10,-1)]
list_3.sort(key=lambda x: x[1])
print(list_3)


# List comprehension 

# Gives [0,1,2,3,4]
list_5 = [a for a in range(5)]
print(list_5) 

# now, let's say if we only want even numbers 
list_6 = [a for a in range(5) if a % 2 == 0]
print(list_6)

# Set Comprehension --> Similar to list comprehension

# Gives [0,1,2,3,4]
set_5 = {a for a in range(5)}
print(set_5) 

# now, let's say if we only want even numbers 
set_6 = {a for a in range(5) if a % 2 == 0}
print(set_6)

# Dictionary Comprehension 

dict_5 = {key:key**2 for key in range(5)}
print(dict_5)


# Exercise
# Find duplicates in a list and return the list of duplicates 
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicate_list = list(set([item for item in some_list if some_list.count(item) > 1]))

print(duplicate_list)