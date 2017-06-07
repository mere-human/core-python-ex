from time import ctime, sleep

def tsfunc(func):
	'''
	Decorator that displays a timestamp
	'''
	def wrappedFunc(): # inner function
		print('[%s] %s() called' % (ctime(), func.__name__))
		return func() # call target function	
	return wrappedFunc

@tsfunc
def foo(): pass

foo()
sleep(4)

for i in range(2):
	sleep(1)
	foo()