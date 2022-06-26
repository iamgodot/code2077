# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。


# 1. 移位运算
# 时间复杂度 O(logn) 空间复杂度 O(1)
def hamming_weight(n: int) -> int:
    res = 0
    while n > 0:
        res += n & 1
        n >>= 1
    return res


# 2. 比较 n 与 n-1 判断最后面的一位 1
# 时间复杂度 O(m) m 为 1 的个数，空间复杂度 O(1)
def hamming_weight2(n: int) -> int:
    res = 0
    while n > 0:
        res += 1
        n = n & (n - 1)
    return res


# 两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
# 给你两个整数 x 和 y，计算并返回它们之间的汉明距离。


# 1. 移位运算，同上
# 2. 同上
def hamming_distance(self, x: int, y: int) -> int:
    xor = x ^ y
    res = 0
    while xor > 0:
        res += 1
        xor &= xor - 1
    return res
