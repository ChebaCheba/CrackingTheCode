import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.binary_search_tree import BinarySearchTree 

def minimal_tree(array, minimal_t = None):
    first = False
    if not minimal_t:
        minimal_t = BinarySearchTree()
        first = True
    if len(array)==1:
        minimal_t.insert_node(array[0])
        return
    elif len(array)<1:
        return
    mid = int(len(array)//2)
    minimal_t.insert_node(array[mid])
    minimal_tree(array[:mid], minimal_t)
    minimal_tree(array[mid+1:], minimal_t)
    if first:
        return minimal_t

if __name__=="__main__":
    array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    minimal_t = minimal_tree(array)
    minimal_t.print_tree()
    
