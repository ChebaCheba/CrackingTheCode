class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodes = list()
        self.head = None
        self.tail = None
    def create(self, nodes):
        new_node = Node(nodes[0])
        self.nodes.append(new_node)
        for i in range(1,len(nodes)):
           new_node = Node(nodes[i])
           self.nodes[-1].next = new_node
           self.nodes.append(new_node)
        self.head = self.nodes[0]
        self.tail = self.nodes[-1]
    def add_node(self, val):
        if self.nodes:
            new_node = Node(val)
            self.nodes[-1].next = new_node
            self.nodes.append(new_node)
            self.tail = self.nodes[-1]
        else:
            self.create([val])
    def delete_node(self, val):
        if self.nodes[0].val == val:
            node = self.nodes[0]
            node.next = None
            self.nodes = self.nodes[1:]
            self.head = self.nodes[0]
            return node
        elif self.nodes[len(self.nodes)-1].val == val:
            self.tail = self.nodes[len(self.nodes)-2]
            self.nodes[len(self.nodes)-2].next = None
            return self.nodes.pop()
        for i in range(1,len(self.nodes)-1):
            if self.nodes[i].val == val:
                node = self.nodes[i]
                self.nodes[i-1].next = self.nodes[i+1]
                node.next = None
                self.nodes = self.nodes[:i]+self.nodes[i+1:]
                return node
        return None
    def delete_node_by_index(self, index):
        if index == 0 or index == (len(self.nodes)-1):
            self.delete_node(self.nodes[index].val)
        else:
            try:
                node = self.nodes[index]
                node.next = None
                self.nodes[index-1].next = self.nodes[index+1]
                self.nodes = self.nodes[:index]+self.nodes[index+1:]            
                return node
            except:
                return None
    def add_nodes(self, nodes):
        if self.nodes:
            new_node = Node(nodes[0])
            self.nodes[-1].next = new_node
            self.nodes.append(new_node)
            for i in range(1,len(nodes)):
                new_node = Node(nodes[i])
                self.nodes[-1].next = new_node
                self.nodes.append(new_node)
            self.tail = self.nodes[-1]
        else:
            self.create(nodes)
    def print_list(self):
        if self.nodes:
            string = ''
            for i in range(len(self.nodes)-1):
                string += '('+str(self.nodes[i].val)+')=>'
            string+='('+str(self.nodes[-1].val)+')'
            print(string)
        else:
            print('()')

class ListlessLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def create(self, nodes):
        prev_node = None
        for node in nodes:
            new_node = Node(node)
            self.length += 1
            if prev_node:
                prev_node.next = new_node
                prev_node = new_node
            else:
                self.head = new_node
                prev_node = new_node
        self.tail = prev_node
    def add_node(self, node):
        if length:
            new_node = Node(node)
            self.length += 1
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.create([node])
    def return_node(self, num):
        node = self.head
        for i in range(num-1):
            node = node.next
        return node 
    def print_list(self, loop = False):
        if self.head:
            node = self.head
            string = ''
            while node.next != None:
                string += '('+str(node.val)+')=>'
                if loop and node == self.tail:
                    node = node.next
                    break
                node = node.next
            string += '('+str(node.val)+')'
            print(string)
        else:
            print('()')
                
        
    