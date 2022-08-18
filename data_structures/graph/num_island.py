# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。

from collections import deque

# 注意：
# 1. 题目告知了 m, n 至少为 1
# 2. 应当确认是否可以修改原数组
# 3. 网格的值为字符串而不是数字
# 4. 找到陆地之后标为 '2' 而不是 '0'，这样可以和原来的海洋做区分


def num_of_islands_by_dfs(grid) -> int:
    """
    遍历每一个 cell，每次都通过 dfs 找到 '1' 并标记为 '2'
    这样对于一个 '1' 的 cell 就会把整个岛屿找出来，下次遇到直接跳过
    这类的 dfs 的总次数就是岛屿总数
    时间复杂度：O(m*n)
    空间复杂度：O(mn) 最坏情况下（所有都是陆地）
    """

    def dfs(i, j) -> None:
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] != "1":
            return
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
