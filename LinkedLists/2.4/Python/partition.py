import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import ListlessLinkedList

def partition(head, num):
    node = head
    part_node = None
    while node.next != None:
        if node.val >= num:
            if not part_node:
                part_node = node
            temp = part_node.val
            sw_node = part_node.next
            while sw_node != None:
                if sw_node.val < num:
                    part_node.val = sw_node.val
                    sw_node.val = temp
                    part_node = part_node.next
                    break
                else:
                    sw_node = sw_node.next
            node = sw_node
        else:
            node = node.next

if __name__=="__main__":
    llist = ListlessLinkedList()
    length = int(input("Introduce length of the list\n"))
    nodes = []
    for i in range(length):
        val = int(input("Introduce value of node\n"))
        nodes.append(val)
    num = int(input("Introduce partition number\n"))
    llist.create(nodes)    
    llist.print_list()
    partition(llist.head, num)
    llist.print_list()