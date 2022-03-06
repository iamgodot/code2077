# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


def remove_elements(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(next=head)
    cur = dummy

    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next

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
