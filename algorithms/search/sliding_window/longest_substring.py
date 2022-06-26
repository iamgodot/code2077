# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

# 1. BruteForce: 两层遍历，时间复杂度 O(n^2)
# 2. 应用滑动窗口，不含有重复字符则右指针右移，否则左指针右移，使用集合来判断是否含有重复字符
# 时间复杂度 O(n) 空间复杂度 O(m) 其中 m 为所有字符的数量
def longest_substr(s: str) -> int:
    chars = set()
    res = left = right = 0
    for right, char in enumerate(s):
        while char in chars:
            chars.remove(s[left])
            left += 1
        if (right - left + 1) > res:
            res = right - left + 1
        chars.add(char)

    return res


if __name__ == "__main__":
    assert longest_substr("abcabcbb") == 3
    assert longest_substr("bbbbb") == 1
    assert longest_substr("pwwkew") == 3
    assert longest_substr("") == 0
