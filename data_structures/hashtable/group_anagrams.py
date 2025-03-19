# Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Sort the strings.

    Time: O(n*k*logk) where k is the max length of strings
    Space: O(n*k)
    """
    from collections import defaultdict

    hashtable = defaultdict(list)
    for string in strs:
        sorted_s = "".join(sorted(string))
        hashtable[sorted_s].append(string)
    return list(hashtable.values())


def group_anagrams2(strs: list[str]) -> list[list[str]]:
    """
    Time: O(n*k)
    Space: O(n*k)
    """
    from collections import defaultdict

    hashtable = defaultdict(list)
    for string in strs:
        chars = [0] * 26
        for char in string:
            chars[ord(char) - ord("a")] += 1
        hashtable[tuple(chars)].append(string)
    return list(hashtable.values())


if __name__ == "__main__":
    for func in group_anagrams, group_anagrams2:
        res = func(["eat", "tea", "tan", "ate", "nat", "bat"])
        assert sorted(sorted(item) for item in res) == [
            ["ate", "eat", "tea"],
            ["bat"],
            ["nat", "tan"],
        ]
