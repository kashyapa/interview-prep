# Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such
# that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.
#
# Given a directed graph, find the topological ordering of its vertices.
#
# Example 1:
#
# Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
# Output: Following are the two valid topological sorts for the given graph:
# 1) 3, 2, 0, 1
# 2) 3, 2, 1, 0

from collections import deque


def topological_sort(vertices, edges):
    sortedOrder = []

    # build graph
    # build in_degree
    # build sources
    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for parent, child in edges:
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for child, incoming in in_degree.items():
        if incoming == 0:
            sources.append(child)

    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)

        # get neighbors

        for neighbor in graph[vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                sources.append(neighbor)

    return sortedOrder


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


if __name__ == "__main__":
    main()
