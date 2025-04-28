# Next Permutation
# https://leetcode.com/problems/next-permutation/


def nextPermutation(nums: list[int]) -> None:
    """
    Essentially we want to find 2 ascending elements while keeping the smaller one as right as possibile and the larger one as small as possible.
    1. Find the rightmost ascending pair of elements.
    2. Keep the left one and find the smallest larger one from the right end.
    3. Swap 2 elements and sort elements after the left in ascending order. Remember we just need to swap elements for sorting since they're already in descending order.

    Time: O(n)
    Space: O(1)
    """
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    # NOTE: if i < 0, which means all elements are in descending order, we just need to return them in ascending order, e.g. [3, 2, 1] -> [1, 2, 3]
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
