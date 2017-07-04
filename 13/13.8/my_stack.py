'''
13-8. Stack Class. A stack is a data structure with last-in-first-out (LIFO) characteristics.
Think of a stack of cafeteria trays. The first one in the spring-loaded device is the last
one out, and the last one in is the first one out. Your class will have the expected push() (add an item to the stack) and pop() (remove an item from the stack) methods.
Add an isempty() Boolean method that returns TRue if the stack is empty and False
otherwise, and a peek() method that returns the item at the top of the stack without
popping it off.

Note that if you are using a list to implement your stacks, the pop() method is already
available as of Python 1.5.2. Create your new class so that it contains code to detect if
the pop() method is available. If so, call the built-in one; otherwise, it should execute
your implementation of pop(). You should probably use a list object; if you do, do not
worry about implementing any list functionality (i.e., slicing). Just make sure that your
Stack class can perform both of the operations above correctly. You may subclass a
real list object or come up with your own list-like object.
'''

class BaseStack(object):
    __slots__ = ()

    def push(self, obj):
        self.data.append(obj)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return len(self.data) <= 0

    def peek(self):
        return self.data[-1]

class Stack(BaseStack):
    __slots__ = ('data')
    def __init__(self):
        self.data = []

def test():
    s = Stack()

    s.push(1)
    assert s.peek() == 1

    s.push(2)
    assert s.peek() == 2

    assert s.pop() == 2
    assert s.peek() == 1
    assert s.is_empty() == False

    s.pop()
    assert s.is_empty() == True

if __name__ == '__main__':
    test()
