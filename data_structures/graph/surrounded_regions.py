# Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/


def solve(board) -> None:
    """
    Time: O(m*n)
    Space: O(m*n)
    """
    m, n = len(board), len(board[0])

    def dfs(i, j):
        if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
            board[i][j] = "1"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

    for column in range(n):
        dfs(0, column)
        dfs(m - 1, column)
    for row in range(m):
        dfs(row, 0)
        dfs(row, n - 1)
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
