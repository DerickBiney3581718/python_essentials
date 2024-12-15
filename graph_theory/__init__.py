from collections import namedtuple

Graph = namedtuple("Graph", ['nodes', 'edges'])

nodes = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B'),
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('D', 'B')
]
G = Graph(nodes, edges)

print(G._asdict())