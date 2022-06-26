# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：

# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。

# 以这种方式修改数组后，返回数组 可能的最大和 。

# 提示：

# 1 <= nums.length <= 104
# -100 <= nums[i] <= 100
# 1 <= k <= 104

import heapq
from collections import Counter
from typing import List


def largest_sum_after_k_negations(nums: List[int], k: int) -> int:
    """
    利用提示条件 2，先利用计数排序完成 O(n) 时间的排序
    然后先将所有的负数都取反，如果 k 仍然不为 0 而且为 奇数，那么
    只需要在结果中减去最小正数（或者 0）的两倍即可
    时间复杂度：O(m + n) 空间复杂度：O(m) m 为 nums 中不重复数字的个数
    """
    counter = Counter(nums)
    index = 0
    for i in range(-100, 101):
        for _ in range(counter[i]):
            nums[index] = i
            index += 1

    for i in range(len(nums)):
        num = nums[i]
        if num >= 0 or k == 0:
            break
        else:
            nums[i] = -num
            k -= 1

    res = sum(nums)
    return res - 2 * min(nums) if k % 2 == 1 else res


def largest_sum_after_k_negations2(nums: List[int], k: int) -> int:
    """
    利用最小堆，每次取出最小值然后取反即可
    时间复杂度 O(k * log(n) + O(n)) 其中 O(n) 为 heapify 的成本
    空间复杂度 O(n) 考虑改变了 nums 的顺序
    """

    heapq.heapify(nums)
    while k > 0:
        min_ = heapq.heappop(nums)
        heapq.heappush(nums, -min_)
        k -= 1

    return sum(nums)


if __name__ == "__main__":
    for method in [largest_sum_after_k_negations, largest_sum_after_k_negations2]:
        assert method([2, -3, -1, 5, -4], 2) == 13
        assert method([2, -3, -1, 5, -4], 20) == 13
