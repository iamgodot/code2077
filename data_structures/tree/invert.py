# Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/description/
from data_structures.tree import TreeNode, levelorder


def invert(root: TreeNode):
    if root:
        root.left, root.right = invert(root.right), invert(root.left)
    return root


def invert_it(root: TreeNode):
    stack = []
    cur = root
    while cur or stack:
        if cur:
            cur.left, cur.right = cur.right, cur.left
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()

    return root


if __name__ == "__main__":
    for method in [invert, invert_it]:
        root = TreeNode(
            val=4,
            left=TreeNode(val=2, left=TreeNode(1), right=TreeNode(3)),
            right=TreeNode(val=7, left=TreeNode(6), right=TreeNode(9)),
        )
        # Before invert
        # 4
        # | \
        # 2  7
        # |\ |\
        # 1 36 9
        # After invert
        # 4
        # | \
        # 7  2
        # |\ |\
        # 9 63 1
        res = levelorder(method(root))
        assert [i for j in res for i in j] == [4, 7, 2, 9, 6, 3, 1]
