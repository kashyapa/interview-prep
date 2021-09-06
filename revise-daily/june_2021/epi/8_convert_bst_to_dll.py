def convert_bst_to_dll(tree):

    def get_inorder_nodes(node):
        if not node:
            return None

        get_inorder_nodes(node.left)
        inorder_nodes.append(node)
        get_inorder_nodes(node.right)
        return

    inorder_nodes = []
    get_inorder_nodes(tree)

    prev = inorder_nodes[0]
    for i in range(1, len(inorder_nodes)):
        inorder_nodes[i].left = prev
        prev.right = inorder_nodes[i]

    return inorder_nodes[0]




