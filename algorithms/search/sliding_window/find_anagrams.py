# Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/


def find_anagrams(s, p):
    """
    Use a sliding window, we only store and update chars
    from string p in the hash table, just like Minimum window substring.

    Time: O(m+n)
    Space: O(1)
    """
    len_s, len_p = len(s), len(p)
    if len_s < len_p:
        return []
    res = []
    from collections import Counter

    counter = Counter(p)
    diff = len_p
    for i in range(len_p):
        if counter[s[i]] > 0:
            diff -= 1
        counter[s[i]] -= 1
    if diff == 0:
        res.append(0)
    for i in range(len_s - len_p):
        c1, c2 = s[i], s[i + len_p]
        if c1 in counter:
            counter[c1] += 1
            if counter[c1] > 0:
                diff += 1
        if c2 in counter:
            if counter[c2] > 0:
                diff -= 1
            counter[c2] -= 1
        if diff == 0:
            res.append(i + 1)
    return res


if __name__ == "__main__":
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]
