from data_structures.linked_list import ListNode

# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/description


def mergeTwolists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = cur = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


# Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/


def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    """
    Assume n is the average length of each list.

    If using brute-force, time complexity will be O(nk^2)
    We can also use a heap, (node.val, index) is the element goes in the heap

    Time: O(nklogk)
    Space: O(logk)
    """
    import heapq

    hq = []
    dummy = cur = ListNode()

    for i in range(len(lists)):
        node = lists[i]
        if node:
            heapq.heappush(hq, (node.val, i))

    while hq:
        _, index = heapq.heappop(hq)
        node = lists[index]
        cur.next = node
        cur = cur.next
        if node.next:
            node = node.next
            heapq.heappush(hq, (node.val, index))
            lists[index] = node

    return dummy.next


def mergeKLists2(lists: list[ListNode | None]) -> ListNode | None:
    """
    We can also use a divide-and-conquer appraoch.
    There're in total logk rounds, the first round has k/2 groups and takes O(2n) time, resulting in O(nk) total time, and the same goes for all the subsequent rounds.

    Time: O(nklogk)
    Space: O(logk)
    """

    def _merge(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = cur = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 or list2
        return dummy.next

    def _merge_k_lists(lists, left, right) -> ListNode | None:
        # NOTE: in case lists is empty
        if left > right:
            return None
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = _merge_k_lists(lists, left, mid)
        l2 = _merge_k_lists(lists, mid + 1, right)
        return _merge(l1, l2)

    return _merge_k_lists(lists, 0, len(lists) - 1)
