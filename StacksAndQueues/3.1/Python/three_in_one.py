import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.three_stacks import ThreeInOne


if __name__ == "__main__":
    three = ThreeInOne()
    print(three.length)
    print(three.is_empty(1))
    three.push(6766, 2)
    three.push(6866, 2)
    three.push(6966, 3)
    print(three.stacks)
    for i in range(120):
        three.push(i+1000, 1)
    three.print_stack(1)
    print(three.length)
    print(three.pop(1).val)
    print(three.stacks)
    print(three.stack_size)
    three.print_stack(1)
    three.print_stack(2)
    three.print_stack(3)
    print(three.peek(1).val)
    print(three.is_empty(1))