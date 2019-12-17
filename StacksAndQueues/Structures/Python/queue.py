class Queue:
    def __init__(self):
        self.queue = []
    def add(self, item):
        self.queue.append(item)
    def remove(self):
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item
    def peek(self):
        return self.queue[-1]
    def is_empty(self):
        if self.queue:
            return False
        else:
            return True