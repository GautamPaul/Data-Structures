class Queue:
    def __init__(self, limit=10):
        self.queue = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def get_rear_element(self):
        if self.rear is None:
            return "Queue is empty."
        else:
            return self.queue[self.rear]

    def get_front_element(self):
        if self.front is None:
            return "Queue is empty."
        else:
            return self.queue[self.front]


queue = Queue(5)
print(queue.get_front_element())