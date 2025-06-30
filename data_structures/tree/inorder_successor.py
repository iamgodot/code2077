# Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/description/


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


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Inorder Successor in BST II
# https://leetcode.com/problems/inorder-successor-in-bst-ii/description/


def find_next(node: TreeNode | None) -> TreeNode | None:
    """
    1. 如果右子树存在，那么返回右子树的最小（左）节点
    2. 右子树不存在，向上查找父节点
      1. 如果当前节点为父节点的左子节点，那么直接返回父节点
      2. 如果当前节点为父节点的右子节点，那么继续向上查找
        1. 如果某个父节点为其父节点的左子节点，返回其父节点
        2. 否则最终返回空节点
    """
    if not node:
        return None
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur
    else:
        cur = node
        while cur.next:
            parent = cur.next
            if cur is parent.left:
                return parent
            else:
                cur = parent
    return None
