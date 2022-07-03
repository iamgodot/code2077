# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。


def find_anagrams(s: str, p: str) -> list:
    """
    Time: O(m+n)
    Space: O(k) k 为字符集长度
    """
    m, n = len(s), len(p)
    if m < n:
        return []

    res = []
    from collections import Counter

    hashtable = Counter(p)
    diff = n

    for char in s[:n]:
        if char in hashtable:
            if hashtable[char] > 0:
                diff -= 1
            hashtable[char] -= 1

    if diff == 0:
        res.append(0)

    for i in range(m - n):
        char_del, char_add = s[i], s[i + n]

        if char_del in hashtable:
            hashtable[char_del] += 1
            if hashtable[char_del] > 0:
                diff += 1

        if char_add in hashtable:
            if hashtable[char_add] > 0:
                diff -= 1
            hashtable[char_add] -= 1

        if diff == 0:
            res.append(i + 1)

    return res


if __name__ == "__main__":
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]
