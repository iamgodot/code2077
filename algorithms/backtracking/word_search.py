# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


# 时间复杂度 O(3^k*m*n) 最差情况下需要遍历整个矩阵，每次都存在 3^k 次可能
# 空间复杂度 O(k) 递归深度为 word 长度，最差情况下 k=m*n
def exist(board: list, word: str) -> bool:
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


if __name__ == "__main__":
    assert (
        exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
        is True
    )
