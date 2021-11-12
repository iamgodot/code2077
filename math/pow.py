# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4


# 1. Brute-force 解法时间复杂度为 O(n)
# 2. 快速求幂，首先想到递归实现分治法，每次令 n 折半，时间和空间复杂度为 O(logn)
def _pow_helper(x: float, n: int):
    if n == 1:
        return x
    multi = _pow_helper(x, n // 2)
    if n % 2 == 1:
        return multi * multi * x
    else:
        return multi * multi


def pow(x: float, n: int) -> float:
    """
    对于数字，应当想到特殊的取值情况以及是否可能溢出
    取值：对于 x 等于 0 或者 1 以及 n 等于 0 的情况，确认都应当返回 1，所以直接短路掉；
        如果 n 小于 0，那么就需要取 abs(n) 计算结果的倒数
    溢出：根据提示可以确认取值范围，而在 Python 中 int 不会发生溢出情况，至于 float 则可以覆盖取值范围
    """
    if x == 0 or x == 1 or n == 0:
        return 1.0

    res = _pow_helper(x, abs(n))
    return float(res) if n > 0 else float(1 / res)


# 3. 使用迭代实现分治法求幂，时间复杂度 O(logn)，空间复杂度 O(1)
def pow(x: float, n: int) -> float:
    """
    这里的迭代思路可以理解为
    初始状态：x^n = x^n * 1
    最终状态：x^n = x^0 * res = res
    每当 n 为奇数的时候就把多出来的 x 纳入 res。因为 count 总会抵达 1，所以最终 res 会结合不断平方的 x
    """
    if x == 0 or x == 1:
        return 1
    res = 1.0
    count = abs(n)
    while count > 0:
        if count % 2 == 1:
            res *= x
        x *= x
        count //= 2
    return res if n > 0 else 1 / res


if __name__ == "__main__":
    assert pow(0, 1) == 1
    assert pow(1, 2) == 1
    assert pow(2, 0) == 1
    assert pow(2, 10) == 1024
    # 这里的精度不一致，如果不 round 的话会得到 9.261000000000001
    assert round(pow(2.1, 3), 3) == 9.261
    assert pow(2, -2) == 0.25
