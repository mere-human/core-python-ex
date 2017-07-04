dashes = '\n' + '-' * 50

exec_dict = {
    # for
    'f': '''
for %s in %s:
    print(%s)
''',

    # seq while
    's': '''
%s = 0
%s = %s
while %s < len(%s):
    print(%s[%s])
    %s += 1
''',

    # counting while
    'n': '''
%s = %d
while %s < %d:
    print(%s)
    %s = %s + %d
'''
}

def main():
    ltype = input('Loop type? (for/while)')
    dtype = input('Data type? (number/seq)')

    if dtype == 'n':
        start = input('Starting value?')
        stop = input('Ending value?')
        step = input('Stepping value?')
        seq = str(range(int(start), int(stop), int(step)))
    else:
        seq = eval(input('Enter sequence: '))
    var = input('Iterative var name?')
    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)
    elif ltype == 'w':
        if dtype == 's':
            svar = input('Enter seq name?')
            exec_str = exec_dict['s'] % \
            (var, svar, seq, var, svar, svar, var, var, var)
        elif dtype == 'n':
            exec_str = exec_dict['n'] % \
            (var, start, var, stop, var, var, var, step)

    print(dashes)
    print('Code:' + dashes)
    print(exec_str + dashes)
    print('Test:' + dashes)
    exec(exec_str)
    print(dashes)

if __name__ == '__main__':
    main()