class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Data: {self.data}"


class BinaryTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None
    
    def insert_left(self, data):
        new_node = Node(data)
        if self.left is None:
            self.left = new_node
        else:
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, data):
        new_node = Node(data)
        if self.right is None:
            self.right = new_node
        else:
            new_node.right = self.right
            self.right = new_node

bt = BinaryTree()
bt.insert_left(1)
bt.insert_left(2)
bt.insert_left(3)
bt.insert_right(4)
bt.insert_right(5)
print(bt.left)
print(bt.right)
