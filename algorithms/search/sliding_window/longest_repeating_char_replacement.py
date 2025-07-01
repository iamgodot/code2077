# Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/


def replace(s: str, k: int) -> int:
    from collections import defaultdict

    hashtable = defaultdict(int)
    res = left = max_repeat = 0
    for right, char in enumerate(s):
        hashtable[char] += 1
        # NOTE: here max_repeat maintains the max frequency
        # in the entire history rather than the current window
        # so we don't update it when moving left
        max_repeat = max(max_repeat, hashtable[char])
        while right - left + 1 > max_repeat + k:
            hashtable[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res


if __name__ == "__main__":
    assert replace("ABAB", 2) == 4
    assert replace("AABABBA", 1) == 4
    assert replace("ABCDE", 1) == 2
