__author__ = "Mathusuthan N Kannan"
__email__ = "mathkann@gmail.com"
__copyright__ = "Copyright 2015, Mathusuthan N Kannan"
__license__ = "The MIT License (MIT)"

# Example 1
from random import randint
random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
print(bin(random_bits))


# Loop over the list using the sequence
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)


# Iterate over the list and also print index
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))


# enumerate wraps any iterator with a lazy generator. This generator yields pairs of the loop index and the
# next value from the iterator.
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))


# Can also specify the starting value of index ... this makes it much neater
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))
