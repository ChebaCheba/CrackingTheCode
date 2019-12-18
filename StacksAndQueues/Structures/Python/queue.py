class Node:
    def __init__(self, val):
        self.val = val

class Queue:
    def __init__(self):
        self.queue = []
    def add(self, item):
        node = Node(item)
        self.queue.append(node)
    def remove(self):
        node = self.queue[0]
        self.queue = self.queue[1:]
        return node
    def peek(self):
        return self.queue[-1].val
    def is_empty(self):
        if self.queue:
            return False
        else:
            return True