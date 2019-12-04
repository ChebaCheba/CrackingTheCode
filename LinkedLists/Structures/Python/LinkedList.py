class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodes = list()
        self.head = None
    def create(self, nodes):
        for node in nodes:
            new_node = Node(node)
            self.nodes.append(new_node)
        self.head = self.nodes[0]
    def print_list(self):
        string = ''
        for i in range(len(self.nodes)-1):
            string += '('+str(self.nodes[i].val)+')=>'
        string+='('+str(self.nodes[-1].val)+')'
        print(string)

llist = LinkedList()
nodes = [0,1,2,3,4,5]
llist.create(nodes)
llist.print_list()