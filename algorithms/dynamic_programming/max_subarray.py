# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/


def max_subarray(nums: list) -> int:
    """
    dp[n] = max(dp[n-1] + nums[n], nums[n])

    Time: O(n)
    Space: O(1)
    """
    res = nums[0]
    cur = 0
    for n in nums:
        if cur < 0:
            cur = 0
        cur += n
        res = max(res, cur)
    return res


def max_subarray2(nums):
    if len(nums) == 1:
        return nums[0]
    if nums[0] >= 0:
        print(nums[0], max_subarray2(nums[1:]))
        return nums[0] + max_subarray2(nums[1:])
    else:
        return max_subarray2(nums[1:])


def max_subarray3(nums: list) -> int:
    """
    Kadane's algorithm.
    """
    res, sum_ = -float("inf"), 0
    for num in nums:
        sum_ += num
        res = max(res, sum_)
        sum_ = max(sum_, 0)

    return int(res)


if __name__ == "__main__":
    assert max_subarray([1]) == 1
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print(max_subarray([-1, 1, 3, -5, 7, 9, -11, 13, 15, -17, 19, 21, -23]))
    print(max_subarray2([-1, 1, 3, -5, 7, 9, -11, 13, 15, -17, 19, 21, -23]))
