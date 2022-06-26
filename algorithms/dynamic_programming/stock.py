# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。


from typing import List


def max_profit(prices: List[int]) -> int:
    res, min_ = 0, float("inf")
    for price in prices:
        min_ = min(min_, price)
        res = max(res, price - min_)
    return res


# 给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。
# 在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
# 返回 你能获得的 最大 利润 。


def max_profit(prices: List[int]) -> int:
    """
    dp[i][0] 表示第 i 天不持有股票的最大利润，
    dp[i][1] 表示第 i 天持有股票的最大利润。

    递推公式：
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

    初始化：
        dp[0][0] = 0
        dp[0][1] = -prices[0]

    时间复杂度 O(n) 空间复杂度 O(n)
    """
    length = len(prices)
    dp = [[0, 0] for _ in range(length)]
    dp[0][1] = -prices[0]

    for i in range(1, length):
        price = prices[i]
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + price)
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - price)

    return dp[-1][0]


# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


def max_profit(prices: List[int]) -> int:
    length = len(prices)
    dp = [[0, 0, 0, 0, 0] for _ in range(length)]
    dp[0][1] = dp[0][3] = -prices[0]

    for i in range(1, length):
        price = prices[i]
        # dp[i][0] = dp[i-1][0]
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - price)
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + price)
        dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - price)
        dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + price)

    return dp[-1][-1]


# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


def max_profit(k: int, prices: List[int]) -> int:
    if not prices:
        return 0
    length = len(prices)
    dp = [[0 for _ in range(2 * k + 1)] for _ in range(length)]
    for i in range(2 * k + 1):
        if i % 2 == 1:
            dp[0][i] = -prices[0]

    for i in range(1, length):
        for j in range(1, 2 * k + 1):
            price = -prices[i] if j % 2 == 1 else prices[i]
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + price)

    return dp[-1][-1]
