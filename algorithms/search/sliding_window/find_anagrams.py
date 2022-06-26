# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

from collections import Counter


# 可以看作是滑动窗口中窗口大小固定的情况
# 时间复杂度：O(n)
# 空间复杂度：O(1)
def find_anagrams(s: str, p: str) -> list:
    anagram_orig, anagram_new = Counter(p), {}

    res = []
    for i in range(len(s) - len(p) + 1):
        if not anagram_new:
            anagram_new = Counter(s[i : i + len(p)])
        else:
            anagram_new[s[i - 1]] -= 1
            anagram_new[s[i + len(p) - 1]] += 1

        for k, v in anagram_orig.items():
            if anagram_new[k] != v:
                break
        else:
            res.append(i)

    return res


# 因为固定窗口大小每次都只是删除一个字符再添加一个字符，所以比较异位词的时候只需要
# 参考两个字符的变化就够了，通过 diff 来记录子串与异位词的差异数
def find_anagrams2(s: str, p: str) -> list:
    res = []
    len_s, len_p = len(s), len(p)
    counter, diff = Counter(p), len_p

    for char in s[:len_p]:
        if counter[char] > 0:
            diff -= 1
        counter[char] -= 1

    if diff == 0:
        res.append(0)

    for i in range(len_s - len_p):
        char_del, char_add = s[i], s[i + len_p]

        counter[char_del] += 1
        if counter[char_del] > 0:
            diff += 1

        if counter[char_add] > 0:
            diff -= 1
        counter[char_add] -= 1

        if diff == 0:
            res.append(i + 1)

    return res


if __name__ == "__main__":
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]
    assert find_anagrams2("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams2("abab", "ab") == [0, 1, 2]
