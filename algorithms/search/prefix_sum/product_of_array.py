# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Time: O(n)
    Space: O(1) 不考虑输出数组
    """
    length = len(nums)
    res = [1] * length
    for i in range(1, length):
        res[i] = res[i - 1] * nums[i - 1]
    x = nums[-1]
    for i in range(length - 2, -1, -1):
        res[i] *= x
        x *= nums[i]
    return res


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
