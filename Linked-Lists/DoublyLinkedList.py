# class to represent node of Doubly Linked List
# methods: constructor(data, next, previous), getters and setters of data, next and previous; function of has_next and has_previous
class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next
    
    def set_previous(self, previous):
        self.previous = previous

    def get_previous(self):
        return self.previous
    
    def has_next(self):
        return self.next != None
    
    def has_previous(self):
        return self.previous != None
