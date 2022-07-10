# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。


from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    对于可能的连续序列结果，只有当 first 元素减一的元素不存在才开始计算。
    Time: O(n)
    Space: O(n)
    """
    s = set(nums)
    res = 0
    for num in nums:
        if num - 1 not in s:
            count = 1
            start = num
            while start + 1 in s:
                count += 1
                start += 1
            res = max(res, count)
    return res


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
