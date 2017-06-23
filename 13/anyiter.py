class AnyIter(object):
	def __init__(self, data, safe=False):
		self.iter = iter(data)
		self.safe = safe

	def __iter__(self):
		return self

	def __next__(self, howmany=1):
		retval = []
		for each in range(howmany):
			try:
				retval.append(self.iter.__next__())
			except StopIteration:
				if self.safe:
					break
				else:
					raise
		return retval

def main():
	it = AnyIter(range(10))
	for i in range(1, 5):
		print(i, it.__next__(i))

if __name__ == '__main__':
	main()