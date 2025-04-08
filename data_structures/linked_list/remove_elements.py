# Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def remove_elements(head: ListNode | None, val: int) -> ListNode | None:
    dummy = cur = ListNode(next=head)

    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


# Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


def delete_duplicates(head: ListNode) -> ListNode:
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


# Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


def delete_duplicates2(head: ListNode | None) -> ListNode | None:
    dummy = cur = ListNode(next=head)
    while cur.next:
        node = cur.next
        if node.next and node.val == node.next.val:
            while cur.next and cur.next.val == node.val:
                cur.next = cur.next.next
        else:
            cur = node
    return dummy.next


if __name__ == "__main__":
    for data, val, res in (
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([], 1, []),
        ([7, 7, 7, 7], 7, []),
    ):
        head = make_linked_list(data)
        head_new = remove_elements(head, val)
        assert traverse_linked_list(head_new) == res
