import sys
import os

sys.path.append(os.path.join("..","..", ".."))
from TreesAndGraphs.Structures.Python.binary_tree import BinaryTree
from LinkedLists.Structures.Python.linked_list import ListlessLinkedList

def list_depths(binary_tree):
    list_d = []
    traverse(list_d, binary_tree.root)
    return list_d

def traverse(list_d, node, level = 0):
    if len(list_d)<level+1:
        llist = ListlessLinkedList()
        list_d.append(llist)
    list_d[level].add_node(node.val)
    if node.left:
        traverse(list_d, node.left, level+1)
    if node.right:
        traverse(list_d, node.right, level+1)

if __name__=="__main__":
    binary_tree = BinaryTree()
    nodes = [0,1,2,3,4,5,6,7,8,9]
    for node in nodes:
        binary_tree.insert_node(node)
    binary_tree.print_tree()
    linked_lists = list_depths(binary_tree)
    for llist in linked_lists:
        llist.print_list()


