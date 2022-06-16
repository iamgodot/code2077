# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

from data_structures.tree import TreeNode


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
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
