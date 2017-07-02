'''
11-6. Variable-Length Arguments. Write a function called printf(). There is one positional
argument, a format string. The rest are variable arguments that need to be displayed
to standard output based on the values in the format string, which allows the special
string format operator directives such as %d, %f, etc. Hint: The solution is trivialthere is
no need to implement the string operator functionality, but you do need to use the
string format operator ( % ) explicitly.
'''
def printf(fmt_str, *args):
    print(fmt_str % tuple(args))

printf("%d", 11)
printf("%s is a %s", 'string', 'string')