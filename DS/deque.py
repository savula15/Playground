class Deque:

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


def palindrome_checker(astring):
    '''Runtime: Compares will be half the size of chars in string'''

    d = Deque()

    for ch in astring:
        d.add_rear(ch)

    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False
    return True

print(palindrome_checker("madam"))
print(palindrome_checker("raceeacar"))


def palindrome_list_slice(astring):
    '''Runtime: Compares will be size of string.
    In-Efficient compared to Deque
    '''
    return astring == astring[::-1]

print(palindrome_checker("madam"))
print(palindrome_checker("raceeacar"))
