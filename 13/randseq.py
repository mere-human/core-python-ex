from random import choice

class RandSeq(object):
	def __init__(self, seq):
		self.seq = seq

	def __iter__(self):
		return self

	def __next__(self):
		return choice(self.seq)

def main():
	for each in RandSeq(('rock', 'paper', 'scissorts')):
		print(each)
		i = input()

if __name__ == '__main__':
	main()