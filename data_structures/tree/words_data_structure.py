# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

# 实现词典类 WordDictionary ：

# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_child(self, val: str) -> "Node":
        self.children[val] = Node()
        return self.children[val]

    def get_child(self, val: str) -> "Node":
        return self.children.get(val)


class WordDictionary:
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
            # 注意是 children.values()
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
