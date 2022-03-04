# 给定一个链表，判断链表中是否有环。
# 如果链表中存在环，则返回 true 。 否则，返回 false 。

from data_structures.linked_list import ListNode


def has_cycle(head: ListNode) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True

    return False


def detect_cycle(head: ListNode) -> ListNode:
    slow = fast = head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            m, n = head, slow

            while m != n:
                m = m.next
                n = n.next

            return m

    return None
