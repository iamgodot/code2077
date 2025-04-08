# Sort List
# https://leetcode.com/problems/sort-list/description/


from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def sort_list(head: ListNode | None) -> ListNode | None:
    """
    2 ways of applying merge sort.

    Top-down: time O(nlogn), space O(logn) since we don't need a new array.
    Bottom-up: time O(n), space O(1)
    """
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # Split in half
    mid = slow.next
    slow.next = None

    node1, node2 = sort_list(head), sort_list(mid)
    dummy = cur = ListNode()
    while node1 and node2:
        if node1.val <= node2.val:
            cur.next = node1
            node1 = node1.next
        else:
            cur.next = node2
            node2 = node2.next
        cur = cur.next

    cur.next = node1 or node2

    return dummy.next


if __name__ == "__main__":
    head = make_linked_list([-1, 5, 3, 4, 0])
    assert traverse_linked_list(sort_list(head)) == [-1, 0, 3, 4, 5]
