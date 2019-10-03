class Node(object):

	def __init__(self, data=None, nextNode=None):
		self.data = data
		self.nextNode = nextNode


class LinkedList(object):
	
    def __init__(self):
        self.head = None
	
    def push(self, data):
        temp = Node(data=data)
        current = self.head
        temp.nextNode = current
        self.head = temp
	
    def printList(self, head):
        if head == None:
            return
        current = head
        while current:
            print(current.data)
            current = current.nextNode

def count(head, n):
	count = 0
	current = head
	while current:
		if current.data == n:
			count += 1
		current = current.next
	return count

def getNth(head, index):
	current = head
	count = 0
	while current:
		if count == index:
			return current.data
		count += 1
		current = current.next

def deleteList(head):
	head = None

def pop(head):
	current = head
	result = current.data
	nextNode = current.nextNode
	head = nextNode
	return head, result

def insertNth(head, index, data):
	current = head
	temp = Node(data=data)
	if index == 0:
		temp.nextNode = current
		head = temp
	else:
		for i in range(index-1):
			if not current:
				raise IndexError("Index out of range")
			current = current.nextNode
		if not current:
			raise IndexError("Index out of range")
		prev = current
		current = current.nextNode
		temp.nextNode = current
		prev.nextNode = temp
	return head

def sortedInsert(head, node):
	current = head
	prev = None
	while current:
		if current.data >= node.data:
			break
		prev = current
		current = current.nextNode
	if prev != None:
		prev.nextNode = node
		node.nextNode = current
	else:
		node.nextNode = current
		head = node
	return head

def insertSort(head):
	current = head
	result = LinkedList()
	newHead = result.head
	while current:
		nextNode = current.nextNode
		newHead = sortedInsert(newHead, current)
		current = nextNode
	return newHead

def append(aHead, bHead):
	if aHead == None:
		aHead = bHead
	else:
		current = aHead
		while current.nextNode:
			current = current.nextNode
		current.nextNode = bHead
	bHead = None
	return aHead

def length(head):
	if head == None:
		return 0
	count = 0
	current = head
	while current:
		count += 1
		current = current.nextNode
	return count

def frontBackSplit(head, aHead, bHead):
	if head == None or head.nextNode == None:
		aHead = head
		bHead = None
	else:
		current = head
		slow = current
		fast = current.nextNode
		while fast and fast.nextNode:
			slow = slow.nextNode
			fast = fast.nextNode.nextNode
		aHead = head
		bHead = slow.nextNode
		slow.nextNode = None
	return aHead, bHead

def removeDups(head):
	if head == None:
		return
	current = head
	while current.nextNode:
		if current.data == current.nextNode.data:
			nextNode = current.nextNode.nextNode
			current.nextNode = nextNode
		else:
			current = current.nextNode
	return head

def removeDups2(head):
	""" Remove dups in un-sorted list and with extra buffer for dict
	"""

	d = {}
	current = head
	prev = None
	while current:
		if current.data in d:
			nextNode = current.nextNode
			prev.nextNode = nextNode
			current = nextNode
		else:
			d[current.data] = current.data
			prev = current
			current = current.nextNode
	return head

def moveNode(aHead, bHead):
	if bHead == None:
		return aHead
	newNode = bHead
	bHead = newNode.nextNode
	newNode.nextNode = aHead
	aHead = newNode
	return aHead, bHead

def alternateSplit(head, aHead, bHead):
    """ Elements will be in reverse order for a and b lists
    """
    current = head
    while current:
	    aHead, current = moveNode(aHead, current)
	    if current:
		    bHead, current = moveNode(bHead, current)
    return aHead, bHead

def reverseList(head):
	result = LinkedList()
	rHead = result.head
	current = head
	while current:
		rHead, current = moveNode(rHead, current)
	return rHead

def kthtoLast(head, k):
	current = head
	slow = current
	fast = current
	for _ in range(k):
		fast = fast.nextNode
	while fast:
		slow = slow.nextNode
		fast = fast.nextNode
	return slow.data

