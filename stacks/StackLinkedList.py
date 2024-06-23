# class for node of linked list
class Node:
    # constructor for initializing a Node
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # getters and setters for data
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    # getters and setters for next
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next
    
    # returns True if node points to another node.
    def has_next(self):
        return self.next != None
    
    def __str__(self):
        return f"Data: {self.data}"

# class for Stack using Linked List
class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
    
    # method to push the element in stack
    # Push operation is implemented by inserting element at the beginning of the list
    def push(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    

    def print_stack(self):
        if self.length == 0:
            print("Stack underflow. Empty stack.")
        else:
            stack_data = []
            current_node = self.head
            while current_node != None:
                stack_data.append(current_node.data)
                current_node = current_node.next
            print(stack_data)


stack = Stack()
stack.push(1)
stack.push(2)
stack.print_stack()