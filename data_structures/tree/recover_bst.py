# Recover Binary Search Tree
# https://leetcode.com/problems/recover-binary-search-tree/description/

from data_structures.tree import TreeNode
from data_structures.tree.traversal import levelorder


def recover_tree(root: TreeNode | None) -> None:
    """
    Do not return anything, modify root in-place instead.

    Time: O(n)
    Space: O(h)
    """

    def recover(node: TreeNode | None):
        nonlocal pre, x, y
        if not node:
            return
        recover(node.left)
        if pre and pre.val > node.val:
            if not x:
                x = pre
            y = node
        pre = node
        recover(node.right)

    pre = None
    x = y = None
    recover(root)
    x.val, y.val = y.val, x.val


def recover_tree2(root: TreeNode | None) -> None:
    """
    使用莫里斯遍历达到 O(1) 的空间复杂度。
    1. 如果存在左子节点：寻找左子树的最右节点，核心是为了增加链接以后跳回来。
        1.1. 如果链接不存在，增加链接，然后跳到左子节点。
        1.2. 如果链接存在，说明左子树已经遍历完毕，对当前节点执行逻辑，断开链接，跳到右子节点。
    2. 如果不存在左子节点：对当前节点执行逻辑，跳到右子节点。

    可以看出来 1.2 和 2 做的事情基本是重复的，除了断开链接的部分。

    Time: O(n)
    Space: O(1)
    """
    pre = None
    x = y = None
    while root:
        if root.left:
            node = root.left
            while node.right and node.right is not root:
                node = node.right
            if not node.right:
                node.right = root
                root = root.left
            else:
                if pre and pre.val > root.val:
                    if not x:
                        x = pre
                    y = root
                pre = root
                node.right = None
                root = root.right
        else:
            if pre and pre.val > root.val:
                if not x:
                    x = pre
                y = root
            pre = root
            root = root.right
    x.val, y.val = y.val, x.val


if __name__ == "__main__":
    for func in [recover_tree, recover_tree2]:
        tree = TreeNode(1, left=TreeNode(3, right=TreeNode(2)))
        func(tree)
        assert levelorder(tree) == [[3], [1], [2]]
        tree = TreeNode(3, left=TreeNode(1), right=TreeNode(4, left=TreeNode(2)))
        func(tree)
        assert levelorder(tree) == [[2], [1, 4], [3]]
