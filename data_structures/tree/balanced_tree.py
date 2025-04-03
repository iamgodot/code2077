# Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/description/

from data_structures.tree import TreeNode


# 后序遍历
def is_balanced(root: TreeNode) -> bool:
    """
    Bottom-up approach.
    Could do top-down as well, which requires O(nlogn) time.

    Time: O(n)
    Space: O(n)
    """

    def get_depth(root: TreeNode) -> int:
        if not root:
            return -1
        depth_left = get_depth(root.left)
        if depth_left == -2:
            return -2
        depth_right = get_depth(root.right)
        if depth_right == -2:
            return -2
        if abs(depth_left - depth_right) > 1:
            return -2
        return max(depth_left, depth_right) + 1

    return get_depth(root) != -2


if __name__ == "__main__":
    # 3
    # |\
    # 9 20
    #   |\
    #  15 7
    root = TreeNode(
        val=3,
        left=TreeNode(val=9),
        right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(7)),
    )
    assert is_balanced(root) is True
    # 1
    # |\
    # 2 2
    # |\
    # 3 3
    # |\
    # 4 4
    root = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            left=TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=4)),
            right=TreeNode(val=3),
        ),
        right=TreeNode(val=2),
    )
    assert is_balanced(root) is False
