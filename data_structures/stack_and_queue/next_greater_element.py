# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    单调栈：从后向前遍历元素，使用单调递增栈记录元素值。

    注意列表中的元素各不重复，所以可以使用哈希表来记录，也不用担心比较时发生等于的情况。

    对于每一个元素：
    1. 循环检查栈
        1. 如果栈为空，跳出循环
        2. 如果栈顶元素小于等于当前元素，pop 并比较下一个
    2. 如果栈为空，设置 nge 为 -1，否则设置为栈顶元素
    3. 将当前元素 push 进栈

    时间复杂度 O(m+n) m 为 nums1 长度，n 为 nums2 长度
    空间复杂度 O(n)
    """
    stack, hashtable = [], {}
    length = len(nums2)
    for i in range(length - 1, -1, -1):
        num = nums2[i]
        while stack and stack[-1] <= num:
            stack.pop()
        # 节省空间
        if stack:
            hashtable[num] = stack[-1]
        stack.append(num)
    return [hashtable.get(i, -1) for i in nums1]


# 给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
# 数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。


def next_greater_element2(nums: List[int]) -> List[int]:
    """
    思路同上，但是在遍历过程中使用两倍的长度来模拟扩展数组的情况。
    """
    length = len(nums)
    stack, res = [], [-1 for _ in range(length)]
    for i in range(2 * length - 1, -1, -1):
        num = nums[i % length]
        while stack and stack[-1] <= num:
            stack.pop()
        if stack:
            res[i % length] = stack[-1]
        stack.append(num)
    return res


if __name__ == "__main__":
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1]
    assert next_greater_element2([1, 2, 1]) == [2, -1, 2]
    assert next_greater_element2([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
