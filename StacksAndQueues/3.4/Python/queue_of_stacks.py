import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.stack_queue import StackQueue

if __name__=="__main__":
    queue = StackQueue()
    print(queue.is_empty())
    for i in range(30):
        queue.enqueue(i)
    queue.print_queue()
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()
    print(queue.peek().val)
    print(queue.is_empty())
