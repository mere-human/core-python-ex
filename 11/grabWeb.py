from urllib.request import urlretrieve

def firstNonBlank(lines):
	for eachLine in lines:
		if not eachLine.strip():
			continue
		else:
			return eachLine

def firstLast(webpage):
	f = open(webpage, 'r', encoding='utf-8')
	lines = f.readlines()
	f.close()
	print(firstNonBlank(lines), end='')
	print(firstNonBlank(reversed(lines)), end='')

def downtload(url, process=firstLast):
	try:
		retval = urlretrieve(url)[0]
	except IOError:
		retval = None
	if retval:
		process(retval)

if __name__ == '__main__':
	downtload('https://www.wikipedia.org/')