# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
# 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
# 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
# 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。


from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


def reorder(head: ListNode) -> ListNode:
    h1, h2 = ListNode(), ListNode()
    cur1, cur2 = h1, h2

    is_single = True
    cur = head
    while cur:
        if is_single:
            cur1.next = cur
            cur1 = cur1.next
        else:
            cur2.next = cur
            cur2 = cur2.next
        cur = cur.next
        is_single = not is_single

    # 这里记得一定要将 cur2 后面断开，不然结果会出现环
    # 比如 [1,2,3]，最后 2 和 3 会互相指向对方
    cur2.next = None
    cur1.next = h2.next
    return h1.next


if __name__ == "__main__":
    head = make_linked_list([1, 2, 3, 4, 5])
    assert traverse_linked_list(reorder(head)) == [1, 3, 5, 2, 4]
