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
