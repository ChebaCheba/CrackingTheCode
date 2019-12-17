class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return
    def push(self, item):
        self.stack.append(item)
        return
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return
    def is_empty(self):
        if self.stack:
            return False
        else:
            return True