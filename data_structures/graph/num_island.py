# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。

from collections import deque

# 注意：
# 1. 题目告知了 m, n 至少为 1
# 2. 应当确认是否可以修改原数组
# 3. 网格的值为字符串而不是数字
# 4. 找到陆地之后标为 '2' 而不是 '0'，这样可以和原来的海洋做区分

# 遍历每一个 cell，每次都通过 dfs 找到 '1' 并标记为 '2'
# 这样对于一个 '1' 的 cell 就会把整个岛屿找出来，下次遇到直接跳过
# 这类的 dfs 的总次数就是岛屿总数
# 时间复杂度：O(m*n)
# 空间复杂度：O(mn) 最坏情况下（所有都是陆地）
def _dfs(grid, i, j) -> None:
    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
        return
    if grid[i][j] != "1":
        return

    grid[i][j] = "2"

    _dfs(grid, i - 1, j)
    _dfs(grid, i + 1, j)
    _dfs(grid, i, j - 1)
    _dfs(grid, i, j + 1)


def num_of_islands_by_dfs(grid) -> int:

    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                _dfs(grid, i, j)
                res += 1

    return res


# 思路同上，只是用 bfs 代替 dfs
# 时间复杂度：O(m*n)
# 空间复杂度：O(m*n) 最坏情况下（所有都是陆地）
def _bfs(grid, i, j) -> None:
    dq = deque([(i, j)])
    while dq:
        x, y = dq.pop()
        if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
            continue
        if grid[x][y] != "1":
            continue
        grid[x][y] = "2"
        dq.appendleft((x + 1, y))
        dq.appendleft((x - 1, y))
        dq.appendleft((x, y - 1))
        dq.appendleft((x, y + 1))


def num_of_islands_by_bfs(grid) -> int:

    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                _bfs(grid, i, j)
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
