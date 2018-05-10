import matplotlib.pyplot as plt
import networkx as nx
import random as r

def rand_partition(G, num_partitions):
    G_ = G.copy()
    
    edges = list(G_.edges())
    shuffled = range(len(edges))
    r.shuffle(shuffled)

    subgraphs = []
    for edge_i in shuffled:
        G_.remove_edge(*edges[edge_i])
        subgraphs = list(nx.connected_components(G_))
        if len(subgraphs) == num_partitions:
            break

    return G_, subgraphs
    
def subgraphs_to_classes(subgraphs):
    classes = {}
    for cl, nodes in enumerate(subgraphs):
        for node in nodes:
            classes[node] = cl
    
    return classes

def create_graph_object(G, subgraphs, classes):
    graph = dict(zip(range(len(subgraphs)), [0]*len(subgraphs)))

    for node in G.nodes():
        cl = classes[node]
        graph[cl] = set()
        for child in G[node].keys():
            cl_ = classes[child]
            graph[cl].add(cl_)
    
    print graph
    return nx.Graph(graph)

def hierarchy(G, sizes):
    levels = {}
    curr_G = G

    for level, partitions in enumerate(sizes):
        G_, subgraphs = rand_partition(curr_G, num_partitions=partitions)
        classes = subgraphs_to_classes(subgraphs)
        abstract_G = create_graph_object(curr_G, subgraphs, classes)
        
        levels[level] = (abstract_G, classes, subgraphs)
    
    return levels

def dummy():
    subgraphs = [set([1]), set([2, 3, 4, 8, 10, 11, 12]), set([5, 6]), set([7]), set([9])]
    return subgraphs

def main():
    graph = {
        1 : [2, 5],
        2 : [1, 3],
        3 : [2, 4],
        4 : [3, 8],
        5 : [1, 6],
        6 : [5],
        7 : [8],
        8 : [4, 7],
        9 : [1, 10],
        10 : [9, 11],
        11 : [10, 12],
        12 : [11, 4]
    }

    G = nx.Graph(incoming_graph_data=graph)
    levels = hierarchy(G, sizes=[7, 3, 1])

if __name__ == '__main__':
    main()