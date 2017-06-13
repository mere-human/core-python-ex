'''
5-6. Arithmetic. Create a calculator application. Write code that will take two numbers and
an operator in the format: N1 OP N2, where N1 and N2 are floating point or integer
values, and OP is one of the following: +, -, *, /, %, **, representing addition,
subtraction, multiplication, division, modulus/remainder, and exponentiation,
respectively, and displays the result of carrying out that operation on the input
operands. Hint: You may use the string split() method, but you cannot use the exal
() built-in function.
'''

import operator

def main():
    op_map = {'+':operator.add,
              '-':operator.sub,
              '*':operator.mul,
              '/':operator.truediv,
              '%':operator.mod,
              '**':operator.pow}
    while True:
        text = input()
        op_list = text.split(' ')
        if len(op_list) != 3:
            print('Error: Wrong input')
            break
        n1, op, n2 = op_list
        if op not in op_map:
            print('Error: Unsupported operator', op)
            break
        n1 = int(n1)
        n2 = int(n2)
        r = op_map[op](n1, n2)
        print(r)

if __name__ == '__main__':
    main()