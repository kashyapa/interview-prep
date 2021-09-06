from collections import namedtuple

def max_path_sum(root):
    MaxSum = namedtuple('MaxSum', ('max_sum'))
    def rec(node):
        if node is None:
            return 0

        lsum = max(rec(node.left), 0)
        rsum = max(rec(node.right), 0)
        local_sum = max(lsum+ node.val, rsum+node.val)

        max_sum["m"] = max(max_sum["m"], max(lsum + node.val + rsum))
        max_sum["m"] = max(max_sum["m"], local_sum)

        return local_sum

    max_sum = {"m": 0}

    rec(root)
    return max_sum