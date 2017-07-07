'''
15-9. Match the set of the string representations of all Python floats.
'''

import re

def is_float(text):
    m = re.match(r'[-+]?(\d)*(\.\d+)?([eE][-+]?\d+)?', text)
    return (m is not None) and (m.group() == text)

assert is_float('0')
assert is_float('100')
assert is_float('-100')
assert is_float('+1')
assert is_float('0.1')
assert is_float('.1')
assert is_float('0.13')
assert is_float('1e3')
assert is_float('1e-3')
assert is_float('1.1e-3')
assert is_float('-1.1e-3')
