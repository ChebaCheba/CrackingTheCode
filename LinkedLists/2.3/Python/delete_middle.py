import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import ListlessLinkedList

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
    llist = ListlessLinkedList()
    length = int(input("Introduce length of the list\n"))
    nodes = []
    for i in range(length):
        val = input("Introduce value of node\n")
        nodes.append(val)
    llist.create(nodes)    
    llist.print_list()
    mid_node = llist.return_node(random.randint(2,length-1))
    print("Node to be deleted: ("+str(mid_node.val)+")")
    delete_mid(mid_node)
    llist.print_list()