# 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。

from typing import Optional

from data_structures.tree import TreeNode


# 1. 中序遍历 时间复杂度 O(n) 空间复杂度 递归占用 O(h)
# 2. 要达到 O(1) 的空间复杂度，要使用莫里斯遍历
def recover_tree(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    def recover(node: TreeNode):
        nonlocal val, pre
        nonlocal x, y
        if not node:
            return
        recover(node.left)
        if val is not None and val > node.val:
            if not x:
                x = pre
            # if not y:
            y = node
        val, pre = node.val, node
        recover(node.right)

    val = pre = None
    x = y = None
    recover(root)
    x.val, y.val = y.val, x.val
