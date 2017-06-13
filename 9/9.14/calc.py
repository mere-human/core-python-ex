'''
5-6. Arithmetic. Create a calculator application. Write code that will take two numbers and
an operator in the format: N1 OP N2, where N1 and N2 are floating point or integer
values, and OP is one of the following: +, -, *, /, %, **, representing addition,
subtraction, multiplication, division, modulus/remainder, and exponentiation,
respectively, and displays the result of carrying out that operation on the input
operands. Hint: You may use the string split() method, but you cannot use the exal
() built-in function.

9-14. Logging Results. Convert your calculator program
(Exercise 5-6) to take input from the command line, i.e.,
Output the result only. Also, write each expression and result to a disk file. Issuing a
command of print will cause the entire contents of the "register tape" to be dumped to the screen and
file reset/truncated. 
'''
import operator
import sys

class CalcError(Exception):
    pass

def num_calc(text):
    op_map = {'+':operator.add,
              '-':operator.sub,
              '*':operator.mul,
              '/':operator.truediv,
              '%':operator.mod,
              '**':operator.pow}

    op_list = text.split(' ')
    if len(op_list) != 3:
        raise CalcError('Wrong input ' + str(op_list))
      
    n1, op, n2 = op_list
    if op not in op_map:
        raise CalcError('Error: Unsupported operator ' + op)

    n1 = int(n1)
    n2 = int(n2)
    r = op_map[op](n1, n2)
    return r

def print_log():
    with open('calc.log', 'r+') as log:
        for line in log:
            print(line, end='')
        log.truncate(0)

def dump_log(text, result):
    with open('calc.log', 'a') as log:
        log.write(text)
        log.write('\n')
        log.write(str(result))
        log.write('\n')

def main():
    try:
        argc = len(sys.argv)
        if argc == 2:
            if sys.argv[1] == 'print':
                print_log()
            else:
                raise CalcError('Expected print command')
        elif argc == 4:
            text = ' '.join(sys.argv[1:])
            r = num_calc(text)
            print(r)
            dump_log(text, r)
        else:
            raise CalcError('Expected 3 args, provided ' + str(argc))
    except EOFError as e:
        pass # exit silently
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    main()