import networkx as nx
import math

# This function computes the distance between two points.
def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def get_graph(coordinates):
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(i, j, weight=dist(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]))
    return g

# Consider the following 3 points.
coordinates = [
    (166, 282),
    (43, 79),
    (285, 44)
    ]
# Create a corresponding graph.
g = get_graph(coordinates)

for v in g.nodes():
    print(v)

print(g[0][1]['weight'])
print(g[1][0]['weight'])
