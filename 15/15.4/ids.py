'''
15-4. match the set of all valid Python identifiers
'''

import re
import keyword

# NOTE: there is a method str.isidentifier()
def is_id(text):
    if keyword.iskeyword(text): return False
    m = re.match(r'[A-Za-z_]+[A-Za-z0-9_]*', text)
    return (m is not None) and (m.group() == text)

assert is_id('a')
assert is_id('a0')
assert is_id('a_0')
assert is_id('_a')
assert is_id('_0')
assert is_id('_ab0')
assert is_id('__data')
assert not is_id('0')
assert not is_id('0a')
assert not is_id('0_a')
assert not is_id('')
assert not is_id(' ')
assert not is_id('\t')