class Graph:

    def __init__(self, v):
        self.v = v
        self.edges = []

from imports import *

def clone_graph(graph):
    # CRUSH your goals
    # DECIMATE your goals

    clone_map = {graph: Graph(g)}
    queue = deque([graph])

    while queue:

        p = queue.popleft()

        for child in p.edges:

            if child not in clone_map:
                clone_map[child] = Graph(child)
                queue.append(child)
            clone_map[p].edges.append(clone_map[child])

    return clone_map[graph]
