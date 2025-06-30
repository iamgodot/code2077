# Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/

from data_structures.tree import TreeNode


def is_substructure(A: TreeNode | None, B: TreeNode | None) -> bool:
    """
    Time: O(mn)
    Space: O(m)
    """

    def is_similar(a, b):
        if not a or not b:
            return a is b if not a else True
        return (
            a.val == b.val
            and is_similar(a.left, b.left)
            and is_similar(a.right, b.right)
        )

    if not A or not B:
        return False

    return is_similar(A, B) or is_substructure(A.left, B) or is_substructure(A.right, B)


if __name__ == "__main__":
    a = TreeNode(
        val=3,
        left=TreeNode(val=4, left=TreeNode(1), right=TreeNode(2)),
        right=TreeNode(5),
    )
    b = TreeNode(4, left=TreeNode(1))
    assert is_substructure(a, b) is True
