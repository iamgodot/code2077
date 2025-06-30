# Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

from data_structures.linked_list import ListNode
from data_structures.tree import TreeNode


def sorted_array_to_bst(nums: list) -> TreeNode:
    """
    Time: O(n)
    Space: O(logn)
    """

    def build(left, right) -> TreeNode:
        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = build(left, mid - 1)
        node.right = build(mid + 1, right)
        return node

    return build(0, len(nums) - 1)


# Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/


def linked_list_to_bst(head: ListNode) -> TreeNode:
    """
    Time: O(nlogn)
    Space: O(logn)
    """

    def build(left: ListNode, right: ListNode) -> TreeNode:
        if left is right:
            return None

        slow, fast = left, left.next
        while fast is not right and fast.next is not right:
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.val)
        root.left = build(left, slow)
        root.right = build(slow.next, right)
        return root

    return build(head, None)


def linked_list_to_bst2(head: ListNode) -> TreeNode:
    """
    Time: O(n)
    Space: O(logn)
    """

    def build(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode()
        root.left = build(left, mid - 1)
        nonlocal head
        root.val = head.val
        head = head.next
        root.right = build(mid + 1, right)
        return root

    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    return build(0, length - 1)
