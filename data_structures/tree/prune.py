# 给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。
# 返回移除了所有不包含 1 的子树的原二叉树。
# 节点 node 的子树为 node 本身加上所有 node 的后代。

# 树中节点的数目在范围 [1, 200] 内
# Node.val 为 0 或 1

from typing import Optional

from data_structures.tree import TreeNode
from data_structures.tree.traversal import levelorder


def prune_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
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


# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树 不应该 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 唯一的答案 。
# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。


def trim_bst(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
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
