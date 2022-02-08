# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

# 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。


# 对于众数 votes +1 否则 -1. 如此循环整个数组可以达到 O(n) 的时间复杂度
# 如果没有给一定存在多数元素的前提条件，则最后需要判断 res 在数组中出现的次数
def majorityElement(self, nums: List[int]) -> int:
    res = votes = 0
    for num in nums:
        if votes == 0:
            res = num
        votes += 1 if res == num else -1
    return res
