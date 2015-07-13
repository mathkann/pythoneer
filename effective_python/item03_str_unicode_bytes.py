__author__ = "Mathusuthan N Kannan"
__email__ = "mathkann@gmail.com"
__copyright__ = "Copyright 2015, Mathusuthan N Kannan"
__license__ = "The MIT License (MIT)"

# Know the difference between bytes, str, and unicode
# In Python 3, there are two types that represent sequences of characters: bytes and str.
# Instances of bytes contain raw 8-bit values. Instances of str contain Unicode characters

# There are many ways to represent Unicode characters as binary data (raw 8-bit values). The most common
# encoding is UTF-8. Importantly, str instances in Python 3 and unicode instances in Python 2 do not have an
# associated binary encoding. To convert Unicode characters to binary data, you must use the encode method.
#  To convert binary data to Unicode characters, you must use the decode method.
import logging

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of type str

print(repr(to_str(b'foo')))
print(repr(to_str('foo')))

# To convert Unicode character to binary, use the encode method

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # Instance of type bytes

print(repr(to_bytes(b'foo')))
print(repr(to_bytes('foo')))

# Example 5
try:
    import os
    with open('/tmp/random.bin', 'w') as f:
        f.write(os.urandom(10))
except:
    logging.exception('Expected')
else:
    assert False

# In Python 3, you must indicate that the data is being opened in write binary mode ('wb')
# instead of write character mode ('w').
# This problem also exists for reading data from files.
# The solution is the same: Indicate binary mode by using 'rb' instead of 'r' when opening a file.

with open('/tmp/random.bin', 'wb') as f:
    f.write(os.urandom(10))
