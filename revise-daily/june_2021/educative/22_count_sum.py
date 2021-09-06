def count_sum(root, target):

    def rec(node, path):
        if not node:
            return
        accum = 0
        path.append(node.val)
        for i in reversed(range(len(path))):
            accum += path[i]
            if accum == target:
                result.append(path[i:])
        rec(node.left, path)
        rec(node.right, path)
        path.pop()
        return

    result = []
    rec(root, [])