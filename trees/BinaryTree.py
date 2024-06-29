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

    # method to insert node in left of binary tree
    def insert_right(self, data):
        new_node = Node(data)           # create a new node with data
        if self.right is None:          # check if there is any right of binary tree
            self.right = new_node       # set right of binary tree to point to new node
        else:
            new_node.right = self.right # set right of new node to point to current right of binary tree
            self.right = new_node       # make this new node as right of binary tree
        self.root.right = self.right    # set right of binary tree to point to new node

    # method to get root of binary tree
    def get_root(self):
        return self.root

    @staticmethod       # made it static method to access without class
    def in_order_traversal_iterative(root):
        if not root:    # if there is not root, return
            return
        result = []
        stack = []
        current_node = root                         # set current node as root
        while True:
            # this condition is moving towards the left most node
            if current_node is not None:            # if there is current node
                stack.append(current_node)          # append the node in stack
                current_node = current_node.left    # move to left node
            # this condition left most node is reached, get data from this node 
            # and backtrack to node at the top of stack, then visit the right node
            elif stack:
                current_node = stack.pop()
                result.append(current_node.data)
                current_node = current_node.right
            else:
                print("in_order_traversal_iterative:",result)
                break

# recursive function for in order traversal
def in_order_traversal_recursive(root, result):
    if root is None:
        return
    in_order_traversal_recursive(root.left, result)     # move towards left
    result.append(root.data)                            # add data of node in result
    in_order_traversal_recursive(root.right, result)    # move towards right

# recursive function for pre order traversal
def pre_order_traversal_recursive(root, result):
    if root is None:
        return
    result.append(root.data)                            # add data of node in result
    pre_order_traversal_recursive(root.left, result)    # move towards left
    pre_order_traversal_recursive(root.right, result)   # move towards right

# method for pre order traversal
def pre_order_traversal_iterative(root):
    if root is None:
        return
    else:
        result = []
        stack = []                                      # stack to track nodes visited
        stack.append(root)                              # add root in stack
        # Pop all items one by one. Do following for every popped item
        # a) print it
        # b) push its right child
        # c) push its left child
        # Note that right child is pushed first so that left is processed first
        while stack:                                    # while the stack is not empty
            current_node = stack.pop()                  # get node from stack
            result.append(current_node.data)            # add data of current node to result
            if current_node.right is not None:          # check if current node has a right, and append in stack
                stack.append(current_node.right)
            if current_node.left is not None:           # check if current node has a left, and append in stack
                stack.append(current_node.left)
        print("pre_order_traversal_iterative:",result)

# recursive function for post order traversal
def post_order_traversal_recursive(root, result):
    if root is None:
        return
    post_order_traversal_recursive(root.left, result)    # move towards left
    post_order_traversal_recursive(root.right, result)   # move towards right
    result.append(root.data)                             # add data of node in result


def main():
    bt = BinaryTree(0)
    bt.insert_left(1)
    bt.insert_left(2)
    bt.insert_left(3)
    bt.insert_right(4)
    bt.insert_right(5)
    print(bt.left)
    print(bt.right)
    print(bt.root.right)
    print(bt.get_root())
    bt.in_order_traversal_iterative(bt.get_root())
    in_order_recursive_result = []
    in_order_traversal_recursive(bt.get_root(), in_order_recursive_result)
    print("in_order_recursive_result:",in_order_recursive_result)



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
    #         1
    #       /   \
    #      2     3
    #    /  \   /  \
    #   4    5 6    7
    bt.in_order_traversal_iterative(root_node)
    in_order_recursive_result = []
    in_order_traversal_recursive(root_node, in_order_recursive_result)
    print("in_order_recursive_result:",in_order_recursive_result)


    pre_order_recursive_result = []
    pre_order_traversal_recursive(root_node, pre_order_recursive_result)
    print("pre_order_recursive_result:",pre_order_recursive_result)

    pre_order_traversal_iterative(root_node)


    post_order_recursive_result = []
    post_order_traversal_recursive(root_node, post_order_recursive_result)
    print("post_order_recursive_result:",post_order_recursive_result)


if __name__ == "__main__":
    main()