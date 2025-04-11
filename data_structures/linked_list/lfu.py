# LFU Cache
# https://leetcode.com/problems/lfu-cache/description/


class Node:
    def __init__(
        self,
        key: int = 0,
        val: int = 0,
        prev: "Node|None" = None,
        next: "Node|None" = None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = 1


class LFUCache:
    """
    Use 2 hash maps, 1 for mapping keys to nodes, and 1 for maintaining node lists for each frequency.
    Additionally, maintain a pointer to the minimum frequency list.
    """

    def __init__(self, capacity: int):
        from collections import defaultdict

        self.capacity = capacity
        self.key_to_node = {}

        def new_freq_list():
            dummy = Node()
            dummy.prev = dummy.next = dummy
            return dummy

        self.freq_to_node = defaultdict(new_freq_list)
        self.min_freq = 0

    def get(self, key: int) -> int:
        node = self._get_node(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self._get_node(key)
        if node:
            node.val = value
            return
        # NOTE: Unlike LRU, we have clean up first!
        if len(self.key_to_node) == self.capacity:
            # Remove one from min freq pile
            dummy = self.freq_to_node[self.min_freq]
            # NOTE: We need to remove the least recently used one
            removed = self._remove_node(dummy.prev)
            del self.key_to_node[removed.key]
            # Optionally remove old pile
            if dummy.next is dummy:
                del self.freq_to_node[self.min_freq]
                self.min_freq += 1
        self.key_to_node[key] = node = Node(key, value)
        self._insert_node(self.freq_to_node[1], node)
        self.min_freq = 1  # NOTE: just set to 1!

    def _get_node(self, key: int) -> Node | None:
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        # Remove from old pile
        self._remove_node(node)
        dummy_old = self.freq_to_node[node.freq]
        # Optionally remove old pile
        if dummy_old.next is dummy_old:
            del self.freq_to_node[node.freq]
            if node.freq == self.min_freq:
                self.min_freq += 1
        # Put on new pile
        node.freq += 1
        dummy_new = self.freq_to_node[node.freq]
        self._insert_node(dummy_new, node)
        return node

    def _insert_node(self, head, node):
        node.prev = head
        node.next = head.next
        node.prev.next = node.next.prev = node

    def _remove_node(self, node) -> Node:
        node.prev.next = node.next
        node.next.prev = node.prev
        return node
