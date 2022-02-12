# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。


from typing import List, Optional

from data_structures.linked_list import ListNode


# 1. Bruteforce: 采用合并两个链表的思路，循环合并所有链表。最后的时间复杂度会达到 O(k^2 * n)
# 2. 利用最小堆的特性，每次向堆中插入下一个非空节点，然后取出最小的节点。要注意存储的元素必须可以做比较
# 由于堆的排序特性，最后的时间复杂度为 O(logk * n * k) 即 n*k 个节点，每个消耗 O(logk) 排序
# 空间复杂度 O(k) 为堆占用的空间大小
def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    (node.val, index) is the element goes in the heap
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


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
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


def merge(lists, left, right) -> ListNode:
    # 当 lists 为空，会出现此种 corner case
    if left > right:
        return None
    if left == right:
        return lists[left]
    mid = (left + right) // 2
    return merge_two_lists(merge(lists, left, mid), merge(lists, mid + 1, right))


# 3. 分治法
# 时间复杂度 O(logk * n * k) 一共 logk 轮，第一轮分为 k/2 组，每组排序耗费 O(2n).. 依次递归每一轮的成本都是 O(n * k)
# 空间复杂度 O(logk) 为递归调用栈空间
def merge_k_lists(lists) -> Optional[ListNode]:
    return merge(lists, 0, len(lists) - 1)


if __name__ == "__main__":
    assert merge_k_lists([]) == None
