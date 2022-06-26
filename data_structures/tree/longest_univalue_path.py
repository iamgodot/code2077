# 给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。
# 两个节点之间的路径长度 由它们之间的边数表示。

from typing import Optional

from data_structures.tree import TreeNode


def longest_univalue_path(root: Optional[TreeNode]) -> int:
    def get_uni_edge(node) -> int:
        if not node:
            return 0
        left = get_uni_edge(node.left)
        right = get_uni_edge(node.right)
        nonlocal res
        l = r = 0
        if node.left and node.left.val == node.val:
            l = left + 1
        if node.right and node.right.val == node.val:
            r = right + 1
        res = max(res, l + r)
        return max(l, r)

    res = 0
    get_uni_edge(root)
    return res
