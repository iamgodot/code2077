# Reorder List
# https://leetcode.com/problems/reorder-list/description/


from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def reorder(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.

    Split the list into half, reverse the second half, and then merge them.

    Time: O(n)
    Space: O(1)
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


if __name__ == "__main__":
    head = make_linked_list([1, 2, 3, 4, 5])
    reorder(head)
    assert traverse_linked_list(head) == [1, 5, 2, 4, 3]
