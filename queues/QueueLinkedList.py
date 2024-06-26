# class for node of Queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"Data: {self.data}"

# class for queue
class Queue:
    # constructor of queue
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    # method to enqueue element at end of the queue
    def enqueue(self, data):
        new_node = Node(data)                   # create a new node with data
        if not self.rear:                       # check if queue is empty
            self.front = self.rear = new_node   # set front and rear to point to new node
        else:
            self.rear.next = new_node           # set next of current rear to point to new node
            self.rear = new_node                # set new node as the new rear
        self.size += 1                          # increase size of queue by 1

    # method to dequeue element from the start of the queue
    def dequeue(self):
        if self.size == 0:                      # check if queue is empty
            print("Queue is empty.")
            return
        else:
            current_front = self.front          # get current front
            self.front = self.front.next        # set front to point to next of current front
            if not self.front:                  # if queue becomes empty
                self.rear = None                # set rear as None
            self.size -= 1                      # decrease size of queue by 1
            return current_front.data


    # method to print elements in queue
    def print_queue(self):
        nodes = []
        current_node = self.front               # set front as current node
        while current_node != None:             # iterate till current node becomes None
            nodes.append(current_node.data)     # append data in result
            current_node = current_node.next    # move to next node
        print(nodes)


queue = Queue()
queue.print_queue()
print(queue.dequeue())
print(queue.front, queue.rear)
queue.enqueue(1)
print(queue.front, queue.rear)
print(queue.dequeue())
queue.enqueue(2)
print(queue.front, queue.rear)
queue.enqueue(3)
print(queue.front, queue.rear)


queue.print_queue()
