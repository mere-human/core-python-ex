class NumStr(object):
	def __init__(self, n=0, s=''):
		self.n = n
		self.s = s

	def __str__(self):
		return '[%d :: %r]' % (self.n, self.s)

	__repr__ = __str__

	def __add__(self, other):
		if isinstance(other, NumStr):
			return self.__class__(self.n + other.n, self.s + other.s)
		else:
			raise TypeError('Illegal arg for built-in operation')

	def __mul__(self, num):
		if isinstance(num, int):
			return self.__class__(self.n * num, self.s * num)
		else:
			raise TypeError('Illegal arg for built-in operation')

	def __bool__(self):
		return bool(self.n) or bool(self.s)

	def __eq__(self, other):
		return self.n == other.n and self.s == other.s

def main():
	a = NumStr(3, 'foo')
	print(a)
	b = NumStr(3, 'goo')
	print(b)
	c = NumStr(2, 'foo')
	print(c)
	d = NumStr()
	print(d)
	print(bool(d))
	print(a * 2)
	print(b + c)
	print(b == c)

if __name__ == '__main__':
	main()