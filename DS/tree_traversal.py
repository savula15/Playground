from binary_tree import BinaryTree
from stack import Stack

import operator


def preorder(tree):
    '''preorder traversal'''
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_leftchild())
        preorder(tree.get_rightchild())


def postorder(tree):
    '''postorder traversal'''
    if tree:
        postorder(tree.get_leftchild())
        postorder(tree.get_rightchild())
        print(tree.get_root_val())


def inorder(tree):
    '''inorder traversal'''
    if tree:
        inorder(tree.get_leftchild())
        print(tree.get_root_val())
        inorder(tree.get_rightchild())


def parsetree(expr):
    tokens = expr.split()
    pt = BinaryTree('')
    current_tree = pt
    pstack = Stack()
    pstack.push(current_tree)

    for token in tokens:
        if token == '(':
            current_tree.insert_left('')
            pstack.push(current_tree)
            current_tree = current_tree.get_leftchild()
        elif token not in ['/', '*', '+', '-', ')']:
            current_tree.set_root_val(int(token))
            parent = pstack.pop()
            current_tree = parent
        elif token in ['/', '*', '+', '-']:
            current_tree.set_root_val(token)
            current_tree.insert_right('')
            pstack.push(current_tree)
            current_tree = current_tree.get_rightchild()
        elif token == ')':
            current_tree = pstack.pop()
        else:
            raise ValueError

    return pt


def postorderedeval(ptree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    res1 = None
    res2 = None

    if ptree:
        res1 = postorder(ptree.get_leftchild())
        res2 = postorder(ptree.get_rightchild())

        if res1 and res2:
            return opers[ptree.get_root_val()](res1, res2)
        else:
            return ptree.get_root_val()


def main():
    pt = parsetree("( ( 10 + 5 ) * ( 6 / 2 ) - ( 7 - 3 ) )")
    postorderedeval(pt)


if __name__ == '__main__':
    main()
