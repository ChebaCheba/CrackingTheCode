class Node:
    def __init__(self, val):
        self.val = val
        self.adj = []
class Graph:
    def __init__(self):
        self.nodes = []
    def add_node(self, val):
        node = Node(val)
        self.nodes.append(node)
    def add_adj(self, index1, index2):
        if not (index1<len(self.nodes) and index2<len(self.nodes)):
            return
        node1 = self.nodes[index1]
        node2 = self.nodes[index2]
        node1.adj.append(node2)
    def return_node(self, index):
        if not index<len(self.nodes):
            return
        return self.nodes[index]
    def print_graph(self):
        string = ''
        for node in self.nodes:
            string += str(node.val)+':'
            for i in node.adj:
                string += '['+str(i.val)+']'
            string += '\n'
        print(string)

class GraphDict:
    def __init__(self):
        self.nodes = {}
    def add_node(self, val):
        node = Node(val)
        self.nodes[val] = node
    def add_adj(self, val1, val2):
        if val1 in self.nodes and val2 in self.nodes:
            node1 = self.nodes[val1]
            node2 = self.nodes[val2]
            node1.adj.append(node2)
    def return_node(self, val):
        if val in self.nodes:
            return self.nodes[val]
    def print_graph(self):
        string=''
        for key in self.nodes:
            string += str(key)+':'
            node = self.nodes[key]
            for i in node.adj:
                string += '['+str(i.val)+']'
            if not node.adj:
                string += '[]'
            string += '\n'

        print(string)


        
