# Permutation in String
# https://leetcode.com/problems/permutation-in-string/


def check(s1: str, s2: str) -> bool:
    """
    The same as Find All Anagrams in a String.

    Time: O(m+n)
    Space: O(k)
    """
    m, n = len(s1), len(s2)
    if m > n:
        return False

    from collections import Counter

    hashtable = Counter(s1)
    diff = m

    for char in s2[:m]:
        if char in hashtable:
            if hashtable[char] > 0:
                diff -= 1
            hashtable[char] -= 1

    if diff == 0:
        return True

    for i in range(n - m):
        char_del, char_add = s2[i], s2[i + m]

        if char_del in hashtable:
            hashtable[char_del] += 1
            if hashtable[char_del] > 0:
                diff += 1

        if char_add in hashtable:
            if hashtable[char_add] > 0:
                diff -= 1
            hashtable[char_add] -= 1

        if diff == 0:
            return True

    return False


if __name__ == "__main__":
    assert check("ab", "eidbaooo") is True
    assert check("ab", "eidboaoo") is False
