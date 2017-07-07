import re

expr = re.compile(r'(b|h)(a|i|u)t')

def assert_match(text):
    assert expr.match(text).group() == text

assert_match('bat')
assert_match('bit')
assert_match('but')
assert_match('hat')
assert_match('hit')
assert_match('hut')

assert expr.match('hot') is None
assert expr.match('not') is None
assert expr.match('BAT') is None
assert expr.match('Batbat') is None