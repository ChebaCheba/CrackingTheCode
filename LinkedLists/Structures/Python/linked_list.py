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
