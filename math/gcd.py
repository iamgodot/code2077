# 求两个数的最大公约数 greatest common divisor

# 应当假设 m > 0 and n > 0 and m > n
# 暴力解法：先判断 n 能够被 m 整除，不行的话从 n/2 到 1 开始遍历，复杂度为 O(n)
# 辗转相除法：m 和 n 的最大公约数就是 m%n 和 n 的最大公约数，不断重复直到有一个数为 0 或者 1 为止
# 更相减损术：m 和 n 的最大公约数就是 m-n 和 n 的最大公约数
def gcd(m: int, n: int) -> int:
    if m < n:
        m, n = n, m

    while n != 0:
        m, n = n, m % n

    return m


# 辗转相除法比更相减损术的迭代次数小很多，但是余数运算的性能很差，所以仍有优化空间
# 可以利用高效的移位运算来进一步提升计算效率
# 1. 当 m n 都为偶数时，最大公约数是 m/2 n/2 最大公约数的两倍
# 2. 当 m(n) 为偶数时，最大公约数是 m/2 和 n 的最大公约数
# 3. 当 m n 都为奇数时，利用更相减损术可得到 m-n 为偶数
# 判断奇偶的时候不用余数，而是利用位运算
def gcd(m: int, n: int) -> int:
    if m < n:
        m, n = n, m
    multi = 1
    while n != 0:
        if m & 1 == 0 and n & 1 == 0:
            multi *= 2
            m >>= 1
            n >>= 1
        elif m & 1 == 0:
            m >>= 1
        elif n & 1 == 0:
            n >>= 1
        else:
            m = max(n, m - n)
            n = min(n, m - n)

    return m * multi


if __name__ == "__main__":
    assert gcd(25, 10) == 5
    assert gcd(3, 1) == 1
    assert gcd(11, 10) == 1
