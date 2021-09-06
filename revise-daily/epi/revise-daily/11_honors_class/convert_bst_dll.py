class Tree:
    def __init__(self):
        self.left = None
        self.right = None


def get_inorder_nodes(root):
    if not root:
        return None

    get_inorder_nodes(root.left)
    res.append(root.val)
    get_inorder_nodes(root.right)


def convert_bst_dll(root):
    inorder_nodes = get_inorder_node(root)
    head = inorder_nodes[0]
    pre = head
    for i in range(1, len(inorder_nodes)):
        cur = inorder_nodes[i]
        pre.right = cur
        cur.left = pre
        pre = cur

    return head


if __name__ == "__main__":
    res = []
    print(convert_bst_dll())
