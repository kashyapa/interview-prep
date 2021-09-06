class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def unique_trees(n):

    if n <= 0:
        return []
    
    def rec(start, end):
        result = []
        if start > end:
            result.append(None)
            return result

        for i in range(start, end+1):
            left_trees = rec(start, i-1)
            right_trees = rec(i+1, end)

            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)

        return result
    
    return rec(1, n)