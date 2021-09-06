class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.diameter = 0


def find_diameter(root):
    def find_height(root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        lheight = find_height(root.left)
        rheight = find_height(root.right)

        tree_diameter.diameter = max(tree_diameter.diameter, lheight+rheight+1)
        return max(lheight, rheight) + 1

    tree_diameter = TreeDiameter()

    find_height(root)

    return tree_diameter.diameter


def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(find_diameter(root)))


if __name__ == '__main__':
    main()
