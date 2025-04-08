# Partition List
# https://leetcode.com/problems/partition-list/description/

from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def partition(head: ListNode | None, x: int) -> ListNode | None:
    """
    Time: O(n)
    Space: O(1)
    """
    h1, h2 = ListNode(), ListNode()
    cur1, cur2 = h1, h2
    cur = head
    while cur:
        if cur.val < x:
            cur1.next = cur
            cur1 = cur1.next
        else:
            cur2.next = cur
            cur2 = cur2.next
        cur = cur.next

    cur1.next = h2.next
    cur2.next = None  # NOTE: clean cut

    return h1.next


if __name__ == "__main__":
    head = make_linked_list([1, 4, 3, 2, 5, 2])
    assert traverse_linked_list(partition(head, 3)) == [1, 2, 2, 4, 3, 5]
