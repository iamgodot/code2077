# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


from typing import Optional

from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    采用归并排序的思路：
        1. 递归实现链表的分治，其中使用快慢指针来定位中点
        2. 归并时的逻辑就是经典的合并两个链表的做法
    这样得到的时间复杂度为 O(n * logn)，但是空间复杂度是 O(logn) 而不是 O(n)
    因为链表不是数组不需要新建大小为 n 的数组储存结果。
    如果想要实现常数级别的空间复杂度则不能使用递归来做分治，而是循环实现，
    设置 i 为 1 然后对单个元素成对排序，然后 i*2 再继续两两排序，直到完成所有排序。
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
