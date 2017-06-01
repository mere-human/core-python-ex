#!/usr/bin/env python3
'''
Create a character translator (that works similar to the Unix tr command).
This function, which we will call TR(), takes three strings as arguments: source,
destination, and base strings, and has the following declaration:

def tr(srcstr, dststr, string)

srcstr contains the set of characters you want "translated," dststr contains
the set of characters to translate to, and string is the string to perform the
translation on. For example, if srcstr == 'abc', dststr == 'mno', and string ==
'abcdef', then tr() would output'mnodef'. Note that len(srcstr) == len(dststr).
For this exercise, you can use the chr() and ord() BIFs, but they are not
necessary to arrive at a solution.
'''
def tr(srcstr, dststr, string, icase=False):
  # build a map
  map = {}
  n = min(len(srcstr), len(dststr))
  for i in range(n):
    srcchr = srcstr[i].lower() if icase else srcstr[i]
    dstchr = dststr[i].lower() if icase else dststr[i]
    map[srcchr] = dstchr
  # translate a string
  res = []
  for ch in string:
    mapch = map.get(ch.lower() if icase else ch)
    if mapch:
      if icase:
        # update case
        mapch = mapch.upper() if ch.isupper() else mapch.lower()
      res.append(mapch)
    else:
      res.append(ch)
  return ''.join(res)
  
def test():
  t = tr('abc', 'mno', 'abcdef')
  assert t == 'mnodef'
  t = tr('abc', 'mno', 'AbCdEf')
  assert t == 'AnCdEf'
  t = tr('abc', 'mno', 'AbCdEf', True)
  assert t == 'MnOdEf'
  print('Checks passed OK')
  
if __name__ == '__main__':
  test()