# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。


def _dfs(board, i, j):
    if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
        return
    if board[i][j] != "O":
        return
    board[i][j] = "1"
    _dfs(board, i - 1, j)
    _dfs(board, i + 1, j)
    _dfs(board, i, j - 1)
    _dfs(board, i, j + 1)


# DFS
# 时间复杂度：O(m*n)
# 空间复杂度：O(m*n)
def solve(board) -> None:
    m, n = len(board), len(board[0])
    # Iterate the outest round, dfs all Os and mark as 1s
    for column in range(n):
        _dfs(board, 0, column)
        _dfs(board, m - 1, column)
    for row in range(m):
        _dfs(board, row, 0)
        _dfs(board, row, n - 1)
    # Iterate all cells, mark Os as Xs, mark 1s as Os
    for row in range(m):
        for column in range(n):
            if board[row][column] == "O":
                board[row][column] = "X"
            if board[row][column] == "1":
                board[row][column] = "O"


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    solve(board)
    assert board == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    board = [["X"]]
    solve(board)
    assert board == [["X"]]
