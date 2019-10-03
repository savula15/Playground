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


# class Node:
#     '''Node is where data is stored. Along with data, Node also holds a pointer,
#          which is a reference to next node in the list.'''

#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next_node = next_node

#     def get_data(self):
#         return self.data

#     def set_data(self, newdata):
#         self.data = newdata

#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next

class Node(object):

	def __init__(self, data=None, nextNode=None, downNext=None):
		self.data = data
		self.nextNode = nextNode
		self.downNext = downNext
	def getData(self):
		return self.data
	def setData(self, newData):
		self.data = newData
	def getNext(self):
		return self.nextNode
	def getDownNext(self):
		return self.downNext
	def setNext(self, newNext):
		self.nextNode = newNext
	def setDownNext(self, newDown):
		self.downNext = newDown

"""
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

"""


class OrderedLinkedList(object):
    '''Variant of LinkedList'''
    
    def __init__(self):
		self.head = None
        
    def isEmpty(self):
		return self.head == None

    def size(self):
		current  = self.head
		count = 0
		while current:
			count += 1
			current = current.getNext()
		return count

    def search(self, item):
		current = self.head
		found = False
		stop = False
		while current and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found

    def add(self, item):
		current = self.head
		prev = None
		stop = False
		while current and not stop:
			if current.getData() > item:
				stop = True
			else:
				prev = current
				current = current.getNext()
		temp = Node(item)
		if not prev:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			prev.setNext(temp)

    def reverse(self):
		current = self.head
		prev = None
		while current:
			nextNode = current.getNext()
			current.setNext(prev)
			prev  = current
			current = nextNode
		self.head = prev

    def getMiddle(self):
		slow = self.head
		fast = self.head
		while fast and fast.getNext():
			fast = fast.getNext().getNext()
			slow = slow.getNext()
		return slow.getData()

    def detectLoop(self):
		slow = self.head
		fast = self.head
		while fast and fast.getNext():
			fast = fast.getNext().getNext()
			slow = slow.getNext()
			if slow == fast:
				return True

    def count(self, item):
		current = self.head
		count = 0
		while current:
			if current.getData() == item:
				count += 1
			current = current.getNext()
		return count

    def getNth(self, pos):
		if pos >= self.size() or pos < 0:
			return 'Index Error'
		current = self.head
		index = 0
		while current:
			if pos == index:
				return current.getData()
			index += 1
			current = current.getNext()

    def delete(self):
		self.head = None
    
    def removeLoop(self):
		slow = self.head
		fast = self.head
		while fast and fast.getNext():
			fast = fast.getNext().getNext()
			slow = slow.getNext()
			if slow == fast:
				break
		if slow == fast:
			slow = self.head
			while slow.getNext() != fast.getNext():
				slow = slow.getNext()
				fast = fast.getNext()
			fast.setNext(None)
    
    def pop(self):
        if self.head is None:
            return
		current = self.head
        result = current.data
		self.head = current.nextNode
		return result

    def printItems(self):
		current = self.head
		while current:
			print(current.getData())
			current = current.getNext()

    def _getNthNode(self, pos):
		current = self.head
		index = 0
		while current:
			if pos == index:
				return current
			index += 1
			current = current.getNext()
        return

    def append(self, alist):
		n = self.size()
		if n > 0:
			lastNode = self._getNthNode(n - 1)
		else:
			lastNode = self.head
		if lastNode:
			lastNode.setNext(alist.head)
			alist.head = None
		else:
			self.head.setNext(alist.head)
			alist.head = None

    def removeDuplicates(self):
		current = self.head
		while current:
            runner = current
			while runner.nextNode:
                if runner.nextNode.data  == current.data:
                    runner.nextNode = runner.nextNode.nextNode
                else:
                    runner = runner.nextNode
			current = current.nextNode
        return ll.head

    def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.nextNode


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

