# class to represent node of Doubly Linked List
# methods: constructor(data, next, previous), getters and setters of data, next and previous; function of has_next and has_previous
class Node:
    # constructor for initializing a node
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

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
    
    # getters and setters for previous
    def set_previous(self, previous):
        self.previous = previous

    def get_previous(self):
        return self.previous
    
    # returns True if node points to another node.
    # if a node has some next value, then next is not equal to None, condition passes thus True is returned.
    # if it is the last node, then next is None, conditions fails thus False is returned.
    def has_next(self):
        return self.next != None
    
    def has_previous(self):
        return self.previous != None


# class for Doubly Linked List
class DoublyLinkedList:
    # constructor for initializing Doubly Linked List
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # method to insert data at the end
    def insert_at_end(self, data):
        if self.head == None:                                       # check if the head is none, meaning of empty list
            self.head = Node(data)                                  # create a new node and set head to point to this new node
            self.tail = self.head                                   # set tail to point to head of the list
            self.length += 1                                        # increase length of the doubly linked list by 1
        else:
            current_node = self.head                                # set current node to point to the head
            while current_node.next != None:                        # iterate through the doubly linked list, check if it is the last node
                current_node = current_node.next                    # move to next node
            current_node.next = Node(data, None, current_node)      # create a new node with previous node set as the value of the current node, and assign it to current node
            self.tail = current_node.next                           # set tail of the doubly linked list to next of the current node, since current node is still pointing to the previously last node
            self.length += 1                                        # increase length of the doubly linked list by 1

    def insert_at_beginning(self, data):
        if self.head == None:                               # check if the head is None, that is if the doubly linked list is empty
            self.head = Node(data)                          # create a new node and assign it to head
            self.tail = self.head                           # assign the same to tail
            self.length += 1                                # increase the length of the doubly linked list by 1
        else:
            current_head = self.head                        # set current head
            self.head = Node(data, current_head, None)      # create a new node with next as the current head, then make this new node as head
            current_head.previous = self.head               # set previous of the current head value to point to the head
            self.length += 1                                # increase the length of the doubly linked list by 1

    def print_doubly_linked_list(self):
        doubly_linked_list = []                             # list to store the data of the nodes
        current_node = self.head                            # set current node to point to the head of the doubly linked list
        while current_node != None:                         # iterate till the current node becomes None
            doubly_linked_list.append(current_node.data)    # append the data in the list
            current_node = current_node.next                # move to next node
        print(doubly_linked_list)

dll = DoublyLinkedList()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.insert_at_beginning(-1)
dll.print_doubly_linked_list()