# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。


# 时间复杂度 O(1) 空间复杂度 O(1)
def add(a: int, b: int) -> int:
    # 因为 Python 是无限位数，所以对于负数要做特殊转化
    # 即加和的时候要把负数的高位（32位之外）的 1 -> 0
    # 返回的时候再把负数的高位从 0 -> 1
    bits = 0xFFFFFFFF
    a, b = a & bits, b & bits
    # a 保存 digit sum, b 保存 carry bit
    # 当 b == 0 时 a 即为 a + b 的最终结果
    while b != 0:
        # Shift operators precede bitwise ones
        # Bitwise operators precede boolean ones
        a, b = a ^ b, (a & b) << 1 & bits

    return a if a <= 0x7FFFFFFF else ~(a ^ bits)


# 给你两个二进制字符串，返回它们的和（用二进制表示）。

# 输入为 非空 字符串且只包含数字 1 和 0。

# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。


# 这里不同于上面一题，不考虑负数的情况
# 所以不需要转化，也不用考虑 bin(-5) 为 "-0b101" 这种情况
def add_binary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    assert add(111, 899) == 111 + 899
    print(add_binary("1010", "1011"))
