class MiniStack:
    """ Time complexity: O(1)
    Auxialary space: O(n)
    """

    def __init__(self):
        self.stack = []
        self.min = []

    def get_min(self):
        if self.min:
            return self.min[-1]

    def push(self, item):
        self.stack.append(item)
        if not self.min or item <= self.get_min():
            self.min.append(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.get_min():
            self.min.pop()
        return item


s = MiniStack()

l = range(10)
for i in l:
    s.push(i)

print("Stack full ==>", s.stack)
print("Pop from stack ==>", s.pop())
print("Get min of stack ==>", s.get_min())
print("Stack after pop ==>", s.stack)
