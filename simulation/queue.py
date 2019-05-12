class Queue:
    """
    Attributes:

    """

    def __init__(self):
        self._queue = []

    def enqueue(self, obj):
        self._queue.append(obj)

    def dequeue(self, obj):
        self._queue.remove(obj)
        print("Group {} leaves the queue".format(obj.id))


