import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import ListlessLinkedList

def detect_loop(llist):
    node = llist.head
    hare = node.next.next
    turtle = node.next
    count = 1
    while turtle != hare:
        if hare == None:
            return None
        count += 1
        hare = hare.next.next
        turtle = turtle.next
    col_point = hare
    loop_start = llist.head
    num_node = 1
    while col_point != loop_start:
        num_node += 1
        col_point = col_point.next
        loop_start = loop_start.next
    return loop_start.val, num_node


if __name__=="__main__":
    llist = ListlessLinkedList()
    nodes = [1,3,4,4,4,6,7,8,9]
    llist.create(nodes)
    node = llist.head
    for i in range(5):
        node = node.next
    llist.tail.next = node
    llist.print_list(loop=True)
    loop_node, num_node = detect_loop(llist)
    print("The loop starts at node number",num_node,"and its value is (",loop_node,")")