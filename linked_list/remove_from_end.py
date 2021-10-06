# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 进阶：你能尝试使用一趟扫描实现吗？

from linked_list import ListNode, make_linked_list, traverse_linked_list


# 注意 n 应当为正数并且不大于 linked_list 的 size，否则要做更多判断
def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(next=head)
    slow = fast = dummy

    while n:
        fast = fast.next
        n -= 1

    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next

    return dummy.next


if __name__ == '__main__':
    for data, num, res in ([1], 1, []), ([1,
                                          2], 1, [1]), ([1, 2, 3, 4,
                                                         5], 2, [1, 2, 3, 5]):
        head = make_linked_list(data)
        assert traverse_linked_list(remove_nth_from_end(head, num)) == res
