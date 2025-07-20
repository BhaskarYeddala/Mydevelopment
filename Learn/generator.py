"""
Generator :
----------
Generating the value on demand 

A generator in python is a special type of function that produces one value at a time, on demand, rather than 
returning all values at once

Key features of generators:
---------------------------
Generator uses the yield keyword to retrun a value and saves its state i.e generator "remembers" where it left off
(using a special state machine) between successive calls, making it memory efficient.

only the current value (and its state) is kept in memory, not the whole list of values.
Returns a generator object, which can be iterated using for loop or next().

"""

def my_generator():
    yield 2
    yield 4
    yield 5

gen = my_generator()
print(next(gen))
print(next(gen))

"""
Feature        | Normal Collection           | Generator
Memory Usage   | High(Stores all items)      | Low(Yields items one by one)
Speed(Creation)| Slower(allocates full list) | Faster(No pre-allocation)
iteration      | Faster(stored in memory)    | Slightly slower(on-demand generation)
Best use case  | Small datasets(Web scraping and crawling) | Large datasets/Streaming data

"""
# Generators Vs Normal Collections with respect to performance and memory

