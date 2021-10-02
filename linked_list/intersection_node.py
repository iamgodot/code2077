# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

from linked_list import ListNode, make_linked_list


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> ListNode:
    cur_a, cur_b = head_a, head_b

    while cur_a != cur_b:
        cur_a = cur_a.next if cur_a else head_b
        cur_b = cur_b.next if cur_b else head_a

    return cur_a


if __name__ == '__main__':
    a, b = ListNode(), ListNode()
    assert get_intersection_node(a, b) is None
    head_a = make_linked_list([i for i in range(1, 6)])
    head_b = ListNode(next=head_a.next)
    assert get_intersection_node(head_a, head_b).val == 2
