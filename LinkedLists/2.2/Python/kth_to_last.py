import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import LinkedList

def return_kth_to_last(llist, k,length = 0):
    if length:
        dif = length - k - 1
        node = llist.head
        for i in range(dif):
            node = node.next
        return node.val
    else:
        node = llist.head
        k_element = node
        while node.next != None:
            length+=1
            node = node.next
            if length>k:
                k_element = k_element.next
        return k_element.val
    
if __name__=="__main__":
    len_list = int(input("Introduce length of the linked list\n"))
    llist = LinkedList()
    for i in range(len_list):
        node = int(input("Introduce value of node\n"))
        llist.add_node(node)
    k = int(input("Introduce k\n"))
    llist.print_list()
    #with lenght
    print(return_kth_to_last(llist, k,len_list))
    #without length
    print(return_kth_to_last(llist, k))