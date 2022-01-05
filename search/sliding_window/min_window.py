# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。


# 1. BruteForce: 双层遍历，时间复杂度 O(n^2)，还需要哈希表来比较子串和 t
# 2. 滑动窗口：在子串没有覆盖 t 的时候右指针右移，否则左指针右移。时间复杂度 O(n) 空间复杂度 O(m) m 最多为 26
# 注意实现滑动窗口过程中可以优化的点：
# - 使用 i j 来指定子串范围
# - 使用 diff 数值来代替遍历哈希表判断是否覆盖
# - 左指针在右移的时候直接判断哈希表中字符的数字是否小于 0 即可，因为 t 中的字符一开始初始化 value 肯定大于 0，
#   其他字符默认为 0，所以在 while 中一旦碰到 value 为 0，说明一定是 t 中的字符并且恰好字符数量正好够用，
#   相当于左指针右移到了最后能满足覆盖条件的位置。也因此，while 结束之后下面还要再右移一次，打破覆盖条件。

def min_window(s: str, t: str) -> str:
    from collections import Counter

    left = right = 0
    diff = len(t)
    hashtable = Counter(t)
    i, j = 0, len(s)
    for right, char in enumerate(s):
        if hashtable[char] > 0:
            diff -= 1
        hashtable[char] -= 1

        if diff == 0:
            while hashtable[s[left]] < 0:
                hashtable[s[left]] += 1
                left += 1

            if right - left < j - i:
                i, j = left, right

            hashtable[s[left]] += 1
            left += 1
            diff += 1

    return "" if j == len(s) else s[i : j + 1]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("bba", "ab") == "ba"
