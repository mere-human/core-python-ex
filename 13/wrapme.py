class WrapMe(object):
	def __init__(self, obj):
		self.__obj = obj

	def __str__(self):
		return str(self.__obj)

	def __repr__(self):
		return repr(self.__obj)

	def get(self):
		return self.__obj

	def __getattr__(self, attr):
		return getattr(self.__obj, attr)