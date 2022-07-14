# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 提示：
# 1 <= nums.length <= 105
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

# 2. 使用优化版快排，每次把数据一分为二，如果前半数量多于 k 就继续处理前半，否则处理后半，这样耗费的时间为
# N + N/2 + N/4 + ... -> 2N 即 O(n). 整体时间 O(n) 空间 O(n)
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    借助最小堆得到前 k 的元素，注意题目里说的是可以按任意顺序返回，所以使用堆是符合要求的。
    如果需要排序，则最后再次全部 pop 出来。
    Time: O(nlogk)
    Space: O(n) 其中堆占用 O(k)
    """
    import heapq
    from collections import Counter

    counter = Counter(nums)
    res = []

    for num, count in counter.items():
        if len(res) == k:
            heapq.heappushpop(res, (count, num))
        else:
            heapq.heappush(res, (count, num))

    return [item[1] for item in res]


def top_k_frequent2(nums: List[int], k: int) -> List[int]:
    """
    Time: O(n) 最坏情况下快速选择会达到 O(n^2)
    Space: O(n) 哈希表占用 O(n) 快速选择最坏情况下为 O(n) 平均 O(logn)
    """
    from collections import Counter

    counter = Counter(nums)
    num_freqs = []
    for num, freq in counter.items():
        num_freqs.append((freq, num))

    def quick_select(nums, left, right, k) -> None:
        if left >= right:
            return
        pivot, i, j = left, left, right
        while i < j:
            while nums[j] >= nums[pivot] and i < j:
                j -= 1
            while nums[i] <= nums[pivot] and i < j:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[pivot] = nums[pivot], nums[i]
        if i == k:
            return
        elif i > k:
            quick_select(nums, left, i - 1, k)
        else:
            quick_select(nums, i + 1, right, k)

    quick_select(num_freqs, 0, len(num_freqs) - 1, len(num_freqs) - k)
    return [item[1] for item in num_freqs[len(num_freqs) - k :]]


def top_k_frequent3(nums: list, k: int) -> list:
    """
    利用计数排序对整理后的数据进行 O(n) 时间的排列。
    Time: O(n)
    Space: O(n)
    """
    from collections import defaultdict

    counter = defaultdict(int)

    for num in nums:
        counter[num] += 1
    # 因为数组最大为 10^5，所以一个数出现最多的次数为 10^5
    res = [None] * 100001

    for num, count in counter.items():
        # 注意可能会出现两个数的出现频率相同的情况，所以要用数组保存

        if not res[count]:
            res[count] = [num]
        else:
            res[count].append(num)

    # 注意此处的语法结构

    return [i for j in res if j for i in j][-k:]


if __name__ == "__main__":
    for func in top_k_frequent, top_k_frequent2, top_k_frequent3:
        assert sorted(func([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
        assert func([3, 0, 1, 0], 1) == [0]
