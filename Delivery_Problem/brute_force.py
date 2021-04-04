import networkx as nx
from itertools import permutations

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    def cycle_length(g, cycle):
        # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
        assert len(cycle) == g.number_of_nodes()
        # Write your code here.
        total_weight = 0
        for i in range(len(cycle)-1):
            total_weight += g[cycle[i]][cycle[i+1]]['weight']
        total_weight += g[cycle[-1]][cycle[0]]['weight']
        return total_weight
    init_cycle = [i for i in range(n)]
    shortest = cycle_length(g, init_cycle)
    # Iterate through all permutations of n vertices
    for p in permutations(range(n)):
        temp_length = cycle_length(g, p)
        if temp_length < shortest:
            shortest = temp_length
    return shortest
