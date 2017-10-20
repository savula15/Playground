from queue import Queue


class StackQueue:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q2.enqueue(item)
        while self.q1.size() >= 1:
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.dequeue()

    def size(self):
        return self.q1.size()

    def is_empty(self):
        return self.q1.is_empty()
