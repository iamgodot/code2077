# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
from random import randint


# 使用快速排序的思路来实现快速选择
# 时间复杂度：最差情况下为 O(n^2)，平均水平为 O(n)（可以看作是 n->n/2->n/4... 这个等比数列的和）
# 空间复杂度：递归的情况下为 O(logn)，如果改成迭代实现则是 O(1)
def quick_sort(nums: list, left: int, right: int, k: int) -> int:
    if left >= right:
        return nums[left]

    pivot, i, j = left, left, right

    index_random = randint(left + 1, right)
    nums[pivot], nums[index_random] = nums[index_random], nums[pivot]

    while i < j:
        while i < j and nums[j] >= nums[pivot]:
            j -= 1
        while i < j and nums[i] <= nums[pivot]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[pivot], nums[i] = nums[i], nums[pivot]
    index = len(nums) - k
    if i == index:
        return nums[i]
    elif i > index:
        return quick_sort(nums, 0, i - 1, k)
    else:
        return quick_sort(nums, i + 1, right, k)


def find_kth_largest(nums: list, k: int) -> int:
    # return quick_sort(nums, 0, len(nums) - 1, k)
    import heapq

    hq = []
    for num in nums:
        if len(hq) == k:
            if num > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, num)
        else:
            heapq.heappush(hq, num)

    return heapq.heappop(hq)


if __name__ == "__main__":
    a = find_kth_largest([3, 2, 1, 5, 6, 4], 2)
    print(a)
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
