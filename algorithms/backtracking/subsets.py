# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。


from typing import List


# 子集问题类似组合，因为结果是不区分顺序的
# 时间复杂度 O(n * 2^n)
# 空间复杂度 O(n)
def subsets(nums: List[int]) -> List[List[int]]:
    def bt(start):
        res.append(path.copy())
        if start == len(nums):
            return
        for i in range(start, len(nums)):
            path.append(nums[i])
            bt(i + 1)
            path.pop()

    res, path = [], []
    bt(0)
    return res


# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。


# 类似组合，使用排序和前后元素的等值判断来去重
# 复杂度同上
def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    def bt(start):
        res.append(path.copy())
        if start == len(nums):
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            bt(i + 1)
            path.pop()

    res, path = [], []
    nums.sort()
    bt(0)
    return res
