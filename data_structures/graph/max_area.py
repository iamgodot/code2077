# 给你一个大小为 m x n 的二进制矩阵 grid 。
# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
# 岛屿的面积是岛上值为 1 的单元格的数目。
# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。


def max_area(grid) -> int:
    """
    时间复杂度：O(m*n)
    空间复杂度：O(m*n) 最坏情况（都是陆地）
    """

    def dfs(i, j) -> int:
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] != 1:
            return 0
        grid[i][j] = 2
        return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

    m, n = len(grid), len(grid[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                res = max(res, dfs(i, j))

    return res


if __name__ == "__main__":
    grid = [[1]]
    assert max_area(grid) == 1
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    assert max_area(grid) == 6
