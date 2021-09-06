class GraphVertex:
    def __init__(self, label, edges):
        self.label = label
        self.edges = edges


def is_graph_cyclic(vertices):
    def is_cyclic(v):

        if v in visited:
            return True

        visited.add(v)

        for edge in v.edges:
            if edge not in sorted_set:
                if is_cyclic(edge):
                    return True

        sorted_set.add(v)
        return False

    visited = set()
    sorted_set = set()

    for vertex in vertices:
        if is_cyclic(vertex):
            return True

from imports import *

def cyclic_graph_check(vertices, prerequisites):
    graph = {k: [] for k in range(vertices)}
    in_degree = {k: 0 for k in range(vertices)}

    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque([])
    for k, v in in_degree.items():
        if v == 0:
            sources.append(k)
    sorted_set = set()
    while sources:
        p = sources.popleft()
        sorted_set.add(p)

        for child in p.edges:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_set) != len(vertices)
