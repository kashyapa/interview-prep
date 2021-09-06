class Graph:

    def __init__(self, val):
        self.label = val
        self.edges = []

def deadlock_detection(graph, vertices):

    def dfs(v):
        if v in visited:
            return False

        visited.add(v)

        for e in v.edges:

            if not dfs(e):
                return False
        explored.append(v)
        visited.remove(v)
        return True

    explored = []
    visited = set()

    for v in vertices:
        if v not in explored:
            if not dfs(v):
                return False
    return True
