# Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/


from data_structures.tree import TreeNode


def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Bottom-up approach.

    Time: O(n)
    Space: O(n)
    """

    def get_depth(node) -> int:
        nonlocal max_
        if not node:
            return 0
        left = get_depth(node.left)
        right = get_depth(node.right)
        max_ = max(max_, left + right)
        return max(left, right) + 1

    max_ = -float("inf")
    get_depth(root)
    return max_
