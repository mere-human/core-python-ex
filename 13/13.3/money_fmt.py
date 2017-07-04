'''
13-3. Customizing Classes. 
Create a class to format floating point values to monetary
amounts. In this exercise, we will use United States currency, but feel free to
implement your own.

Preliminary work: Create a function called dollarize() which takes a floating point
value and returns that value as a string properly formatted with symbols and rounded
to obtain a financial amount. For example: dollarize(1234567.8901) =>
'$1,234,567.89. The dollarize() function should allow for commas, such as
1,000,000, and dollar signs. Any negative sign should appear to the left of the dollar
sign. Once you have completed this task, then you are ready to convert it into a useful
class called MoneyFmt.

The MoneyFmt class contains a single data value, the monetary amount, and has five
methods (feel free to create your own outside of this exercise). The __init__()
constructor method initializes the data value, the update() method replaces the data
value with a new one, the __nonzero__() method is Boolean, returning true if the data
value is non-zero, the __repr__() method returns the amount as a float, and the
__str__() method displays the value in the string-formatted manner that dollarize()
does.

a.
Fill in the code to the update() method so that it will update the data value.

b.
Use the work you completed for dollarize() to fill in the code for the __str__()
method.

c.
Fix the bug in the __nonzero__() method, which currently thinks that any value
less than one, i.e., fifty cents ($0.50), has a false value.

d.Extra credit: Allow the user to optionally specify an argument indicating the
desire to see less-than and greater-than pairs for negative values rather than
the negative sign. The default argument should use the standard negative sign.

'''

class MoneyFmt(object):
    def __init__(self, value=0.0):
        self.update(value)

    def update(self, value=None):
        self.value = float(value)

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        sign = '-' if self.value < 0 else ''
        value = abs(round(self.value, 2))
        s = '%.2f' % value
        pos = s.rfind('.')
        fract = s[pos:]
        parts = []
        while pos > 0:
            parts.insert(0, s[pos-3 if pos > 3 else 0:pos])
            pos -= 3
        return sign + '$' + ','.join(parts) + fract

    def __bool__(self):
        return self.value > 0.0


def check_str(val, pat):
    s = str(val)
    assert s == pat, '%s should be %s' % (s, pat)

def test():
    check_str(MoneyFmt(1234567.8901), '$1,234,567.89')
    check_str(MoneyFmt(123456.8901), '$123,456.89')
    check_str(MoneyFmt(-22.3), '-$22.30')

    assert repr(MoneyFmt(123.89)) == '123.89'
    assert repr(MoneyFmt(-22)) == '-22.0'

    if MoneyFmt():
        assert False, 'Default should be converted to False'
    if not MoneyFmt(1):
        assert False, '1 should be converted to True'
    if not MoneyFmt(0.5):
        assert False, '0.5 should be converted to True'

    cash = MoneyFmt(123.45)
    check_str(cash, '$123.45')
    cash.update(100000.4567)
    check_str(cash, '$100,000.46')
    cash.update(-0.3)
    check_str(cash, '-$0.30')
    assert repr(cash) == '-0.3'


if __name__ == '__main__':
    test()