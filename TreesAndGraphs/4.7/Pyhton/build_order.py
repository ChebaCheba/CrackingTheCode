import sys
import os

sys.path.append(os.path.join("..",".."))
from Structures.Python.directed_graph import GraphDict

def get_path(graph):
    pass

if __name__=="__main__":
    graph = GraphDict()
    projects = ['a','b','c','d','e','f']
    for project in projects:
        graph.add_node(project)
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    for i in dependencies:
        graph.add_adj(i[0],i[1])
    graph.print_graph()
