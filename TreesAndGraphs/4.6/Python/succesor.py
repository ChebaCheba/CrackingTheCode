import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.binary_search_tree import BinarySearchTree

def get_succesor(node):
    if node.right != None:
        min_tree = node.right
        while min_tree.left != None:
            min_tree = min_tree.left
        return min_tree
    node_trav = node.parent
    while node_trav != None and node == node_trav.right:
        node = node_trav
        node_trav = node_trav.parent
    return node_trav

if __name__=="__main__":
    bst = BinarySearchTree()
    nodes = [5.1,3,2.3,6.2,8,1,7,9,5,2,0,6]
    for node in nodes:
        bst.insert_node(node)
    bst.print_tree()
    temp = nodes[random.randint(0, len(nodes)-2)]
    node = bst.search(temp)
    print("The node is", node.val)
    succesor = get_succesor(node)
    print("Its succesor is", succesor.val) 