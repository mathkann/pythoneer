__author__ = "Mathusuthan N Kannan"
__email__ = "mathkann@gmail.com"
__copyright__ = "Copyright 2015, Mathusuthan N Kannan"
__license__ = "The MIT License (MIT)"


# Python includes syntax for slicing sequences into pieces. Slicing lets you access a subset of a sequence's
# items with minimal effort. The simplest uses for slicing are the built-in types list, str, and bytes.
# Slicing can be extended to any Python class that implements the __getitem__ and __setitem__  methods

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four:', a[:-4])
print('Middle two:', a[3:-3])

# When slicing from the start of a list, you should leave out the zero index to reduce visual noise.
assert a[:5] == a[0:5]

# When slicing to the end of a list, you should leave out the final index because it's redundant.
assert a[5:] == a[5:len(a)]

# Slicing deals properly with start and end indexes that are beyond the boundaries of the list. That makes it
# easy for your code to establish a maximum length to consider for an input sequence.
first_twenty_items = a[:20]
last_twenty_items = a[-20:]

# The result of slicing a list is a whole new list. References to the objects from the original list
# are maintained. Modifying the result of slicing won't affect the original list.
b = a[4:]
print('Before:   ', b)
b[1] = 99
print('After:    ', b)
print('No change:', a)

# When used in assignments, slices will replace the specified range in the original list. Unlike tuple 
# assignments (like a, b = c[:2]), the length of slice assignments don't need to be the same. The values 
# before and after the assigned slice will be preserved. The list will grow or shrink to accommodate the 
# new values.
b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b           # Still the same list object
print('After ', a)      # Now has different contents
