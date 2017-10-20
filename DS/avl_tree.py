from binary_search_tree import TreeNode, BinarySearchTree


class AvlTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_leftchild():
                self._put(key, val, current_node.leftchild)
            else:
                current_node.leftchild = TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.leftchild)
        else:
            if current_node.has_rightchild():
                self._put(key, val, parent=current_node.rightchild)
            else:
                current_node.rightchild = TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.rightchild)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < 1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.is_leftchild():
                node.parent.balance_factor += 1
            elif node.is_rightchild():
                node.parent.balance_factor -= 1
            if node.balance_factor != 0:
                self.update_balance(node.parent)

    def rotate_left(self):
        pass
