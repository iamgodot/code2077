# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from data_structures.tree import TreeNode


# 后序遍历
def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_it(root: TreeNode) -> int:
    if not root:
        return 0
    from collections import deque

    dq = deque([root])
    depth = 0
    while dq:
        for _ in range(len(dq)):
            node = dq.pop()
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)
        depth += 1
    return depth


# Minumum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/


def min_depth(root: TreeNode) -> int:
    if not root:
        return 0
    min_depth_left = min_depth(root.left)
    min_depth_right = min_depth(root.right)
    if root.left and not root.right:
        return 1 + min_depth_left
    if not root.left and root.right:
        return 1 + min_depth_right
    return 1 + min(min_depth_left, min_depth_right)


def min_depth_it(root: TreeNode) -> int:
    if not root:
        return 0
    from collections import deque

    dq = deque([root])
    depth = 0
    while dq:
        depth += 1
        for _ in range(len(dq)):
            node = dq.pop()
            if not node.left and not node.right:
                return depth
            if node.left:
                dq.appendleft(node.left)
            if node.right:
                dq.appendleft(node.right)
    return depth


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
    for method in [max_depth, max_depth_it]:
        assert method(root) == 3
    for method in [min_depth, min_depth_it]:
        assert method(root) == 2
