# 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。
# 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

# 思路都是对于一块陆地来说，如果周围四个格子出界或者为水域那么就增加 1 的周长


def _dfs(grid, i, j) -> int:
    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
        return 1
    if grid[i][j] == 0:
        return 1
    if grid[i][j] == 2:
        return 0

    grid[i][j] = 2
    return (
        _dfs(grid, i - 1, j)
        + _dfs(grid, i + 1, j)
        + _dfs(grid, i, j - 1)
        + _dfs(grid, i, j + 1)
    )


# DFS 遍历
# 时间复杂度：O(m*n)
# 空间复杂度：O(m*n) 最坏情况（都是陆地）
def islandPerimeter_by_dfs(grid) -> int:
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                return _dfs(grid, i, j)

    return 0


# 直接遍历
# 时间复杂度：O(m*n)
# 空间复杂度：O(1)
def islandPerimeter(grid) -> int:
    m, n = len(grid), len(grid[0])

    def _invalid_count(i, j):
        count = 0
        for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
            if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[0]) - 1:
                count += 1
            elif grid[x][y] == 0:
                count += 1
        return count

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                res += _invalid_count(i, j)

    return res


if __name__ == "__main__":
    for method in [islandPerimeter_by_dfs, islandPerimeter]:
        grid = [[1]]
        assert method(grid) == 4
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        assert method(grid) == 16, method(grid)
