class Node:
    def __init__(self, val):
        self.val = val
        self.timestamp = None

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item, timestamp = None):
        node = Node(item)
        node.timestamp = timestamp
        self.queue.append(node)
    def dequeue(self):
        node = self.queue[0]
        self.queue = self.queue[1:]
        return node
    def peek(self):
        return self.queue[-1]
    def first(self):
        return self.queue[0]
    def is_empty(self):
        if self.queue:
            return False
        else:
            return True
    def print_queue(self):
        string = ''
        if self.queue:
            for i in range(len(self.queue)-1):
                string += str(self.queue[i].val)+'|'
            string += str(self.queue[-1])
        else:
            string = '|'
        print(string)