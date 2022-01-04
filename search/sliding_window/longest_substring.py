# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

# BruteForce: 两层遍历，时间复杂度 O(n^2)
# 借助哈希表记录之前出现过的字符可以使用滑动窗口
# 时间复杂度 O(n) 空间复杂度 O(m) 其中 m 为所有字符的长度，可以假设 ASCII 那么 m 为 128
def longest_substr(s: str) -> int:
    hashtable = {}
    res = length = left = right = 0
    while right < len(s):
        char = s[right]
        while char in hashtable:
            hashtable.pop(s[left])
            length -= 1
            left += 1
        right += 1
        length += 1
        res = max(res, length)
        hashtable[char] = 1

    return res


if __name__ == "__main__":
    assert longest_substr("abcabcbb") == 3
    assert longest_substr("bbbbb") == 1
    assert longest_substr("pwwkew") == 3
    assert longest_substr("") == 0
