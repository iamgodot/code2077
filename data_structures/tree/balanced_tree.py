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

    def height(node: TreeNode) -> int:
        if not node:
            return 0
        left, right = height(node.left), height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

    return height(root) != -1


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
