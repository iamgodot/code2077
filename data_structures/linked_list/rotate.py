# Rotate List
# https://leetcode.com/problems/rotate-list/description/

from data_structures.linked_list import (
    ListNode,
    make_linked_list,
    traverse_linked_list,
)


def rotateRight(head: ListNode | None, k: int) -> ListNode | None:
    """
    Know that k could be very large.

    Time: O(n)
    Space: O(1)
    """
    if not head or not head.next or k == 0:
        return head
    cur = head
    n = 1
    while cur.next:
        cur = cur.next
        n += 1

    k %= n
    if k == 0:
        return head

    cur.next = head
    # NOTE: find new tail
    for _ in range(n - k):
        cur = cur.next
    head_new = cur.next
    cur.next = None
    return head_new


if __name__ == "__main__":
    head = make_linked_list([1, 2, 3, 4, 5])
    assert traverse_linked_list(rotateRight(head, 2)) == [4, 5, 1, 2, 3]
    print("Passed!")
