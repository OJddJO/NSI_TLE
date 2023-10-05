class Queue:
    """Queue represent a queue data structure of n element, where n is the size of the queue.
    Note that the queue is initialized with None.

    Elements are added to the rear of the queue and removed from the front of the queue.
    The queue is empty when the front and rear are the same.
    
    >>> myQueue = Queue(5)
    >>> print(myQueue)
    [None, None, None, None, None]
    
    >>> myQueue.add(1)
    1
    >>> print(myQueue)
    [1, None, None, None, None]
    
    >>> myQueue.add(2)
    2
    
    >>> myQueue.remove()
    1
    >>> print(myQueue)
    [1, 2, None, None, None] # Note that the first element is still 1
    >>> print(myQueue.getQueue())
    [2]"""
    def __init__(self, size: int):
        self._size = size
        self._queue = [None] * size
        self._start = 0
        self._end = 0
    
    def emptyQueue(self) -> bool:
        """Returns True if the queue is empty."""
        return self._start == self._end
    
    def fullQueue(self) -> bool:
        """Returns True if the queue is full."""
        return self._start == self._size
    
    def add(self, element) -> object:
        """Adds an element to the rear of the queue. Returns the element added."""
        if self.fullQueue():
            raise IndexError("Queue is full.")
        else:
            self._queue[self._end] = element
            self._end += 1
            return element

    def remove(self) -> object:
        """Removes the front element from the queue. Returns the element removed."""
        if self.emptyQueue():
            raise IndexError("Queue is empty.")
        else:
            element = self._queue[self._start]
            self._start += 1
            return element
        
    def getQueue(self) -> list:
        """Returns the queue."""
        return self._queue[self._start:self._end]
        
    def __str__(self) -> str:
        """Returns a string representation of the queue."""
        return str(self._queue)
    
    def __len__(self) -> int:
        """Returns the size of the queue."""
        return self._size
    
    def __iter__(self) -> object:
        """Returns an iterator for the queue."""
        return _QueueIterator(self._queue, self._start, self._end)


class _QueueIterator:
    """An iterator for the queue."""
    def __init__(self, queue, start, end):
        self._start = start
        self._end = end
        self._queue = queue[self._start:self._end]
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < self._end - self._start:
            element = self._queue[self._index]
            self._index += 1
            return element
        else:
            raise StopIteration


if __name__ == '__main__':
    queue = Queue(5)
    print("Queue is empty:", queue.emptyQueue())
    print("Queue is full:", queue.fullQueue())
    print("Adding 1 to queue:", queue.add(1))
    print("Adding 2 to queue:", queue.add(2))
    print("Adding 3 to queue:", queue.add(3))
    print("Adding 4 to queue:", queue.add(4))
    print("Queue is empty:", queue.emptyQueue())
    print("Queue is full:", queue.fullQueue())
    print("Removing from queue:", queue.remove())
    print(queue)
    print("Print all element in queue")
    print(queue.getQueue())
    for i in queue:
        print(i)