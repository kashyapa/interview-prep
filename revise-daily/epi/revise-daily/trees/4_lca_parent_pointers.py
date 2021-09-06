def lca_with_parent_pointers(p1, p2):

    def find_depth(node):
        if not node:
            return 0
        depth = 0
        while node:
            node = node.parent
            depth += 1
        return depth

    depth1 = find_depth(p1)
    depth2 = find_depth(p2)

    if depth1 > depth2:
        p1, p2 = p2, p1

    diff = depth2 - depth1

    while p2 and diff > 0:
        p2 = p2.parent
        diff -= 1
    while p1 and p2 and p1.val != p2.val:
        p1 = p1.parent
        p2 = p2.parent

    return p1