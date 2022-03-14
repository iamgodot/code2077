# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 你应当 保留 两个分区中每个节点的初始相对位置。

from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


def partition(head: ListNode, x: int) -> ListNode:
    h1, h2 = ListNode(), ListNode()
    cur1, cur2 = h1, h2
    cur = head
    while cur:
        if cur.val < x:
            cur1.next = cur
            cur1 = cur1.next
        else:
            cur2.next = cur
            cur2 = cur2.next
        cur = cur.next

    cur2.next = None
    cur1.next = h2.next

    return h1.next


if __name__ == "__main__":
    head = make_linked_list([1, 4, 3, 2, 5, 2])
    assert traverse_linked_list(partition(head, 3)) == [1, 2, 2, 4, 3, 5]
