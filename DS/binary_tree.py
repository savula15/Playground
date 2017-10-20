class BinaryTree:

    def __init__(self, rootobj):
        self.key = rootobj
        self.leftchild = None
        self.rightchild = None

    def insert_left(self, newnode):
        if self.leftchild is None:
            self.leftchild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insert_right(self, newnode):
        if self.rightchild is None:
            self.rightchild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def get_rightchild(self):
        return self.rightchild

    def get_leftchild(self):
        return self.leftchild

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


def main():

    r = BinaryTree('a')
    print(r.get_root_val())
    print(r.get_leftchild())
    r.insert_left('b')
    print(r.get_leftchild())
    print(r.get_leftchild().get_root_val())
    r.insert_right('c')
    print(r.get_rightchild())
    print(r.get_rightchild().get_root_val())
    r.get_rightchild().set_root_val('hello')
    print(r.get_rightchild().get_root_val())

if __name__ == '__main__':
    main()
