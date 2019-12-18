import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.stack import Stack

def return_min(stack):
    top = stack.peek()
    if top:
        return top.min
    return

if __name__=="__main__":
    stack = Stack(True)
    stack_size = int(input("Introduce size of stack\n"))
    for i in range(stack_size):
        item = int(input("Introduce item\n"))
        stack.push(item)
    stack.print_stack()
    print('The minimum value is',return_min(stack))
    stack.pop()
    print('The minimum value is',return_min(stack))