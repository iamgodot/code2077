class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def make_linked_list(vals: list) -> ListNode | None:
    dummy = ListNode()
    cur = dummy

    for val in vals:
        cur.next = ListNode(val=val)
        cur = cur.next

    return dummy.next


def traverse_linked_list(head: ListNode | None) -> list:
    res = []

    while head:
        res.append(head.val)
        head = head.next

    return res


__all__ = ["ListNode", "make_linked_list", "traverse_linked_list"]
