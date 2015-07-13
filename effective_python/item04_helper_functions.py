__author__ = "Mathusuthan N Kannan"
__email__ = "mathkann@gmail.com"
__copyright__ = "Copyright 2015, Mathusuthan N Kannan"
__license__ = "The MIT License (MIT)"

# Python's syntax makes it all too easy to write single-line expressions that are overly complicated and
# difficult to read.Move complex expressions into helper functions, especially if you need to use the same logic
# repeatedly.
# The if/else expression provides a more readable alternative to using Boolean operators like
# or / and in expressions.

# Example 1
from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                     keep_blank_values=True)
print(repr(my_values))


# Example 2
print('Red:     ', my_values.get('red'))
print('Green:   ', my_values.get('green'))
print('Opacity: ', my_values.get('opacity'))


# Example 3 - don't do this
# For query string 'red=5&blue=0&green='
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)


# Example 4 - don't do this
red = int(my_values.get('red', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)


# Example 5 - <true> if  <cond> else <false> is way better
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0
green = my_values.get('green', [''])
green = int(green[0]) if green[0] else 0
opacity = my_values.get('opacity', [''])
opacity = int(opacity[0]) if opacity[0] else 0
print('Red:     %r' % red)
print('Green:   %r' % green)
print('Opacity: %r' % opacity)


# Example 6
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0
print('Green:   %r' % green)


# Example 7 - The right way
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


# Example 8
green = get_first_int(my_values, 'green')
print('Green:   %r' % green)
