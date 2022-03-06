# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


def swap_pairs(head: ListNode) -> ListNode:
    dummy = ListNode(next=head)
    pre = dummy

    while pre.next and pre.next.next:
        cur, post = pre.next, pre.next.next
        cur.next = post.next
        post.next = cur
        pre.next = post

        pre = pre.next.next

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
