# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。


# 我们可以将问题重新表述为：给定两个整数，我们要找到它们对应的二进制字符串的公共前缀。
# 所以既可以不断地把 left 和 right 右移，直到两者相等，再左移回去
# 也可以利用 n&n-1 来消除最右边的 1 的技巧来修正 right 直到 right <= left
# 时间复杂度 O(logn) 空间复杂度 O(1)
def range_bitwise_and(left: int, right: int) -> int:
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return right << shift


def range_bitwise_and2(left: int, right: int) -> int:
    while left < right:
        right &= right - 1
    return right


if __name__ == "__main__":
    for method in [range_bitwise_and, range_bitwise_and2]:
        assert method(5, 7) == 4
        assert method(0, 0) == 0
        assert method(1, 2147483647) == 0
