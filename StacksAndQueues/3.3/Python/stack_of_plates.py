import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.plates import StackOfPlates
from Structures.Python.stack import Stack

def pop_at(plates, index):
        if not abs(index) < len(plates.stacks):
            return
        plates.push_index.push(index)
        popped = plates.stacks[index].pop()
        if plates.stacks[index].is_empty():
            if index > plates.stacks[index].stack_size-1:
                plates.stacks = plates.stacks[:index]+plates.stacks[index+1:]
            else:
                plates.stacks = plates.stacks[:index]
            new_stack = Stack()
            for i in range(plates.push_index.stack_size):
                temp = plates.push_index.pop().val
                if not temp == index:
                    new_stack.push(temp)
            plates.push_index = new_stack
        return popped

if __name__=="__main__":
    threshold = int(input("Introduce threshold\n"))
    plates = StackOfPlates(threshold)
    num_items = int(input("Introduce number of items to be pushed\n"))
    for i in range(num_items):
        item = int(input("Introduce item\n"))
        plates.push(item)
    plates.print_stacks()
    pop_at(plates, 0)
    pop_at(plates, 0)
    plates.push(33)
    print('')
    plates.print_stacks()
    pop_at(plates, 0)
    print('')
    plates.print_stacks()
    plates.push(33)
    print('')
    plates.print_stacks()