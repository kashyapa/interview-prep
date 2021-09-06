class GraphVertex:

    def __init__(self, val):
        self.label = val
        self.edges = []

import collections


def clone_graph(graph):

    queue = collections.deque([graph])
    map = {}

    while queue:

        p = queue.popleft()
        map[p] = GraphVertex(p)

        for e in p.edges:
            if e not in map:
                map[e] = GraphVertex(e)
                queue.append(e)
            map[p].edges.append(map[e])
    return map[graph]
