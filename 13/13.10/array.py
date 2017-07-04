'''
13-10. Stacks and Queues. Write a class which defines a data structure that can behave as
both a queue (FIFO) or a stack (LIFO), somewhat similar in nature to arrays in PERL.
There are four methods that should be implemented:
shift() returns the first element and removes it from the list, similar to the
earlier dequeue() function
unshift() "pushes" a new element to the front or head of the list
push() adds a new element to the end of a list, similar to the enqueue() and push
() methods from previous problems
pop() returns the last element and removes it from the list; it works exactly
the same way as pop() from before
See also Exercises 13-8 and 13-9
'''

from sys import path
from os.path import abspath
path.append(abspath('../13.8'))
path.append(abspath('../13.9'))
import my_stack
import my_queue

class Array(my_stack.BaseStack, my_queue.BaseQueue):
    __slots__ = ('data')

    def __init__(self, seq=[]):
        self.data = list(seq)

    shift = my_queue.BaseQueue.dequeue
    push = my_queue.BaseQueue.enqueue

    def unshift(self, obj):
        self.data.insert(0, obj)

def test():
    a = Array()
    a.shift(1)
    a.shift(2)
    a.push(3)
    assert str(a) == '[2, 1, 3]'
    assert a.shift() == 2
    assert a.pop() == 3
    assert a.shift() == 1
    assert a == False