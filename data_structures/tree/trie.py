# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

# 请你实现 Trie 类：

# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


class Node:
    def __init__(self):
        self.children = {}
        self._is_end = False

    def is_end(self):
        return self._is_end

    def set_end(self):
        self._is_end = True

    def get_child(self, val: str) -> "Node":
        return self.children.get(val)

    def add_child(self, val: str) -> "Node":
        self.children[val] = Node()
        return self.children[val]


class Trie:
    """
    映射关系既可以用数组也可以用哈希表，数组相对会占用更多空间，但是查询速度会快一些。

    时间复杂度：TrieTrie 树的每次调用时间复杂度取决于入参字符串的长度。复杂度为 O(Len)O(Len)。
    空间复杂度：结点数量为 nn，字符集大小为 kk。复杂度为 O(nk)O(nk)。
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

    def _find_node(self, word: str) -> Node:
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
        return node is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
