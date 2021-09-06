from collections import deque


def can_reconstruct(original_sequence, sequences):
    sorted_order = []
    graph = {}
    in_degree = {}
    for sequence in sequences:
        for num in sequence:
            graph[num] = []
            in_degree[num] = 0

    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i - 1], sequence[i]
            graph[parent].append(child)
            in_degree[child] += 1

    if len(in_degree) != len(original_sequence):
        return False

    sources = deque()

    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        if len(sources) > 1:
            return False
        if original_sequence[len(sorted_order)] != sources[0]:
            return False

        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

        return len(sorted_order) == len(original_sequence)


def can_construct2(original_sequence, sequences):
    graph = {}
    in_degree = {}
    for seq in sequences:
        for num in seq:
            graph[num] = []
            in_degree[num] = 0

    for seq in sequences:
        for i in range(1, len(seq)):
            graph[seq[i - 1]].append(seq[i])
            in_degree[seq[i]] = 0

    if len(in_degree) != len(original_sequence):
        return False

    # build sources
    sources = deque()
    for k in in_degree:
        if in_degree[k] == 0:
            sources.append(k)

    sorted_order = []
    while sources:

        if len(sources) > 1:
            return False

        if original_sequence[len(sorted_order)] != sources[0]:
            return False

        vertex = sources.popleft()
        sorted_order.append(vertex)

        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == len(original_sequence)


def accounts_merge(accounts):
    email_to_id = {}
    id_to_name = {}

    c = 0
    ds = []

    def find(a):
        if ds[a] < 0:
            return ds[a]
        ds[a] = find(a)
        return ds[a]

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            if ds[a] < ds[b]:
                ds[a] += ds[b]
                ds[b] = a
            else:
                ds[b] = ds[a]
                ds[a] = b

    for account in accounts:
        for email in account[1:]:
            if email not in email_to_id:
                email_to_id[email] = c
                id_to_name[c] = account[0]
                c += 1
                ds.append(-1)
            union(email_to_id[account[1]], email_to_id[email])

    res = {}
    for email, id in email_to_id.items():
        master = find(id)
        res[master] = res.get(master, []) + [email]
        return [[id_to_name[id]] + sorted(emails) for id, emails in res.items()]