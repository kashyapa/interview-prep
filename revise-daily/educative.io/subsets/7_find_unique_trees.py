class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    if n <= 0:
        return []
    return findUnique_trees_recursive(1, n)


def findUnique_trees_recursive(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left_trees = findUnique_trees_recursive(start, i-1)
        right_trees = findUnique_trees_recursive(i+1, end)

        for left in left_trees:
            for right in right_trees:
                root = TreeNode(i)
                root.left = left
                root.right = right
                result.append(root)

    return result


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()
