# 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。

from typing import Optional

from data_structures.tree import TreeNode
from data_structures.tree.traversal import levelorder


# 1. 中序遍历 时间复杂度 O(n) 空间复杂度 递归占用 O(h)
# 2. 要达到 O(1) 的空间复杂度，要使用莫里斯遍历
def recover_tree(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    def recover(node: TreeNode):
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


def recover_tree(root: Optional[TreeNode]) -> None:
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
    root = TreeNode(1, left=TreeNode(3, right=TreeNode(2)))
    recover_tree(root)
    assert levelorder(root) == [[3], [1], [2]]
    root = TreeNode(3, left=TreeNode(1), right=TreeNode(4, left=TreeNode(2)))
    recover_tree(root)
    assert levelorder(root) == [[2], [1, 4], [3]]
