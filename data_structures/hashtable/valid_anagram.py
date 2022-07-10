# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。


# 1.
def is_anagram(s: str, t: str) -> bool:
    """
    直接排序后做对比。
    Time: O(nlogn)
    Space: O(logn + n)
    """
    return sorted(s) == sorted(t)


def is_anagram2(s: str, t: str) -> bool:
    """也可以使用普通的 dict，只是写法稍微麻烦一些。"""
    if len(s) != len(t):
        return False
    from collections import defaultdict

    hashtable = defaultdict(int)

    for char in s:
        hashtable[char] += 1

    for char in t:
        hashtable[char] -= 1
        if hashtable[char] < 0:
            return False

    return True


if __name__ == "__main__":
    for func in [is_anagram, is_anagram2]:
        assert func("anagram", "nagaram") is True
        assert func("rat", "car") is False
