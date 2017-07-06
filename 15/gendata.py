'''
This script generates strings with three fields, delimited by a pair of colons,
or a double-colon. The first field is a random (32-bit) integer, which is converted
to a date. The next field is a randomly generated electronic mail (e-mail) address,
and the final field is a set of integers separated by a single dash ( - ).
'''

from random import randint, choice
from string import ascii_lowercase as lowercase
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')
maxint = 2 ** 32
for i in range(randint(5, 10)):
    dtint = randint(0, maxint-1) # pick date
    dtstr = ctime(dtint) # date string

    shorter = randint(4, 7) # login shorter
    em = ''
    for j in range(shorter): # generate login
        em += choice(lowercase)

    longer = randint(shorter, 12) # domain longer
    dn = ''
    for j in range(longer): # create domain
        dn += choice(lowercase)

    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, em,
        dn, choice(doms), dtint, shorter, longer))