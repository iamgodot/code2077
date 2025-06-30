# Same Tree
# https://leetcode.com/problems/same-tree/description/

from data_structures.tree import TreeNode


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    时间复杂度 O(min(n1, n2))
    空间复杂度 O(min(h1, h2))
    """
    if not p or not q:
        return p is q
    return (
        p.val == q.val
        and is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )
