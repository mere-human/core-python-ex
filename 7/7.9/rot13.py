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

translate_map = {}

def fill_map(map, letters, offset):
  base = ord(min(letters, key=ord))
  size = len(letters)
  for ch in letters:
    src_idx = ord(ch) - base
    dst_idx = (src_idx + offset) % size
    map[ch] = chr(dst_idx + base)

def rot13(text):
  if not translate_map:
    # build a map
    offset = 13
    fill_map(translate_map, string.ascii_lowercase, offset)
    fill_map(translate_map, string.ascii_uppercase, offset)
  # translate a string
  res = []
  for ch in text:
    mapch = translate_map.get(ch)
    if mapch is None:
      # character is not mapped
      res.append(ch)
    else:
      # translate character
      res.append(mapch)
  return ''.join(res)
  
def test():
  t = rot13('This is a short sentence.')
  assert t == 'Guvf vf n fubeg fragrapr.'
  
  t = rot13('Guvf vf n fubeg fragrapr.')
  assert t == 'This is a short sentence.'
  
  print('Checks passed OK')
  
if __name__ == '__main__':
  test()