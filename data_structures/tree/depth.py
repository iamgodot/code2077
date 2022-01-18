# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。

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


# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 说明：叶子节点是指没有子节点的节点。


# 后序遍历
# 注意左右子节点都为空的节点才是叶子节点
# 和求最大深度的区别在于处理左子节点或右子节点为空的情况
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
