class Stack:
    ''' Implementaion of Stack datastructure with top being end of list
    and base being start of list

    push(append) and pop will take O(1) time'''

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):

        try:
            return self.items.pop()
        except:
            raise IndexError('pop from empty list')

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


class Stack2:
    ''' Implementaion of Stack datastructure with top being start of list
    and base being end of list

    push(insert) and pop will take O(n) time'''

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)
        print(self.items)

    def pop(self):
        print(self.items)
        try:
            return self.items.pop(0)
        except:
            raise IndexError('pop from empty list')

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return self.items == []


if __name__ == '__main__':
    s1 = Stack()
    s2 = Stack2()

    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.peek()
    s1.pop()
    s1.pop()
    s1.pop()
    s1.pop()

    s2.push(1)
    s2.push(2)
    s2.push(3)
    s2.push(4)
    s2.peek()
    s2.pop()
    s2.pop()
    s2.pop()
    s2.pop()

