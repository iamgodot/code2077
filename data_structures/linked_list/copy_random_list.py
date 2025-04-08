# Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/description/


class Node:
    def __init__(self, x: int, next: "Node|None" = None, random: "Node|None" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Node | None) -> Node | None:
    """
    Time: O(n)
    Space: O(n)
    """
    hash_map = {}
    cur = head
    while cur:
        hash_map[cur] = Node(cur.val)
        cur = cur.next

    cur = head
    while cur:
        hash_map[cur].next = hash_map.get(cur.next)
        hash_map[cur].random = hash_map.get(cur.random)
        cur = cur.next

    return hash_map.get(head)


def copy_random_list2(head: Node | None) -> Node | None:
    """
    Time: O(n)
    Space: O(1)
    """
    if not head:
        return None
    cur = head
    while cur:
        cur.next = Node(cur.val, next=cur.next)
        cur = cur.next.next
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    pre, cur = head, head.next
    res = head.next
    while cur.next:
        pre.next = pre.next.next
        cur.next = cur.next.next
        pre, cur = pre.next, cur.next
    pre.next = None
    return res
