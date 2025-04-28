# Sort Colors
# https://leetcode.com/problems/sort-colors/


def sort(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

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


def sort2(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

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
