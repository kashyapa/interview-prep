class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def compute_binary_trees(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left_trees = compute_binary_trees(start, i-1)
        right_trees = compute_binary_trees(i+1, end)

        for l in left_trees:
            for r in right_trees:
                node = TreeNode(i)
                node.left = l
                node.right = r
                result.append(node)

    return result


def generate_binary_trees(n):

    return compute_binary_trees(1, n)


if __name__ == '__main__':
    print(generate_binary_trees(4))