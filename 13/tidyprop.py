class HideX(object):
	# def x():
	# 	def fget(self):
	# 		return ~self.__x
	# 	def fset(self, x):
	# 		assert isinstance(x, int), 'x must be int'
	# 		self.__x = ~x
	# 	return locals()
	# x = property(**x())

	@property
	def x(self):
		return ~self.__x
	@x.setter
	def x(self, x):
		assert isinstance(x, int), 'x must be int'
		self.__x = ~x

o = HideX()
o.x = 5
print(o.x)
print(o._HideX__x)