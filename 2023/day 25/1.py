import os
import networkx as nx

file_path = os.path.join('./2023/day 25', 'input.txt')
file = open(file_path, 'r').read().splitlines()

g = nx.Graph()

for line in file:
    left, right = line.split(':')
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))
