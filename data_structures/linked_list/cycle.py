# Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

from data_structures.linked_list import ListNode


def has_cycle(head: ListNode) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True

    return False


# Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/


def detect_cycle(head: ListNode | None) -> ListNode | None:
    """
    1. Use a hash set, time: O(n), space: O(n)
    2. Floyd's Tortoise and Hare Algorithm
    2(a + b) = a + 2b + c -> a = c
    Time: O(n), space: O(1)
    """
    slow = fast = head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            slow = head

            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow
    return None
