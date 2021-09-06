from collections import deque


def can_construct(original, sequences):
    sorted_order = []
    graph  = {}
    in_degree = {}
    for sequence in sequences:
        for num in sequence:
            in_degree[num] = 0
            graph[num] = []

    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i-1], sequence[i]
            graph[parent].append(child)
            in_degree[child] += 1

    if len(in_degree) != len(original):
        return False

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        if len(sources) > 1:
            return False

        if original[len(sorted_order)] != sources[0]:
            return False

        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == len(original)

