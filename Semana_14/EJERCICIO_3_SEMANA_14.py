class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self):
        self.root = None


    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._add(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add(data, node.right)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(f"{node.data} ", end="")
            self._print_tree(node.right)


bt = BinaryTree()
bt.add(0)
bt.add(1)
bt.add(2)
bt.add(3)
bt.add(4)
bt.add(5)

bt.print_tree() 
