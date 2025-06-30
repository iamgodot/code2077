# Merge Two Binary Trees
# https://leetcode.com/problems/merge-two-binary-trees/description/

from data_structures.tree import TreeNode


def merge(root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
    """
    Time: O(min(m, n))
    Space: O(min(h1, h2))
    """
    if not root1 or not root2:
        return root1 or root2
    root1.val += root2.val
    root1.left = merge(root1.left, root2.left)
    root1.right = merge(root1.right, root2.right)
    return root1
