# Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/


from data_structures.tree import TreeNode


def insert(root: TreeNode | None, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


# Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/description/


def delete_node(root: TreeNode | None, key: int) -> TreeNode | None:
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left or not root.right:
            root = root.left or root.right
        else:
            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            root = root.right

    return root
