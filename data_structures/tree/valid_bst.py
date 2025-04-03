# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/description/

from data_structures.tree import TreeNode


def isValidBST(root: TreeNode | None) -> bool:
    """
    Preorder traversal.

    Time: O(n)
    Space: O(h)
    """

    def validate(node, low, high) -> bool:
        if not node:
            return True
        if not low < node.val < high:
            return False
        return validate(node.left, low, node.val) and validate(
            node.right, node.val, high
        )

    return validate(root, -float("inf"), float("inf"))


def isValidBST2(root: TreeNode | None) -> bool:
    """
    Inorder traversal.

    Time: O(n)
    Space: O(h)
    """

    def validate(node: TreeNode | None) -> bool:
        if not node:
            return True
        nonlocal pre
        if not validate(node.left):
            return False
        if node.val <= pre:
            return False
        pre = node.val
        return validate(node.right)

    pre = -float("inf")
    return validate(root)
