# class for Node of binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"Data: {self.data}"

def post_order_iterative(root, result):
    if not root:
        return
    #         1
    #       /   \
    #      2     3
    #    /  \   /  \
    #   4    5 6    7
    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None


left_node = Node(2)
left_node.left = Node(4)
left_node.right = Node(5)
#      2
#    /  \
#   4    5

right_node = Node(3)
right_node.left = Node(6)
right_node.right = Node(7)

#            3
#           /  \
#          6    7

root_node = Node(1)
#         1

root_node.left = left_node
root_node.right = right_node
post_order_iterative_result = []
post_order_iterative(root_node, post_order_iterative_result)
print("post_order_iterative_result:",post_order_iterative_result)