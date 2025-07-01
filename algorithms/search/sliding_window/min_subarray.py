# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/


def min_subarray_len(target: int, nums: list) -> int:
    """
    1. Build prefix sum array: ps[i] = sum(nums[0] + .. + nums[i])
    2. Iterate nums, for every num, find the smallest j and let: ps[j] - ps[i] + nums[i] >= target
    3. Update res with minimum value

    Time: O(nlogn)
    Space: O(n)
    """

    def bs(nums, target, left, right):
        if left > right:
            return -1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left

    res = float("inf")
    prefix_sums = []
    total = 0
    for num in nums:
        total += num
        prefix_sums.append(total)

    length = len(nums)
    for i in range(length):
        index = bs(prefix_sums, target + prefix_sums[i] - nums[i], i, length - 1)
        if index == 0:
            res = min(res, i + 1)
        elif index > length - 1:
            pass
        else:
            res = min(res, index - i + 1)

    return 0 if res == float("inf") else res


def min_subarray_len(target: int, nums: list) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = float("inf")
    total = left = 0

    for right, num in enumerate(nums):
        total += num
        while total >= target:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if res == float("inf") else res


if __name__ == "__main__":
    assert min_subarray_len(1, []) == 0
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray_len(4, [1, 4, 4]) == 1
    assert min_subarray_len(11, [1, 2, 3, 4, 5]) == 3
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
