# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。


from typing import List


def partition_labels(s: str) -> List[int]:
    """
    Count the largest index of each char in s.
    Iterate the string:
        If current index equals to the largest index of appeared chars, then slice it up

    Time: O(n)
    Space: O(1) limited to 26 chars
    """
    length = len(s)
    hashtable = {}
    for i in range(length):
        hashtable[s[i]] = i

    res = []
    end = size = 0
    for i, char in enumerate(s):
        size += 1
        end = max(end, hashtable[char])
        if i == end:
            res.append(size)
            size = 0

    return res


if __name__ == "__main__":
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
