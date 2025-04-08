# Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/

from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Time: O(max(m,n))
    Space: O(1)
    """
    dummy = ListNode()
    cur, cur1, cur2 = dummy, l1, l2
    carry = 0
    while cur1 or cur2:
        val1 = cur1.val if cur1 else 0
        val2 = cur2.val if cur2 else 0
        carry, val = divmod(val1 + val2 + carry, 10)
        cur.next = ListNode(val)
        cur = cur.next
        if cur1:
            cur1 = cur1.next
        if cur2:
            cur2 = cur2.next
    if carry:
        cur.next = ListNode(carry)

    return dummy.next


# Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/description/
def add_two_numbers_rev(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    We can either reverse the lists or use stacks.

    Time: O(m+n)
    Space: O(m+n)
    """
    s1, s2 = [], []
    while l1 or l2:
        if l1:
            s1.append(l1.val)
            l1 = l1.next
        if l2:
            s2.append(l2.val)
            l2 = l2.next

    head = None
    carry = 0
    while s1 or s2:
        val1 = s1.pop() if s1 else 0
        val2 = s2.pop() if s2 else 0
        carry, val = divmod(val1 + val2 + carry, 10)
        head = ListNode(val, head)

    if carry:
        head = ListNode(carry, head)

    return head


if __name__ == "__main__":
    for d1, d2, res in (
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9] * 7, [9] * 4, [8, 9, 9, 9, 0, 0, 0, 1]),
    ):
        l1 = make_linked_list(d1)
        l2 = make_linked_list(d2)
        assert traverse_linked_list(add_two_numbers(l1, l2)) == res

    for d1, d2, res in (
        ([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7]),
        ([2, 4, 3], [5, 6, 4], [8, 0, 7]),
        ([0], [0], [0]),
    ):
        l1 = make_linked_list(d1)
        l2 = make_linked_list(d2)
        assert traverse_linked_list(add_two_numbers_rev(l1, l2)) == res
