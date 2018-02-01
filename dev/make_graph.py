from random import random
import json
no_nodes = 100
sparsity = 0.9

nodes = []
edges = []

# Make nodes
for i in range(no_nodes):
    node = {
        'data': {
            'id': '{}'.format(i)
        }
    }
    nodes.append(node)

# Make edges:
for i in range(no_nodes - 1):
    for j in range(i + 1, no_nodes):
        if random() > sparsity:
            edge = {
                'data': {
                    'id': '{}_{}'.format(i, j),
                    'source': '{}'.format(i),
                    'target': '{}'.format(j)
                }
            }
            edges.append(edge)

graph = {
    'nodes': nodes,
    'edges': edges
}
with open('../data/graph.json', 'w') as f:
    json.dump(graph, f)
