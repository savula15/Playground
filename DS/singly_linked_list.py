''' Implementing Singly Linked list in Python

Ref:
1. https://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/linked%20lists.html
2. https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
3. http://cslibrary.stanford.edu/105/LinkedListProblems.pdf

Singly Linked list:

a linked list is a string of nodes, with each node containing
both data and a reference to the next node in the list

Doubly linked list: The nodes in a doubly linked list will contain
references to both the next node and the previous node.

Advantages:

The main advantage of using a linked list over a similar data structure,
like the static array, is the linked list’s dynamic memory allocation:
if you don't know the amount of data you want to store before hand,
the linked list can adjust on the fly.

Disadvantages:

Dynamic memory allocation requires more space and commands slower look up times.

'''


class Node:
    '''Node is where data is stored. Along with data, Node also holds a pointer,
         which is a reference to next node in the list.'''

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, newdata):
        self.data = newdata

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class UnorderedLinkedList:
    '''Creates a linked list and initilizes its head node to None by default'''

    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
                count += 1
                current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
            if current == None:
                raise ValueError("Data is not found")
        return current

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
            if current == None:
                raise ValueError("Data is not found")
        if previous == None:
            self.head = current.gext_next()
        else:
            previous.set_next(current.get_next())

    def reverse(self):
            previous = None
            current = self.head
            while current:
                next_node = current.next_node
                current.next_node = previous
                previous = current
                current = next_node
            self.head = previous

    def __iter__(self):
            current = self.head
            while current:
                yield current
                current = current.get_next()

    def count(self, data):
        count = 0
        current = self.head
        while current:
            if current.get_data() == data:
                count += 1
            current = current.get_next()
        return count

    def get_nth(self, index):
        current = self.head
        i = 0
        while current and i <= index:
            if i == index:
                return current.get_data()
            else:
                i += 1
                current = current.get_next()
        return 0

    def delete_list(self):
        '''https://<url>/questions/38081643/python-how-to-completely-delete-linked-list
           url = stackoverflow.com'''
        self.head = None

    def remove_first(self):
        current = self.head
        if not current:
            raise ValueError("Data is not found")
        else:
            value = current.get_data()
            self.head = current.get_next()
        return value

    def remove_duplicates(self):
        current = self.head

        while current:
            while current.next_node and (current.next_node.data == current.data):
                current.next_node = current.next_node.next_node
                current = current.next_node

        return self.head

    def insert_nth(self, index, data):
        current = self.head
        if index == 0:
            self.insert(data)
        else:
            for i in range(index - 1):
                current = current.get_next()
        if current:
            new_node = Node(data)
            new_node.set_next(current.get_next())
            current.set_next(new_node)
        else:
            raise ValueError("Index out of range")

    def sorted_insert(self, data):
        pass

    def insert_sort(self, data):
        ''' Use sorted_insert. Ref: http://cslibrary.stanford.edu/105/LinkedListProblems.pdf'''
        pass

    def append(self, list1, list2):
        pass

    def front_back_split(self, list1):
        pass

    def move_node(self, list1, list2):
        pass

    def alternating_split(self, list1):
        pass

    def shuffle_merge(self, list1, list2):
        pass

    def sorted_merge(self, list1, list2):
        pass

    def merge_sort(self, list1):
        pass

    def sorted_intersect(Self, list1, list2):
        pass

    def recursive_reverse(self, list1):
        pass


class OrderedLinkedList:
    '''Variant of LinkedList'''

    def __init__(self, head=None):
            self.head = head

    def add(self, data):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > data:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(data)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, data):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == data:
                found = True
            else:
                if current.get_data() > data:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def reverse(self):
            previous = None
            current = self.head
            while current:
                next_node = current.next_node
                current.next_node = previous
                previous = current
                current = next_node
            self.head = previous

    def __iter__(self):
            node = self.head
            while node:
                yield node
                node = node.get_next()

    def print_list(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

    def is_empty(self):
        return self.head == None

    def get_middle(self):
        mid = self.head
        current = self.head
        count = 0
        while current:
            if (count & 1):
                mid = mid.get_next()
            count += 1
            current = current.get_next()
        if mid is not None:
            return mid.get_data()
        else:
            raise ValueError("list is empty")

    def get_middle2(self):
        slow = self.head
        fast = self.head
        while fast and fast.get_next():
            fast = fast.get_next().get_next()
            slow = slow.get_next()
        return slow.get_data()

    def detect_loop(self):
        fast = self.head
        slow = self.head
        while fast and fast.get_next():
            fast = fast.get_next().get_next()
            slow = slow.get_next()
            if slow == fast:
                return 1

    def remove_loop(self):
        if self.head is None or self.head.next_node is None:
            return
        slow = self.head.next_node
        fast = self.head.next_node.next_node
        while fast is not None:
            if fast.next_node is None:
                break
            if slow == fast:
                break
            slow = slow.next_node
            fast = fast.next_node.next_node
        if slow == fast:
            slow = self.head
            while slow.next_node != fast.next_node:
                slow = slow.next_node
                fast = fast.next_node
            fast.next_node = None


def reverse_words(head):
    current = head
    result = []
    word = []
    while current:
        if current.get_data() == ' ' or current == None:
            result.append(''.join(word[::-1]))
            word = []
        else:
            word.append(current.get_data())
        current = current.get_next()

    result.append(''.join(word[::-1]))

    return ' '.join(result)


if __name__ == '__main__':

    s = 'Hello World I Am Roberto'
    l6 = UnorderedLinkedList()
    for c in s:
        l6.insert(c)

    print("print reverse of linkedlist")
    l6.reverse()
    for node in l6:
        print(node.get_data())

    reverse_words(l6.head)  # 'olleH dlroW  I  mA  treboR '
