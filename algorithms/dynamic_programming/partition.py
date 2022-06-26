# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。


# 时间复杂度：O(n^target) 其中 target 为 nums 总和的一半
# 空间复杂度：O(target)
def can_partition(nums: list) -> bool:
    # bag_weight: sum/2
    # dp[j] = total 对于 bag_weight 为 j 的背包总价值为 total
    if sum(nums) & 1 == 1:
        return False

    sum_half = sum(nums) // 2
    dp = [0 for _ in range(sum_half + 1)]

    for i in range(len(nums)):
        for j in range(sum_half, nums[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

    return dp[sum_half] == sum_half


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
