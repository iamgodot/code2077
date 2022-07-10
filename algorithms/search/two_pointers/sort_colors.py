# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
# 必须在不使用库的sort函数的情况下解决这个问题。

from typing import List


def sort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    两次遍历，第一次把所有的 0 放到头部，第二次把 1 放到头部。

    Time: O(n)
    Space: O(1)
    """
    p = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1
    for i in range(p, len(nums)):
        if nums[i] == 1:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1


def sort2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    一次遍历。

    Time: O(n)
    Space: O(1)
    """
    p0, p2 = 0, len(nums) - 1
    i = 0
    while i <= p2:
        while i <= p2 and nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1
        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1
        i += 1


if __name__ == "__main__":
    for func in sort, sort2:
        numbers = [2, 0, 2, 1, 1, 0]
        func(numbers)
        assert numbers == [0, 0, 1, 1, 2, 2]
        numbers = [2, 0, 1]
        func(numbers)
        assert numbers == [0, 1, 2]
