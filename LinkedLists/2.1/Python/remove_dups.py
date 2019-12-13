import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.linked_list import LinkedList

def remove_dups(llist):
    temp = set()
    i = 0
    while i < len(llist.nodes):
        if llist.nodes[i].val not in temp:
            temp.add(llist.nodes[i].val)
            i+=1
        else:
            llist.delete_node_by_index(i)
    return llist        

if __name__=="__main__":
    len_list = int(input("Introduce length of the linked list\n"))
    llist = LinkedList()
    for i in range(len_list):
        node = int(input("Introduce value of node\n"))
        llist.add_node(node)
    llist.print_list()
    llist = remove_dups(llist)
    llist.print_list()