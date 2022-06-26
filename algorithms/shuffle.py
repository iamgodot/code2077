# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。

# 实现 Solution class:

# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果

# 提示：

# 1 <= nums.length <= 200
# -106 <= nums[i] <= 106
# nums 中的所有元素都是 唯一的
# 最多可以调用 5 * 104 次 reset 和 shuffle


# 洗牌方案：对于一个数组，从第一个元素开始，把当前元素及后面的元素一起随机
# 再将得到的元素与当前元素交换，然后继续从第二个元素开始执行。
# 这样可以保证每个元素排到该位置的概率都是等于 1/n 的
# 时间复杂度也可以简化到 O(n)
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.orig = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.orig[:]
        return self.nums

    def shuffle(self) -> List[int]:
        from random import randrange

        for i in range(len(self.nums)):
            j = randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums
