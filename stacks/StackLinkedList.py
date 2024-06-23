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
    # constructor for stack initialization
    def __init__(self):
        self.head = None
        self.length = 0
    
    # method to push the element in stack
    # Push operation is implemented by inserting element at the beginning of the list
    def push(self, data):
        new_node = Node(data)           # create a new node with data
        if self.length == 0:            # if stack is empty, set head to point to this new node
            self.head = new_node
        else:
            new_node.next = self.head   # set next of the new node to current head
            self.head = new_node        # make new node as head
        self.length += 1                # increase length by 1
    

    # method to print the stack
    # Note: this is printed in reverse order,
    # that is first element is top of stack and last element is bottom of stack
    def print_stack(self):
        if self.length == 0:                            # check if stack is empty
            print("Stack underflow. Empty stack.")
        else:
            stack_data = []                             # result list to store content of stack
            current_node = self.head                    # set head as current node
            while current_node != None:                 # loop till current node becomes None
                stack_data.append(current_node.data)    # add data of current node in result list
                current_node = current_node.next        # move to next node
            print(stack_data)

    # method to peek the top element in stack
    def peek(self):
        if self.length == 0:                            # check if stack is empty
            print("Stack underflow. Empty stack.")
        else:
            return self.head.data                       # return data of head node


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(5)
print(stack.peek())
stack.print_stack()