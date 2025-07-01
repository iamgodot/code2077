# Pow(x, n)
# https://leetcode.com/problems/powx-n/


def pow(x: float, n: int) -> float:
    """
    Time: O(logn)
    Space: O(logn)
    """
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / pow(x, -n)

    if n % 2 == 1:
        return x * pow(x * x, (n - 1) // 2)
    else:
        return pow(x * x, n // 2)


def pow2(x: float, n: int) -> float:
    """
    Time: O(logn)
    Space: O(1)
    """
    if n == 0:
        return 1.0
    if n < 0:
        x = 1.0 / x
        n = -n
    res = 1.0
    while n > 0:
        if n % 2 == 1:
            res *= x
            n -= 1
        x *= x
        n //= 2
    return res


if __name__ == "__main__":
    for method in [pow, pow2]:
        assert method(0, 1) == 1
        assert method(1, 2) == 1
        assert method(2, 0) == 1
        assert method(2, 10) == 1024
        # 这里的精度不一致，如果不 round 的话会得到 9.261000000000001
        assert round(method(2.1, 3), 3) == 9.261
        assert method(2, -2) == 0.25
        method(2.0, -2147483648)
