class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def generate_binary_trees(n):

    def rec(start, end):

        if start > end:
            return None
        res = []
        for i in range(start, end):
            left = generate_binary_trees(start, i)
            right = generate_binary_trees(i+1, end)

            for l in left:
                for r in right:
                    root = Tree(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
    return rec(0, n)

