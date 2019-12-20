from .stack import Stack

class StackQueue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()
    def enqueue(self, item):
        self.first.push(item)
    def dequeue(self):
        if self.second.is_empty():
            if self.first.is_empty():
                return
            else:
                while not self.first.is_empty():
                    node = self.first.pop().val
                    self.second.push(node)
                popped = self.second.pop().val 
                node = self.second.pop().val
                self.first.push(node)
                return popped
        else:
            popped = self.first.pop()
            node = self.second.pop().val
            self.first.push(node)
            return popped
    def peek(self):
        return self.first.peek()
    def is_empty(self):
        return self.first.is_empty()
    def print_queue(self):
        string = ''
        if not self.second.is_empty():
            for i in range(self.second.stack_size):
                string += str(self.second.stack[i].val)+'|'
        if not self.first.is_empty():
            for i in range(self.first.stack_size-1):
                string += str(self.first.stack[self.first.stack_size-1-i].val)+'|'
            string += str(self.first.stack[0].val)
            print(string)
        else:
            print('|')