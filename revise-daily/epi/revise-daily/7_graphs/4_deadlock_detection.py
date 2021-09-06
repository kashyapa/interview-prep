class GraphVertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.color = GraphVertex.WHITE
        self.edges = []


def is_graph_cyclic(vertices: list[GraphVertex]):

    def is_cyclic(v: GraphVertex):

        if v.color == GraphVertex.GRAY:
            return True

        v.color = GraphVertex.GRAY

        for neighbour in v.edges:
            if neighbour.color != GraphVertex.BLACK:
                if is_graph_cyclic(neighbour) is False:
                    return True

        v.color = GraphVertex.BLACK
        return False

    for vertex in vertices:
        if vertex.color == GraphVertex.WHITE:
            if is_cyclic(vertex):
                return True

    return False

from collections import deque

class Graph:
    def __init__(self, label):
        self.label = label
        self.edges = []


def is_graph_cyclic(vertices, prerequisites):
    graph = {k: [] for k in range(len(vertices))}
    in_degree = {k: 0 for k in range(len(vertices))}

    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque([])
    for k, v in in_degree.items():
        if in_degree[k] == 0:
            sources.append(k)
    sorted_order = []
    while sources:
        p = sources.popleft()
        sorted_order.append(p)
        for edge in p.edges:
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                sources.append(edge)
    return len(sorted_order) != len(vertices)


class GraphVertex2:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self, color, edges):
        self.color = color
        self.edges = edges


def is_there_a_cycle(node):
    if not node:
        return False
    if node.color == GraphVertex2.GRAY:
        return True

    node.color = GraphVertex2.GRAY
    for neighbor in node.edges:
        if neighbor.color != GraphVertex2.BLACK:
            if is_there_a_cycle(neighbor):
                return True
    node.color = GraphVertex2.BLACK
    return False

def is_cyclic(graph):
    for v in graph:
        if v.color != GraphVertex2.BLACK:
            if is_there_a_cycle(v):
                return True
