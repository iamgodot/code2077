# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。


# 1. BruteForce: 双层遍历，时间复杂度 O(n^2)，还需要哈希表来比较子串和 t
# 2. 滑动窗口：在子串没有覆盖 t 的时候右指针右移，否则左指针右移。时间复杂度 O(n) 空间复杂度 O(m) m 最多为 26


def min_window(s: str, t: str) -> str:
    from collections import Counter

    left = 0
    diff = len(t)
    hashtable = Counter(t)
    min_left, min_len = 0, float("inf")
    for right, char in enumerate(s):
        # 只需要关心 hashtable 存在的 char
        if char in hashtable:
            if hashtable[char] > 0:
                diff -= 1
            hashtable[char] -= 1

        while diff == 0:
            if right - left + 1 < min_len:
                min_left = left
                min_len = right - left + 1
            char_left = s[left]
            if char_left in hashtable:
                hashtable[char_left] += 1
                if hashtable[char_left] > 0:
                    diff += 1
            left += 1
    return "" if min_len == float("inf") else s[min_left : min_left + min_len]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("bba", "ab") == "ba"
