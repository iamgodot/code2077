# Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/description/


class Node:
    def __init__(self):
        self.children = {}
        self._is_end = False

    def is_end(self):
        return self._is_end

    def set_end(self):
        self._is_end = True

    def get_child(self, char: str) -> "Node|None":
        return self.children.get(char)

    def add_child(self, char: str) -> "Node":
        if char not in self.children:
            self.children[char] = Node()
        return self.children[char]


class Trie:
    """
    We can also use arrays which may take up more space, but with quicker lookups.
    **Note that a word can also be a prefix.**

    Time: O(m) for insertion and search, where m is the length of the string
    Space: O(m) for insertion, O(1) for search, O(nk) for total space where n is number of nodes
    """

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            child = cur.get_child(char)
            if not child:
                child = cur.add_child(char)
            cur = child
        cur.set_end()

    def _find_node(self, word: str) -> Node | None:
        cur = self.root
        for char in word:
            child = cur.get_child(char)
            if not child:
                return None
            else:
                cur = child
        return cur

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node.is_end() if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self._find_node(prefix)
        # NOTE: it's still a prefix even if it's the end
        return node is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
