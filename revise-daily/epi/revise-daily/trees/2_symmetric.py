def symmetric(root):

    if not root:
        return True

    def check_symmetry(t1, t2):

        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        return t1.val == t2.val and check_symmetry(t1.left, t2.right) and check_symmetry(t1.right, t2.left)