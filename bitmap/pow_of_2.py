# 判断一个整数是否为 2 的整数次幂

# 1. 使用二分的思想来做可以得到 O(logn) 的复杂度
# 2. 换成 bitmap 可以优化为 O(1)，因为如果 n 为 2 的整数次幂，那么 n 和 n-1 的二进制做和运算一定为 0
# 要注意 0 不是 2 的整数次幂，但是 0 和任何数做和运算都得到 0
# 如果是负数的话也要排除
def pow_of_2(n: int) -> bool:
    if n <= 0:
        return False
    return n & n - 1 == 0


if __name__ == "__main__":
    assert pow_of_2(-1) is False
    assert pow_of_2(0) is False
    assert pow_of_2(1) is True
    assert pow_of_2(8) is True
    assert pow_of_2(10) is False
