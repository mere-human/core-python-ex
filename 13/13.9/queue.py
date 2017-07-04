'''
13-9. Queue Class. A queue is a data structure that has first-in-first-out (FIFO)
characteristics. A queue is like a line where items are removed from the front and
added to the rear. The class should support the following methods:
enqueue() adds a new element to the end of a list
dequeue() returns the first element and removes it from the list.
See the previous problem and Example 6.4 for motivation.
'''

class BaseQueue(object):

    def enqueue(self, obj):
        self.data.append(obj)

    def dequeue(self):
        return self.data.pop(0)

    def __str__(self):
        return str(self.data)

    __repr__ = __str__

    def __bool__(self):
        return len(self.data) > 0

class Queue(BaseQueue):
    __slots__ = ('data')

    def __init__(self, seq=[]):
        self.data = list(seq)

def test():
    q = Queue()
    q.enqueue('Bring out')
    q.enqueue('your dead!')
    assert str(q) == "['Bring out', 'your dead!']"
    assert q.dequeue() == 'Bring out'
    assert q.dequeue() == 'your dead!'
    assert q == False