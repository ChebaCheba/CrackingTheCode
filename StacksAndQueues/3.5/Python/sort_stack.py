import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.stack import Stack

def sort_stack(stack):
    sort_s = Stack()
    if stack.is_empty():
        return
    temp = stack.pop().val
    sort_s.push(temp)
    while not stack.is_empty():
        node = stack.pop().val
        while not sort_s.is_empty() and node < sort_s.peek().val:
            stack.push(sort_s.pop().val)
        sort_s.push(node)
    while not sort_s.is_empty():
        stack.push(sort_s.pop().val)
    return stack

if __name__ == "__main__":
    stack = Stack()
    elements = [6,7,9,8,5,3,1,6,7]
    for el in elements:
        stack.push(el)
    stack.print_stack()
    sorted_stack = sort_stack(stack)
    sorted_stack.print_stack()