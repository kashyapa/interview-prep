from collections import deque


class GraphVertex:

    def __init__(self, label):
        self.label = label
        self.edges = []


def clone_graph(graph: GraphVertex):
    if graph is None:
        return None
    q = deque([graph])
    vertex_map = {graph: GraphVertex(graph.label)}

    while q:
        p = q.popleft()

        for neighbor in p.edges:
            if neighbor not in vertex_map:
                vertex_map[neighbor] = GraphVertex(neighbor.label)
                q.append(neighbor)
            vertex_map[p].edges.append(vertex_map[neighbor])

    return vertex_map[graph]


def clone_graph2(graph: GraphVertex):
    if graph is None:
        return None
    q = deque([graph])
    vertex_map = {q: GraphVertex(graph.label)}

    while q:
        p = q.popleft()

        for neighbor in p.edges:
            if neighbor not in vertex_map:
                vertex_map[neighbor] = GraphVertex(neighbor.label)
            q.append(neighbor)
            vertex_map[p].edges.append(vertex_map[neighbor])
    return vertex_map[graph]


