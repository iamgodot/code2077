# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


# 1. 循环法，时间复杂度 O(n)，空间复杂度 O(1)
def reverse_list(head: ListNode) -> ListNode:
    pre, cur = None, head

    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre


# 2. 递归法，时间复杂度 O(n)，空间复杂度 O(n)
def reverse_list_by_recursion(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverse_list_by_recursion(head.next)
    head.next.next = head
    head.next = None

    return new_head


# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


# 1. 直接找到区间边界的两个元素，反转区间子链表，最后调整边界指针
def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    def reverse(head, n):
        pre, cur = None, head
        while cur and n:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_
            n -= 1

        return pre

    dummy = start = end = ListNode(next=head)
    for _ in range(left - 1):
        start = start.next
    for _ in range(right + 1):
        end = end.next
    head = start.next
    head_new = reverse(head, right - left + 1)
    start.next = head_new
    head.next = end

    return dummy.next


# 2. 第一种方法需要遍历两次，如果想要只遍历一次的话，就必须在遍历的过程中即时更新指针
# 简单来说就是对于需要反转的子链表，每次把下一个元素插入到区间的第一个位置，这样一次
# 遍历完成之后就不用再做多余的调整。
def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    dummy = pre = ListNode(next=head)
    for _ in range(left - 1):
        pre = pre.next

    cur = pre.next
    for _ in range(right - left):
        next_ = cur.next
        cur.next = next_.next
        next_.next = pre.next
        pre.next = next_

    return dummy.next


if __name__ == "__main__":
    for method in [reverse_list, reverse_list_by_recursion]:
        head = make_linked_list([1, 2, 3])
        assert traverse_linked_list(method(head)) == [3, 2, 1]
