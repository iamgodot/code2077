# Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/


def is_anagram(s: str, t: str) -> bool:
    """
    Sort the strings.

    Time: O(nlogn)
    Space: O(logn + n)
    """
    return sorted(s) == sorted(t)


def is_anagram2(s: str, t: str) -> bool:
    """
    Use a frequency counter.
    We need to use a hash table for unicode strings.

    Time: O(n)
    Space: O(1)
    """
    if len(s) != len(t):
        return False
    counter = [0] * 26
    for char in s:
        index = ord(char) - ord("a")
        counter[index] += 1
    for char in t:
        index = ord(char) - ord("a")
        counter[index] -= 1
        if counter[index] < 0:
            return False
    return True


if __name__ == "__main__":
    for func in [is_anagram, is_anagram2]:
        assert func("anagram", "nagaram") is True
        assert func("rat", "car") is False
