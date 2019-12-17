import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import ListlessLinkedList

def is_palindrome(llist, length = 0):
    node = llist.head
    mid = 0
    even = False
    stack = []
    if length:
        if length%2==0:
            mid = length/2
            even = True
        else:
            mid = length//2 + 1
        for i in range(mid):
            stack.append(node.val)
            node = node.next
        if not even:
            stack.pop()
        while node != None:
            letter = stack.pop()
            if letter != node.val:
                return False
            node = node.next
        return True     
    else:
        count = 0
        while node != None:
            count+=1
            node = node.next
        return is_palindrome(llist, count)

if __name__=="__main__":
    llist = ListlessLinkedList()
    string = list(input("Introduce a word\n"))
    llist.create(string)
    llist.print_list()
    is_pal = is_palindrome(llist)
    if is_pal:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome")
