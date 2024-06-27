# class for Node of binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Data: {self.data}"


# class for Binary Tree
class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
        self.left = None
        self.right = None

    # method to insert node in left of binary tree
    def insert_left(self, data):
        new_node = Node(data)           # create a new node with data
        if self.left is None:           # check if there is any left of binary tree
            self.left = new_node        # set left of binary tree to point to new node
        else:
            new_node.left = self.left   # set left of new node to point to current left of binary tree
            self.left = new_node        # make this new node as left of binary tree
        self.root.left = self.left      # set left of root to point to left of binary tree

    def insert_right(self, data):
        new_node = Node(data)           # create a new node with data
        if self.right is None:          # check if there is any right of binary tree
            self.right = new_node       # set right of binary tree to point to new node
        else:
            new_node.right = self.right # set right of new node to point to current right of binary tree
            self.right = new_node       # make this new node as right of binary tree
        self.root.right = self.right    # set right of binary tree to point to new node

bt = BinaryTree(0)
bt.insert_left(1)
bt.insert_left(2)
bt.insert_left(3)
bt.insert_right(4)
bt.insert_right(5)
print(bt.left)
print(bt.right)
print(bt.root.right)
