def find_paths(root, target):

    def rec(node, path, sum):

        if node is None:
            if sum == 0 and len(path) > 0:
                res.append(path.copy())
        path.append(node.val)
        rec(node.left, path, sum - node.val)
        rec(node.right, path, sum - node.val)
        path.pop()

    res = []
    rec(root, [], target)
    return res
