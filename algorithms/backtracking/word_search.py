# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


from typing import List


def exist(board: list, word: str) -> bool:
    """
    Time: O(3^k*m*n) 最差情况下需要遍历整个矩阵，每次都存在 3^k 次可能
    Space: O(k) 递归深度为 word 长度，最差情况下 k=m*n
    """

    def dfs(i, j, k) -> bool:
        # 不需要判断 k > len(word) - 1 因为每次都会比较 word[k]
        if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        board[i][j] = ""
        res = (
            dfs(i - 1, j, k + 1)
            or dfs(i + 1, j, k + 1)
            or dfs(i, j - 1, k + 1)
            or dfs(i, j + 1, k + 1)
        )
        board[i][j] = word[k]
        return res

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False


# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。


class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.word = None

    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]
        cur.word = word


def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Time: O(3^k*m*n) k 为单词的长度
    Space: O(k*l) l 为单词的个数，用于存储前缀树，此外还有递归的开销 O(k)
    """

    def dfs(trie, i, j) -> None:
        if not 0 <= i < m or not 0 <= j < n or not board[i][j] in trie.children:
            return
        char = board[i][j]
        child = trie.children[char]
        if child.word:
            res.add(child.word)
        board[i][j] = ""
        dfs(child, i - 1, j)
        dfs(child, i + 1, j)
        dfs(child, i, j - 1)
        dfs(child, i, j + 1)
        board[i][j] = char

    res = set()
    m, n = len(board), len(board[0])
    trie = Trie()
    for word in words:
        trie.insert(word)
    for i in range(m):
        for j in range(n):
            dfs(trie, i, j)
    return list(res)


if __name__ == "__main__":
    assert (
        exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
        is True
    )
    assert (
        find_words(
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
        )
        == ["oath", "eat"]
    )
    assert (
        find_words(
            [
                ["o", "a", "b", "n"],
                ["o", "t", "a", "e"],
                ["a", "h", "k", "r"],
                ["a", "f", "l", "v"],
            ],
            ["oa", "oaa"],
        )
        == ["oa", "oaa"]
    )
