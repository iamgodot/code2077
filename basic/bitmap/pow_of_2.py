# 判断一个整数是否为 2 的整数次幂

# 1. 使用二分的思想来做可以得到 O(logn) 的复杂度
# 2. 换成 bitmap 可以优化为 O(1)，因为如果 n 为 2 的整数次幂，那么 n 和 n-1 的二进制做和运算一定为 0
# 要注意 0 不是 2 的整数次幂，但是 0 和任何数做和运算都得到 0
# 如果是负数的话也要排除
def pow_of_2(n: int) -> bool:
    return n > 0 and n & n - 1 == 0


# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x


# 如果满足条件那么除了是 2 的整数次幂另外二进制的 1/3/5 等位置上肯定都是 1
# 时间复杂度 O(1) 空间复杂度 O(1)
def pow_of_4(n: int) -> bool:
    return (
        n > 0 and n & n - 1 == 0 and n & int("10101010101010101010101010101010", 2) == 0
    )


if __name__ == "__main__":
    assert pow_of_2(-1) is False
    assert pow_of_2(0) is False
    assert pow_of_2(1) is True
    assert pow_of_2(8) is True
    assert pow_of_2(10) is False
    assert pow_of_4(16) is True
    assert pow_of_4(5) is False
    assert pow_of_4(8) is False
