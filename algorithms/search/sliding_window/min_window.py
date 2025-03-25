# Minumum window substring
# https://leetcode.com/problems/minimum-window-substring/description/


def min_window(s: str, t: str) -> str:
    """
    With a sliding window, we only care about chars in t,
    so the hash table only stores those chars, and also a count var

    Time: O(n)
    Space: O(1)
    """
    res = ""
    from collections import defaultdict

    hash_table = defaultdict(int)  # char: count
    for char in t:
        hash_table[char] += 1
    left = 0
    count = len(t)
    for right, char in enumerate(s):
        if char in hash_table:
            if hash_table[char] > 0:
                count -= 1
            hash_table[char] -= 1
        while count == 0:
            sub_s = s[left : right + 1]
            if res == "" or len(sub_s) < len(res):
                res = sub_s

            char_left = s[left]
            if char_left in hash_table:
                hash_table[char_left] += 1
                if hash_table[char_left] > 0:
                    count += 1
            left += 1
    return res


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("bba", "ab") == "ba"
