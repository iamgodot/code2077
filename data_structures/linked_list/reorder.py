# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：

# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


def reorder(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.

    一种思路是将所有节点拷贝到数组中，再利用数组元素随机存取的特性和双指针解决；
    另一种思路是先将链表对半拆分，把后半部分反转，再重新组合为新链表。这样就不需要额外的空间。
    """

    def reverse(head):
        pre, cur = None, head
        while cur:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_

        return pre

    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    cur1, cur2 = head, reverse(slow.next)
    slow.next = None
    while cur1 and cur2:
        n1, n2 = cur1.next, cur2.next
        cur1.next = cur2
        cur2.next = n1
        cur1, cur2 = n1, n2

    return head


if __name__ == "__main__":
    head = make_linked_list([1, 2, 3, 4, 5])
    reorder(head)
    assert traverse_linked_list(head) == [1, 5, 2, 4, 3]
