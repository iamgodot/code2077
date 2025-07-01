# Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/


def assign(g: list[int], s: list[int]) -> int:
    """
    Time: O(mlogm + nlogn)
    Space: O(logm + logn)
    """
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1

    return i


if __name__ == "__main__":
    assert assign([1, 2, 3], [1, 1]) == 1
    assert assign([1, 2], [1, 2, 3]) == 2
    assert assign([1], []) == 0
    assert assign([10, 9, 8, 7], [5, 6, 7, 8]) == 2
