# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

from linked_list import ListNode, make_linked_list, traverse_linked_list


# 1. 循环法，时间复杂度 O(n)，空间复杂度 O(1)
def reverse_list(head: ListNode) -> ListNode:
    pre, cur = None, head

    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre


# 2. 递归法，时间复杂度 O(n)，空间复杂度 O(n)
def reverse_list_by_recursion(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverse_list_by_recursion(head.next)
    head.next.next = head
    head.next = None

    return new_head


if __name__ == '__main__':
    for method in [reverse_list, reverse_list_by_recursion]:
        head = make_linked_list([1, 2, 3])
        assert traverse_linked_list(method(head)) == [3, 2, 1]
