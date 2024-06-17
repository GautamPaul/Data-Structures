# class to represent node of Linked List
# methods: constructor(data, next), getters and setters of data and next, function of has_next
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
    def add_node(self, node: Node):
        if self.length == 0:
            self.add_node_at_beginning(node)
        else:
            self.add_node_at_last(node)

    # method to add node at the beginning of the linked list
    def add_node_at_beginning(self, node: Node):
        new_node = node                 # create a temporary node
        new_node.next = self.head       # set next of temporary node to be current head of linked list
        self.head = new_node            # set head of the linked list to the temporary node
        self.length += 1                # increase length of the linked list by 1

    # method to add node at the last
    def add_node_at_last(self, node: Node):
        current_node = self.head                # set head as the current node
        while current_node.next != None:        # iterate to find the last node of the linked list
            current_node = current_node.next
        new_node = node                         # create temporary node(this will be new last node)
        new_node.next = None                    # set next of temporary node to None
        current_node.next = new_node            # set next of current node(earlier last node) to point the new last node
        self.length += 1                        # increase length of the linked list by 1


    # method to insert node after a certain with given data
    def add_node_after_value(self, data, node: Node):
        new_node = node                 # create temporary node 
        current_node = self.head        # set head of linked list as the current node

        # iterate through the linked list, till the last node is reached(current_node.next != None)
        # or the data of the current node is the data after which the new node has to be added(current_node.data != data)
        while current_node.next != None or current_node.data != data:
            if current_node.data == data:               # if the current node has the data after which the node has to be added
                new_node.next = current_node.next       # set next of the new node to point to the next pointed by the current node
                current_node.next = new_node            # set next of the current node to the newly added node
                self.length += 1                        # increase length of the linked list by 1
                return
            else:
                current_node = current_node.next        # move to next node in the linked list
            
        # if flow reaches the end of linked list, it means provided data is not present
        print(f"The data provided, {data}, is not present in the linked list.")

    
    # method to add node at given position
    def add_node_at_position(self, position, new_node):
        count = 0                       # count variable to track position
        previous_node = self.head       # set head as previous node
        current_node = self.head        # set head as current node

        # if the position given is greater than current list length, or lesser than 0, then it is invalid position
        if position>self.length or position<1:
            print(f"The given position does not exist in linked list. Positions available: 0-{self.length}")
        elif position == 1:                             # if the target position is 1
            self.add_node_at_beginning(new_node)        # then the node has to be added at beginning
        else:
            # iterate through list till last node is reached or count goes past given position
            while current_node.next != None or count<position:
                count += 1                              # firstly, increase count position by 1, since it is initialized at 0
                if count == position:                   # if the position is reached
                    previous_node.next = new_node       # set next of previous node to point the new node
                    new_node.next = current_node        # set next of new node to point to the current node
                    self.length += 1                    # increase length of linked list by 1
                    return
                else:
                    previous_node = current_node        # the current node will now become previous node
                    current_node = current_node.next    # move to the next node


    
    # method to insert data in linked list
    def insert_data(self, data):
        if self.length == 0:
            self.insert_data_at_beginning(data)
        else:
            self.insert_data_at_last(data)

    # method to insert data at the beginning of the linked list
    def insert_data_at_beginning(self, data):
        new_node = Node(data)           # create a new node with data
        new_node.next = self.head       # set next of new node to point current head
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

    # method to insert data after some value
    def insert_data_after_value(self, data, after_value):
        current_node = self.head                    # set head of linked list as the current node

        # iterate through the linked list, till the last node is reached(current_node.next != None)
        # or the data of the current node is the data after which the new node has to be added(current_node.data != data)
        while current_node.next != None or current_node.data != after_value:
            if current_node.data == after_value:        # if the current node has the data after which the node has to be added
                new_node = Node(data)                   # create a new node with the provided data
                new_node.next = current_node.next       # set next of the new node to point to the next pointed by the current node
                current_node.next = new_node            # set next of the current node to the newly added node
                self.length += 1                        # increase length of the linked list by 1
                return
            else:
                current_node = current_node.next        # move to next node of the linked list
        print(f"The data provided, {after_value}, is not present in the linked list.")


    # method to insert data at given position
    def insert_data_at_position(self, position, data):
        count = 0                       # set count to track position
        previous_node = self.head       # set previous node to point at head of linked list
        current_node = self.head        # set current node to point at head of linked list

        # check if position is valid
        if position>self.length or position<1:
            print(f"The given position does not exist in linked list. Positions available: 0-{self.length}")
        elif position == 1:                         # if position is 1
            self.insert_data_at_beginning(data)     # insert data at the beginning of the linked list
        else:
            # iterate through list till last node is reached or count goes past given position
            while current_node.next != None or count<position:
                count += 1                              # firstly, increase count position by 1, since it is initialized at 0
                if count == position:                   # if the position is reached
                    new_node = Node(data)               # create a new node with the given data
                    new_node.next = current_node        # set next of the new node to point at the current node
                    previous_node.next = new_node       # set next of the previous node to point at the new node
                    self.length += 1                    # increase length of the linked list by 1
                    return
                else:
                    previous_node = current_node        # if the position is reached
                    current_node = current_node.next    # move to next node

    # method to delete node from beginning
    def delete_from_beginning(self):
        if self.length == 0:                        # condition to check if the linked list is empty
            print("The linked list is empty.")
        else:
            self.head = self.head.next              # set head to point to the next of the head
            self.length -= 1                        # decrease the length of the linked list by 1

    # method to delete node from last
    def delete_from_last(self):
        if self.length == 0:                        # condition to check if the linked list is empty
            print("The linked list is empty.")
        else:
            current_node = self.head                # set current node to point at head of linked list
            previous_node = self.head               # set previous node to point at head of linked list
            while current_node.next != None:        # iterate through the linked list till the last node
                previous_node = current_node        # set previous node to point to current node
                current_node = current_node.next    # move to next node
            previous_node.next = None               # set next of previous node to point to None, making it last node
            self.length -= 1                        # decrease the length of the linked list by 1

    # method to get length of the linked list
    def get_length(self):
        return self.length
    
    # method to get first element of the linked list
    def get_first_element(self):
        if self.length == 0:                        # condition to check if the linked list is empty
            print("The linked list is empty.")
            return None
        else:
            return self.head.data                   # since head points to the first element of the linked list, return its data

    # method to get last element of the linked list
    def get_last_element(self):
        if self.length == 0:                        # condition to check if the linked list is empty
            print("The linked list is empty.")
            return None
        else:
            current_node = self.head                # set current node to point to the head of the linked list
            while current_node.next != None:        # iterate through the linked list till the last node, which will have next as None
                current_node = current_node.next

            return current_node.data                # return data of the node


    # method to print content of linked list
    def print_linked_list(self):
        linked_list = []
        current_node = self.head                    # set head as current node
        while current_node != None:                 # iterate through the linked list
            linked_list.append(current_node.data)   # add the data of current node to result
            current_node = current_node.next        # set next node as current node
        print(linked_list)

node1 = Node(1)
node2 = Node(2)
ll = LinkedList()
ll.get_first_element()
ll.get_last_element()
ll.add_node(node1)
ll.add_node(node2)
ll.insert_data(3)
ll.add_node_after_value(1,Node(5))
ll.print_linked_list()

ll.insert_data_after_value(6, 5)
ll.print_linked_list()


ll.add_node_at_position(5, Node(7))
ll.print_linked_list()

ll.insert_data_at_position(6,8)
ll.print_linked_list()


print("Length:",ll.get_length())
print("First element:",ll.get_first_element())
print("Last element:",ll.get_last_element())

ll.print_linked_list()
print("Deleting from beginning")
ll.delete_from_beginning()
ll.print_linked_list()
print("Deleting from last")
ll.delete_from_last()
ll.print_linked_list()