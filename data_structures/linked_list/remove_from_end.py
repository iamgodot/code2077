# Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def remove_nth_from_end(head: ListNode, n: int) -> ListNode | None:
    """
    1. 2-pass, time: O(n), space: O(1)
    2. 1-pass with 2 pointers, time: O(n), space: O(1)
    3. Use a stack, time: O(n), space: O(n)

    Remember to use a dummy node to handle empty list after deletion.
    """
    dummy = slow = fast = ListNode(next=head)

    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
    for data, num, res in (
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ):
        head = make_linked_list(data)
        assert traverse_linked_list(remove_nth_from_end(head, num)) == res
