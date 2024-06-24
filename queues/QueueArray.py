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

    def enqueue(self, data):
        if self.size == self.limit:
            print("Queue Overflow.")
            return
        else:
            self.queue.append(data)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue Underflow.")
            return
        else:
            self.queue.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size-1

queue = Queue(5)
print(queue.get_front_element())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()

print(queue.queue)
print(queue.get_rear_element())
print(queue.get_front_element())