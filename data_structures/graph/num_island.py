# Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

from collections import deque


def num_of_islands_by_dfs(grid) -> int:
    """
    It's easier to mark 1s as 2s without using a visited set.
    Also watch out for cell values, which are strings rather than integers.

    Time: O(mn)
    Space: O(mn)
    """

    def dfs(i, j) -> None:
        if 0 <= i < m or 0 <= j < n and grid[i][j] == "1":
            grid[i][j] = "2"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                dfs(i, j)
                res += 1

    return res


def num_of_islands_by_bfs(grid) -> int:
    """
    # 时间复杂度：O(m*n)
    # 空间复杂度：O(m*n) 最坏情况下（所有都是陆地）
    """

    def bfs(i, j) -> None:
        dq = deque([(i, j)])
        grid[i][j] = "2"
        while dq:
            i, j = dq.pop()
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                    grid[x][y] = "2"
                    dq.appendleft((x, y))

    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                bfs(i, j)
                res += 1

    return res


if __name__ == "__main__":
    for method in [num_of_islands_by_dfs, num_of_islands_by_bfs]:
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert method(grid) == 3
