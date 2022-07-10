# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Time: O(n*k*logk) k 为 strs 中字符串的最大长度
    Space: O(n*k)
    """
    from collections import defaultdict

    hashtable = defaultdict(list)
    for string in strs:
        sorted_s = "".join(sorted(string))
        hashtable[sorted_s].append(string)
    return list(hashtable.values())


def group_anagrams2(strs: List[str]) -> List[List[str]]:
    """
    Time: O(n*(k + c)) c 为字符集长度，用于生成 hash key
    Space: O(n*(k + c))
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
