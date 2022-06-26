# 实现 strStr() 函数。

# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

#

# 说明：

# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。


# 1. BruteForce: 时间复杂度 O(m*n)
# 2. KMP: 时间复杂度 O(m+n)
def find_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    res = -1
    len_h, len_n = len(haystack), len(needle)
    for i in range(len_h - len_n + 1):
        for j in range(len_n):
            if haystack[i + j] != needle[j]:
                break
        else:
            return i

    return res


if __name__ == "__main__":
    assert find_str("hello", "ll") == 2
    assert find_str("abc", "c") == 2
    assert find_str("misissipi", "misissipi") == 0
