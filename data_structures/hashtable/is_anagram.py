# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。


# 1. 直接排序后做对比。时间复杂度为 O(nlogn)，即快排消耗；空间复杂度排序需要 O(logn)，但字符串拷贝还需要 O(n)
def is_anagram_by_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# 2. 使用 hashtable 存储做对比。时间复杂度为 O(n)，空间复杂度为常量，即长度 26 的数组
def is_anagram_with_list(s: str, t: str) -> bool:
    '''一开始的长度判断是必要的，因为如果不判断而 s 长度小于 t 就会出错。'''

    if len(s) != len(t):
        return False

    array = [0] * 26
    ord_a = ord('a')

    for i in range(len(s)):

        array[ord(s[i]) - ord_a] += 1
        array[ord(t[i]) - ord_a] -= 1

    return all(val == 0 for val in array)


def is_anagram_with_dict(s: str, t: str) -> bool:
    '''也可以使用普通的 dict，只是写法稍微麻烦一些。'''
    from collections import defaultdict

    d1, d2 = defaultdict(int), defaultdict(int)

    for char in s:
        d1[char] += 1

    for char in t:
        d2[char] += 1

    return d1 == d2


if __name__ == '__main__':
    s, t = 'anagram', 'nagaram'

    for method in [
            is_anagram_by_sort, is_anagram_with_list, is_anagram_with_dict
    ]:
        print(s, t, method(s, t))
