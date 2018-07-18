class Stack:

    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []

def base_converter(n, b):
    digits = '0123456789ABCDEF'

    s = Stack()
    while n > 0:
        rem = n%b
        s.push(rem)
        n //= b
    newstr = ''
    while not s.is_empty():
        newstr += digits[s.pop()]
    return ''.join(newstr)

def divby3(n):

    if n < 1:
        n *= -1

    astr = base_converter(n, 3)

    return int(astr[-1]) == 0

def divby3_ver2(n):

    if n < 10:
        if n == 0 or n == 3 or n == 6 or n == 9:
            return 1
        else:
            return 0

    else:
        r = 0
        while n:
            r, n = r + (n%10), (n//10)

        return divby3_ver2(r)

def divby2(n):

    if n < 1:
        n *= -1

    astr = base_converter(n, 2)

    return int(astr[-1]) == 0
