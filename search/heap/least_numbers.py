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
    def qs(l, r):
        if l >= r:
            return
        i, j = l, r
        while i < j:
            while i < j and arr[j] >= arr[l]:
                j -= 1
            while i < j and arr[i] <= arr[l]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]

        arr[l], arr[i] = arr[i], arr[l]
        if k < i:
            qs(l, i - 1)
        elif k > i:
            qs(i + 1, r)
        else:
            return

    qs(0, len(arr) - 1)
    return arr[:k]


if __name__ == "__main__":
    assert sorted(get_least_nums([3, 2, 1], 2)) == [1, 2]
    assert sorted(get_least_nums2([3, 2, 1], 2)) == [1, 2]
