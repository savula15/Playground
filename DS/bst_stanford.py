class TreeNode(object):
	def __init__(self, key, left=None, right=None, parent=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent

def insert(root, key):
	if root == None:
		return (TreeNode(key=key))
	else:
		if key <= root.key:
			root.left = insert(root.left, key=key)
		else:
		     root.right = insert(root.right, key=key)
		return root

def lookup(root, data):
	if root == None:
		return False
	else:
		if data == root.key:
		     return True
		elif data < root.key:
		     return lookup(root.left, data)
		else:
		     return lookup(root.right, data)

def size(root):
	if root == None:
		return 0
	else:
		return 1 + size(root.left) + size(root.right)

 def maxDepth(root):
	if root == None:
		return 0
	else:
		return 1 + max(maxDepth(root.left), maxDepth(root.right))

def minValue(root):
	current = root
	while current.left:
		current = current.left
	return current.key

def maxValue(root):
	current = root
	while current.right:
		current = current.right
	return current.key

def printTree(root):
	if root == None:
		return
	else:
		printTree(root.left)
		print(root.key)
		printTree(root.right)

		     
def printPostOrder(root):
	if root == None:
		return
	else:
		printPostOrder(root.left)
		printPostOrder(root.right)
		print(root.key)

def printPreOrder(root):
	if root == None:
		return
	else:
		print(root.key)
		printPreOrder(root.left)
		printPreOrder(root.right)

def hasPathSum(root, target):
	if root == None:
		return target == 0
	else:
		subSum = target - root.key
		return hasPathSum(root.left, subSum) or hasPathSum(root.right, subSum)

def mirror(root):
	if root == None:
		return
	else:
		mirror(root.left)
		mirror(root.right)
        root.left, root.right = root.right, root.left

def doubleTree(root):
	if root == None:
		return
	else:
        doubleTree(root.left)
		doubleTree(root.right)
		oldLeft = root.left
		root.left = TreeNode(root.key)
		root.left.left = oldLeft
		
def sameTree(aRoot, bRoot):
	if aRoot == None and bRoot == None:
		return True
	else:
		if aRoot != None and bRoot != None:
			return (aRoot.key == bRoot.key and sameTree(aRoot.left, bRoot.left)
			and sameTree(aRoot.right, bRoot.right))
		else:
		     return False

def isBST(root):
  return(isBSTUtil(root, INT_MIN, INT_MAX))

"""
 Returns true if the given tree is a BST and its
 values are >= min and <= max.
"""

def isBSTUtil(root, amin, amax) {
  if root== None:
      return True

  #false if this node violates the min/max constraint
  if (root.key<amin or root.key>amax):
    return False

  # otherwise check the subtrees recursively, tightening the min or max constraint
  return isBSTUtil(root.left, amin, root.key) and isBSTUtil(root.right, root.key+1, amax)

