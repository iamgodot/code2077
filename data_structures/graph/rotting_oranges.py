# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    注意要一开始就把所有的腐烂橘子添加进队列，这样保证同时进行扩散。

    Time: O(mn)
    Space: O(mn)
    """
    m, n = len(grid), len(grid[0])
    from collections import deque

    dq = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                dq.append((i, j, 0))
    res = 0
    while dq:
        for _ in range(len(dq)):
            i, j, res = dq.pop()
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dq.appendleft((x, y, res + 1))
                    grid[x][y] = 2
    from itertools import chain

    if any(i == 1 for i in chain(*grid)):
        return -1
    else:
        return res


if __name__ == "__main__":
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2
    assert oranges_rotting([[0]]) == 0
