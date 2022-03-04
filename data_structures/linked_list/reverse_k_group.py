# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。

# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 进阶：

# 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


from typing import List

from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


def reverse_by_k(head: ListNode, k: int) -> ListNode:
    pre, cur = None, head
    while cur and k:
        next_ = cur.next
        cur.next = pre
        pre = cur
        cur = next_
        k -= 1

    return pre


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    dummy = pre = ListNode(next=head)

    while pre.next:
        head = head_next = pre.next
        for _ in range(k):
            if not head_next:
                return dummy.next
            head_next = head_next.next
        head_new = reverse_by_k(head, k)
        pre.next = head_new
        head.next = head_next
        pre = head

    return dummy.next


if __name__ == "__main__":
    head = make_linked_list([1, 2, 3, 4, 5])
    assert traverse_linked_list(reverse_k_group(head, 2)) == [2, 1, 4, 3, 5]
