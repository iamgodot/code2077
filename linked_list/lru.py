# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
# 实现 LRUCache 类：

# LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

# 进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？


class DoubleLinkedListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashtable = {}
        self.head = DoubleLinkedListNode()
        self.tail = DoubleLinkedListNode()
        self.head.next = self.tail
        self.tail.previous = self.head

    def remove_node(self, node) -> None:
        node.previous.next = node.next
        node.next.previous = node.previous

    def add_to_head(self, node) -> None:
        node.next = self.head.next
        node.previous = self.head
        self.head.next.previous = node
        self.head.next = node

    def move_to_head(self, node) -> None:
        self.remove_node(node)
        self.add_to_head(node)

    def remove_from_tail(self) -> DoubleLinkedListNode:
        node = self.tail.previous
        self.remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key in self.hashtable:
            node = self.hashtable[key]
            self.move_to_head(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashtable:
            node = self.hashtable[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = DoubleLinkedListNode(key, value)
            self.hashtable[key] = node
            self.add_to_head(node)
            if len(self.hashtable) > self.capacity:
                node_least_used = self.remove_from_tail()
                self.hashtable.pop(node_least_used.key)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
