'''
13-20. Class Customization. Improve on the time60.py script as seen in Section 13.13.2,
Example 13.3.

a.
Allow "empty" instantiation: If hours and minutes are not passed in, then
default to zero hours and zero minutes.

b.
Zero-fill values to two digits because the current formatting is undesirable. In
the case below, displaying wed should output "12:05."
>>> wed = Time60(12, 5)
>>> wed
12:5

c.In addition to instantiating with hours (HR) and minutes (min), also support
time entered as:
- A tuple of hours and minutes (10, 30)
- A dictionary of hours and minutes ({'HR' : 10, 'min': 30})
- A string representing hours and minutes ("10:30") Extra Credit: Allow
for improperly formatted strings like "12:5" as well.

d.
Do we need to implement __radd__()? Why or why not? If not, when would or
should we override it?

e.
The implementation of __repr__() is flawed and misguided. We only overrode
this function so that it displays nicely in the interactive interpreter without
having to use the print statement. However, this breaks the charter that repr
() should always give a (valid) string representation of an evaluatable Python
expression. 12:05 is not a valid Python expression, but Time60('12:05') is.
Make it so.

f.
Add support for sexagesimal (base 60) operations. The output for the following
example should be 19:15 not 18:75:
>>> thu = Time60(10, 30)
>>> fri = Time60(8, 45)
>>> thu + fri
18:75
'''
class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hr=0, min=0):
        'constructor - takes hours and minutes'
        if isinstance(hr, tuple):
            self.hr, self.min = hr
        elif isinstance(hr, dict):
            self.hr = hr['HR']
            self.min = hr['min']
        elif isinstance(hr, str):
            l = hr.split(':')
            self.hr = int(l[0])
            self.min = int(l[1])
        else:
            self.hr = hr
            self.min = min

    def __str__(self):
        'string representation'
        return '%d:%02d' % (self.hr, self.min)

    def __repr__(self):
        return "%s(%d, %d)" % (self.__class__.__name__, self.hr, self.min)

    def __add(self, hr, min):
        self.hr += hr
        if self.min >= 24:
            self.hr = self.hr % 24
        self.min += min
        if self.min >= 60:
            self.hr += self.min // 60
            self.min = self.min % 60

    def __add__(self, other):
        'overloading the addition operator'
        if isinstance(other, self.__class__):
            res = self.__class__(self.hr, self.min)
            res.__add(other.hr, other.min)
            return res
        else:
            raise ValueError("Not supported operand's type")

    def __iadd__(self, other):
        'overloading in-place addition'
        if isinstance(other, self.__class__):
            self.__add(other.hr, other.min)
            return self
        else:
            raise ValueError("Not supported operand's type")

    # NOTE: __radd__ is not implemented since addition works only if
    # both operands are of type Time60


def main():
    assert str(Time60()) == '0:00'
    assert str(Time60(12, 5)) == '12:05'

    assert str(Time60((10, 30))) == '10:30'
    assert str(Time60({'HR':10, 'min':30})) == '10:30'
    assert str(Time60('10:30')) == '10:30'
    assert str(Time60('12:5')) == '12:05'

    assert str(Time60('10:30') + Time60('11:15')) == '21:45'
    assert str(Time60('10:30') + Time60('8:45')) == '19:15'
    assert str(Time60('21:30') + Time60('8:45')) == '6:15'

    t = Time60('10:05')
    t += Time60('11:10')
    assert str(t) == '21:15'

    t = Time60('10:30')
    t += Time60('8:45')
    assert str(t) == '19:15'

    t = eval(repr(Time60('10:05')))
    assert isinstance(t, Time60)
    assert str(t) == '10:05'

if __name__ == '__main__':
    main()