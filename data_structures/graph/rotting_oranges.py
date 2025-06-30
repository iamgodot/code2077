# Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/description/


def oranges_rotting(grid: list[list[int]]) -> int:
    """
    Multi-source BFS.

    Corner cases:
    1. If there's no rotting oranges, return 0.
    2. If there's fresh oranges left, return -1.

    Time: O(mn)
    Space: O(mn)
    """
    rows, cols = len(grid), len(grid[0])
    from collections import deque

    queue = deque()
    minutes = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, minutes))

    while queue:
        i, j, minutes = queue.pop()
        for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                queue.appendleft((x, y, minutes + 1))
                grid[x][y] = 2

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return -1

    return minutes


if __name__ == "__main__":
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2
    assert oranges_rotting([[0]]) == 0
