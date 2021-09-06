from imports import *


class Graph:
    def __init__(self, v):
        self.d = -1
        self.edges = []


def make_wired_connections(graph):
    # no question of missing the target

    def bfs(v):

        queue = deque([v])

        while queue:
            p = queue.popleft()

            for child in p.edges:
                if child.d == -1:
                    child.d = p.d + 1
                else:
                    return False
        return True
    return all(bfs(v) for v in graph if v.d == -1)
