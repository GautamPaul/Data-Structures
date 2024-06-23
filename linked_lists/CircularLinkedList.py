# class to represent node of Circular Linked List
# methods: constructor(data, next), getters and setters of data and next
class Node:
    # constructor for initializing a Node
    def __init__(self, data):
        self.data = data
        self.next = None

    # getters and setters for data
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

    # getters and setters for next
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

    def __str__(self):
        return f"Data: {self.data}"


# class for Circular Linked List
class CircularLinkedList:
    #constructor for initializing circular linked list 
    def __init__(self):
        self.head = None
        self.length = 0

    # method to add node at the beginning
    def add_node_at_beginning(self, data):
        new_node = Node(data)                       # create a new node with given data
        if self.head:                               # check if there are nodes present
            current_node = self.head                # set current node to point head
            while current_node.next != self.head:   # loop till current node has next point to head, means it will be last node
                current_node = current_node.next    # move to next node
            new_node.next = self.head.next          # set next of the new node to point to the next of the current head
            self.head = new_node                    # set head to point to the new node
            current_node.next = self.head           # set next of the last node to point to head
        else:
            # no nodes
            new_node.next = new_node                # set next of the new node to point to itself
            self.head = new_node                    # set head to point to new node
        self.length += 1                            # increase length of the circular linked list by 1


    # method to print the nodes in the circular linked list
    def print_circular_linked_list(self):
        if self.length == 0:                                    # check if length of circular linked list is 0
            print("No elements in Circular Linked List")
        elif self.length == 1:                                  # check if there is only one node
            print(f"[{self.head.data}]")
        else:                                                   # for more than 1 nodes
            circular_linked_list = [self.head.data]             # set data of the first node
            current_node = self.head.next                       # set head to point to the second node
            while current_node != self.head:                    # iterate till current node is head
                circular_linked_list.append(current_node.data)  # append data of the current node
                current_node = current_node.next                # move to next node
            print(circular_linked_list)



def main():
    cll = CircularLinkedList()
    print("cll initialized. printing.")
    cll.print_circular_linked_list()
    print("inserting 1 at beginning")
    cll.add_node_at_beginning(1)
    print("inserting 2 at beginning")
    cll.add_node_at_beginning(2)
    print("printing cll")
    cll.print_circular_linked_list()

if __name__ == "__main__":
    main()