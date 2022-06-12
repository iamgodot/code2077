# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

from data_structures.linked_list import ListNode
from data_structures.tree import TreeNode


def sorted_array_to_bst(nums: list) -> TreeNode:
    """
    时间复杂度 O(n)
    空间复杂度 O(logn)
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


# 单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差不超过 1。


def linked_list_to_bst(head: ListNode) -> TreeNode:
    """
    时间复杂度 O(n*logn) 相当于每次递归中去找 mid 的成本是 O(n)
    空间复杂度 O(logn) 注意是平衡二叉树
    """

    def build(left: ListNode, right: ListNode):
        # 注意 base case
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


def linked_list_to_bst(head: ListNode) -> TreeNode:
    """
    利用中序遍历来构建 BST，这样可以直接使用 head 节点而不需要每次都找中间节点了
    时间复杂度 O(n)
    空间复杂度 O(logn) 注意是平衡二叉树
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
