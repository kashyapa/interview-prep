class GraphVertex:
    def __init__(self):
        self.edges = []
        self.max_distance = 0


def find_largest_number_teams(graph: list[GraphVertex]):
    def dfs(curr: GraphVertex):
        curr.max_distance = max(
            ((vertex.max_distance if vertex.max_distance != 0 else dfs(vertex)) + 1
             for vertex in curr.edges), default=1)

        return curr.max_distance
    return max(dfs(g) for g in graph if g.max_distance == 0)
