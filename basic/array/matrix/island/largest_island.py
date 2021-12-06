# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
# 返回执行此操作后，grid 中最大的岛屿面积是多少？
# 岛屿 由一组上、下、左、右四个方向相连的 1 形成。


def _is_invalid_pos(grid, i, j) -> bool:
    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
        return True
    return False


def _dfs(grid, i, j, index) -> int:
    if _is_invalid_pos(grid, i, j):
        return 0
    if grid[i][j] != 1:
        return 0
    grid[i][j] = index
    return (
        1
        + _dfs(grid, i - 1, j, index)
        + _dfs(grid, i + 1, j, index)
        + _dfs(grid, i, j - 1, index)
        + _dfs(grid, i, j + 1, index)
    )


# 先 dfs 标记每一个岛屿出来，再遍历水域找四周的岛屿
# 注意全岛屿或者全水域的情况，另外水域连接的有可能是同一片岛屿
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)
def largest_island(grid) -> int:
    m, n = len(grid), len(grid[0])
    index = 2
    index_to_area = {}
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                index_to_area[index] = _dfs(grid, i, j, index)
                index += 1

    res = max(1, max(index_to_area.values() or [0]))
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                vals = set()
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if not _is_invalid_pos(grid, x, y) and grid[x][y] > 1:
                        vals.add(grid[x][y])
                if vals:
                    connected = sum(index_to_area[i] for i in vals) + 1
                    res = max(res, connected)

    return res


if __name__ == "__main__":
    for grid, ans in (
        ([[1, 1], [1, 0]], 4),
        ([[1, 0], [0, 1]], 3),
        ([[0, 0], [0, 0]], 1),
        ([[1, 1], [1, 1]], 4),
    ):
        assert largest_island(grid) == ans
