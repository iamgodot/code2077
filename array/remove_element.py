# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


# 1. Brute force 双层 for 循环可以解决，时间复杂度 O(n^2)
# 2. 首尾双指针，时间复杂度 O(n)，空间复杂度 O(1)
def remove_element(nums: list, val: int) -> int:
    # deal with edge case

    if not nums:
        return 0

    left, right = 0, len(nums) - 1

    while left < right:
        while left < right and nums[left] != val:
            left += 1

        while left < right and nums[right] == val:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]

    return left if nums[left] == val else left + 1


if __name__ == '__main__':
    for nums, val, length in ([], 0, 0), ([3, 2, 2, 3], 3,
                                          2), ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5):
        assert remove_element(nums, val) == length
        print(nums)
