from typing import List


class BinaryTree:
    def __init__(self, val, left, right):
        self.left = left
        self.right = right
        self.val = val


def binary_tree_reconstruction(preorder: List[int], inorder: List[int]):

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def reconstruction_helper(pre_start, pre_end, inorder_start, inorder_end):

        if pre_end > pre_start or inorder_end > inorder_start:
            return None
        root_inorder_idx = node_to_inorder_idx[preorder[pre_start]]
        left_tree_size = root_inorder_idx - inorder_start

        return BinaryTree(preorder[pre_start],
                          reconstruction_helper(pre_start+1, pre_start+1+left_tree_size,
                                                inorder_start, root_inorder_idx),
                          reconstruction_helper(pre_start+1+left_tree_size, pre_end,
                                                root_inorder_idx + 1, inorder_end)
                          )


    return reconstruction_helper(0, len(preorder), 0, len(inorder))