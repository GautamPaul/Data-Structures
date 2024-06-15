# node of Linked List: constructor(data, next), getters and setters of data and next, function of has_next
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
    # if a node has some next value, then next is not equal to None, condition passes thus True is returned.
    # if it is the last node, then next is None, conditions fails thus False is returned.
    def has_next(self):
        return self.next != None
    

# class for Linked List
class LinkedList():
    #constructor for initializing linked list 
    def __init__(self):
        self.length = 0
        self.head = None

    # method to add node in linked list
    # check if the length of the linked list is 0, if so add the node at beginning of the list, else add at the end of the list
    def add_node(self, node):
        if self.length == 0:
            self.add_node_at_beginning(node)
        else:
            self.add_node_at_last(node)

    # method to add node at the beginning of the linked list
    def add_node_at_beginning(self, node):
        new_node = node                 # create a temporary node
        new_node.next = self.head       # set next of temporary node to be current head of linked list
        self.head = new_node            # set head of the linked list to the temporary node
        self.length += 1                # increase length of the linked list by 1

    # method to add node at the last
    def add_node_at_last(self, node):
        current_node = self.head                # set head as the current node
        while current_node.next != None:        # iterate to find the last node of the linked list
            current_node = current_node.next
        new_node = node                         # create temporary node(this will be new last node)
        new_node.next = None                    # set next of temporary node to None
        current_node.next = new_node            # set next of current node(earlier last node) to point the new last node
        self.length += 1                        # increase length of the linked list by 1

    
    # method to insert data in linked list
    def insert_data(self, data):
        if self.length == 0:
            self.insert_data_at_beginning(data)
        else:
            self.insert_data_at_last(data)

    # method to insert data at the beginning of the linked list
    def insert_data_at_beginning(self, data):
        new_node = Node(data)           # create a new node with data
        self.head = new_node            # set head of the linked list to point to new node
        self.length += 1                # increase length of the linked list by 1


    # method to insert data at the end of the linked list
    def insert_data_at_last(self, data):
        current_node = self.head                # set head as the current node
        while current_node.next != None:        # iterate to find the last node of the linked list
            current_node = current_node.next

        new_node = Node(data)                   # create temporary node(this will be new last node)
        new_node.next = None                    # set next of temporary node to None
        current_node.next = new_node            # set next of current node(earlier last node) to point the new last node
        self.length += 1                        # increase length of the linked list by 1

    def print_linked_list(self):
        linked_list = []
        current_node = self.head
        while current_node != None:
            linked_list.append(current_node.data)
            current_node = current_node.next
        print(linked_list)

node1 = Node(1)
node2 = Node(2)
ll = LinkedList()
ll.add_node(node1)
ll.add_node(node2)
ll.insert_data(3)
ll.print_linked_list()

