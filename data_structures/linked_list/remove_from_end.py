# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 进阶：你能尝试使用一趟扫描实现吗？

from data_structures.linked_list import (ListNode, make_linked_list,
                                         traverse_linked_list)


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """
    注意 n 应当为正数并且不大于 linked_list 的 size，否则要做更多判断
    1. 先计算出链表的总长度，再找到第 L - n 个节点进行删除
    2. 借助栈，先全部入栈，再弹出 n 个节点，然后用栈顶节点删除
    3. 双指针法，如此只需要一趟遍历

    使用 dummy 节点来简化 head 节点的删除操作。
    """
    dummy = ListNode(next=head)
    node1, node2 = head, dummy

    for _ in range(n):
        node1 = node1.next
    while node1:
        node1, node2 = node1.next, node2.next
    node2.next = node2.next.next

    return dummy.next


if __name__ == "__main__":
    for data, num, res in (
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ):
        head = make_linked_list(data)
        assert traverse_linked_list(remove_nth_from_end(head, num)) == res
