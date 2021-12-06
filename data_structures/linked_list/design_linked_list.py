from linked_list import ListNode, traverse_linked_list


# 非常考验链表的基础认识
# 首先要认识到给链表的结构加上 size，这样可以减少很多 edge cases 的额外检验
# 其次就是 dummy(sentinel) node 的使用，也可以直接把 head 做成伪头
# 另外还有细节的检查，比如 index 为负的情况，需要更新 size 和 head 等
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head

        for _ in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # < 0 -> head
        index = max(index, 0)
        # > size -> nothing

        if index > self.size:
            return
        else:
            dummy = ListNode(0, next=self.head)
            cur = dummy

            for _ in range(index):
                cur = cur.next

            # == -> tail 这里合并了 insert 和 append 两种情况
            cur.next = ListNode(val, next=cur.next)
            # update head
            self.head = dummy.next
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        dummy = ListNode(next=self.head)
        cur = dummy

        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
        # update head
        self.head = dummy.next
        self.size -= 1


if __name__ == '__main__':
    ll = MyLinkedList()
    ll.addAtHead(4)
    ll.addAtHead(3)
    ll.addAtTail(2)
    ll.addAtIndex(1, 1)
    assert traverse_linked_list(ll.head) == [3, 1, 4, 2]
    assert ll.get(-1) == -1
    assert ll.get(4) == -1
    assert ll.get(1) == 1
    ll.deleteAtIndex(-1)
    ll.deleteAtIndex(4)
    ll.deleteAtIndex(2)
    assert traverse_linked_list(ll.head) == [3, 1, 2]
