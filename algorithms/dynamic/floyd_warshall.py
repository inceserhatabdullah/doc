#!/usr/bin/env python3

# Floyd Warshall Algorithm in python
"""                 FLOYD WARSHALL
# * Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph.
# ? This algorithm works for both the directed and undirected weighted graphs
# ? But, it does not work for the graphs with negative cycles (where the sum of the edges in a cycle is negative).
# ? This algorithm follows the dynamic programming approach to find the shortest paths.
# ? To find the shortest path is a directed graph, To find the transitive closure of directed graphs
# ? To find the Inversion of real matrices, For testing whether an undirected graph is bipartite
# * Floyd-Warhshall algorithm is also called as Floyd's algorithm, Roy-Floyd algorithm, Roy-Warshall algorithm, or WFI algorithm.
# * https://www.programiz.com/dsa/floyd-warshall-algorithm
"""

# The number of vertices
nV = 4
INF = 999

# Algorithm implementation
def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # Adding vertices individually
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    print_solution(distance)

# Printing the solution
def print_solution(distance):
    for i in range(nV):
        for j in range(nV):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, 5],
         [2, 0, INF, 4],
         [INF, 1, 0, INF],
         [INF, INF, 2, 0]]
floyd_warshall(G)