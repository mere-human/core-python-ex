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

def dollarize(value):
    value = round(value, 2)
    s = str(value)
    pos = s.rfind('.')
    fract = s[pos:]
    parts = []
    while True:
        if pos < 3:
            parts.insert(0, s[0:pos])
            break
        parts.insert(0, s[pos-3:pos])
        pos -= 3
    return '$' + ','.join(parts) + fract

print(dollarize(1234567.8901))