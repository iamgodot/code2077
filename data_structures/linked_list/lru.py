# LRU Cache
# https://leetcode.com/problems/lru-cache/description/


class Node:
    def __init__(self, key=None, value=None, previous=None, next=None):
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next


class LRUCache:
    """Use a combination of hash map and doubly linked list.

    The most recently used item: head
    The least recently used item: tail
    Hash map: key -> node(key, value)

    Time: O(1) for both get and put
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashtable = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.previous = self.head

    def _move_to_head(self, node) -> None:
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_from_tail(self) -> Node:
        return self._remove_node(self.tail.previous)

    def _add_to_head(self, node) -> None:
        node.previous = self.head
        node.next = self.head.next
        self.head.next.previous = node
        self.head.next = node

    def _remove_node(self, node) -> Node:
        node.previous.next = node.next
        node.next.previous = node.previous
        node.previous = node.next = None
        return node

    def get(self, key: int) -> int:
        if key in self.hashtable:
            node = self.hashtable[key]
            self._move_to_head(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashtable:
            node = self.hashtable[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.hashtable[key] = node
            self._add_to_head(node)
            if len(self.hashtable) > self.capacity:
                node_least_used = self._remove_from_tail()
                self.hashtable.pop(node_least_used.key)


class LRUCache2:
    def __init__(self, capacity):
        from collections import OrderedDict

        self.capacity = capacity
        self.hashtable = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.hashtable:
            self.hashtable.move_to_end(key, last=False)
            return self.hashtable[key]

        return -1

    def put(self, key: int, value: int) -> None:
        self.hashtable[key] = value
        self.hashtable.move_to_end(key, last=False)
        if len(self.hashtable) > self.capacity:
            self.hashtable.popitem()


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
