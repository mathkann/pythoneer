__author__ = "Mathusuthan N Kannan"
__email__ = "mathkann@gmail.com"
__copyright__ = "Copyright 2015, Mathusuthan N Kannan"
__license__ = "The MIT License (MIT)"

import logging

# Python has special syntax for the stride of a slice in the form somelist[start:end:stride]. This lets you take
# every nth item when slicing a sequence. For example, the stride makes it easy to group by even and odd
# indexes in a list.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Odd ::', a[::2])
print('Even ::', a[1::2])

# The problem is that the stride syntax often causes unexpected behavior that can introduce bugs.
# For example, a common Python trick for reversing a byte string is to slice the string with a stride of -1.

x = b'mongoose'
y = x[::-1]
print(y)

# But this fails with Unicode characters encoded as UTF-8
try:
    w = '??'
    x = w.encode('utf-8')
    y = x[::-1]
    z = y.decode('utf-8')
except UnicodeDecodeError:
    logging.exception('Expected')
else:
    assert False

# Are negative strides besides -1 useful ?

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])   # ['a', 'c', 'e', 'g']
print(a[::-2])  # ['h', 'f', 'd', 'b']

print(a[2::2])    # ['c', 'e', 'g']
print(a[-2::-2])   # ['g', 'e', 'c', 'a']
print(a[-2:2:-2])  # ['g', 'e']
print(a[2:2:-2])   # []

# The point is that the stride part of the slicing syntax can be extremely confusing. Having three numbers
# within the brackets is hard enough to read because of its density. Then it's not obvious when the start and
# end indexes come into effect relative to the stride value, especially when stride is negative.
#
# To prevent problems, avoid using stride along with start and end indexes. If you must use a stride, prefer
# making it a positive value and omit start and end indexes. If you must use stride with start or end indexes,
# consider using one assignment to stride and another to slice.
