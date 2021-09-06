def topological_sorting(vertices, edges):

    graph = {k: [] for k in range(len(vertices))}
    in_degree = {k: 0 for k in range(len(vertices))}

    sorted_order = []
    for e1, e2 in edges:
        graph[e1].append(e2)
        in_degree[e2] += 1

    import collections
    sources = collections.deque()

    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for d in graph[vertex]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                sources.append(d)

    return sorted_order
