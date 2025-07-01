# Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/


from data_structures.linked_list import ListNode, make_linked_list, traverse_linked_list


def reverse_by_n(head: ListNode | None, n: int) -> ListNode | None:
    pre, cur = None, head
    # NOTE: don't forget to check if n is 0
    while cur and n > 0:
        next_ = cur.next
        cur.next = pre
        pre = cur
        cur = next_
        n -= 1

    return pre


def reverse_k_group(head: ListNode | None, k: int) -> ListNode | None:
    dummy = pre = ListNode(next=head)

    while pre.next:
        start = post = pre.next
        for _ in range(k):
            # NOTE: here we need to check post first
            if not post:
                return dummy.next
            post = post.next
        pre.next = reverse_by_n(start, k)
        start.next = post
        pre = start

    return dummy.next


if __name__ == "__main__":
    head = make_linked_list([1, 2, 3, 4, 5])
    assert traverse_linked_list(reverse_k_group(head, 2)) == [2, 1, 4, 3, 5]
