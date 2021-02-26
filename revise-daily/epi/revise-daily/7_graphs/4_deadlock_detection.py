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

