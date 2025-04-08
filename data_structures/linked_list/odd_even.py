# Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/description/


from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def reorder(head: ListNode | None) -> ListNode | None:
    h1, h2 = ListNode(), ListNode()
    cur1, cur2 = h1, h2
    is_odd = True
    cur = head
    while cur:
        if is_odd:
            cur1.next = cur
            cur1 = cur1.next
        else:
            cur2.next = cur
            cur2 = cur2.next
        cur = cur.next
        is_odd = not is_odd

    cur1.next = h2.next
    cur2.next = None  # NOTE: clean cut, same as partition
    return h1.next


if __name__ == "__main__":
    head = make_linked_list([1, 2, 3, 4, 5])
    assert traverse_linked_list(reorder(head)) == [1, 3, 5, 2, 4]
