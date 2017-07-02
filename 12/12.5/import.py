'''
12-5. Using __import__().
a. Use __import__() to import a module into your namespace. What is the correct
syntax you finally used to get it working?
b. Same as above, but use __import__() to import only specific names from
modules.
'''

sys = __import__('sys')
print(repr(sys))

_os = __import__(name='os', fromlist=['cpu_count'])
cpu_count = _os.cpu_count
print('cpu_count', cpu_count())