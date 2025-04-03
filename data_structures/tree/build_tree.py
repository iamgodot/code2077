# Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

from data_structures.tree import TreeNode


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """
    Use the preorder array to find root node and inorder array to split for subtrees.

    Time: O(n)
    Space: O(h), in the worst case O(n)
    """

    def _build(pre_l, in_l, in_r) -> TreeNode | None:
        if in_l > in_r:
            return None
        val = preorder[pre_l]
        root = TreeNode(val)
        i = index[val]
        root.left = _build(pre_l + 1, in_l, i - 1)
        # NOTE: the index of left child(pre_l + 1) plus the size of left subtree(i - in_l)
        root.right = _build(pre_l + 1 + i - in_l, i + 1, in_r)
        return root

    index = {v: i for i, v in enumerate(inorder)}
    return _build(0, 0, len(inorder) - 1)


# Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/


def build_tree2(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    """Same as above, just use postorder array from the end."""

    def build(post_r, in_l, in_r) -> TreeNode | None:
        if in_l > in_r:
            return None
        val = postorder[post_r]
        root = TreeNode(val)
        i = index[val]
        # NOTE: the index of right child(post_r - 1) minus the size of right subtree(in_r - i)
        root.left = build(post_r - 1 - (in_r - i), in_l, i - 1)
        root.right = build(post_r - 1, i + 1, in_r)
        return root

    index = {v: i for i, v in enumerate(inorder)}
    return build(len(postorder) - 1, 0, len(inorder) - 1)


# Construct Binary Tree from Preorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/


def build_tree3(preorder: list[int], postorder: list[int]) -> TreeNode | None:
    """
    From preorder array, find root node and left child node for left subtree,
    then index postorder array to get the size of left subtree.

    Time: O(n) with a hash map index
    Space: O(h), in the worst case O(n)
    """

    def _build(pre_l, pre_r, post_l) -> TreeNode | None:
        if pre_l > pre_r:
            return None
        root = TreeNode(preorder[pre_l])
        if pre_l == pre_r:
            return root
        left_size = index[preorder[pre_l + 1]] - post_l + 1
        root.left = _build(pre_l + 1, pre_l + left_size, post_l)
        root.right = _build(pre_l + left_size + 1, pre_r, post_l + left_size)
        return root

    index = {v: i for i, v in enumerate(postorder)}
    return _build(0, len(preorder) - 1, 0)
