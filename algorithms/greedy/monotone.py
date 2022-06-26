# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
# 给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。


def monotone_increasing_digits(n: int) -> int:
    """
    按照每一位从左到右遍历，如果遇到 i > j 则把 i 减一，后面的位数全部设置为 9
    但是对于 332 这种情况还不够，所以要先从 i 往回找到第一个同样大小为 i 的位数，
    然后把该位数减一，后面的位数全部设置为 9 即可。
    """
    digits = [int(i) for i in str(n)]
    length = len(digits)
    for i in range(length - 1):
        x, y = digits[i], digits[i + 1]
        if x > y:
            while i > 0 and digits[i] == digits[i - 1]:
                i -= 1
            digits[i] -= 1
            while i < length - 1:
                i += 1
                digits[i] = 9
            break

    return int("".join([str(i) for i in digits]))


if __name__ == "__main__":
    assert monotone_increasing_digits(10) == 9
    assert monotone_increasing_digits(1234) == 1234
    assert monotone_increasing_digits(332) == 299
