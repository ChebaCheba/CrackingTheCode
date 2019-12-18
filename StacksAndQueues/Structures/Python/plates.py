from .stack import Stack

class StackOfPlates:
    def __init__(self, threshold):
        self.stacks = []
        self.push_index = Stack()
        self.threshold = threshold
    def push(self, item):
        if not self.stacks:
            self.stacks.append(Stack())
        if not self.push_index.is_empty():
            index = self.push_index.pop().val
            self.stacks[index].push(item)
            return
        if self.stacks[-1].stack_size==self.threshold:
            self.stacks.append(Stack())
        self.stacks[-1].push(item)
    def pop(self):
        if self.stacks:
            popped = self.stacks[-1].pop()
            if self.stacks[-1].is_empty():
                self.stacks.pop()
            return popped
    def peek(self):
        if self.stacks:
            return self.stacks[-1].peek()
    def is_empty(self):
        if self.stacks:
            return False
        else:
            return True
    def print_stacks(self):
        for stack in self.stacks:
            stack.print_stack()

