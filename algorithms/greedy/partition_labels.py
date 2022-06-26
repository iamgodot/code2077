# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。


from typing import List


def partition_labels(s: str) -> List[int]:
    """
    Count the largest index of each char in s.
    Iterate the string:
        If current index equals to the largest index of appeared chars, then slice it up
    """
    length = len(s)
    hashtable = {}
    for i in range(length):
        hashtable[s[i]] = i

    res = []
    left = right = 0
    for i in range(length):
        right = max(right, hashtable[s[i]])
        if i == right:
            res.append(right - left + 1)
            left = right = i + 1

    return res


if __name__ == "__main__":
    assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
