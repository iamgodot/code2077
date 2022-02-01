# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

from data_structures.tree import TreeNode


def treeToDoublyList(root: TreeNode) -> TreeNode:
    def traversal(cur):
        nonlocal pre, head
        if not cur:
            return
        traversal(cur.left)
        if not pre:
            head = cur
        else:
            pre.right, cur.left = cur, pre
        pre = cur
        traversal(cur.right)

    if not root:
        return None
    head = pre = None
    traversal(root)
    head.left, pre.right = pre, head
    return head
