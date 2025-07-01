def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Time: O(nlogk)
    Space: O(n)
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


def top_k_frequent2(nums: list[int], k: int) -> list[int]:
    """
    Time: O(n) in worst case O(n^2)
    Space: O(logn) in worst case O(n)
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
