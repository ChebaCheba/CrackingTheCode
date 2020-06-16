import sys
import os
import random

sys.path.append(os.path.join("..",".."))
from Structures.Python.directed_graph import GraphDict

def get_path_dfs(graph,node,build_o):
    node = graph.return_node(node)
    if node == None:
        return True
    if node.state == "visiting":
        return False
    node.state = "visiting"
    for adj in node.adj:
        success = get_path_dfs(graph,adj.val,build_o)
        if not success:
            return False
    build_o.append(node.val)
    del graph.nodes[node.val]
    return True

def get_path(graph):
    build_o = []
    while len(graph.nodes) > 0:
        node = random.choice(list(graph.nodes.keys()))
        success = get_path_dfs(graph,node, build_o)
        if not success:
            return []
    return build_o

def get_order(libraries, dependencies):
    build_o = []
    building = True
    while building:
        cycle = True
        not_buildable = set()
        for dependency in dependencies:
            if dependency[1] not in not_buildable:
                not_buildable.add(dependency[1])
        for i in range(len(dependencies)):
            dependency = dependencies[len(dependencies)-1-i][0]
            if dependency not in not_buildable:
                if dependency in libraries:
                    build_o.append(dependency)
                    libraries.remove(dependency)
                cycle = False
                dependencies.pop(len(dependencies)-1-i)
        if not dependencies:
            building = False
        if cycle:
            return []
    for i in libraries:
        build_o.append(i)
    return build_o

if __name__=="__main__":
    graph = GraphDict()
    projects = {'a','b','c','d','e','f'}
    #projects_list = ['a','b','c','d','e','f'] 
    for project in projects:
        graph.add_node(project)
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
    for i in dependencies:
        graph.add_adj(i[0],i[1])
    graph.print_graph()
    build_o1 = get_order(projects, dependencies)
    print("Solution without dfs",build_o1)
    build_o2 = get_path(graph)
    print("Solution with dfs",build_o2[::-1])
