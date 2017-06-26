class ReqStr(type):
	def __new__(cls, name, bases, attrd):
		print('***Init ReqStr')
		# super().__init__(cls, bases, attrd)
		if '__str__' not in attrd:
			raise TypeError('__str__() is required')

print('***Defined ReqStr')

class C1(object, metaclass=ReqStr):
	def __init__(self):
		print('***Init C1')

	def __str__(self):
		return self.__class__.__name__

print('***Defined C1')

class C2(object, metaclass=ReqStr):
	def __init__(self):
		print('***Init C2')


print('***Defined C2')

c1 = C1()
c2 = C2()