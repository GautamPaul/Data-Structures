class Queue:
    def __init__(self, limit=10):
        self.queue = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0
        