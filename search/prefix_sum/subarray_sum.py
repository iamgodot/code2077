# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

from collections import defaultdict


# 1. BruteForce: 两层遍历，其中求和复杂度为 O(1)，总体时间复杂度 O(n^2)
# 2. 因为数组中不一定全是正数，所以无法应用滑动窗口，
# 但是可以利用子数组的和为前缀和之差的关系把问题转化为求两数之和，
# 这样整体达到了 O(n) 的时间复杂度
def subarray_sum(nums: list, k: int) -> int:
    """
    注意 nums[j] - nums[i-1] 代表了 i-j 子数组的和，
    所以提前加入了 {0: 1} 来对应子数组只有单个元素的情况。
    另外在循环过程中，每个元素可以看作 j 元素，因为顺序是从头到尾，所以可以保证 i <= j
    哈希表存储的是前缀和：符合前缀和的元素总个数。
    在遍历过程中，应当先把当前元素加入到总和中，再搜索哈希表，最后才更新哈希表（这样保证了不会重复使用当前元素）。
    """
    count = total = 0

    # 注意这里需要提前添加 total 为 0 的元素，针对数组中第一个数即为 k 的情况
    hashtable = defaultdict(int, {total: 1})
    for num in nums:
        total += num
        count += hashtable.get(total - k, 0)
        hashtable[total] += 1

    return count


if __name__ == "__main__":
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1], 0) == 0
