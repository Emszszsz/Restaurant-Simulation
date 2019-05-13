class Queue:
    """
    Attributes:

    """

    def __init__(self):
        self._queue = []

    def enqueue(self, obj):
        self._queue.append(obj)

    def dequeue(self):
        self._queue.pop(0)
