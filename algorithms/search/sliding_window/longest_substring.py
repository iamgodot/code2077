# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def longest_substr(s: str) -> int:
    """
    Use a sliding window which maintains non-repeating characters.

    Time: O(n)
    Space: O(m) where m is the number of distinct characters
    """
    from collections import defaultdict

    hash_table = defaultdict(int)
    res = left = 0
    for right, char in enumerate(s):
        hash_table[char] += 1
        while hash_table[char] > 1:
            # NOTE: here we need to get the left char before moving the pointer
            hash_table[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res


# Longest Substring with At Most Two Distinct characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/


def longest_substr_two_distinct(s: str) -> int:
    """
    Here we need to check the length of hash table's keys rather than values.

    Time: O(n)
    Space: O(m)
    """
    from collections import defaultdict

    hash_table = defaultdict(int)
    res = left = 0
    for right, char in enumerate(s):
        hash_table[char] += 1
        while len(hash_table) > 2:
            char_left = s[left]
            hash_table[char_left] -= 1
            if hash_table[char_left] == 0:
                hash_table.pop(char_left)
            left += 1
        res = max(res, right - left + 1)
    return res


# Longest Substring with At Most K Distinct characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/


def longest_substr_k_distinct(s: str, k: int) -> int:
    from collections import defaultdict

    hash_table = defaultdict(int)
    res = left = 0
    for right, char in enumerate(s):
        hash_table[char] += 1
        while len(hash_table) > k:
            char_left = s[left]
            hash_table[char_left] -= 1
            if hash_table[char_left] == 0:
                hash_table.pop(char_left)
            left += 1
        res = max(res, right - left + 1)
    return res


if __name__ == "__main__":
    assert longest_substr("abcabcbb") == 3
    assert longest_substr("bbbbb") == 1
    assert longest_substr("pwwkew") == 3
    assert longest_substr("") == 0
    assert longest_substr_two_distinct("eceba") == 3
    assert longest_substr_two_distinct("ccaabbb") == 5
    assert longest_substr_k_distinct("eceba", 2) == 3
    assert longest_substr_k_distinct("aa", 1) == 2
