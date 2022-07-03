# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
# 在执行上述操作后，返回包含相同字母的最长子字符串的长度。


def replace(s: str, k: int) -> int:
    from collections import defaultdict

    hashtable = defaultdict(int)
    res = left = 0
    for right, char in enumerate(s):
        hashtable[char] += 1
        repeat_max = max(hashtable.values())
        while right - left + 1 - repeat_max > k:
            hashtable[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res


if __name__ == "__main__":
    assert replace("ABAB", 2) == 4
    assert replace("AABABBA", 1) == 4
    assert replace("ABCDE", 1) == 2
