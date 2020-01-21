import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.binary_tree import BinaryTree

def check_balanced(binary_tree):
    node = binary_tree.root
    is_balanced = _balanced(node, True)
    return is_balanced

def _balanced(node, first=False):
    if node.right == None and node.left==None:
        return 0
    else:
        left_h = 0
        right_h = 0
        try:
            if node.left != None:
                left_h = _balanced(node.left) + 1
            if node.right != None:
                right_h = _balanced(node.right) + 1
        except:
            return None
        if abs(left_h - right_h)>1:
            return None
        if first:
            if left_h and right_h:
                return True
            else:
                return False
        return max(left_h, right_h)

                    
if __name__=="__main__":
    binary_tree = BinaryTree()
    nodes = [0,1,2,3,4,5]
    for node in nodes:
        binary_tree.insert_node(node)
    binary_tree.print_tree()
    balanced = check_balanced(binary_tree)
    if balanced:
        print("The tree is balanced")
    else:
        print("The tree is not balanced")

    