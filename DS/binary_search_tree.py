''' Notes:
1.  Height of a tree is the number of edges between the root and the deepest leaf node.
2.  If the keys are added in a random order, the height of the tree is going to be around log2n
    where n is the number of nodes in the tree.
3.  The number of nodes at any particular level is 2d where d is the depth of the level.
4.  The total number of nodes in a perfectly balanced binary tree is 2^h+1−1,
    where h represents the height of the tree.

Runtime:
1.  In a perfectly balanced tree, worst-case perf of "put" is O(logn) (same as height),
    but if height turns out to be "n" then it'll be O(n).
2.  Same analysis applies to "get", "delete" and "in/contains"

'''


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
            if key < current_node.key:
                if current_node.has_leftchild():
                    self._put(key, val, current_node.leftchild)
                else:
                    current_node.leftchild = TreeNode(key, val, parent=current_node)
            else:
                if current_node.has_rightchild():
                    self._put(key, val, current_node.rightchild)
                else:
                    current_node.rightchild = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, val):
        self.put(key, val)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif current_node.key < key:
            self._get(key, current_node.leftchild)
        else:
            self._get(key, current_node.rightchild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return None

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, Key is not found in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, Key is not found in tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node):
        if current_node.is_leaf():  # leaf
            if current_node == current_node.parent.leftchild:
                current_node.parent.leftchild = None
            else:
                current_node.parent.rightchild = None
        elif current_node.has_both_children():  # interior
            succ = current_node.find_succesor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:  # this node has one child
            if current_node.has_leftchild():
                if current_node.is_leftchild():
                    current_node.leftchild.parent = current_node.parent
                    current_node.parent.leftchild = current_node.leftchild
                elif current_node.is_rightchild():
                    current_node.rightchild.parent = current_node.parent
                    current_node.parent.rightchild = current_node.leftchild
                else:
                    current_node.replace_node_data(current_node.leftchild.key,
                                                   current_node.leftchild.payload,
                                                   current_node.leftchild.leftchild,
                                                   current_node.leftchild.rightchild)
            else:
                if current_node.is_leftchild():
                    current_node.rightchild.parent = current_node.parent
                    current_node.parent.leftchild = current_node.rightchild
                elif current_node.is_rightchild():
                    current_node.rightchild.parent = current_node.parent
                    current_node.parent.rightchild = current_node.rightchild
                else:
                    current_node.replace_node_data(current_node.rightchild.key,
                                                   current_node.rightchild.payload,
                                                   current_node.rightchild.leftchild,
                                                   current_node.rightchild.rightchild)

        def find_succesor(self):
            succ = None
            if self.has_rightchild():
                succ = self.rightchild.find_min()
            else:
                if self.parent:
                    if self.is_leftchild():
                        succ = self.parent
                    else:
                        self.parent.rightchild = None
                        succ = self.parent.find_succesor()
                        self.parent.rightchild = self
            return succ

        def find_min(self):
            current = self
            while current.has_leftchild():
                current = current.leftchild
            return current

        def splice_out(self):
            if self.is_leaf():
                if self.is_leftchild():
                    self.parent.leftchild = None
                else:
                    self.parent.rightchild = None
            elif self.has_any_children():
                if self.has_leftchild():
                    if self.is_leftchild():
                        self.parent.leftchild = self.leftchild
                    else:
                        self.parent.rightchild = self.rightchild
                    self.leftchild.parent = self.parent
                else:
                    if self.is_leftchild():
                        self.parent.leftchild = self.rightchild
                    else:
                        self.parent.rightchild = self.rightchild
                    self.rightchild.parent = self.parent


class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def has_leftchild(self):
        return self.leftchild

    def has_rightchild(self):
        return self.rightchild

    def is_leftchild(self):
        return self.parent and self.parent.leftchild == self

    def is_rightchild(self):
        return self.parent and self.parent.rightchild == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.leftchild or self.rightchild)

    def has_any_children(self):
        return self.leftchild or self.rightchild

    def has_both_children(self):
        return self.leftchild and self.rightchild

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.leftchild = lc
        self.rightchild = rc
        if self.has_leftchild():
            self.leftchild.parent = self
        if self.has_rightchild():
            self.rightchild.parent = self

    def __iter__(self):
        if self:
            if self.has_leftchild():
                for elem in self.leftchild:
                    yield elem
            yield self.key

            if self.has_rightchild():
                for elem in self.rightchild:
                    yield elem


def height_of_bst(root):
        if root is None:
            return -1
        else:
            return 1 + max(height_of_bst(root.leftchild), height_of_bst(root.rightchild))


def main():
    bst = BinarySearchTree()
    bst[3] = 'blue'
    bst[4] = 'green'
    bst[5] = 'yellow'
    bst[2] = 'red'

    print(bst[4])
    print(bst[2])
    print(bst[1])


if __name__ == '__main__':
    main()
