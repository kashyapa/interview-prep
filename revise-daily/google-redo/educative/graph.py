from collections import deque


def reconstruct_sequence(original_sequence, sequences):

    graph = {}
    in_degree = {}

    for sequence in sequences:
        for num in sequence:
            graph[num] = []
            in_degree[num] = 0

    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i-1], sequence[i]
            graph[parent].append(child)
            in_degree[child] += 1

    sources = deque([])
    for k,v in in_degree.items():
        if graph[k] == 0:
            sources.append(k)

    if len(in_degree) != len(original_sequence):
        return False

    sorted_order = []
    while sources:
        if len(sources) > 1:
            return False

        if original_sequence[len(sorted_order)] != sources[0]:
            return False

        p = sources.popleft()
        sorted_order.append(p)
        for child in graph[p]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == len(original_sequence)


def alien_dictionary(words):

    graph = {}
    in_degree = {}

    for i, w in enumerate(words):
        graph[w] = []
        in_degree[w] = 0

    for i, w in enumerate(words[1:])
        w1, w2 = w[i-1], w[i]
        for j in range(min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    sources = deque()
    for k in in_degree:
        if graph[k] == 0:
            sources.append(k)

    sorted_order = []
    while sources:

        p = sources.popleft()
        sorted_order.append(p)

        for child in graph[p]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    if len(sorted_order)!=len(in_degree):
        return ""

    return "".join(sorted_order)


def can_reconstruct(original_sequence, sequences):

    graph = {}
    in_degree ={}

    for seq in sequences:
        for i in range(len(seq)):
            graph[seq[i]] = []
            in_degree[seq[i]] = 0

    for seq in sequences:
        for i in range(1, len(seq)):
            parent, child = seq[i], seq[i-1]
            graph[parent].append(child)
            in_degree[child] += 1

    if len(in_degree) != len(original_sequence):
        return False

    sources = deque()
    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)

    sorted_order = []
    while sources:
        p = sources.popleft()

        if len(sources) > 1:
            return False

        if original_sequence[len(sorted_order)] != sources[0]:
            return False
        sorted_order.append(p)
        for child in graph[p]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(sorted_order) != len(original_sequence):
        return False

    return "".join(sorted_order)

def alien_dictionary2(words):
    graph = {}
    in_degree = {}

    for w in words:
        for j in range(len(w)):
            graph[w] = []
            in_degree[w] = 0

    for i, w in enumerate(words[1:]):
        w1, w2 = w[i-1], w[i]

        for j in range(min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    sources = deque()

    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)

    sorted_order = []

    while sources:
        p = sources.popleft()
        sorted_order.append(p)

        for child in graph[p]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    if len(sorted_order) != len(in_degree):
        return ""

    return "".join(sorted_order)

def all_tasks_scheduling(tasks, prerequisites):

    def print_from_all_sources(sources, res, in_degree):

        n = len(sources)

        for i in range(n):
            p = sources.popleft()
            res.append(p)
            sources_for_next_call = deque(sources)

            for child in graph[p]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)
            print_from_all_sources(sources_for_next_call, res, in_degree)

            res.pop()
            for child in graph[p]:
                in_degree[child] += 1
        if len(res) == len(in_degree):
            print(res)

    graph = {i: [] for i in range(len(tasks))}

    in_degree = {i: 0 for i in range(len(tasks))}

    for parent, child in prerequisites:
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()

    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)
    print_from_all_sources(sources, [], in_degree)
