from time import time, ctime

class TimeWrapMe(object):
	def __init__(self, obj):
		self.__obj = obj
		self.__ctime = self.__atime = self.__mtime = time()

	def __str__(self):
		self.__atime = time()
		return str(self.__obj)

	def __repr__(self):
		self.__atime = time()
		return repr(self.__obj)

	def get(self):
		self.__atime = time()
		return self.__obj

	def set(self, obj):
		self.__obj = obj
		self.__atime = self.__mtime = time()

	def gettimestr(self, typ):
		if typ not in 'cma':
			raise TypeError('Unsupported type')
		else:
			time_val = getattr(self, '_%s__%stime' % \
				(self.__class__.__name__, typ))
			return ctime(time_val)

	def __getattr__(self, attr):
		self.__atime = time()
		return getattr(self.__obj, attr)