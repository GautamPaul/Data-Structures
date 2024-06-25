# class for Queue
class Queue:
    # constructor for queue
    def __init__(self, limit=10):
        self.queue = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    # method to check if queue is empty
    def is_empty(self):
        return self.size == 0

    # method to get current size of queue
    def get_size(self):
        return self.size

    # method to get current rear element of the queue
    def get_rear_element(self):
        if self.rear is None:
            return "Queue is empty."
        else:
            return self.queue[self.rear]    # return element at position pointed by rear

    # method to get current front element
    def get_front_element(self):
        if self.front is None:
            return "Queue is empty."
        else:
            return self.queue[self.front]   # return element at position pointed by current front

    # method to enqueue an element in the queue
    def enqueue(self, data):
        if self.size == self.limit:         # condition for full queue
            print("Queue Overflow.")
            return
        else:
            self.queue.append(data)         # append data at last of queue
        if self.front is None:              # if the queue was empty
            self.front = self.rear = 0      # set front and rear to point to 0
        else:
            self.rear = self.size           # set rear to point to current size of the queue
        self.size += 1                      # increase size of the queue by 1

    def dequeue(self):
        if self.size == 0:                      # condition for full queue
            print("Queue Underflow.")
            return
        else:
            self.queue.pop(0)                   # pop element from start. pop takes default value as -1
            self.size -= 1                      # decrease size of queue by 1
            if self.size == 0:                  # if size has become, that means queue has became empty
                self.front = self.rear = None   # set front and read as None
            else:
                self.rear = self.size-1         # set rear to size - 1

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