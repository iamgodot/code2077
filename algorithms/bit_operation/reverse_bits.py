# 颠倒给定的 32 位无符号整数的二进制位。


# 1. 不断遍历最后一位然后右移，过程中记录每一位二进制数。时间复杂度 O(logn) 空间复杂度 O(1)
# 2. 位运算分治，即不断地分割最小的两位数，交换之后，再交换逐渐变大的分段。时间复杂度 O(1) 空间复杂度 O(1)
def reverse_bits(n: int) -> int:
    res = 0
    for _ in range(32):
        res <<= 1
        res |= n & 1
        n >>= 1
    return res


if __name__ == "__main__":
    assert reverse_bits(int("00000010100101000001111010011100", 2)) == 964176192
