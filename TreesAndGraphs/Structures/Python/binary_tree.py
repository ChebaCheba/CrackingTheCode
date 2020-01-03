import random
import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.height = 0
    def insert_node(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        current_node = self.root
        direction = random.randint(0,1)
        while True:
            if direction:
                if not current_node.right:
                    current_node.right = node
                    self.get_height()
                    return
                else:
                    current_node = current_node.right
            else:
                if not current_node.left:
                    current_node.left = node
                    self.get_height()
                    return
                else:
                    current_node = current_node.left
            direction = random.randint(0,1)
    def search(self, val, node = None):
        found_node = None
        if not node:
            node = self.root
        if node.val != val:
            if node.right:
                found_node = self.search(val, node.right)
            if not found_node:
                found_node = self.search(val, node.left)
        else:
            found_node = node
            return found_node
    def get_height(self, node= None, level = 1):
        temp = level
        root = False
        if not node:
            node = self.root
            root = True
        if node.right == None and node.left == None:
            current_height = int(math.log(level,2))
            if self.height < current_height:
                self.height = current_height
        else:
            if node.left != None:
                self.get_height(node.left, temp*2)
            if node.right !=  None:
                self.get_height(node.right, temp*2)
        if root:
            return self.height
    def _arr_string(self, node = None, level = 1, arr = []):
        current_height = int(math.log(level,2))
        root = False
        if not arr:
            for i in range(self.height+1):
                arr.append([])
        if not node:
            node = self.root
            root = True
        arr[current_height].append(node.val)
        if node.right == None and node.left == None:
            self._insert_none(current_height, arr, True)
        else:
            if node.left != None:
                self._arr_string(node.left, level*2)
            else:
                self._insert_none(current_height,arr, False)
            if node.right !=  None:
                self._arr_string(node.right, level*2)
            else:
                self._insert_none(current_height, arr, False)
        if root:
            return arr
    def _insert_none(self, current_height, arr, both):
        for i in range(self.height-current_height):
                current_arr = arr[self.height-i]
                lost_nodes = int(((2**self.height)/2**current_height)/(2**i))
                if not both:
                    lost_nodes = int(lost_nodes/2)
                for i in range(lost_nodes):
                    current_arr.append(None)
    def print_tree(self):
        arr =self._arr_string()
        string = ''
        for i in range(len(arr)):
            string += '  '*(2**(len(arr)-i-1))
            for j in range(len(arr[i])):
                if arr[i][j] or arr[i][j]==0:
                    string += '('+str(arr[i][j])+')'
                else:
                    string += '( )'
                string += '   '*((2**(len(arr)-i-1))-1)
            string += '\n'
        print(string)          


        