__author__ = "Mathusuthan N Kannan"
__email__ = "mathkann@gmail.com"
__copyright__ = "Copyright 2015, Mathusuthan N Kannan"
__license__ = "The MIT License (MIT)"

# The problem with list comprehensions is that they may create a whole new list containing one item for each value in
# the input sequence. This is fine for small inputs, but for large inputs this could consume significant amounts of
# memory and cause your program to crash.

# Say you want to read a file and return the number of characters on each line. Doing this with a list comprehension
# would require holding the length of every line of the file in memory. If the file is absolutely enormous or perhaps a
# never-ending network socket, list comprehensions are problematic.

import random
with open('tmp/my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')


# Here we use a list comprehension in a way that can only handle small input values.
value = [len(x) for x in open('tmp/my_file.txt')]
print(value)


# Generator expressions don't materialize the whole output sequence when they're run. Instead, generator expressions
# evaluate to an iterator that yields one item at a time from the expression.
# A generator expression is created by putting list-comprehension-like syntax between () characters.
it = (len(x) for x in open('tmp/my_file.txt'))
print(it)


# The returned iterator can be advanced one step at a time to produce the next output from the generator expression as
# needed (using the next built-in function)
print(next(it))
print(next(it))


# Another powerful outcome of generator expressions is that they can be composed together. Here, we take the iterator
# returned by the generator expression above and use it as the input for another generator expression.
roots = ((x, x**0.5) for x in it)


# Chaining generators like this executes very quickly in Python. When you're looking for a way to compose functionality
# that's operating on a large stream of input, generator expressions are the best tool for the job. The only gotcha is
# that the iterators returned by generator expressions are stateful, so be careful not to use them more than once
print(next(roots))
