# 给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。


from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.

    Time: O(n)
    Space: O(1)
    """

    def reverse(nums, left, right) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    length = len(nums)
    k = k % length
    reverse(nums, 0, length - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, length - 1)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7]
    rotate(numbers, 3)
    assert numbers == [5, 6, 7, 1, 2, 3, 4]
