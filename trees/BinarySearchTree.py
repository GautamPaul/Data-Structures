from typing import Optional

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Data: {self.data}"

# method to insert node in Binary Search Tree
def insert_node(root: Optional[BSTNode], node: BSTNode):
    if root is None:                            # check if root is present, if not this node will become root
        root = node
    else:
        if node.data < root.data:               # if data in node is less than data in root
            if root.left is None:               # if left of root is empty, set left of root to as node
                root.left = node
            else:
                insert_node(root.left, node)    # traverse to the left
        else:
            if root.right is None:              # if right of root is empty, set right of root to as node
                root.right = node
            else:
                insert_node(root.right, node)   # traverse to the right


# method to find a given node
def find_node(root: BSTNode, data):
    current_node = root                                             # start with root node as the current node
    while current_node is not None or current_node.data != data:    # iterate till current node becomes None, that is it reaches the leaf node
        if current_node.data == data:                               # if current node has the data, return the node
            return current_node
        elif data > current_node.data:                              # if target data is greater than current node's data, move right
            current_node = current_node.right
        else:                                                       # else move left
            current_node = current_node.left

# method to find the minimum node in BST
def find_minimum_node(root: BSTNode):
    current_node = root                     # set root as current node
    while current_node.left is not None:    # iterate till the left most node in the BST
        current_node = current_node.left
    return current_node

# method to find the minimum node in BST
def find_maximum_node(root: BSTNode):
    current_node = root                     # set root as current node
    while current_node.right is not None:   # iterate till the right most node in the BST
        current_node = current_node.right
    return current_node

#method for in order traversal
def in_order_traversal(root: Optional[BSTNode]):
    if not root:
        return
    in_order_traversal(root.left)           # recursive call towards left
    print(root.data, end=" ")               # printing data of root
    in_order_traversal(root.right)          # recurdive call towards right
            


def main():
    root = BSTNode(10)
    print(root.left)
    print(root.right)
    insert_node(root, BSTNode(3))
    insert_node(root, BSTNode(14))
    print(root.left)
    print(root.right)
    in_order_traversal(root)
    print()
    print(find_minimum_node(root).data)
    print(find_maximum_node(root).data)
    print(find_node(root, 14))
    print(find_node(root, 3))
    
       


if __name__ == "__main__":
    main()