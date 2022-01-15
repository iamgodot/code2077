# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。


from linked_list import ListNode


# 1. 结合链表和哈希表，第一次迭代创建新节点并建立新旧节点的映射关系，第二次补全新节点的互联关系
# 这样时间复杂度为 O(n) 空间复杂度也是 O(n)
# 2. 还可以在原链表的基础上复制新链表，新旧节点相邻，这样第二遍遍历时就可以通过旧的 random.next 找到新的 random node，最后再拆分链表为两个
# 时间复杂度 O(n) 空间复杂度 O(1)
def copy_random_list(head: ListNode) -> ListNode:
    if not head:
        return head

    mappings = {}
    cur = head
    while cur:
        mappings[cur] = ListNode(cur.val)
        cur = cur.next

    cur = head
    while cur:
        mappings[cur].next = mappings.get(cur.next)
        mappings[cur].random = mappings.get(cur.random)
        cur = cur.next

    return mappings[head]
