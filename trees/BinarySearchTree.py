from typing import Optional

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Data: {self.data}"

def insert_node(root: Optional[BSTNode], node: BSTNode):
    if root is None:
        root = node
    else:
        if node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                insert_node(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert_node(root.right, node)
            


def main():
    root = BSTNode(10)
    print(root.left)
    print(root.right)
    insert_node(root, BSTNode(3))
    insert_node(root, BSTNode(14))
    print(root.left)
    print(root.right)
       


if __name__ == "__main__":
    main()