def tree_path_sum(root, sum):

    def rec(node, path):
        if node is None:
            return None

        path.append(node.val)
        sum_val = 0
        for i in range(len(path), -1, -1):
            sum_val += path[i]
            if sum_val == sum:
                res



