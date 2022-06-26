# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组 是数组中的一个连续部分。


def max_subarray(nums: list) -> int:
    """
    动态规划：dp[n] = max(dp[n-1] + nums[n], nums[n])
    """
    length = len(nums)
    pre, res = nums[0], nums[0]

    for i in range(1, length):
        pre = max(pre + nums[i], nums[i])
        res = max(res, pre)

    return res


def max_subarray2(nums: list) -> int:
    """
    贪心：如果前面的和加起来小于 0 则全部抛弃然后从新开始
    """
    res, sum_ = -float("inf"), 0
    for num in nums:
        sum_ += num
        res = max(res, sum_)
        sum_ = max(sum_, 0)

    return res


if __name__ == "__main__":
    assert max_subarray([1]) == 1
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
