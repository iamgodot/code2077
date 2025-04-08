# Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def swap_pairs(head: ListNode | None) -> ListNode | None:
    """
    Time: O(n)
    Space: O(1)
    """
    dummy = pre = ListNode(next=head)

    while pre.next and pre.next.next:
        first, second = pre.next, pre.next.next
        first.next = second.next
        second.next = first
        pre.next = second
        pre = first

    return dummy.next


if __name__ == "__main__":
    for before, after in (
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
    ):
        head = make_linked_list(before)
        assert traverse_linked_list(swap_pairs(head)) == after
