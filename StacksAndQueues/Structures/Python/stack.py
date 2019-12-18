class Node:
    def __init__(self, val):
        self.val = val
        self.min = None

class Stack:
    def __init__(self, mins = False):
        self.stack = []
        self.mins = mins
    def pop(self):
        if self.stack:
            return self.stack.pop()
    def push(self, item):
        node = Node(item)
        if not self.is_empty() and self.mins:
            prev_node = self.peek().min
            if prev_node < item:
                node.min = prev_node
            else:
                node.min = item
        else:
            node.min = item 
        self.stack.append(node)
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def is_empty(self):
        if self.stack:
            return False
        else:
            return True
    def print_stack(self):
        string = ''
        if not self.is_empty():
            for i in range(len(self.stack)-1):
                string += str(self.stack[i].val)+'|'
            string += str(self.stack[-1].val)
            print(string)
        else:
            print('|')