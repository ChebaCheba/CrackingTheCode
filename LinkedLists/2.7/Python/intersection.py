import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import ListlessLinkedList

def intersect(llist1, llist2):
    len1 = 0
    len2 = 0
    node1 = llist1.head
    node2 = llist2.head
    while node1 != None or node2 != None:
        if node1:
            len1 += 1
            node1 = node1.next
        if node2:
            len2 += 1
            node2 = node2.next
    node1 = llist1.head
    node2 = llist2.head
    length = len1
    if len1 > len2:
        length = len2
        for i in range(len1-len2):
            node1 = node1.next
    elif len2 > len1:
        for i in range(len2-len1):
            node2 = node2.next
    while node1.next != None and node2.next != None:
        if node1.next == node2.next:
            return node1.next
        else:
            node1 = node1.next
            node2 = node2.next
    
if __name__ == "__main__":
    llist1 = ListlessLinkedList()
    llist2 = ListlessLinkedList()
    nodes1 = [0,1,2,3,4,5]
    nodes2 = [0,9,8,3,3,3,3,3]    
    llist1.create(nodes1)
    llist2.create(nodes2)

    node = llist1.head
    for i in range(3):
        node = node.next
    llist2.tail.next = node
    llist2.tail = llist1.tail
    
    llist1.print_list()
    llist2.print_list()

    inter_node = intersect(llist1, llist2)
    print('The intersection node is ('+str(inter_node.val)+')')

