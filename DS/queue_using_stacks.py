from stack import Stack


class QueueStack:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if self.s1.is_empty() and self.s2.is_empty():
            raise IndexError("Queue is empty")
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def size(self):
        return self.s1.size()

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()
