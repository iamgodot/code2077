# Coin Change
# https://leetcode.com/problems/coin-change/


def coinChange(coins: list[int], amount: int) -> int:
    """
    Greedy is not applicable here, e.g. [1, 3, 4, 5] and amount = 7

    Time: O(amount * len(coins))
    Space: O(amount)
    """
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1


# Coin Change II
# https://leetcode.com/problems/coin-change-2/


def change(amount: int, coins: list[int]) -> int:
    """
    dp[i][j] means using coins from index i to sum up to amount j.

    Time: O(amount * len(coins))
    Space: O(amount * len(coins))
    """
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(n - 1, -1, -1):
        for j in range(1, amount + 1):
            if j >= coins[i]:
                dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]
            else:
                dp[i][j] = dp[i + 1][j]
    return dp[0][-1]


def change2(amount: int, coins: list[int]) -> int:
    """
    Time: O(amount * len(coins))
    Space: O(amount)
    """
    n = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(n - 1, -1, -1):
        for j in range(coins[i], amount + 1):
            dp[j] += dp[j - coins[i]]
    return dp[-1]
