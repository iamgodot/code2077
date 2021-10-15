# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 提示：
# 1 <= nums.length <= 105
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

# 首先需要先整理出数组中每个数字对应其出现频率并存放起来，再决定如何从中选取前 k 的元素
# 那么整理就需要：时间 O(n) 空间 O(n)

# 1. 对整理后的数据按照频率直接快排，这样的好处是可以选取任意前几的结果，因为已经完全排序。时间 O(n*logn) 空间 O(n)
# 这种方法对于进阶的要求就无法满足了，所以必须继续优化

# 2. 使用优化版快排，每次把数据一分为二，如果前半数量多于 k 就继续处理前半，否则处理后半，这样耗费的时间为
# N + N/2 + N/4 + ... -> 2N 即 O(n). 整体时间 O(n) 空间 O(n)


# 3. 借助最小堆得到前 k 的元素，耗费的时间为 O(n*logk)，空间为 O(k)。综合起来时间 O(n*logk) 空间 O(n)
# 注意题目里说的是可以按任意顺序返回，所以使用堆是符合要求的，否则会有问题，因为堆不能保证所有的元素都是顺序的
def top_k_freq_with_heap(nums: list, k: int) -> list:
    import heapq
    from collections import defaultdict
    counter = defaultdict(int)

    for num in nums:
        counter[num] += 1
    res = []

    for num, count in counter.items():
        if len(res) == k:
            heapq.heappushpop(res, (count, num))
        else:
            heapq.heappush(res, (count, num))

    return [item[1] for item in res]


# 4. 利用计数排序对整理后的数据进行 O(n) 时间的排列。整体时间 O(n) 空间 O(n)
def top_k_freq_with_bucket(nums: list, k: int) -> list:
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


if __name__ == '__main__':
    for nums, k, res in ([1, 1, 1, 2, 2, 3], 2, {1, 2}), ([3, 0, 1,
                                                           0], 1, {0}):
        assert set(top_k_freq_with_heap(nums, k)) == res
        assert set(top_k_freq_with_bucket(nums, k)) == res
