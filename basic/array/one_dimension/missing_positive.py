# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。


from typing import List


def find(nums: List[int]) -> int:
    """
    遍历数组，目的是把 1~n 的元素交换到对应的位置，比如 [2,1,3] -> [1,2,3]
    如果元素不在 1~n 范围内，则直接跳过，否则找到正确的位置并与其交换。
    注意：
        1. 如果两个位置的数大小相同则跳过，造成这种情况的也可能是当前元素正好处于正确的位置
        2. 在交换的时候不要这么写：nums[i], nums[nums[i] - 1] = ... 因为前面更新了 nums[i] 的值
            之后后面的 index 就不再是原有的位置了
    """
    i, n = 0, len(nums)
    while i < n:
        number = nums[i]
        # number 等于 nums[number - 1] 说明两个数正好相等，或者就是同一个数
        if number < 1 or number > n or number == nums[number - 1]:
            i += 1
        else:
            nums[i], nums[number - 1] = nums[number - 1], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    for input, ans in ([1, 2, 0], 3), ([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1):
        assert find(input) == ans
