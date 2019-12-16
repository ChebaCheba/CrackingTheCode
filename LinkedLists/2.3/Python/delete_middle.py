import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import Node

def delete_mid(mid_node):
    node = mid_node
    while node.next.next != None:
        node.val = node.next.val
        node = node.next
    node.val = node.next.val
    node.next = None

def print_list(node):
    string = ''
    while node.next != None:
        string+='('+str(node.val)+')=>'
        node = node.next
    string+='('+str(node.val)+')'
    print(string)

if __name__=="__main__":
    length = int(input("Introduce length of the list\n"))
    prev_node = None
    nodes = []
    head = None
    for i in range(length):
        val = int(input("Introduce value of node\n"))
        node = Node(val)
        nodes.append(node)
        if prev_node:
            prev_node.next = node
            prev_node = node
        else:
            head = node
            prev_node = node
    print_list(head)
    mid_node = nodes[random.randint(1,length-2)]
    print("Node to be deleted: ("+str(mid_node.val)+")")
    delete_mid(mid_node)
    print_list(head)