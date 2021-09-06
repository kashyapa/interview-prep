import collections


def find_nodes_at_k_distance(root, target, k):
    parent_links = {}

    def get_node(node, target):

        if not node:
            return None

        if node.val == target:
            return node

        p = get_node(node.left, target)
        if p:
            return p
        return get_node(node.right, target)


    def find_parents(parent, child):
        if not child:
            return None

        parent_links[child.val] = parent
        parent = child
        find_parents(parent, child.left)
        find_parents(parent, child.right)
        return
    find_parents(None, root)

    res = []

    t = get_node(root, target)
    queue = collections.deque([(t, 0)])

    while queue:
        n = len(queue)

        for _ in range(n):
            p, distance = queue.popleft()

            if distance == k:
                res.append(p)

            if p.left and distance+1 < k:
                queue.append((p.left, distance+1))
            if p.right and distance+1 < k:
                queue.append((p.right, distance+1))
            if parent_links[p] and distance+1 < k:
                queue.append((parent_links[p], distance+1))
    return res
