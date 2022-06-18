# 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。
# 节点 p 的后继是值比 p.val 大的节点中键值最小的节点。


from data_structures.tree import TreeNode


def inorder_successor(root: TreeNode, p: TreeNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(n)
    """

    def traversal(node) -> None:
        if not node:
            return
        traversal(node.left)
        nonlocal pre, res
        if pre is p:
            res = node
        pre = node
        traversal(node.right)

    pre = res = None
    traversal(root)
    return res


def inorder_successor(root: TreeNode, p: TreeNode) -> TreeNode:
    """
    Time: O(h)
    Space: O(1)
    """
    cur = root
    res = None
    while cur:
        if cur.val > p.val:
            res = cur
            cur = cur.left
        else:
            cur = cur.right
    return res
