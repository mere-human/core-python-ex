#!/usr/bin/env python3
'''
Encryption. Using your solution to the previous problem, and create a "rot13"
translator. "rot13" is an old and fairly simplistic encryption routine whereby each letter
of the alphabet is rotated 13 characters. Letters in the first half of the alphabet will be
rotated to the equivalent letter in the second half and vice versa, retaining case. For
example, a goes to n and X goes to K. Obviously, numbers and symbols are immune
from translation.
'''
import string
def rot13(text):
  # build a map
  map = {}
  offset = 13
  base = ord(min(string.ascii_letters, key=ord))
  print(base)
  n_chars = len(string.ascii_letters)
  for ch in string.ascii_letters:
    src_idx = ord(ch) - base
    dst_idx = (src_idx + offset) % n_chars
    print('ch %s ord %d src %d dst %d ord %d ch %s' % (ch, ord(ch), src_idx, dst_idx, dst_idx + base, chr(dst_idx + base)))
    map[ch] = chr(dst_idx + base)
  # translate a string
  res = []
  for ch in text:
    mapch = map.get(ch)
    if mapch is None:
      # character is not mapped
      res.append(ch)
    else:
      # translate character
      res.append(mapch)
  return ''.join(res)
  
def test():
  t = rot13('This is a short sentence.')
  print(t)
  assert t == 'Guvf vf n fubeg fragrapr.'
  
  t = rot13('This is a short sentence.')
  assert t == 'This is a short sentence.'
  
  print('Checks passed OK')
  
if __name__ == '__main__':
  test()