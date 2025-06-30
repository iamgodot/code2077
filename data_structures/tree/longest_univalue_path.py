# Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/description/

from data_structures.tree import TreeNode


def longest_univalue_path(root: TreeNode | None) -> int:
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
