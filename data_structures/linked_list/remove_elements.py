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


# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。


def delete_duplicates(head: ListNode) -> ListNode:
    dummy = cur = ListNode(next=head)
    while cur.next:
        node = cur.next
        if node and node.next and node.val == node.next.val:
            node.next = node.next.next
        else:
            cur = cur.next
    return dummy.next


# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。


def delete_duplicates2(head: ListNode) -> ListNode:
    """注意如果整个链表都是重复的，那么要返回空节点"""
    dummy = cur = ListNode(next=head)
    while cur.next:
        node = cur.next
        if node and node.next and node.val == node.next.val:
            while cur.next and cur.next.val == node.val:
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
