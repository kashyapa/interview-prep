import string

def word_ladder(w1, w2, dictionary:[set]):
    alphabets = [chr(ord('a')+ i) for i in range(0, 26)]

    dictionary.remove(w1)

    for i in range(len(w1)):
        for c in alphabets:
            next_word = w1[:i] + c + w1[i+1:]
            if next_word == w2:
                return True
            if next_word in dictionary:
                dictionary.remove(next_word)
                if word_ladder(next_word, w2, dictionary):
                    return True
    return False

from collections import deque

def word_ladder_bfs(s1, s2, dictionary):

    queue = deque([(s1, 0)])
    dictionary.remove(s1)

    while queue:
        s, distance = queue.popleft()

        if s == s2:
            return distance
        
        for i in range(len(s)):
            for c in string.ascii_lowercase:
                next_word = s[:i] + c + s[i+1:]
                if next_word in dictionary:
                    dictionary.remove(next_word)
                    queue.append((next_word, distance+1))
                    
    return -1


class GraphVertex:

    def __init__(self, label):
        self.d = 0
        self.edges = []
        self.label = None
        

def check_wired_connections(graph):

    def bfs(v):
        queue = deque([v])

        while queue:
            p = queue.popleft()

            for x in p.edges:
                if x.d == -1:
                    x.d += 1
                elif x.d == p.d:
                    return False
        return True
    return all([bfs(v) for v in graph if v.d == -1])


def clone_graph(graph):

    if graph is None:
        return None

    q = deque([graph])
    clone_map = {graph: GraphVertex(graph.label)}
    while q:
        p = q.popleft()
        clone = clone_map[p]
        
        for v in p.edges:
            if v not in clone_map:
                clone_map[v] = GraphVertex(v.label)
            q.append(v)
            clone.edges.append(clone_map[v])
    return clone_map[graph]


# def compute_enclosed_regions(cells, ):
#
#     queue = deque([])
#     m, n = len(cells), len(cells[0])
#
#     queue = deque([(i, j) for k in range(m) for i, j in ((k, 0), (k, n-1))]
#                   + [(i, j) for k in range(n) for i, j in ((0, k), (m-1, k))])
#
#     while queue:
#         i, j = queue.popleft()



