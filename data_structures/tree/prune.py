# Binary Tree Pruning
# https://leetcode.com/problems/binary-tree-pruning/description/

from data_structures.tree import TreeNode
from data_structures.tree.traversal import levelorder


def prune_tree(root: TreeNode | None) -> TreeNode | None:
    """
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return None

    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)
    if not root.left and not root.right and root.val == 0:
        return None
    else:
        return root


# Trim a Binary Search Tree
# https://leetcode.com/problems/trim-a-binary-search-tree/description/


def trim_bst(root: TreeNode | None, low: int, high: int) -> TreeNode | None:
    """
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return None
    if root.val < low:
        return trim_bst(root.left, low, high)
    elif root.val > high:
        return trim_bst(root.right, low, high)
    else:
        root.left = trim_bst(root.left, low, high)
        root.right = trim_bst(root.right, low, high)
        return root


if __name__ == "__main__":
    tree = TreeNode(1, right=TreeNode(0, left=TreeNode(0), right=TreeNode(1)))
    node = prune_tree(tree)
    assert levelorder(node) == [[1], [0], [1]]
