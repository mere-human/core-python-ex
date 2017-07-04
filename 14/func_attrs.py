# inspired by example from PEP 232
def foo():
    return True

def bar():
    'bar() does not do much'
    return True

foo.__doc__ = 'foo() does not do much'
foo.tester = '''
if foo():
    print('PASSED')
else:
    print('FAILED')
'''

for attr in dir():
    obj = eval(attr)
    if isinstance(obj, type(foo)):
        if hasattr(obj, '__doc__'):
            print('Function %s has a doc:\n %s' % (attr, obj.__doc__))
        if hasattr(obj, 'tester'):
            print('Function %s has a tester... executing' % attr)
            exec(obj.tester)
        else:
            print('Function %s has no tester... skipping' % attr)
    else:
        print('%s is not a function' % attr)