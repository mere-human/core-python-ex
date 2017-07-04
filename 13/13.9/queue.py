'''
13-9. Queue Class. A queue is a data structure that has first-in-first-out (FIFO)
characteristics. A queue is like a line where items are removed from the front and
added to the rear. The class should support the following methods:
enqueue() adds a new element to the end of a list
dequeue() returns the first element and removes it from the list.
See the previous problem and Example 6.4 for motivation.
'''

class Queue(object):
    def __init__(self, seq=[]):
        self.__list = list(seq)

    def enqueue(self, obj):
        self.__list.append(obj)

    def dequeue(self):
        return self.__list.pop(0)

    def __str__(self):
        return str(self.__list)

    __repr__ = __str__

    def __bool__(self):
        return len(self.__list) > 0

def test():
    q = Queue()
    q.enqueue('Bring out')
    q.enqueue('your dead!')
    assert str(q) == "['Bring out', 'your dead!']"
    assert q.dequeue() == 'Bring out'
    assert q.dequeue() == 'your dead!'
    assert q == False