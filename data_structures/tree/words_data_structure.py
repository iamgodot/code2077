# Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_child(self, val: str) -> "Node":
        self.children[val] = Node()
        return self.children[val]

    def get_child(self, val: str) -> "Node|None":
        return self.children.get(val)


class WordDictionary:
    """
    It requires a DFS approach for fuzzy searching.
    Also remember to check if we reach to the end of the word.

    Time: O(m) for insertion and O(n*26^m) for search where m is the length of the word and n is the number of keys
    Space: O(m) for both insertion and search(recursion stack)
    """

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            child = cur.get_child(char)
            if not child:
                child = cur.add_child(char)
            cur = child
        cur.is_end = True

    def _search(self, word: str, index: int, node: Node) -> bool:
        if index == len(word):
            return node.is_end
        if word[index] == ".":
            # NOTE: remember to use values()
            for child in node.children.values():
                if self._search(word, index + 1, child):
                    return True
        else:
            child = node.get_child(word[index])
            return child is not None and self._search(word, index + 1, child)
        return False

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.root)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
