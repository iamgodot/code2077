# Island Perimeter
# https://leetcode.com/problems/island-perimeter/


def islandPerimeter(grid) -> int:
    """
    Time: O(m*n)
    Space: O(m*n)
    """

    def dfs(i, j):
        if not 0 <= i < m or not 0 <= j < n or grid[i][j] == 0:
            return 1
        if grid[i][j] == 2:
            return 0
        grid[i][j] = 2
        return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                return dfs(i, j)

    return 0


def islandPerimeter2(grid) -> int:
    """
    Time: O(m*n)
    Space: O(1)
    """
    rows = len(grid)
    cols = len(grid[0])

    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                result += 4

                if r > 0 and grid[r - 1][c] == 1:
                    result -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    result -= 2

    return result


if __name__ == "__main__":
    for method in [islandPerimeter, islandPerimeter2]:
        grid = [[1]]
        assert method(grid) == 4
        grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        assert method(grid) == 16, method(grid)
