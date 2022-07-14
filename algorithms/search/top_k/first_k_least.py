# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


import heapq
from typing import List


# 因为求最小的 k 个数，所以要用最大堆
# Python 的 heapq 默认为最小堆，所以要取负数
def get_least_nums(arr: List[int], k: int) -> List[int]:
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        else:
            heapq.heappushpop(heap, -num)

    return [-i for i in heap]


# 快速排序，迭代到前半部分满足 k 个元素之后即可以停止
# 时间复杂度 O(n) 空间复杂度 O(logn) 递归占用
def get_least_nums2(arr: List[int], k: int) -> List[int]:
    def qs(nums, left, right, k):
        if left >= right:
            return
        i, j = left, right
        while i < j:
            while i < j and arr[j] >= arr[left]:
                j -= 1
            while i < j and arr[i] <= arr[left]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]

        arr[left], arr[i] = arr[i], arr[left]
        if k < i:
            qs(nums, left, i - 1, k)
        elif k > i:
            qs(nums, i + 1, right, k)
        else:
            return

    qs(arr, 0, len(arr) - 1, k)
    return arr[:k]


if __name__ == "__main__":
    assert sorted(get_least_nums([3, 2, 1], 2)) == [1, 2]
    assert sorted(get_least_nums2([3, 2, 1], 2)) == [1, 2]
