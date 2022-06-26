# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 测试用例的答案是一个 32-位 整数。
# 子数组 是数组的连续子序列。


from typing import List


# 如果遇到负数，那么交换前面的最小和最大值
def max_product(nums: List[int]) -> int:
    res = -float("inf")
    min_ = max_ = 1
    for num in nums:
        if num < 0:
            min_, max_ = max_, min_
        min_ = min(min_ * num, num)
        max_ = max(max_ * num, num)
        res = max(res, max_)

    return res


if __name__ == "__main__":
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
