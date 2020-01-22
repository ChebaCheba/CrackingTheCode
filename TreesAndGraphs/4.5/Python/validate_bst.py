import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.binary_tree import BinaryTree
from Structures.Python.binary_search_tree import BinarySearchTree

def validate_bst(tree):
    node = tree.root
    is_bst = _bst(node)
    return is_bst

def _bst(node, lim_max=None, lim_min=None):
    if node.left==None and node.right==None:
        if node.val<=lim_max and node.val>=lim_min:
            return True
        else:
            return False
    else:
        if lim_max==None or lim_min==None:
            lim_max = sys.maxsize
            lim_min = sys.maxsize*-1
        check_l = True
        check_r = True
        if node.left != None:
            check_l = _bst(node.left, lim_max=node.val, lim_min=lim_min)
        if node.right != None:
            check_r = _bst(node.right, lim_max=lim_max, lim_min=node.val) 
        if node.val<=lim_max and node.val>=lim_min and check_l and check_r:
            return True
        else:
            return False 
    



if __name__=="__main__":
    bst = BinarySearchTree()
    nodes = [5,3,6,8,7,2,0,3]
    for node in nodes:
        bst.insert_node(node)
    bst.print_tree()
    is_bst = validate_bst(bst)
    if is_bst:
        print("It is indeed a binary search tree")
    else:
        print("It is unfortunately not a binary search tree")
    bt = BinaryTree()
    for node in nodes:
        bt.insert_node(node)
    bt.print_tree()
    is_bst = validate_bst(bt)
    if is_bst:
        print("It is indeed a binary search tree")
    else:
        print("It is unfortunately not a binary search tree")