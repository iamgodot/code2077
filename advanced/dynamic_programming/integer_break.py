# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

# 返回 你可以获得的最大乘积 。


def integer_break(n: int) -> int:
    dp = [0 for i in range(n + 1)]
    dp[2] = 1
    for i in range(3, n + 1):
        for j in range(1, i - 1):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

    return dp[-1]


def integer_break(n: int) -> int:
    """
    除去 2,3,4 的特例，尽量将 n 拆分为多个 3，
    如果最后余 1，则拿出一个 3 来组成 4
    """
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    x, y = divmod(n, 3)

    from math import pow

    res = 0
    if y == 0:
        res = pow(3, x)
    elif y == 1:
        res = pow(3, x - 1) * 4
    else:
        res = pow(3, x) * y

    return int(res)


if __name__ == "__main__":
    assert integer_break(5) == 6
    assert integer_break(6) == 9
    assert integer_break(10) == 36
