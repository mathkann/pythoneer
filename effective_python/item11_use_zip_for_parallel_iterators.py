__author__ = "Mathusuthan N Kannan"
__email__ = "mathkann@gmail.com"
__copyright__ = "Copyright 2015, Mathusuthan N Kannan"
__license__ = "The MIT License (MIT)"

names = ['Anupama' 'Anuradha', 'Anuprema']
letters = [len(n) for n in names]

# the items in derived list letters are related to the items in the source list by their indices
# to loop over both lists in parallel, we can use zip function in Python 3

longest_name = None
max_letters = 0

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

# Note: If you want to zip very large iterators in Python 2, use the izip from the itertools built-in module.
# In Python 3, zip is a lazy generator that produces tuples.
# In Python 2, zip returns the full result as a list of tuples.

# An issue is that issue is that zip behaves strangely if the input iterators are of different lengths. For example,
# if we add another name to the list above but forget to update the letter counts. Running zip on the two input lists
# will not print the newly added name

names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)

# Note : zip always assumes equal length lists. If we are not sure about the length of our lists, use the zip_longest
# function from the itertools built-in module instead
