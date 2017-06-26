class DevNull(object):
	def __get__(self, obj, typ=None):
		print('get', obj)
		pass
	def __set__(self, obj, val):
		print('set', obj, val)
		pass

class C1(object):
	foo = DevNull()
c1 = C1()
c1.foo = 'bar'
print(c1.foo)