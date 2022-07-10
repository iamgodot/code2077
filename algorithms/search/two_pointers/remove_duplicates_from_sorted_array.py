# 由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k 个元素应该保存最终结果。
# 将最终结果插入 nums 的前 k 个位置后返回 k 。
# 不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    length = len(nums)
    if length <= 1:
        return length
    i = 1
    for j in range(1, length):
        if nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1
    return i


# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。


def remove_duplicates2(nums: List[int]) -> int:
    """
    对于 k 的情况一样可以扩展实现。

    Time: O(n)
    Space: O(1)
    """
    length = len(nums)
    if length <= 2:
        return length
    i = 2
    for j in range(2, length):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1
    return i


if __name__ == "__main__":
    numbers = [1, 1, 2]
    assert remove_duplicates(numbers) == 2
    assert numbers[:2] == [1, 2]
    numbers = [1, 1, 1, 2, 2, 3]
    assert remove_duplicates2(numbers) == 5
    assert numbers[:5] == [1, 1, 2, 2, 3]
