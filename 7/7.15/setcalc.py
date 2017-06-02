#!/usr/bin/env python3
'''
7-15.
Set Calculator. Create an application that allows
users to input a pair of sets, A and B, and allow users to give an operation symbol, i.
e., in, not in, &, |, ^, <, <=, >, >=, ==, !=, etc. (For sets, you define the input
syntax.) Parse the entire input string and execute the operation on the input sets as requested by the
user.
'''

import operator
import sys

def not_contains(seq, obj):
  return obj not in seq

oper_map = {
    'in':operator.contains,
    'not in':not_contains,
    '&':operator.and_,
    '|':operator.or_,
    '^':operator.xor,
    '<':operator.lt,
    '<=':operator.le,
    '>':operator.gt,
    '>=':operator.ge,
    '==':operator.eq,
    '!=':operator.ne
  }

# Syntax is "{1, 2} | {1, 3}"

def main():
  if len(sys.argv) != 2:
    raise Exception()
  text = sys.argv[1]
 
  a_expr_end = text.index('}')
  b_expr_start = text.index('{', a_expr_end)

  a_expr = text[0:a_expr_end].replace(' ', '')[1:]
  b_expr = text[b_expr_start:-1].replace(' ', '')[1:]
  oper_str = text[a_expr_end+1:b_expr_start].strip()

  a = set(a_expr.split(','))
  b = set(b_expr.split(','))
  x = oper_map[oper_str](a, b)

  # print('a: {}\nb: {}\nop: {}\nx: {}'.format(a, b, oper_str, x))
  print(x)
  
if __name__ == '__main__':
  main()