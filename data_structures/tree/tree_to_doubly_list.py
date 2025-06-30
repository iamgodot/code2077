# Convert Binary Search Tree to Sorted Doubly Linked List
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

from data_structures.tree import TreeNode


def treeToDoublyList(root: TreeNode | None) -> TreeNode | None:
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
