import heapq


def get_least_nums(arr: list[int], k: int) -> list[int]:
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        else:
            heapq.heappushpop(heap, -num)

    return [-i for i in heap]


def get_least_nums2(arr: list[int], k: int) -> list[int]:
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
