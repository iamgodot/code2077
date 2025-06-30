# Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/description/

from data_structures.tree import TreeNode


def count(root: TreeNode | None) -> int:
    # TODO: add explanation
    if not root:
        return 0

    def count_level(node):
        level = 0
        while node:
            level += 1
            node = node.left
        return level

    left = count_level(root.left)
    right = count_level(root.right)

    if left == right:
        return 2**left + count(root.right)
    else:
        return 2**right + count(root.left)


if __name__ == "__main__":
    # 1
    # | \
    # 2  3
    # |\ |
    # 4 56
    root = TreeNode(
        val=1,
        left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(5)),
        right=TreeNode(val=3, left=TreeNode(val=6)),
    )
    assert count(root) == 6
