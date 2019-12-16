import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import ListlessLinkedList


def sum_lists_reversed(llist1, llist2):
    num1 = ''
    num2 = ''
    node1 = llist1.head
    node2 = llist2.head
    while node1 != None and node2 != None:
        if node1:
            num1 = str(node1.val)+num1
            node1 = node1.next
        if node2:
            num2 = str(node2.val)+num2
            node2 = node2.next
    sum = str(int(num1)+int(num2))
    sum_llist = ListlessLinkedList()
    sum_llist.create(sum[::-1])
    return sum_llist

def sum_lists(llist1, llist2):
    num1 = ''
    num2 = ''
    node1 = llist1.head
    node2 = llist2.head
    while node1 != None and node2 != None:
        if node1:
            num1 += str(node1.val)
            node1 = node1.next
        if node2:
            num2 += str(node2.val)
            node2 = node2.next
    sum = str(int(num1)+int(num2))
    sum_llist = ListlessLinkedList()
    sum_llist.create(sum)
    return sum_llist

if __name__=="__main__":
    n1 = list(input("Introduce first number\n"))
    n2 = list(input("Introduce second number\n"))
    reversed = input("Are the numbers reversed? Say yes or no")
    llist1 = ListlessLinkedList()
    llist1.create(n1)
    llist2 = ListlessLinkedList()
    llist2.create(n2)
    if reversed == "yes":
        sum_llist = sum_lists_reversed(llist1, llist2)
    else:
        sum_llist = sum_lists(llist1, llist2)
    sum_llist.print_list()