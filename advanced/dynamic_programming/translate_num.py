# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


# 1. 假设 dp[i-1] 表示第 i-1 个以及前面所有的字符代表的数字的翻译方法数量
# 那么如果 chars[i-1] + chars[i] 能够翻译为 10-25 之内的数字（注意 09 这种不可以）
# 则 dp[i] = dp[i-1] + dp[i-2] 否则 dp[i] = dp[i-1]
# 如此以来时间复杂度为 O(n) 而空间复杂度也是 O(n)
# 2. 实际上从左到右和从右到左的验证结果是一致的，所以可以利用整数取余来每次
# 对 num 除以 10，进而判断翻译次数。这样空间复杂度就可以降低为 O(1)
def translate_num(num: int) -> int:
    pre = cur = 1
    chars = list(str(num))
    for i in range(1, len(chars)):
        if "10" <= chars[i - 1] + chars[i] <= "25":
            pre, cur = cur, pre + cur
        else:
            pre = cur

    return cur


if __name__ == "__main__":
    assert translate_num(26) == 1
    assert translate_num(12258) == 5
