# 对于总容量为 W 的背包，如何装物品使得价值最大


def most_bag_value(bag_weight: int, weights: list, values: list) -> int:
    num_of_objs = len(weights)
    # dp[i][j] 对于 0-i 中任意个物品和容量 j 的背包，最大的价值总和是多少
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])
    dp = [[0 for j in range(bag_weight + 1)] for i in range(num_of_objs)]
    for j in range(weights[0], bag_weight + 1):
        dp[0][j] = values[0]

    for i in range(1, num_of_objs):
        for j in range(1, bag_weight + 1):
            if j < weights[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])

    return dp[-1][-1]


def most_bag_value_v2(bag_weight: int, weights: list, values: list) -> int:
    # dp[j] 容量为 j 的背包，装物品得到的最大价值总和
    # dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
    num_of_objs = len(weights)
    dp = [0 for _ in range(bag_weight + 1)]
    for i in range(num_of_objs):  # 这里必须从 0 开始，因为还没做过初始化
        for j in range(bag_weight, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[-1]


if __name__ == "__main__":
    v = most_bag_value(4, [1, 3, 4], [15, 20, 30])
    print(v)
    v = most_bag_value_v2(4, [1, 3, 4], [15, 20, 30])
    print(v)
