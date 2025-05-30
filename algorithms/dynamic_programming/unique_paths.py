# Unique Paths
# https://leetcode.com/problems/unique-paths/


def uniquePaths(m: int, n: int) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    # dp = [[0] * n for _ in range(m)]
    # for i in range(m):
    #     dp[i][0] = 1
    # for j in range(n):
    #     dp[0][j] = 1
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


# Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/


def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    if obstacleGrid[0][0] == 1:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(1, m):
        if obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1:
            dp[i][0] = 1
    for j in range(1, n):
        if obstacleGrid[0][j] == 0 and dp[0][j - 1] == 1:
            dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] != 1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]
