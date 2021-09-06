def alien_dictionary(words):

    graph = {}
    in_degree = {}

    for i in range(len(words)):
        for j in range(len(words[i])):
            graph[words[i][j]] = []
            in_degree[words[i][j]] = 0

    for i in range(1, len(words)):
        for j in range(min(len(words[i-1]), len(words[i]))):
            if words[i][j] != words[i-1][j]:
                graph[words[i-1][j]].append(words[i][j])
                in_degree[graph[words[i][j]]] += 1
                break

    import collections
    sources = collections.deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    import collections
    sorted_order = collections.deque()

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)

        for key in graph[vertex]:
            in_degree[key] -= 1
            if in_degree[key] == 0:
                sources.append(key)

    if len(sorted_order) != len(in_degree):
        return ""

    return "".join(sorted_order)
