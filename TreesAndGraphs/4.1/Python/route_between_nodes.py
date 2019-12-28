import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.directed_graph import Graph

def dfs(node1, node2):
    if node1 == node2:
        return True
    stack = []
    visited = []
    stack.append(node1)
    while stack:
         current_node = stack.pop()
         if current_node in visited:
             break
         if current_node == node2:
             return True
         visited.append(current_node)
         for node in current_node.adj:
             if node not in visited:
                stack.append(node)
    return False
        
if __name__=="__main__":
    graph = Graph()
    nodes = [0,1,2,3,4,5,6]
    for i in nodes:
        graph.add_node(i)
    graph.add_adj(0,1)
    graph.add_adj(0,2)
    graph.add_adj(0,5)
    graph.add_adj(1,2)
    graph.add_adj(1,4)
    graph.add_adj(2,3)
    graph.add_adj(3,3)
    graph.add_adj(3,5)
    graph.add_adj(3,6)
    graph.add_adj(4,3)
    graph.add_adj(4,1)
    graph.add_adj(4,6)
    graph.add_adj(6,5)
    graph.print_graph()
    node1 = graph.return_node(1)
    node2 = graph.return_node(6)
    print(dfs(node1,node2))
    node1 = graph.return_node(0)
    node2 = graph.return_node(6)
    print(dfs(node1,node2))
    node1 = graph.return_node(4)
    node2 = graph.return_node(5)
    print(dfs(node1,node2))
    node1 = graph.return_node(5)
    node2 = graph.return_node(1)
    print(dfs(node1,node2))

